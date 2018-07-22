import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import random
import pickle
import os
import os.path
import requests
import json
import time
from gtts import gTTS

Client = discord.Client()
bot_prefix= "v!"
client = commands.Bot(command_prefix=bot_prefix)
server = discord.Server(id='426680388002250753')
footer_text = "Violets™"
error_img = ':warning:'
default_invite = 'https://discord.gg/GnkADTA'
banner = 'https://cdn.discordapp.com/attachments/403309394139545600/467636297989750794/ezgif.com-video-to-gif_1.gif'

#roles
member_role = '464963766027812880'
punished_role = '464963800043356160'
helper_role = '464963841588199440'
mod_role = '464963897871564800'
admin_role = '464963985889034250'
manager_role = '464963985889034250'
owner_role = '464964048065396746'
partner_role = '469369789585031178'
logs = '470464384725024768'



#Welcome and Leave

@client.event
async def on_ready():
    t1 = time.perf_counter()
    print("============================================================")
    print("Name: {}".format(client.user.name))
    print("ID: {}".format(client.user.id))
    print("============================================================")
    await client.change_presence(game=discord.Game(name='on Violets™'))
    await client.wait_until_ready()
    t2 = time.perf_counter()
    print("Ping: {}".format(round((t2-t1)*1000)))
    print("============================================================")
    
@client.async_event
async def on_member_join(userName: discord.User):
    m2 = "Welcome to **Violets**, <@{}>! We hope you enjoy your stay and have fun.".format(userName.id)
    m2 += "\nAll information is in the <#426683264682557440> channel, but feel free to ask the staff about anything you want to know."
    m2 += "\https://gph.is/2lnKhvK"
    m = "\n**Welcome to Violets™ <@{}>! :sparkles:".format(userName.id)
    m += "\nPlease make sure to read the rules and if you want to partner, contact any of the staff with the role Partnership Manager :smiley:"
    m += "\nAlso don't forget to get roles and colors in the <#440562714989821982> and the <#427124007377305611> channels :wink: \nEnjoy your stay :sparkling_heart:**"
    m += "\nhttps://gph.is/2lnKhvK"
    await client.send_message(client.get_channel("426680388585521163"), "{}".format(m))
    server = client.get_server('426680388002250753')
    await client.send_message(client.get_channel("429874952934785025"), ":large_blue_circle: `{}` joined the server! Now we have {} members.".format(userName, len(server.members)))
    try:
        await client.send_message(userName, "{}".format(m2))
    except:
        print("")

@client.async_event
async def on_member_remove(userName: discord.User):
    leaves = ["Cya `{}` :wave:".format(userName)]
    await client.send_message(client.get_channel("426680388585521163"), "{}".format(random.choice(leaves)))
    print("Leave")
    
#EMOTES

huglinks = ["https://i.imgur.com/yE2RnXK.gif",
            "https://i.imgur.com/R9sYxk8.gif",
            "https://i.imgur.com/iLBEoKv.gif",
            "https://i.imgur.com/cc554e8.gif",
            "https://i.imgur.com/1dqkjHe.gif",
            "https://i.imgur.com/Ph8GTqg.gif",
            "https://i.imgur.com/G6EnOxd.gif",
            "https://i.imgur.com/ZxwHn5Y.gif",
            "https://i.imgur.com/movPIsP.gif",
            "https://i.imgur.com/tKlfSgo.gif",
            "https://i.imgur.com/ICg9nCr.gif",
            "https://i.imgur.com/yC95DC2.gif",
            "https://i.imgur.com/hRYXNKX.gif",
            "https://i.imgur.com/br3bGQc.gif",
            "https://i.imgur.com/IcNGAQD.gif"]

patlinks = ["https://i.imgur.com/8eApUKG.gif",
            "https://i.imgur.com/qVcP9Pt.gif",
            "https://i.imgur.com/X9hKO2p.gif",
            "https://i.imgur.com/v8cRPH9.gif",
            "https://i.imgur.com/N6C7C30.gif",
            "https://i.imgur.com/M9QPcY6.gif",
            "https://i.imgur.com/oUSdjX6.gif",
            "https://i.imgur.com/mFFr4e0.gif",
            "https://i.imgur.com/3F7kmCd.gif",
            "https://i.imgur.com/7yFvJ6m.gif",
            "https://i.imgur.com/y3La9yP.gif"]

kisslinks = ["https://i.imgur.com/0Ri9sfq.gif",
             "https://i.imgur.com/EMdpmXW.gif",
             "https://i.imgur.com/Y9iLoiv.gif",
             "https://i.imgur.com/ZlqZy8S.gif",
             "https://i.imgur.com/ySav1IQ.gif",
             "https://i.imgur.com/ZGfrn2d.gif",
             "https://i.imgur.com/glwWeUl.gif",
             "https://i.imgur.com/j5hDl7V.gif",
             "https://i.imgur.com/w7mVYty.gif",
             "https://i.imgur.com/FJ5bckO.gif",
             "https://i.imgur.com/KqVmVU7.gif",
             "https://i.imgur.com/EM1C9a6.gif",
             "https://i.imgur.com/TACVpH9.gif",
             "https://i.imgur.com/opiHLtc.gif",
             "https://i.imgur.com/LylJAea.gif"]

nomlinks = ["https://i.imgur.com/E1eQPfu.gif",
            "https://i.imgur.com/UUZY3Rb.gif",
            "https://i.imgur.com/Zd6fIpA.gif",
            "https://i.imgur.com/i2NaBS7.gif",
            "https://i.imgur.com/Up5J6Nn.gif",
            "https://i.imgur.com/J5MLku7.gif",
            "https://i.imgur.com/7yYgZXE.gif"]

