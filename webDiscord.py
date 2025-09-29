import discord
import re
import random as ra
import math as ma
from discord.ext import commands
from discord import app_commands
import os
from keepalive import keep_alive
from eric import emprun

TOKEN=os.getenv("DISCORD_TOKEN")
Dad_Limit=os.getenv("Dad_Limit")
dlim=os.getenv("dé_limit")

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
Lcomité.append("Thomas")
Lcomité.append("Sébastien")
Lcomité.append("Éric")
Lcomité.append("Eric")

Lidcomte=list()
Lidcomte.append(282237085908467713)#andré
Lidcomte.append(259772130516795392)#thomas
Lidcomte.append(633975303756185603)#blanche
Lidcomte.append(579395206680412172)#leo
Lidcomte.append(1165720948851355761)#lucas
Lidcomte.append(697405782429270018)#éric
Lidcomte.append(364435666039341056)#mathis
Lidcomte.append(559073108443660499)#roy
Lidcomte.append(444068012249710593)#pochita
Lidcomte.append(830494223794831422) #séba
Lidcomte.append(556476223354830879) #titou
Lidcomte.append(149928233201172480) #nathan

Allcomite=list()
Allcomite.append([282237085908467713,"André"])
Allcomite.append([259772130516795392,"Thomas"])
Allcomite.append([633975303756185603,"Blanche"])
Allcomite.append([579395206680412172,"Léo"])
Allcomite.append([1165720948851355761,"Lucas"])
Allcomite.append([697405782429270018,"Éric"])
Allcomite.append([364435666039341056,"Mathis"])
Allcomite.append([559073108443660499,"Roy"])
Allcomite.append([444068012249710593,"Alonso"])
Allcomite.append([830494223794831422,"Sébastien"])
Allcomite.append([556476223354830879,"Titouan"])
Allcomite.append([149928233201172480,"Nathan"])


list6=list()
list6.append("J'espère pour toi que t'auras pas cette note à l'exa")
list6.append("Aïe, coup dur pour Guillaume")
list6.append("C'est juste au milieu, mais ça ne passe pas")
list6.append("C'est bon on passe")
list6.append("Très propre franchement")
list6.append("Félicitations ! Tu as transcendé la condition humaine !")

list10=list()
list10.append("C'est ciao pour toi.")
list10.append("C'est pas passé loin !")
list10.append("C'est pas ton jour aujourd'hui dit-donc.")
list10.append("Pas fifou ça.")
list10.append("C'est moyen, littéralement.")
list10.append("T'aimes bien passer juste non ?")
list10.append("Ça commence à devenir bon.")
list10.append("Impressionnant.")
list10.append("On approche de la perfection !")
list10.append("Excellent ça !")

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
ludann_id=1416834037183418439
admin_id=1361760489268318228
comite_id=1407440127210422383
mauvais_id=1417910380138725396
logs_id=1422224976605610115

def findname( comiteid ):
    for i in Allcomite:
        if i[0]==comiteid:
            return i[1]
    return None


def add_count (cible : discord.member) :
    iden=cible.id
    return

def reset_count( cible:discord.member):
    iden=cible.id
    return

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
    b=10
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
    elif n==7:
        return "Il ne faut pas jouer à LoL."
    elif n==8:
        return "LoL est une abomination."
    elif n==9:
        return "Il faut arrêter LoL et prendre une douche à la place."
    elif n==10:
        return "LoL mène le monde à sa perte."
    
keep_alive()

async def imnotreadingthat(message :discord.message):
    try :
        with open('notread.png', 'rb') as f:
            picture = discord.File(f)
            await message.channel.send(file=picture)
    except:
        await message.channel.send("Je ne lirais pas ça")

async def plusrole (role :discord.Role, user: discord.Member):
    if (not role in user.roles) :
        await user.add_roles(role)

async def minusrole (role: discord.Role, user: discord.Member):
    if role in user.roles and user and role:
        await user.remove_roles(role)


