import discord
import re
import random as ra
import math as ma
from discord.ext import commands
from discord import app_commands
import os
from keepalive import keep_alive

TOKEN=os.getenv("DISCORD_TOKEN")

Lcomité=list()
Lcomité.append("Lucas")
Lcomité.append("Nathan") 
Lcomité.append("André")
Lcomité.append("Mathis")
Lcomité.append("Roy")
Lcomité.append("Blanche")
Lcomité.append("Alonso")
Lcomité.append("Léo")
Lcomité.append("Titouan")
Lcomité.append("Éric")
Lcomité.append("Eric")


list6=list()
list6.append("J'espère pour toi que t'auras pas cette note à l'exa")
list6.append("Aïe, coup dur pour Guillaume")
list6.append("C'est juste au milieu, mais ça ne passe pas")
list6.append("C'est bon on passe")
list6.append("Très propre franchement")
list6.append("Félicitations ! Tu as transcendé la condition humaine !")

list20=list()
list20.append("C'est ciao pour toi.")
list20.append("C'est pas passé loin !")
list20.append("")
list20.append("")
list20.append("")
list20.append("")
list20.append("")
list20.append("")
list20.append("")
list20.append("")
list20.append("")
list20.append("")
list20.append("")
list20.append("")
list20.append("")
list20.append("")
list20.append("")
list20.append("")
list20.append("")
list20.append("Excellent ça !")

trucs=list()
trucs.append("jesuis")
trucs.append("jsuis")
trucs.append("chuis")
trucs.append("chui")
trucs.append("im")
trucs.append("iam")

#variable globales (Chapellier va rien faire contre moi)
LudopServId=1361756747303358524

prison_id=1361761128438563146
prisonnier_id=1373418119078346833
chabienv_id=1361763187799756890

def iscomité (mot :str) :
    mot=mot.lower()
    mot=re.sub(r"[^a-z0-9àâçéèêëîïôûùüÿñæœ\s]", " ", mot)
    mot= mot.replace(" ","")
    for name in Lcomité :
        if name!="Eric":
            if mot ==name.lower() :
                return name
        elif mot=="Eric".lower():
            return "Éric"
    return None



def islol(word) :
    words=word.lower()
    words = re.sub(r'[^a-z0-9\s]', '', words)
    words= words.replace(" ","")
    if "lol" in words :
        return True  
    elif "leagueoflegend" in words :
        return True
    else :
        return False    


def lolbad() :
    b=6
    n=ra.randint(0, b)
    if n==0 :
        return "LoL is bad."
    elif n==1 :
        return "LoL is evil."
    elif n==2 :
        return "LoL est une addiction."
    elif n==3 :
        return "LoL est mauvais."
    elif n==4 :
        return "LoL ne doit pas être utilisé."
    elif n==5 :
        return "LoL is not good."
    elif n==6 :
        return "LoL n'est pas bien."
    
keep_alive()

async def plusrole (role :discord.Role, user: discord.Member):
    if (not role in user.roles) :
        await user.add_roles(role)

async def minusrole (role: discord.Role, user: discord.Member):
    if role in user.roles and user and role:
        await user.remove_roles(role)


async def prisontime(guild : discord.guild, user: discord.Member) :
    prisonnier=discord.utils.get(guild.roles  ,id=prisonnier_id)
    peuple=discord.utils.get(guild.roles,id=1373305997053136936)
    print(type(guild))
    print(type(user))
    await minusrole(peuple,user)
    await plusrole(prisonnier,user)


async def freedom(guild, user) :
    prisonnier=discord.utils.get(guild.roles  ,id=prisonnier_id)
    peuple=discord.utils.get(guild.roles,id=1373305997053136936)
    print(type(guild))
    print(type(user))
    await minusrole(prisonnier,user)
    await plusrole(peuple,user)


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
#Version faite par IA car je ne sais pas comment traiter les cas super compliqués
FRENCH_PATTERNS = [
    re.compile(r"\bje[\s_\-]*suis\b", re.IGNORECASE),
    re.compile(r"\bjsuis\b", re.IGNORECASE),
    re.compile(r"\bchuis\b", re.IGNORECASE),
    re.compile(r"\bchui\b", re.IGNORECASE),
]

ENGLISH_PATTERNS = [
    re.compile(r"\bi(?:\W|_)*m\b", re.IGNORECASE),   # matches I'm / I’m / i-m / i m / im
    re.compile(r"\bi(?:\W|_)*am\b", re.IGNORECASE),  # matches I am / I_am / iam
]

def dadtrigger(text: str) -> tuple[int, re.Match | None]:
    text=text.lower()
    for pat in FRENCH_PATTERNS:
        m = pat.search(text)
        if m:
            return (1, m)
    for pat in ENGLISH_PATTERNS:
        m = pat.search(text)
        if m:
            return (2, m)
    return (0, None)

