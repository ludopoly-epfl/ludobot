import discord
import re
import random as ra
import math as ma
from discord.ext import commands
from discord import app_commands
import os
from keepalive import keep_alive
from eric import emprun
from outilsCheck import islol,iscomité,findname,isnatel,dad,amogus
from comité import Lcomité,Lidcomte,Allcomite
from variablesglobales import feur_id,ludobot_id,lol_id,Gandalf_id,bigE_id,chabienv_id,comite_id,prison_id,prisonnier_id,ludann_id,logs_id,LudopServId,imperium_id,magic_id,mauvais_id,admin_id,list6,list10,trucs

from outilsDiscord import prisontime,minusrole,plusrole,freedom,masterchange,checkrole,slay
from lolisbad import lolbad

TOKEN=os.getenv("DISCORD_TOKEN")
Dad_Limit=os.getenv("Dad_Limit")
#dlim=os.getenv("dé_limit")
dlim=10

def add_count (cible : discord.member) :
    iden=cible.id
    return

def reset_count( cible:discord.member):
    iden=cible.id
    return


keep_alive() # NE SURTOUT PAS TOUCHER 

""""
        case :
            return "."
"""  

class Client(commands.Bot):
    async def on_ready(self):
        print(f'Hello World')

        try :
            print('hmm')
            LudopServ=discord.Object(id=LudopServId)
            print("hee")
            synced= await self.tree.sync(guild=LudopServ)
            print("hehe")
            print(f'nb = {len(synced)} at guild {LudopServ.id}')

        except Exception as e:
            print(f'not good we {e}')

    async def on_member_join(self, member:discord.Member):
        
        logcha=discord.utils.get(member.guild.channels, id=logs_id)
        pris_test=await checkrole(prisonnier_id ,member)
        lol_test= await checkrole(lol_id,member)
        m_test=await checkrole(mauvais_id,member)
        bienvenue="za warudo"
        await logcha.send("pit")
        if True :
            await logcha.send("aaa")
            await logcha.send(pris_test)
            await logcha.send(lol_test)
            await logcha.send(m_test)
        if lol_test :
            await logcha.send("We're gonna have to kill this guy")
        if pris_test or lol_test :
            bienvenue=f'Bienvenue {member.mention}, tu commence ta vie ici dans la {member.guild.get_channel(prison_id)}, regarde le message pin là bas'
            await prisontime(member.guild, member)
            await logcha.send("hag")
        if m_test:
            await logcha.send("hon")
            bienvenue=f'Bienvenue {member.mention}, tu commence ta vie ici hors de la {member.guild.get_channel(prison_id)}, pour le moment...'
        bienvenue=f'Bienvenue {member.mention} dans le serveur de Ludopoly, un lieu de jeu et de mise en prison arbitraire !'

        
        await member.guild.get_channel(chabienv_id).send(bienvenue)



intents = discord.Intents.default()
intents.message_content = True
intents.guilds= True
intents.members= True
client= Client(command_prefix="!", intents=intents)

LuluServ=discord.Object(id=LudopServId)

GUILD_ID=discord.Object(id=1315014960325328926)#serv de test



@client.event
async def on_message( message):
        #print(f'From {message.author} : {message.content} ')
        if message.author != client.user:
            if isnatel(message.content):
                add_count(message.author)
            
            await amogus(message,client)

            phrase=dad(message.content)
            if (phrase!=None):
                #if (len(phrase)>Dad_Limit) :
                 #   await message.channel.send(content="C'est beaucoup trop de mots, je ne lis pas ça")
                if "@" in phrase:
                    await message.channel.send("Bien essayé !")
                else:
                    await message.channel.send(phrase)
            elif islol(message.content):
                await message.channel.send(lolbad())
                add_count

@client.tree.command(name="lolisgood",description="Interdit ça", guild=LuluServ)
async def lolisgood(interaction : discord.Interaction) :
        GUILD=interaction.guild
        channel = discord.utils.get(GUILD.channels, id=ludann_id)
        await channel.send(content=f'{interaction.user.mention} a choisi le chemin du mal.')
        await interaction.response.send_message(content="You are going to Brazil !",ephemeral=True)
        await prisontime(GUILD, interaction.user)
        add_count(interaction.user)

