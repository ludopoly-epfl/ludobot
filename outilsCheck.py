import re
from comité import Lcomité,Lidcomte,Allcomite
import discord
from variablesglobales import twi_id
#Toutes les fonctions utilisées pour vérifier des conditions sont dedans 



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
    
def findname( comiteid ):
    for i in Allcomite:
        if i[0]==comiteid:
            return i[1]
    return None

def isnatel(word) :
    words=word.lower()
    words = re.sub(r'[^a-z0-9\s]', '', words)
    words= words.replace(" ","")
    if "natel" in words :
        return True  
    else :
        return False   
    



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
        
async def amogus_cond( message: discord.message):
    channel=message.channel
    twil=discord.utils.get(message.author.guild.channels, id=twi_id)
    nathan_id=149928233201172480
    return (channel==twil and message.author.id==nathan_id) or ("amogus" in message.content)