def finddad(text: str, match: re.Match) -> str:
    after = text[match.end():].strip()
    # Cut at punctuation or end of string
    m = re.match(r"([a-zàâçéèêëîïôûùüÿñæœ\s'’]+)", after, re.IGNORECASE)
    return m.group(1).strip() if m else after
#Fin du truc IA 

def dad(texte:str) :
    num, match= dadtrigger(texte)
    if num==0 :
        return None
    bla=finddad(texte,match)
    if num==1 :
        
        mots="Bonjour "+ bla+" ! Je suis Ludobot !"
        return mots
    else  :
        mots="Hi "+bla+" ! I'm Ludobot !"
        return mots

    

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
        bienvenue=f'Bienvenue {member.mention}, tu commence ta vie ici dans la {member.guild.get_channel(prison_id)}, regarde le message pin là bas'
        prisonnier=discord.utils.get(member.guild.roles,id=prison_id)
        await prisontime(member.guild, member)
        print(bienvenue)
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
            phrase=dad(message.content)
            if (phrase!=None):
                if "@" in phrase:
                    await message.channel.send("Bien essayé !")
                else:
                    await message.channel.send(phrase)
            elif islol(message.content):
                await message.channel.send(lolbad())

@client.tree.command(name="lolisgood",description="Interdit ça", guild=LuluServ)
async def lolisgood(interaction : discord.Interaction) :
        GUILD=interaction.guild
        await interaction.response.send_message(f'{interaction.user.mention} a choisi le chemin du mal.')
        await prisontime(GUILD, interaction.user)

@client.tree.command(name="exécution",description="Retirer le rôle peuple de la cible et la place en prison",guild=LuluServ)
async def kill(interaction: discord.Interaction, cible :discord.User ):
    GUILD=interaction.guild
    try:
        await prisontime(GUILD, cible)
        await interaction.response.send_message("Cible éliminée",ephemeral=True)
    except:
        await interaction.response.send_message("Erreur",ephemeral=True)


@client.tree.command(name="victoire",description="Libère cible, et lui donne le rôle 'comité' slayer et 'jeu' master",guild=LuluServ)
async def victoire(interaction: discord.Interaction, cible :discord.User , comité: str, jeu : str) :
    await interaction.response.defer(ephemeral=True)
    nom=iscomité(comité)
    if nom == None:
        await interaction.followup.send("Nom de membre du comité invalide",ephemeral=True)
        return
    envoyer=nom+" Slayer"
    rolle=discord.utils.get(interaction.guild.roles  ,name=envoyer)
    await freedom(interaction.guild, cible)
    await plusrole(rolle, cible)
    game=jeu +" Master"
    attempt=discord.utils.get(interaction.guild.roles  ,name=game)
    if attempt :
        await plusrole(attempt, cible)
    else :
        await interaction.guild.create_role(name=game,colour=discord.Colour(0xe74c3c))
        rolls=discord.utils.get(interaction.guild.roles  ,name=game)
        await plusrole(rolls, cible)
    await interaction.followup.send("Opération réussie",ephemeral=True)
    victor_phrase=f'Oyez oyez ! {cible.mention} à triomphé de {nom} au {jeu} et a obtenu la liberté !'
    await interaction.guild.get_channel(prison_id).send(victor_phrase)





@client.tree.command(name="dé",description="Lance un dé. val>1 correspond au nombre de faces", guild=LuluServ)
async def dice(interaction : discord.Interaction, val: int) :
        GUILD=interaction.guild
        if val <= 1 :
            await interaction.response.send_message("Je vais te retrouver si tu continues à mettre des valeurs comme ça") 
        else :

            num=ra.randint(1,val)
            if val ==6 :
                if num==1:
                    await prisontime(GUILD, interaction.user)
                mots=f'{interaction.user.mention} à lancé {1} d{val} et à fait {num} : '+list6[num-1]
                await interaction.response.send_message(mots)
            else :
                if num==1:
                    await prisontime(GUILD, interaction.user)
                numv=((1-20)*num+20-val)/(1-val)
                if (num<20) and (num>19) :
                    mots=f'{interaction.user.mention} à lancé {1} d{val} et à fait {19} : '+list20[19-1]
                    await interaction.response.send_message(mots)
                else :
                    numv=ma.ceil(numv)
                    mots=f'{interaction.user.mention} à lancé {1} d{val} et à fait {num} : '+list20[numv-1]
                    await interaction.response.send_message(mots)  

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
                        mots=f'{interaction.user.mention} à lancé {1} d{val} et à fait {19} : '+list20[19-1]
                        await interaction.response.send_message(mots)
                    else :
                        num=ma.ceil(num)
                        mots=f'{interaction.user.mention} à lancé {1} d{val} et à fait {num} : '+list20[num-1]
                        await interaction.response.send_message(mots)  
"""

client.run(TOKEN)
#client.run(os.getenv("DISCORD_TOKEN"))




#Pour plus tard
#await interaction.response.defer(ephemeral=True)
#await interaction.followup.send("bla",ephemeral=True)