@client.tree.command(name="exécution",description="Retirer le rôle peuple de la cible et la place en prison",guild=LuluServ)
async def kill(interaction: discord.Interaction, cible :discord.User ):
    GUILD=interaction.guild
    prisonnier=discord.utils.get(interaction.guild.roles  ,id=prisonnier_id)
    try:
        await prisontime(GUILD, cible)
        await interaction.response.send_message("Cible éliminée",ephemeral=True)
        channel = discord.utils.get(GUILD.channels, id=ludann_id)
        mots=f'{cible.mention} monte sur l\'échafaud ...'
        if not prisonnier in cible.roles:
            mots+=' Mais ne meurt pas !'
        await channel.send(content=mots)
    except:
        await interaction.response.send_message("Erreur",ephemeral=True)

@client.tree.command(name="évasion",description="Sortir de prison",guild=LuluServ)
async def evasion(interaction: discord.Interaction):
    await interaction.response.defer(ephemeral=True)
    guild=interaction.guild
    user=interaction.user
    try:
        prisonnier=discord.utils.get(guild.roles  ,id=prisonnier_id)
        mauvais=discord.utils.get(guild.roles,id=mauvais_id)
        await minusrole(prisonnier,user)
        await plusrole(mauvais,user)
        await interaction.followup.send("Evasion réussie !",ephemeral=True)
        channel = discord.utils.get(guild.channels, id=ludann_id)
        escape=f'{user.mention} a pris la poudre d\'escampette !'
        await channel.send(content=escape)

        
    except:
        await interaction.response.send_message("Erreur",ephemeral=True)


@client.tree.command(name="rolelist",description="Donne la liste des roles",guild=LuluServ)
async def rolelist(interaction: discord.Interaction):
    guild=interaction.guild
    await interaction.response.defer(ephemeral=True)
    logcha=discord.utils.get(guild.channels, id=logs_id)
    await logcha.send(f'Liste des rôles de {interaction.user.mention} :')
    for role in interaction.guild.roles :
        await logcha.send(f'{await checkrole(role.id,interaction.user)} : {role.name} ')

    await interaction.followup.send("Tache accomplie",ephemeral=True)




@client.tree.command(name="change_roles",description="UTILISER QUE SI COMBAT NE MARCHES PAS !",guild=LuluServ)
@app_commands.describe(gagnant="Membre victorieux du combat", perdant="Membre vaincu",jeu="Jeu d'affrontement")
async def change(interaction: discord.Interaction, gagnant :discord.Member , perdant: discord.Member, jeu : str) :
    await interaction.response.defer(ephemeral=True)
    await masterchange(interaction.guild,gagnant,perdant,jeu)
    await interaction.followup("C'est bon")


@client.tree.command(name="imperium",description="Ajoute le rôle Twilight Imperium",guild=LuluServ)
@app_commands.describe(cible="Membre à donner le rôle")
async def imperium(interaction: discord.Interaction, cible :discord.Member) :
    await interaction.response.defer(ephemeral=True)
    imperator=discord.utils.get(interaction.guild.roles  ,id=bigE_id)
    guys=discord.utils.get(interaction.guild.roles  ,id=imperium_id)
    if imperator in interaction.user.roles :
        await plusrole(guys,cible)
        await interaction.followup("Ave Imperator")
    else:
        await interaction.followup("Absolutely not, go fuck yourself")

@client.tree.command(name="magic",description="Ajoute le rôle Magic",guild=LuluServ)
@app_commands.describe(cible="Membre à donner le rôle")
async def magic(interaction: discord.Interaction, cible :discord.Member) :
    await interaction.response.defer(ephemeral=True)
    Mage=discord.utils.get(interaction.guild.roles  ,id=Gandalf_id)
    guys=discord.utils.get(interaction.guild.roles  ,id=magic_id)
    if Mage in interaction.user.roles :
        await plusrole(guys,cible)
        await interaction.followup("Bien Magicien")
    else:
        await interaction.followup("Absolutely not, go fuck yourself")


