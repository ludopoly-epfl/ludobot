import discord
import re
import random as ra
import math as ma
from discord.ext import commands
from discord import app_commands

from outilsCheck import islol,iscomité,findname,isnatel,dad
from comité import Lcomité,Lidcomte,Allcomite
from variablesglobales import Gandalf_id,bigE_id,chabienv_id,comite_id,prison_id,prisonnier_id,ludann_id,logs_id,LudopServId,imperium_id,magic_id,mauvais_id,admin_id,list6,list10,trucs


async def imnotreadingthat(message :discord.message):
    try :
        with open('notread.png', 'rb') as f:
            picture = discord.File(f)
            await message.channel.send(file=picture)
    except:
        await message.channel.send("Je ne lirais pas ça")

async def plusrole (role :discord.Role, user: discord.Member):
    try :
        if not (role in user.roles):
            await user.add_roles(role)
    except:
        logcha=discord.utils.get(role.guild.channels, id=logs_id)
        logcha.send("Les roles ne rolent pas bien")

 

async def minusrole (role: discord.Role, user: discord.Member):
    if role in user.roles and user and role:
        await user.remove_roles(role)

async def checkrole (roleid :int, user: discord.Member ,guild :discord.guild):
    role =discord.utils.get(guild.roles  ,id=roleid)
    return role in user.roles and user and role


async def prisontime(guild : discord.guild, user: discord.Member) :
    admin=discord.utils.get(guild.roles, id=admin_id)
    if admin in user.roles:
        return
    prisonnier=discord.utils.get(guild.roles  ,id=prisonnier_id)
    peuple=discord.utils.get(guild.roles,id=1373305997053136936)
    comite=discord.utils.get(guild.roles  ,id=comite_id)
    mauvais=discord.utils.get(guild.roles  ,id=mauvais_id)
    await minusrole(comite,user)
    await minusrole(peuple,user)
    await minusrole(mauvais,user)
    await plusrole(prisonnier,user)



async def freedom(guild:discord.guild, user:discord.member) :
    logcha=discord.utils.get(guild.channels, id=logs_id)
    prisonnier=discord.utils.get(guild.roles  ,id=prisonnier_id)
    peuple=discord.utils.get(guild.roles,id=1373305997053136936)
    comite=discord.utils.get(guild.roles  ,id=comite_id)
    await minusrole(prisonnier,user)
    await plusrole(peuple,user)
    if user.id in Lidcomte:
        nam=findname(user.id)
        logcha.send(f' {nam} has breached containment')
        await plusrole(comite,user)


async def masterchange(guild:discord.guild, W:discord.Member, L:discord.Member, jeu:str):
    logcha=discord.utils.get(guild.channels, id=logs_id)
    jeu=jeu.strip().lower().capitalize()
    game=jeu +" Master"
    fallen=False
    attempt=discord.utils.get(guild.roles  ,name=game)
    if attempt :
        await plusrole(attempt, W)
        if attempt in L.roles :
            await minusrole(attempt,L)
            fallen=True
    else :
        await guild.create_role(name=game,colour=discord.Colour(0xe74c3c))
        rolls=discord.utils.get(guild.roles  ,name=game)
        await plusrole(rolls, W)
        if rolls in L.roles :
            await minusrole(rolls,L)
            fallen=True
    gameL="Fallen "+jeu +" Master"
    attempt1=discord.utils.get(guild.roles  ,name=gameL)
    
    if attempt1 :
        if fallen :
            await plusrole(attempt1, L)
        await minusrole(attempt1,W)
    else :
        if fallen :
            await guild.create_role(name=gameL,colour=discord.Colour(0x455a95))
            rolls1=discord.utils.get(guild.roles  ,name=gameL)
            await plusrole(rolls1, L)
            await minusrole(rolls1,W)
    await logcha.send(f'Changement roles : {jeu}  Gagnant = {W.name} Perdant = {L.name} fallen = {fallen} ')


async def slay(guild:discord.guild ,W:discord.Member, id_L: int):
    name=findname(id_L)
    logcha=discord.utils.get(guild.channels, id=logs_id)
    Nrole= name+" Slayer"
    rolle=discord.utils.get(guild.roles  ,name=Nrole)
    await plusrole(rolle, W)
    logcha.send(f'{name} has fallen')