throwlinks = ["https://i.imgur.com/o9j2oNi.gif",
              "https://i.imgur.com/wSb8aux.gif",
              "https://i.imgur.com/QO8TrkK.gif",
              "https://i.imgur.com/Ts3Cc52.gif",
              "https://i.imgur.com/D3ggzfW.gif",
              "https://i.imgur.com/eD5mE7R.gif",
              "https://i.imgur.com/JCUipZJ.gif",
              "https://i.imgur.com/VSg0YLw.gif",
              "https://i.imgur.com/8mUufrm.gif"]

bitelinks = ["https://i.imgur.com/E0jIIa9.gif",
             "https://i.imgur.com/Nvkw6hN.gif",
             "https://i.imgur.com/wr7l06j.gif",
             "https://i.imgur.com/uce91VI.gif"]

bloodsucklinks = ["https://i.imgur.com/UbaeYIq.gif",
                  "https://i.imgur.com/qi83Eft.gif",
                  "https://i.imgur.com/CtwmzpG.gif",
                  "https://i.imgur.com/DAuEJ2F.gif",
                  "https://i.imgur.com/By6IGzq.gif"]

cuddlelinks = ["https://i.imgur.com/GWNWcLH.gif",
               "https://i.imgur.com/i3Eqqgz.gif",
               "https://i.imgur.com/GpFk6fE.gif",
               "https://i.imgur.com/mc3Z7wf.gif",
               "https://i.imgur.com/N5JYB5r.gif",
               "https://i.imgur.com/PGp8JYq.gif"]

highfivelinks = ["https://i.imgur.com/hjoQeOt.gif",
                 "https://i.imgur.com/9nhheqT.gif",
                 "https://i.imgur.com/yw3xMOu.gif",
                 "https://i.imgur.com/Y4g5fsT.gif",
                 "https://i.imgur.com/p6Hvx5r.gif",
                 "https://i.imgur.com/33nuO9D.gif",
                 "https://i.imgur.com/uFQnmYa.gif",
                 "https://i.imgur.com/9KG3k2n.gif",
                 "https://i.imgur.com/nHCC1ps.gif",
                 "https://i.imgur.com/aKvaNba.gif",
                 "http://i.imgur.com/hnHR29x.gif"]

pokelinks = ["https://i.imgur.com/HAAktbl.gif",
             "https://i.imgur.com/Fmd0Rsu.gif",
             "https://i.imgur.com/1rObSM3.gif",
             "https://i.imgur.com/Wo2fc94.gif",
             "https://i.imgur.com/rtTucBW.gif",
             "https://i.imgur.com/4c2mC5d.gif",
             "https://i.imgur.com/1DVD84G.gif"]

slaplinks = ["https://i.imgur.com/EAF42MG.gif",
             "https://i.imgur.com/tLTT9Q4.gif",
             "https://i.imgur.com/tEWjg7v.gif",
             "https://i.imgur.com/MlkLTjv.gif",
             "https://i.imgur.com/hoTYJZP.gif",
             "https://i.imgur.com/Pthhs3Y.gif"]


punchlinks = ["https://i.imgur.com/T2HdIv8.gif",
              "https://i.imgur.com/LZz65rg.gif",
              "https://i.imgur.com/FqPBIf3.gif",
              "https://i.imgur.com/KmqPDQG.gif",
              "https://i.imgur.com/yEx4aKu.gif"]

starelinks = ["https://i.imgur.com/f8rFNH0.gif",
              "https://i.imgur.com/ACCQDj4.gif",
              "https://i.imgur.com/1Co1i9t.gif",
              "https://i.imgur.com/uPZHQxV.gif",
              "https://i.imgur.com/wXQLAb3.gif",
              "https://i.imgur.com/hY7ZngK.gif"]

facepalmlinks = ["http://media.giphy.com/media/8BYLSNmnJYQxy/giphy.gif",
                 "https://uploads.disquscdn.com/images/84e9a7cef36a59ae605fad98c7ac567841be388820bf3fb936fd21b646a1d605.gif",
                 "https://media1.tenor.com/images/74199573d51d1bd9b61029b611ee7617/tenor.gif?itemid=5695432",
                 "http://i0.kym-cdn.com/photos/images/original/000/173/877/Facepalm.gif",
                 "http://i.imgur.com/gXOcRsW.gif",
                 "https://media.giphy.com/media/8cPpgUhTMjhF6/giphy.gif",
                 "https://media1.tenor.com/images/a0282083ab6b592ab419659e4fb08624/tenor.gif?itemid=4745847"]

crylinks = ["https://media1.giphy.com/media/ROF8OQvDmxytW/giphy-downsized.gif",
            "https://media1.tenor.com/images/06ae6bbe852471939cf61a81e5a9eb23/tenor.gif?itemid=5370823",
            "https://78.media.tumblr.com/e9fb46144efc579746e57bcaebd3350a/tumblr_olrmy4djBG1tydz8to1_500.gif",
            "http://i.imgur.com/k5B1CBd.jpg",
            "https://media.giphy.com/media/hyU0RHvlS3iQU/giphy.gif",
            "https://media1.tenor.com/images/5912cbe4bc0dec511b5e0996a2ad9b6f/tenor.gif?itemid=8620704",
            "https://s9.favim.com/orig/131225/an-anime-anime-gif-anime-guy-Favim.com-1182388.gif"]

licklinks = ["https://i.imgur.com/QkRz1GJ.gif",
             "https://i.imgur.com/ObCPKYV.gif",
             "https://i.imgur.com/7fWrYqd.gif",
             "https://i.imgur.com/O8CNVUL.gif",
             "https://i.imgur.com/4QIlJtC.gif",
             "https://i.imgur.com/LptJIi1.gif",
             "https://i.imgur.com/THGgRJz.gif"]