async def prisontime(guild : discord.guild, user: discord.Member) :
    admin=discord.utils.get(guild.roles, id=admin_id)
    if admin in user.roles:
        return
    prisonnier=discord.utils.get(guild.roles  ,id=prisonnier_id)
    peuple=discord.utils.get(guild.roles,id=1373305997053136936)
    comite=discord.utils.get(guild.roles  ,id=comite_id)
    await minusrole(comite,user)
    await minusrole(peuple,user)
    await plusrole(prisonnier,user)



async def freedom(guild:discord.guild, user:discord.member) :
    prisonnier=discord.utils.get(guild.roles  ,id=prisonnier_id)
    peuple=discord.utils.get(guild.roles,id=1373305997053136936)
    comite=discord.utils.get(guild.roles  ,id=comite_id)
    await minusrole(prisonnier,user)
    await plusrole(peuple,user)
    if user.id in Lidcomte:
        await plusrole(comite,user)


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
    if islol(bla):
        if num==1 :
            mots="Bonjour "+ bla+" ! Je suis Ludobot, le plus grand hater de LoL !"
            return mots
        else  :
            mots="Hi "+bla+" ! I'm Ludobot, LoL's n°1 hater !"
            return mots
    else :
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
                if (len(phrase)>Dad_Limit) :
                    await message.channel.send(content="C'est beaucoup trop de mots, je ne lis pas ça")
                if "@" in phrase:
                    await message.channel.send("Bien essayé !")
                else:
                    await message.channel.send(phrase)
            elif islol(message.content):
                await message.channel.send(lolbad())

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
    try:
        await prisontime(GUILD, cible)
        await interaction.response.send_message("Cible éliminée",ephemeral=True)
        channel = discord.utils.get(GUILD.channels, id=ludann_id)
        await channel.send(content=f'{cible.mention} monte sur l\'échafaud.')
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




@client.tree.command(name="victoire",description="Libère cible, et lui donne le rôle 'comité' slayer et 'jeu' master",guild=LuluServ)
@app_commands.describe(cible="Membre à libérer", comité="Membre du Comité vaincu",jeu="Jeu d'affrontement")
async def victoire(interaction: discord.Interaction, cible :discord.Member , comité: discord.Member, jeu : str) :
    await interaction.response.defer(ephemeral=True)
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
    jeu=jeu.strip().lower().capitalize()
    game=jeu +" Master"
    attempt=discord.utils.get(interaction.guild.roles  ,name=game)
    if attempt :
        await plusrole(attempt, cible)
    else :
        await interaction.guild.create_role(name=game,colour=discord.Colour(0xe74c3c))
        rolls=discord.utils.get(interaction.guild.roles  ,name=game)
        await plusrole(rolls, cible)
    await interaction.followup.send("Opération réussie",ephemeral=True)
    victor_phrase=f'Oyez oyez ! {cible.mention} à triomphé de {comité.mention} au {jeu} et a obtenu la liberté !'
    await interaction.guild.get_channel(ludann_id).send(victor_phrase)
    reset_count(cible)




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
            await interaction.response.send_message(content="Je vais te retrouver si tu continues à mettre des valeurs comme ça") 
        else :
            num=ra.randint(1,val)
            logcha= discord.utils.get(GUILD.channels,id=logs_id)
            await logcha.send(f'dé de {val} lancé donne {num}')
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
                if (num<dlim) and (num>dlim) :
                    try :
                        mots=f'{interaction.user.mention} à lancé {1} d{val} et à fait {dlim} : '+list10[dlim-1]
                        await interaction.followup.send(content=mots)
                    except:
                        await interaction.followup.send(content="Il y a un truc chelou avec les dés fin")
                else :
                    try:
                        numv=ma.ceil(numv)
                        mots=f'{interaction.user.mention} à lancé {1} d{val} et à fait {num} : '+list10[numv-1]
                        await interaction.followup.send(content=mots)  
                    except:
                        await interaction.followup.send(content="Il y a un truc chelou avec les dés")

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

client.run(TOKEN)
#client.run(os.getenv("DISCORD_TOKEN"))




#Pour plus tard
#await interaction.response.defer(ephemeral=True)
#await interaction.followup.send("bla",ephemeral=True)
