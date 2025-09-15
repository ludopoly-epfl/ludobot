import discord
from discord import app_commands
from discord.ext import commands
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from discord.ui import Button, View
from datetime import datetime
from fuzzywuzzy import fuzz

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
client = gspread.authorize(credentials)
""""
@bot.tree.command(name="emprunt", description="Emprunter un jeu")
@app_commands.describe(nom_jeu="Nom complet du jeu à emprunter",
                       date="Date de récupération (JJ/MM/AAAA)",
                       heure="Heure de récupération (HH:MM)")
"""

async def emprunt(interaction: discord.Interaction, nom_jeu: str, date: str, heure: str):
    
    await interaction.response.defer(ephemeral=True)

    try:

        # Validation de la date
        try:
            date_obj = datetime.strptime(date, "%d/%m/%Y")
        except ValueError:
            await interaction.followup.send("❌ Format de date invalide. Utilisez JJ/MM/AAAA.", ephemeral=True)
            return

        # Validation de l'heure
        try:
            heure_obj = datetime.strptime(heure, "%H:%M")
        except ValueError:
            await interaction.followup.send("❌ Format d'heure invalide. Utilisez HH:MM.", ephemeral=True)
            return

        # Combinaison date + heure
        datetime_recup = datetime.combine(date_obj.date(), heure_obj.time())
        
        if datetime_recup < datetime.now():
            await interaction.followup.send("❌ La date/heure doit être dans le futur !", ephemeral=True)
            return

        # Récupérer les données nécessaires
        client = gspread.authorize(credentials)
        sheet_membres = client.open("Membres").sheet1
        sheet_prets = client.open("Prêts Membres").sheet1
        sheet_jeux = client.open("Inventaire").sheet1

        # Vérifier l'existence du jeu
        jeux_data = sheet_jeux.get_all_values()
        jeu_trouve = False
        nom_jeu_correction = ""

        for row in jeux_data[1:]:
            nom_complet = ' '.join(filter(None, row[0:3])).strip()
            score = fuzz.ratio(nom_complet.lower(), nom_jeu.lower())
            
            if score > 85:  # Seuil de similarité à 85%
                jeu_trouve = True
                nom_jeu_correction = nom_complet  # Garder le nom exact de la feuille
                break

        if not jeu_trouve:
            await interaction.followup.send(f"❌ Jeu introuvable.", ephemeral=True)
            return

        # Vérifier si le jeu est déjà emprunté
        prets_data = sheet_prets.get_all_values()
        for row in prets_data[1:]:  # Ignorer l'en-tête
            if row[2].strip().lower() == nom_jeu.lower():
                await interaction.followup.send("❌ Ce jeu est déjà emprunté.", ephemeral=True)
                return   

        # Trouver le membre dans la sheet membres
        membres_data = sheet_membres.get_all_values()
        membre_trouve = None

        for row in membres_data[1:]:
            discord_username = f"{interaction.user.name}"

            if row[3].strip().lower() == discord_username.lower() and row[0].strip().lower() == "oui":
                membre_trouve = row[1]  # Colonne NOM
                break

        if membre_trouve == None:
            await interaction.followup.send("❌ Vous n'êtes pas membre.", ephemeral=True)
            return

        # Ajouter le prêt
        new_row = [membre_trouve, date, nom_jeu_correction]
        sheet_prets.append_row(new_row)

        await interaction.followup.send("✅ Demande d'emprunt du " + nom_jeu_correction + 
                                        " enregistrée !\nVous serez prévenu dès qu'elle aura été prise en charge.", ephemeral=False)

    except Exception as e:
        print(f"ERREUR: {str(e)}")
        await interaction.followup.send("⚠️ Une erreur est survenue.", ephemeral=True)   

    # Récupérer le salon "gestion-prêts"
    channel = discord.utils.get(interaction.guild.channels, name="gestion-prêts")

    view = View()
    button = ConfirmButton(interaction.user, nom_jeu, date, heure)
    view.add_item(button)

    await channel.send(
            f"⚠️ Nouvel emprunt du {nom_jeu} demandé par **{membre_trouve}** (" + discord_username + f") le **{date}** à **{heure}** \n", view=view)


class ConfirmButton(Button):
    def __init__(self, emprunteur, jeu, date, heure):
        super().__init__(label="Je m'en occupe", style=discord.ButtonStyle.green)
        self.emprunteur = emprunteur
        self.jeu = jeu
        self.date = date
        self.heure = heure

    async def callback(self, interaction: discord.Interaction):

        channel = discord.utils.get(interaction.guild.channels, name="gestion-prêts")

        await self.emprunteur.send(f"Le **{self.jeu}** sera disponible en cm qqchose. \n"
                                   f"Date : " + self.date + "\n"
                                   f"Heure : " + self.heure)
        
        await channel.send("✅ Confirmation envoyée !")