spanklinks = ["https://i.imgur.com/dt1TTQu.gif",
              "https://i.imgur.com/ZsTbDvh.gif",
              "https://i.imgur.com/4LHwG60.gif",
              "https://i.imgur.com/xLOoHKP.gif",
              "https://i.imgur.com/UShywVv.gif",
              "https://i.imgur.com/RE3mnrA.gif"]

# v!hug <user>
@client.command(pass_context=True)
async def hug(ctx, user: discord.Member = None):
    author = ctx.message.author
    msg = discord.Embed(colour=0x870099, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if user == None:
        msg.add_field(name=error_img, value="Please mention someone you want to hug.")
    else:
        msg.set_image(url="{}".format(random.choice(huglinks)))
        msg.add_field(name=":small_blue_diamond: EMOTE :small_blue_diamond:", value="<@{}> got a hug from <@{}>! Nawww.".format(user.id, author.id))
    await client.say(embed=msg)

# v!kiss <user>
@client.command(pass_context=True)
async def kiss(ctx, user: discord.Member = None):
    author = ctx.message.author
    msg = discord.Embed(colour=0x870099, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if user == None:
        msg.add_field(name=error_img, value="Please mention someone you want to kiss.")
    else:
        msg.set_image(url="{}".format(random.choice(kisslinks)))
        msg.add_field(name=":small_blue_diamond: EMOTE :small_blue_diamond:", value="<@{}> got a kiss from <@{}>! owo what's this?".format(user.id, author.id))
    await client.say(embed=msg)

# v!cuddle <user>
@client.command(pass_context=True)
async def cuddle(ctx, user: discord.Member = None):
    author = ctx.message.author
    msg = discord.Embed(colour=0x870099, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if user == None:
        msg.add_field(name=error_img, value="Please mention someone you want to cuddle.")
    else:
        msg.set_image(url="{}".format(random.choice(cuddlelinks)))
        msg.add_field(name=":small_blue_diamond: EMOTE :small_blue_diamond:", value="<@{}> cuddled <@{}>! Aww.".format(author.id, user.id))
    await client.say(embed=msg)

# v!bite <user>
@client.command(pass_context=True)
async def bite(ctx, user: discord.Member = None):
    author = ctx.message.author
    msg = discord.Embed(colour=0x870099, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if user == None:
        msg.add_field(name=error_img, value="Please mention someone you want to bite.")
    else:
        msg.set_image(url="{}".format(random.choice(bitelinks)))
        msg.add_field(name=":small_blue_diamond: EMOTE :small_blue_diamond:", value="<@{}> got biten by <@{}>! Ouch.".format(user.id, author.id))
    await client.say(embed=msg)

# v!bloodsuck <user>
@client.command(pass_context=True)
async def bloodsuck(ctx, user: discord.Member = None):
    author = ctx.message.author
    msg = discord.Embed(colour=0x870099, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if user == None:
        msg.add_field(name=error_img, value="Please mention someone you want to suck blood from.")
    else:
        msg.set_image(url="{}".format(random.choice(bloodsucklinks)))
        msg.add_field(name=":small_blue_diamond: EMOTE :small_blue_diamond:", value="<@{}> sucked some of <@{}>'s blood! Yummy.".format(author.id, user.id))
    await client.say(embed=msg)

# v!throw <user>
@client.command(pass_context=True)
async def throw(ctx, user: discord.Member = None):
    author = ctx.message.author
    msg = discord.Embed(colour=0x870099, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if user == None:
        msg.add_field(name=error_img, value="Please mention someone you want to throw.")
    else:
        msg.set_image(url="{}".format(random.choice(throwlinks)))
        msg.add_field(name=":small_blue_diamond: EMOTE :small_blue_diamond:", value="<@{}> got throw by <@{}>! Weee.".format(user.id, author.id))
    await client.say(embed=msg)

# v!pat <user>
@client.command(pass_context=True)
async def pat(ctx, user: discord.Member = None):
    author = ctx.message.author
    msg = discord.Embed(colour=0x870099, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if user == None:
        msg.add_field(name=error_img, value="Please mention someone you want to pat.")
    else:
        msg.set_image(url="{}".format(random.choice(patlinks)))
        msg.add_field(name=":small_blue_diamond: EMOTE :small_blue_diamond:", value="<@{}> got a pat from <@{}>! uwu".format(user.id, author.id))
    await client.say(embed=msg)

# v!punch <user>
@client.command(pass_context=True)
async def punch(ctx, user: discord.Member = None):
    author = ctx.message.author
    msg = discord.Embed(colour=0x870099, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if user == None:
        msg.add_field(name=error_img, value="Please mention someone you want to punch.")
    else:
        msg.set_image(url="{}".format(random.choice(punchlinks)))
        msg.add_field(name=":small_blue_diamond: EMOTE :small_blue_diamond:", value="<@{}> got punched by <@{}>! Wow, calm down.".format(user.id, author.id))
    await client.say(embed=msg)

# v!nom <user>
@client.command(pass_context=True)
async def nom(ctx, user: discord.Member = None):
    author = ctx.message.author
    msg = discord.Embed(colour=0x870099, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if user == None:
        msg.add_field(name=error_img, value="Please mention someone you want to nom.")
    else:
        msg.set_image(url="{}".format(random.choice(nomlinks)))
        msg.add_field(name=":small_blue_diamond: EMOTE :small_blue_diamond:", value="<@{}> nommed <@{}>! ( ͡° ͜ʖ ͡°)".format(author.id, user.id))
    await client.say(embed=msg)

# v!highfive <user>
@client.command(pass_context=True)
async def highfive(ctx, user: discord.Member = None):
    author = ctx.message.author
    msg = discord.Embed(colour=0x870099, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if user == None:
        msg.add_field(name=error_img, value="Please mention someone you want to highfive.")
    else:
        msg.set_image(url="{}".format(random.choice(highfivelinks)))
        msg.add_field(name=":small_blue_diamond: EMOTE :small_blue_diamond:", value="<@{}> highfived <@{}>! Woo.".format(author.id, user.id))
    await client.say(embed=msg)

# v!poke <user>
@client.command(pass_context=True)
async def poke(ctx, user: discord.Member = None):
    author = ctx.message.author
    msg = discord.Embed(colour=0x870099, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if user == None:
        msg.add_field(name=error_img, value="Please mention someone you want to poke.")
    else:
        msg.set_image(url="{}".format(random.choice(pokelinks)))
        msg.add_field(name=":small_blue_diamond: EMOTE :small_blue_diamond:", value="<@{}> got poked by <@{}>! Hmm?".format(user.id, author.id))
    await client.say(embed=msg)

# v!slap <user>
@client.command(pass_context=True)
async def slap(ctx, user: discord.Member = None):
    author = ctx.message.author
    msg = discord.Embed(colour=0x870099, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if user == None:
        msg.add_field(name=error_img, value="Please mention someone you want to slap.")
    else:
        msg.set_image(url="{}".format(random.choice(slaplinks)))
        msg.add_field(name=":small_blue_diamond: EMOTE :small_blue_diamond:", value="<@{}> got slapped by <@{}>! They probably deserved it.".format(user.id, author.id))
    await client.say(embed=msg)

# v!stare <user>
@client.command(pass_context=True)
async def stare(ctx, user: discord.Member = None):
    author = ctx.message.author
    msg = discord.Embed(colour=0x870099, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if user == None:
        msg.add_field(name=error_img, value="Please mention someone you want to stare at.")
    else:
        msg.set_image(url="{}".format(random.choice(starelinks)))
        msg.add_field(name=":small_blue_diamond: EMOTE :small_blue_diamond:", value="<@{}> is staring at <@{}>! Creep.".format(author.id, user.id))
    await client.say(embed=msg)

# v!facepalm
@client.command(pass_context=True)
async def facepalm(ctx):
    author = ctx.message.author
    msg = discord.Embed(colour=0x870099, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    msg.set_image(url="{}".format(random.choice(facepalmlinks)))
    msg.add_field(name=":small_blue_diamond: EMOTE :small_blue_diamond:", value="<@{}> facepalmed. <_<".format(author.id))
    await client.say(embed=msg)

# v!spank <user>
@client.command(pass_context=True)
async def spank(ctx, user: discord.Member = None):
    author = ctx.message.author
    msg = discord.Embed(colour=0x870099, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if user == None:
        msg.add_field(name=error_img, value="Please mention someone you want to spank.")
    else:
        msg.set_image(url="{}".format(random.choice(spanklinks)))
        msg.add_field(name=":small_blue_diamond: EMOTE :small_blue_diamond:", value="<@{}> got spanked by <@{}>! =3".format(user.id, author.id))
    await client.say(embed=msg)

# v!lick <user>
@client.command(pass_context=True)
async def lick(ctx, user: discord.Member = None):
    author = ctx.message.author
    msg = discord.Embed(colour=0x870099, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if user == None:
        msg.add_field(name=error_img, value="Please mention someone you want to lick.")
    else:
        msg.set_image(url="{}".format(random.choice(licklinks)))
        msg.add_field(name="**:small_blue_diamond: EMOTE :small_blue_diamond: **", value="<@{}> licked <@{}>! Uhm...".format(author.id, user.id))
    await client.say(embed=msg)
    
#FUN

# v!battle <user>
@client.command(pass_context=True)
async def battle(ctx, userName: discord.Member = None):
    author = ctx.message.author
    msg = discord.Embed(colour=0x870099, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if userName == None:
        msg.add_field(name=error_img, value="Please mention someone you want to battle.\nExample: `v!battle @Huskie`.")
    else:
        a_attacks = ["<@{}> punches <@{}> :punch: ".format(author.id, userName.id),
                     "<@{}> kicks <@{}> :boot: ".format(author.id, userName.id),
                     "<@{}> grabs and throws <@{}> :raised_hands: ".format(author.id, userName.id),
                     "<@{}> stabs <@{}> :dagger: ".format(author.id, userName.id),
                     "<@{}> shoots <@{}> :gun: ".format(author.id, userName.id),
                     "<@{}> cuts <@{}> :knife: ".format(author.id, userName.id),
                     "<@{}> hits <@{}> with a hammer :hammer: ".format(author.id, userName.id),
                     "<@{}> uses dark magic on <@{}> :skull_crossbones: ".format(author.id, userName.id),
                     "<@{}> uses chains to choke <@{}> :chains: ".format(author.id, userName.id),
                     "<@{}> casts a spell on <@{}> :sparkles: ".format(author.id, userName.id),
                     "<@{}> pukes on <@{}> :nauseated_face: ".format(author.id, userName.id),
                     "<@{}> scares <@{}> :ghost: ".format(author.id, userName.id),
                     "<@{}> summons a demon to attack <@{}> :smiling_imp: ".format(author.id, userName.id),
                     "<@{}> calls a robot army to attack <@{}> :robot: ".format(author.id, userName.id),
                     "<@{}> farts at <@{}> :dash: ".format(author.id, userName.id),
                     "<@{}> creates a tornado behind <@{}> :cloud_tornado: ".format(author.id, userName.id),
                     "<@{}> summons a meteor and the meteor falls on <@{}> :comet: ".format(author.id, userName.id),
                     "<@{}> strikes <@{}> with lightning :zap: ".format(author.id, userName.id),
                     "<@{}> freezes <@{}> :snowflake: ".format(author.id, userName.id),
                     "<@{}> cripples <@{}> :boom: ".format(author.id, userName.id),
                     "<@{}> shoots <@{}> with a bow and arrow :gun: ".format(author.id, userName.id),
                     "<@{}> drives over <@{}> :red_car: ".format(author.id, userName.id),
                     "<@{}> chops off <@{}>'s leg :crossed_swords: ".format(author.id, userName.id),
                     "<@{}> drains some of <@{}>'s life :broken_heart: ".format(author.id, userName.id),
                     "<@{}> steals <@{}>'s soul :black_heart: ".format(author.id, userName.id),
                     "<@{}> stuns <@{}> :octagonal_sign: ".format(author.id, userName.id),
                     "<@{}> uses nuclear energy to attack <@{}> :radioactive: ".format(author.id, userName.id),
                     "<@{}> stabs <@{}> in the eyes and blinds them :eye: ".format(author.id, userName.id),
                     "<@{}> uses ear-rape to deafen <@{}> :ear: ".format(author.id, userName.id),
                     "<@{}> uses mind control on <@{}> :alien: ".format(author.id, userName.id),
                     "<@{}> summons minions to attack <@{}> :busts_in_silhouette: ".format(author.id, userName.id),
                     "<@{}> traps <@{}> :spider_web: ".format(author.id, userName.id)]
        
        u_attacks = ["<@{}> punches <@{}> :punch: ".format(userName.id, author.id),
                     "<@{}> kicks <@{}> :boot: ".format(userName.id, author.id),
                     "<@{}> grabs and throws <@{}> :raised_hands: ".format(userName.id, author.id),
                     "<@{}> stabs <@{}> :dagger: ".format(userName.id, author.id),
                     "<@{}> shoots <@{}> :gun: ".format(userName.id, author.id),
                     "<@{}> cuts <@{}> :knife: ".format(userName.id, author.id),
                     "<@{}> hits <@{}> with a hammer :hammer: ".format(userName.id, author.id),
                     "<@{}> uses dark magic on <@{}> :skull_crossbones: ".format(userName.id, author.id),
                     "<@{}> uses chains to choke <@{}> :chains: ".format(userName.id, author.id),
                     "<@{}> casts a spell on <@{}> :sparkles: ".format(userName.id, author.id),
                     "<@{}> pukes on <@{}> :nauseated_face: ".format(userName.id, author.id),
                     "<@{}> scares <@{}> :ghost: ".format(userName.id, author.id),
                     "<@{}> summons a demon to attack <@{}> :smiling_imp: ".format(userName.id, author.id),
                     "<@{}> calls a robot army to attack <@{}> :robot: ".format(userName.id, author.id),
                     "<@{}> farts at <@{}> :dash: ".format(userName.id, author.id),
                     "<@{}> creates a tornado behind <@{}> :cloud_tornado: ".format(userName.id, author.id),
                     "<@{}> summons a meteor and the meteor falls on <@{}> :comet: ".format(userName.id, author.id),
                     "<@{}> strikes <@{}> with lightning :zap: ".format(userName.id, author.id),
                     "<@{}> freezes <@{}> :snowflake: ".format(userName.id, author.id),
                     "<@{}> cripples <@{}> :boom: ".format(userName.id, author.id),
                     "<@{}> shoots <@{}> with a bow and arrow :gun: ".format(userName.id, author.id),
                     "<@{}> drives over <@{}> :red_car: ".format(userName.id, author.id),
                     "<@{}> chops off <@{}>'s leg :crossed_swords: ".format(userName.id, author.id),
                     "<@{}> drains some of <@{}>'s life :broken_heart: ".format(userName.id, author.id),
                     "<@{}> steals <@{}>'s soul :black_heart: ".format(userName.id, author.id),
                     "<@{}> stuns <@{}> :octagonal_sign: ".format(userName.id, author.id),
                     "<@{}> uses nuclear energy to attack <@{}> :radioactive: ".format(userName.id, author.id),
                     "<@{}> stabs <@{}> in the eyes and blinds them :eye: ".format(userName.id, author.id),
                     "<@{}> uses ear-rape to deafen <@{}> :ear: ".format(userName.id, author.id),
                     "<@{}> uses mind control on <@{}> :alien: ".format(userName.id, author.id),
                     "<@{}> summons minions to attack <@{}> :busts_in_silhouette: ".format(userName.id, author.id),
                     "<@{}> traps <@{}> :spider_web: ".format(userName.id, author.id)]
        a_health = []
        u_health = []
        r = []
        for i in range(1000):
            a_health.append(".")
            u_health.append(".")
        msg.add_field(name=":crossed_swords: **__D E A T H   B A T T L E__** :crossed_swords: ", value="***`>>>`*** <@{}> :vs: <@{}> ***`<<<`***\n**~~__==============================__~~**".format(author.id, userName.id))
        for i in range(1000):
            if len(a_health) == 0 or len(u_health) == 0:
                if len(a_health) > len(u_health):
                    m = ":crown: WINNER: <@{}>\n:heart: `{}` Health".format(author.id, len(a_health))
                    m += "\n "
                    m += "\n:thumbsdown: LOSER: <@{}>\n:heart: `{}` Health".format(userName.id, len(u_health))
                elif len(a_health) < len(u_health):
                    m = ":crown: WINNER: <@{}>\n:heart: `{}` Health".format(userName.id, len(u_health))
                    m += "\n "
                    m += "\n:thumbsdown: LOSER: <@{}>\n:heart: `{}` Health".format(author.id, len(a_health))
                else:
                    k = random.randint(0, 100)
                    if k >= 50:
                        m = ":crown: RANDOM WINNER: <@{}>\n:heart: `{}` Health".format(author.id, len(a_health))
                        m += "\n "
                        m += "\n:thumbsdown: LOSER: <@{}>\n:heart: `{}` Health".format(userName.id, len(u_health))
                    else:
                        m = ":crown: RANDOM WINNER: <@{}>\n:heart: `{}` Health".format(userName.id, len(u_health))
                        m += "\n "
                        m += "\n:thumbsdown: LOSER: <@{}>\n:heart: `{}` Health".format(author.id, len(a_health))
                msg.add_field(name="**~~__==============================__~~**", value=m)
                break
            else:
                r.append(".")
                a_d = random.randint(100, 250)
                u_d = random.randint(100, 250)
                m = ":small_red_triangle_down: {}!\n`{}` DMG!".format(random.choice(a_attacks), a_d)
                m += "\n:small_red_triangle_down: {}!\n`{}` DMG!".format(random.choice(u_attacks), u_d)
                msg.add_field(name=":arrow_right: ROUND `{}`:".format(len(r)), value=m)
                for i in range(a_d):
                    if len(u_health) == 0:
                        break
                    else:
                        u_health.remove(".")
                for i in range(u_d):
                    if len(a_health) == 0:
                        break
                    else:
                        a_health.remove(".")
    await client.say(embed=msg)
    
# v!ship <something> and <something else>
@client.command(pass_context=True)
async def ship(ctx, *, args = None):
    author = ctx.message.author
    msg = discord.Embed(colour=0x870099, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if args == None:
        msg.add_field(name=error_img, value="Please give 2 things you want to ship.\nExample: `v!ship Hikari and Yami`.")
    else:
        if len(str(args)) > 400:
            msg.add_field(name=error_img, value="The ship cannot be longer than 400 characters.")
        else:
            if "|" in str(args):
                a = args.split(' and ')
                if len(a) > 2:
                    msg.add_field(name=error_img, value="The command was used incorrectly.\nExample: `v!ship Hikari and Yami`.")
                else:
                    p = random.randint(0, 101)
                    if p >= 0 and p <= 10:
                        m = ":small_red_triangle_down: **{}**\n:small_red_triangle: **{}**\n```fix\n{}% - Shit\n```\n:sob: ".format(a[0], a[1], p)
                    elif p >= 11 and p <= 20:
                        m = ":small_red_triangle_down: **{}**\n:small_red_triangle: **{}**\n```fix\n{}% - Awful\n```\n:cry: ".format(a[0], a[1], p)
                    elif p >= 21 and p <= 30:
                        m = ":small_red_triangle_down: **{}**\n:small_red_triangle: **{}**\n```fix\n{}% - Really Bad\n```\n:frowning2: ".format(a[0], a[1], p)
                    elif p >= 31 and p <= 40:
                        m = ":small_red_triangle_down: **{}**\n:small_red_triangle: **{}**\n```fix\n{}% - Bad\n```\n:slight_frown: ".format(a[0], a[1], p)
                    elif p >= 41 and p <= 50:
                        m = ":small_red_triangle_down: **{}**\n:small_red_triangle: **{}**\n```fix\n{}% - Okay\n```\n:neutral_face: ".format(a[0], a[1], p)
                    elif p >= 51 and p <= 60:
                        m = ":small_red_triangle_down: **{}**\n:small_red_triangle: **{}**\n```fix\n{}% - Good\n```\n:slight_smile: ".format(a[0], a[1], p)
                    elif p >= 61 and p <= 70:
                        m = ":small_red_triangle_down: **{}**\n:small_red_triangle: **{}**\n```fix\n{}% - Very Good\n```\n:smiley: ".format(a[0], a[1], p)
                    elif p >= 71 and p <= 80:
                        m = ":small_red_triangle_down: **{}**\n:small_red_triangle: **{}**\n```fix\n{}% - Fantastic\n```\n:blush: ".format(a[0], a[1], p)
                    elif p >= 81 and p <= 90:
                        m = ":small_red_triangle_down: **{}**\n:small_red_triangle: **{}**\n```fix\n{}% - Amazing\n```\n:heart_eyes: ".format(a[0], a[1], p)
                    else:
                        m = ":small_red_triangle_down: **{}**\n:small_red_triangle: **{}**\n```fix\n{}% - Perfect\n```\n:revolving_hearts: ".format(a[0], a[1], p)
                    msg.add_field(name=":heartpulse: **__S H I P   M A C H I N E__** :heartpulse: ", value=m)
            else:
                msg.add_field(name=error_img, value="The command was used incorrectly.\nExample: `v!ship Hikari and Yami`")
    await client.say(embed=msg)
    
# v!rps <rock/paper/scissors>
@client.command(pass_context=True)
async def rps(ctx, o = None):
    author = ctx.message.author
    msg = discord.Embed(colour=0x870099, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if o == None:
        msg.add_field(name=error_img, value="Please choose what you want to use.\nExample: `v!rps rock`.")
    else:
        if o == "rock" or o == "paper" or o == "scissors":
            a = ["rock", "paper", "scissors"]
            c = random.choice(a)
            msg.add_field(name=":fist: **__ROCK, PAPER, SCISSORS__** :fist: ", value="**~~__==============================__~~**\n:arrow_forward: <@{}>\n------- `{}`\n:arrow_forward: <@{}>\n------- `{}`".format(author.id, o, client.user.id, c))
            if o == "rock" and c == "scissors":
                msg.add_field(name="**~~__==============================__~~**", value=":crown: WINNER: <@{}>\n \n:thumbsdown: LOSER: <@{}>".format(author.id, client.user.id))
            elif o == "paper" and c == "rock":
                msg.add_field(name="**~~__==============================__~~**", value=":crown: WINNER: <@{}>\n \n:thumbsdown: LOSER: <@{}>".format(author.id, client.user.id))
            elif o == "scissors" and c == "paper":
                msg.add_field(name="**~~__==============================__~~**", value=":crown: WINNER: <@{}>\n \n:thumbsdown: LOSER: <@{}>".format(author.id, client.user.id))
            elif o == "rock" and c == "paper":
                msg.add_field(name="**~~__==============================__~~**", value=":crown: WINNER: <@{}>\n \n:thumbsdown: LOSER: <@{}>".format(client.user.id, author.id))
            elif o == "paper" and c == "scissors":
                msg.add_field(name="**~~__==============================__~~**", value=":crown: WINNER: <@{}>\n \n:thumbsdown: LOSER: <@{}>".format(client.user.id, author.id))
            elif o == "scissors" and c == "rock":
                msg.add_field(name="**~~__==============================__~~**", value=":crown: WINNER: <@{}>\n \n:thumbsdown: LOSER: <@{}>".format(client.user.id, author.id))
            else:
                msg.add_field(name="**~~__==============================__~~**", value=":no_entry: It's a tie!")
        else:
            msg.add_field(name=error_img, value="Invalid choice.\nChoices: `rock`, `paper`, `scissors`.")
    await client.say(embed=msg)
    
# v!eightball <yes or no question>
@client.command(pass_context=True)
async def eightball(ctx, *, args = None):
    author = ctx.message.author
    msg = discord.Embed(colour=0x870099, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if args == None:
        msg.add_field(name=error_img, value="Please ask a yes/no question.")
    else:
        if len(str(args)) > 1900:
            msg.add_field(name=error_img, value="The question cannot be longer than 1900 characters.")
        else:
            a = ["Hell no!",
                 "No!",
                 "Hell yes!",
                 "Yes!",
                 "Definitely!",
                 "Definitely not!",
                 "Probably!",
                 "Probably not!",
                 "Most likely!",
                 "Yes! I'm sure of it!",
                 "No! I'm sure of it!"]
            msg.add_field(name=":8ball: ", value=":grey_question: `Question:`\n<@{}>: {}\n \n:grey_exclamation: `Answer:`\n**Magic Eight Ball**: {}".format(author.id, args, random.choice(a)))
    await client.say(embed=msg)
    
# v!rate <text>
@client.command(pass_context=True)
async def rate(ctx, *, args = None):
    author = ctx.message.author
    msg = discord.Embed(colour=0x870099, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if args == None:
        msg.add_field(name=error_img, value="Nothing to rate given.")
    else:
        if len(str(args)) > 1900:
            msg.add_field(name=error_img, value="The text cannot be longer than 1900 characters.")
        else:
            msg.add_field(name=":scales:", value=":arrow_forward: <@{}>\nI'd rate {} a {}/10!".format(author.id, args, random.randint(0, 11)))
    await client.say(embed=msg)
    
# v!urban <text>
@client.command(pass_context=True)
async def urban(ctx, *, args = None):
    author = ctx.message.author
    msg = discord.Embed(colour=0x870099, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if args == None:
        msg.add_field(name=error_img, value="Please give something you want to define.")
    else:
        if len(str(args)) > 150:
            msg.add_field(name=error_img, value="The text cannot be longer than 150 characters.")
        else:
            try:
                defs = ud.define('{}'.format(args))
                msg.add_field(name=":bookmark_tabs: Urban Dictionary", value="<@{}>: What is {}?\n \n{}".format(author.id, args, random.choice(defs)))
            except:
                msg.add_field(name=":bookmark_tabs: Urban Dictionary", value="<@{}>: What is {}?\n \nNo definition found.".format(author.id))
    await client.say(embed=msg)
    
#GENERAL

# }invite
@client.command(pass_context=True)
async def invite(ctx):
    msg = discord.Embed(colour=0x870099, url=default_invite, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    msg.add_field(name=":link: ", value="Here is the default server invite:\n{}".format(default_invite))
    await client.say(embed=msg)
    
# }suggest <suggestion>
@client.command(pass_context=True)
async def suggest(ctx, *, args = None):
    author = ctx.message.author
    channel = client.get_channel('457604410344865814')
    msg = discord.Embed(colour=0x870099, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if args == None:
        msg.add_field(name=error_img, value="Please give a suggestion.\nExample: `v!suggest Create a new role called Huskie's Servant.`.")
    else:
        if len(str(args)) > 500:
            msg.add_field(name=error_img, value="The suggestion cannot be longer than 500 characters.")
        else:
            m = discord.Embed(colour=0x04FF00, description= "")
            m.title = ""
            m.set_footer(text=footer_text)
            m.add_field(name=":speech_balloon: ", value="{}".format(args))
            m.add_field(name="===============", value="Suggested by: `{}` ### `{}`\nIf you like this suggestion, react with :white_check_mark: and if you don't like it, react with :x:.".format(author, author.id))
            await client.send_message(channel, embed=m)
            async for message in client.logs_from(channel):
                if len(message.reactions) == 0:
                    await client.add_reaction(message, '\u2705')
                    await client.add_reaction(message, '\u274C')
                    break
                else:
                    print("")
            msg.add_field(name=":speech_balloon: ", value="Suggestion sent!\nYou can see it in <#457604410344865814>.")
    await client.say(embed=msg)

# }userinfo <user>
@client.command(pass_context=True)
async def userinfo(ctx, userName: discord.Member = None):
    punish = discord.utils.get(ctx.message.server.roles, id=punished_role)
    msg = discord.Embed(colour=0x870099, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if userName == None:
        msg.add_field(name=error_img, value="Please tag the user you want to get information on.")
    else:
        imageurl = userName.avatar_url
        msg.title = "USER INFO"
        msg.set_thumbnail(url=imageurl)
        msg.add_field(name="NAME:", value="`{}`".format(userName), inline=True)
        msg.add_field(name="ID:", value="`{}`".format(userName.id), inline=True)
        msg.add_field(name="CREATED AT:", value="`{}`".format(userName.created_at), inline=True)
        msg.add_field(name="JOINED AT:", value="`{}`".format(userName.joined_at), inline=True)
        msg.add_field(name="STATUS:", value="`{}`".format(userName.status), inline=True)
        msg.add_field(name="IS BOT:", value="`{}`".format(userName.bot), inline=True)
        msg.add_field(name="GAME:", value="{}".format(userName.game), inline=True)
        msg.add_field(name="NICKNAME:", value="`{}`".format(userName.nick), inline=True)
        msg.add_field(name="TOP ROLE:", value="`{}`".format(userName.top_role), inline=True)
        msg.add_field(name="VOICE CHANNEL:", value="`{}`".format(userName.voice_channel), inline=True)
        if punish in userName.roles:
            msg.add_field(name="MUTED:", value="True", inline=True)
        else:
            msg.add_field(name="PUNISHED:", value="False", inline=True)
    await client.say(embed=msg)
    
# }serverinfo
@client.command(pass_context=True)
async def serverinfo(ctx):
    msg = discord.Embed(colour=0x870099, description= "")
    msg.title = "SERVER INFORMATION"
    msg.set_footer(text=footer_text)
    imageurl = ctx.message.server.icon_url
    msg.set_thumbnail(url=imageurl)
    msg.add_field(name="MEMBERS", value="`{}`".format(len(ctx.message.server.members)), inline=True)
    msg.add_field(name="CHANNELS", value="`{}`".format(len(ctx.message.server.channels)), inline=True)
    msg.add_field(name="EMOJIS", value="`{}`".format(len(ctx.message.server.emojis)), inline=True)
    msg.add_field(name="ID", value="`{}`".format(ctx.message.server.id), inline=True)
    msg.add_field(name="REGION", value="`{}`".format(ctx.message.server.region), inline=True)
    msg.add_field(name="ROLES", value="`{}`".format(len(ctx.message.server.roles)), inline=True)
    msg.add_field(name="OWNER", value="`{}`".format(ctx.message.server.owner), inline=True)
    msg.add_field(name="CREATED AT", value="`{}`".format(ctx.message.server.created_at), inline=True)
    msg.set_image(url="{}".format(banner))
    await client.say(embed=msg)
    
# v!mc
@client.command(pass_context=True)
async def mc(ctx):
    msg = discord.Embed(colour=0x870099, description= "")
    msg.title = "MEMBER COUNT"
    msg.set_footer(text=footer_text)
    msg.add_field(name="Members", value="`{}`".format(len(ctx.message.server.members)), inline=True)
    await client.say(embed=msg)
    
# v!say <text>
@client.command(pass_context=True)
async def say(ctx, *, args = None):
    author = ctx.message.author
    helper = discord.utils.get(ctx.message.server.roles, name='Jr. Mod')
    mod = discord.utils.get(ctx.message.server.roles, name='Moderator')
    msg = discord.Embed(colour=0x870099, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if helper in author.roles or mod in author.roles:
        if args == None:
            msg.add_field(name=error_img, value="Please give a message that you want the bot to say.")
            await client.say(embed=msg)
        else:
            if len(str(args)) > 1990:
                msg.add_field(name=error_img, value="The message cannot be longer than 1990 characters.")
                await client.say(embed=msg)
            else:
                await client.say("`{}`".format(args))
                await client.delete_message(ctx.message)
    else:
        msg.add_field(name=error_img, value="This command can only be used by Helpers and Moderators!")
        await client.say(embed=msg)
        
# v!partner <user>
@client.command(pass_context=True)
async def partner(ctx, userName: discord.Member = None):
    author = ctx.message.author
    helper = discord.utils.get(ctx.message.server.roles, name='Jr. Mod')
    mod = discord.utils.get(ctx.message.server.roles, name='Moderator')
    admin = discord.utils.get(ctx.message.server.roles, name='Admin')
    manager = discord.utils.get(ctx.message.server.roles, name='Co-Owner')
    owner = discord.utils.get(ctx.message.server.roles, name='Owner')
    partner = discord.utils.get(ctx.message.server.roles, name='Partner')
    msg = discord.Embed(colour=0x870099, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    chnl = client.get_channel('470464384725024768')
    l = client.get_channel(logs)
    if helper in author.roles or mod in author.roles or admin in author.roles or manager in author.roles or owner in author.roles:
        if userName == None:
            msg.add_field(name=error_img, value="Please mention the person you want to give/remove the partner role to/from.")
        else:
            try:
                if partner in userName.roles:
                    await client.remove_roles(userName, partner)
                    msg.add_field(name=":handshake: ", value="<@{}> removed the partner role from <@{}>.".format(author.id, userName.id))
                else:
                    await client.add_roles(userName, partner)
                    msg.add_field(name=":handshake: ", value="<@{}> gave the partner role to <@{}>.".format(author.id, userName.id))
            except:
                msg.add_field(name=error_img, value="There was an error while trying to give/take the partner role to/from that user.")
    else:
        msg.add_field(name=error_img, value="This command can only be used by the staff!")
    await client.say(embed=msg)
##################################
client.run(os.environ['BOT_TOKEN'])
