
""" Version pas finie faite par moi car trop compliqué
def dadtrigger(word :str): #détecte si dad doit parler
    words=word.lower()
    words = re.sub(r'[^a-z0-9\s]', '', words)
    words= words.replace(" ","")
    if ("jesuis" in words) :
        return 1
    elif ("jsuis" in words) :
        return 2
    elif ("chuis" in words) :
        return 3
    elif "chui" in words:
        return 4
    elif ("im" in words) :
        return 5
    elif ("iam" in words):
        return 6
    else :
        return 0
    
def finddad(mots :str, key :str ) : #donne le texte avec "je suis" en moins
    mots=mots.lower()
    id=mots.find(key)
    res= mots[id+len(key):]
    return res 
"""



#@client.tree.command(name="victoire",description="Libère cible, et lui donne le rôle 'comité' slayer et 'jeu' master",guild=LuluServ)
#@app_commands.describe(cible="Membre à libérer", comité="Membre du Comité vaincu",jeu="Jeu d'affrontement")
"""async def victoire(interaction: discord.Interaction, cible :discord.Member , comité: discord.Member, jeu : str) :
    #await interaction.response.defer(ephemeral=True)
    comite=discord.utils.get(interaction.guild.roles  ,id=comite_id)
    if   not comite in comité.roles :
        await interaction.followup.send("Membre de comité invalide",ephemeral=True)
        return
    nom= findname(comité.id)
    if nom==None:
        await interaction.followup.send("Erreur comité",ephemeral=True)
        return   
    prisonnier=discord.utils.get(interaction.guild.roles  ,id=prisonnier_id)
    if not prisonnier in cible.roles :
        await interaction.followup.send("La cible n'est pas en prison",ephemeral=True)
        return
    envoyer=nom+" Slayer"
    rolle=discord.utils.get(interaction.guild.roles  ,name=envoyer)
    await freedom(interaction.guild, cible)
    await plusrole(rolle, cible)
    masterchange(interaction.guild, cible, comité, jeu)
    await interaction.followup.send("Opération réussie",ephemeral=True)
    victor_phrase=f'Oyez oyez ! {cible.mention} à triomphé de {comité.mention} au {jeu} et a obtenu la liberté !'
    await interaction.guild.get_channel(ludann_id).send(victor_phrase)
    reset_count(cible)
"""



"""
@client.tree.command(name="dé",description="Lance un dé. Val et la taille du dé et nb le nombre de dés lancés.", guild=GUILD_ID)
async def dice(interaction : discord.Interaction, val: int, nb:int) :
        if val <= 0 or nb<= 0 :
            await interaction.response.send_message("Je vais te retrouver si tu continues à mettre des valeurs comme ça") 
        else :
            for k in range(nb) :
                num=ra.randint(1,val)
                if val ==6 :
                    mots=f'{interaction.user.mention} à lancé {1} d{val} et à fait {num} : '+list6[num-1]
                    await interaction.response.send_message(mots)
                else :
                    num=((1-20)*num+20-val)/(1-val)
                    if (num<20) and (num>19) :
                        mots=f'{interaction.user.mention} à lancé {1} d{val} et à fait {19} : '+list10[19-1]
                        await interaction.response.send_message(mots)
                    else :
                        num=ma.ceil(num)
                        mots=f'{interaction.user.mention} à lancé {1} d{val} et à fait {num} : '+list10[num-1]
                        await interaction.response.send_message(mots)  
"""


#client.run(os.getenv("DISCORD_TOKEN"))