@client.tree.command(name="combat",description="A utiliser quand un défi impliquant un comité est résolu",guild=LuluServ)
@app_commands.describe(gagnant="Membre victorieux du combat", perdant="Membre vaincu",jeu="Jeu d'affrontement")
async def combat(interaction: discord.Interaction, gagnant :discord.Member , perdant: discord.Member, jeu : str) :
    guild=interaction.guild
    await interaction.response.defer(ephemeral=True)
    prisonnier=discord.utils.get(interaction.guild.roles  ,id=prisonnier_id)
    logcha=discord.utils.get(guild.channels, id=logs_id)
    n=0
    if perdant.id==ludobot_id :
        await interaction.followup.send("Tu peux pas Slay le Ludobot, tu te prends pour qui ?",ephemeral=True)
        await prisontime(guild,interaction.user)
        if prisonnier in interaction.user.roles:
            boom=f'Jour d\'infamie à Ludopoly ! Dans un élan d\'orgeuil, {interaction.user.mention} a tenté de commettre l\'impensable ! Grande sera sa punition !'
            await interaction.guild.get_channel(ludann_id).send(boom)
        return
    
    if gagnant.id==ludobot_id:
        await interaction.followup.send("Le Ludobot n'a besoin de slay personne",ephemeral=True)
        return
    
    if gagnant.id == feur_id or perdant.id==feur_id:
        await interaction.followup.send("Feur !")
        return
    jeu=jeu.strip().lower().capitalize()
    game=jeu+" Master"
    comite=discord.utils.get(interaction.guild.roles  ,id=comite_id)
    if  comite in gagnant.roles :
        n=n+1
    if  comite in perdant.roles :
        n=n+1
    if(n==0):
        await interaction.followup.send("Aucun membre spécifié n'est comité",ephemeral=True)
        return
    await masterchange(interaction.guild,gagnant,perdant,jeu)
    if (n==2):
        
        boom=f'Oyez oyez ! Après avoir triomphé sur {perdant.mention}, {gagnant.mention} prends le titre de {game} !'
        await interaction.guild.get_channel(ludann_id).send(boom)
        await slay(interaction.guild,gagnant,perdant.id)
        await interaction.followup.send("it is done")
        return
    if (n==1):
            if perdant.id in Lidcomte :
                await slay(interaction.guild,gagnant,perdant.id)
            if   not comite in perdant.roles :
                await interaction.followup.send("C'est bon",ephemeral=True)
                hehe=f'Oyez oyez ! Face à {perdant.mention}, {gagnant.mention} réussi à défendre sa position pour devenir {game} !'
                await interaction.guild.get_channel(ludann_id).send(hehe)
                return
            nom= findname(perdant.id)
            if nom==None:
                await interaction.followup.send("Erreur comité",ephemeral=True)
                return   
            
            if not prisonnier in gagnant.roles :
                await interaction.followup.send("La cible n'est pas en prison",ephemeral=True)
                return
            await slay(interaction.guild,gagnant,perdant.id)
            await freedom(interaction.guild, gagnant)
            
            
            await interaction.followup.send("Opération réussie",ephemeral=True)
            victor_phrase=f'Oyez oyez ! {gagnant.mention} à triomphé de {perdant.mention} au {jeu} et a obtenu la liberté !'
            await interaction.guild.get_channel(ludann_id).send(victor_phrase)
            reset_count(gagnant)



@client.tree.command(name="emprunt", description="Emprunter un jeu",guild=LuluServ)
@app_commands.describe(nom_jeu="Nom complet du jeu à emprunter",date="Date de récupération (JJ/MM/AAAA)",heure="Heure de récupération (HH:MM)")
async def  emprunt(interaction: discord.Interaction, nom_jeu: str, date: str, heure: str):
    await emprun(interaction, nom_jeu, date, heure)
    #interaction.response.send_message("hello") 


@client.tree.command(name="dé",description="Lance un dé à val faces", guild=LuluServ)
@app_commands.describe(val=">1 : Nombre de faces")
async def dice(interaction : discord.Interaction, val: int) :
        GUILD=interaction.guild
        await interaction.response.defer()
        if val <= 1 :
            await interaction.followup.send(content="Je vais te retrouver si tu continues à mettre des valeurs comme ça") 
        else :
            num=ra.randint(1,val)
            if val ==6 :
                if num==1:
                    #await prisontime(GUILD, interaction.user)
                    add_count(interaction.user)
                mots=f'{interaction.user.mention} à lancé {1} d{val} et à fait {num} : '+list6[num-1]
                await interaction.followup.send(content=mots)
            else :
                if num==1:
                    #await prisontime(GUILD, interaction.user)
                    add_count(interaction.user)
                numv=((1-dlim)*num+dlim-val)/(1-val)
                
                if (num<dlim) and (num>dlim-1) :
                    
                    try :
                        mots=f'{interaction.user.mention} à lancé {1} d{val} et à fait {dlim} : {list10[dlim-1]}'
                        await interaction.followup.send(content=mots)
                    except:
                        await interaction.followup.send(content="Il y a un truc chelou avec les dés fin")
                else :
                    
                    try:
                        numv=ma.ceil(numv)
                        mots=f'{interaction.user.mention} à lancé {1} d{val} et à fait {num} : {list10[numv-1]}'
                        await interaction.followup.send(content=mots)  
                    except:
                        await interaction.followup.send(content="Il y a un truc chelou avec les dés")


client.run(TOKEN)





#Pour plus tard
#await interaction.response.defer(ephemeral=True)
#await interaction.followup.send("bla",ephemeral=True)
