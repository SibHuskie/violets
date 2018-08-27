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
import urbandictionary as ud

Client = discord.Client()
bot_prefix= "v!"
client = commands.Bot(command_prefix=bot_prefix)
server = discord.Server(id='426680388002250753')
footer_text = "Violets™"
error_img = ':warning:'
default_invite = 'https://discord.gg/Cbzd4fy'
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

client.remove_command('help')

# v!shop
@client.command(pass_context=True)
async def help(ctx):
    author = ctx.message.author
    msg = discord.Embed(colour=0x4286f4, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    msg2 = discord.Embed(colour=0x4286f4, description= "")
    msg2.title = ""
    msg2.set_footer(text=footer_text)
    await client.send_typing(ctx.message.channel)
    m1 = "__**Commands**__"
    m1 += "\n`=================================`"
    m2 = "\n:large_blue_circle: EMOTES :large_blue_circle:"
    m2 += "\n- v!hug <user>"
    m2 += "\n- v!pat <user>"
    m2 += "\n- v!kiss <user>"
    m2 += "\n- v!nom <user>"
    m2 += "\n- v!throw <user>"
    m2 += "\n- v!bite <user>"
    m2 += "\n- v!bloodsuck <user>"
    m2 += "\n- v!cuddle <user>"
    m2 += "\n- v!highfive <user>"
    m2 += "\n- v!poke <user>"
    m2 += "\n- v!slap <user>"
    m2 += "\n- v!punch <user>"
    m2 += "\n- v!stare <user>"
    m2 += "\n- v!facepalm"
    m2 += "\n- v!lick <user>"
    m2 += "\n- v!spank <user>"
    m3 = "\n:large_blue_circle: FUN :large_blue_circle:"
    m3 += "\n- v!battle <user>"
    m3 += "\n- v!ship <text> and <text>"
    m3 += "\n- v!rps <rock/paper/scissors>"
    m3 += "\n- v!eightball <yes or no questions>"
    m3 += "\n- v!rate <text>"
    m3 += "\n- v!urban <word>"
    m3 += "\n- v!rainbow"
    m3 += "\n- v!kill <user>"
    m4 = "\n:large_blue_circle: GENERAL :large_blue_circle: "
    m4 += "\n- v!invite"
    m4 += "\n- v!suggest <suggestion>"
    m4 += "\n- v!userinfo <user>"
    m4 += "\n- v!serverinfo"
    m4 += "\n- v!mc"
    m5 = "\n:large_blue_circle: CURRENCY :large_blue_circle:"
    m5 += "\n- v!work"
    m5 += "\n- v!steal <user> "
    m5 += "\n- v!hack <number from 1 to 20> "
    m5 += "\n- v!slots <amount>"
    m5 += "\n- v!bal [user]"
    m5 += "\n- v!profile [user]"
    m5 += "\n- v!shop"
    m5 += "\n- v!buy <perk>"
    m5 += "\n- v!fish"
    m5 += "\n- v!pay <user> <amount>"
    m5 += "\n- v!boost"
    m5 += "\n- v!convert"
    m6 = "\n:large_blue_circle: STAFF :large_blue_circle:"
    m6 += "\n- v!bc"
    m6 += "\n- v!kick <user> [reason]"
    m6 += "\n- v!hackban <id> <reason>"
    m6 += "\n- v!unban <user id>"
    m6 += "\n- v!ban <user> [reason]"
    m6 += "\n- v!purge <number>"
    m6 += "\n- v!warn <user> <reason>"
    m6 += "\n- v!check <user>"
    m6 += "\n- v!partner <user>"
    m6 += "\n- v!mute <user> <time> [reason]"
    m6 += "\n- v!unmute <user>"
    m6 += "\n- v!take <user> <role>"
    m6 += "\n- v!give <user> <role>"
    m6 += "\n- v!money <add/del/set> <user> <amount>"
    m6 += "\n- v!reset <perk/money/all> <user>"
    m6 += "\n- v!say <text>"
    m6 += "\n- v!perk <add/del> <user> <perk>"
    msg.add_field(name="`=================================`", value=m2)
    msg.add_field(name="`=================================`", value=m3)
    msg.add_field(name="`=================================`", value=m4)
    msg.add_field(name="`=================================`", value=m5)
    msg.add_field(name="`=================================`", value=m6)
    try:
        await client.send_message(author, embed=msg)
        msg2.add_field(name=":diamond_shape_with_a_dot_inside:", value="Check your DMs, <@{}>.".format(author.id))
    except:
        msg2.add_field(name=error_img, value="I am unable to DM you, <@{}>.".format(author.id))
    await client.say(embed=msg2)

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
    
@client.command(pass_context=True)
async def rainbow(ctx):
    color = discord.Color(random.randint(0x000000, 0xFFFFFF))
    msg = discord.Embed(colour=color, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    msg.add_field(name=":rainbow: RAINBOWS :rainbow: ", value=":rainbow: R A I N B O W S :rainbow: ")
    channel = ctx.message.channel
    b = await client.send_message(channel, embed=msg)
    g = [":large_blue_circle:", ":red_circle:", ":white_circle:", ":purple_heart:", ":green_heart:", ":yellow_heart:", ":black_circle:"]
    for i in range(20):
        color = discord.Color(random.randint(0x000000, 0xFFFFFF))
        msg2 = discord.Embed(colour=color, description= "")
        msg2.title = ""
        msg2.set_footer(text=footer_text)
        msg2.add_field(name=":rainbow: RAINBOWS :rainbow: ", value=":rainbow: **__R A I N B O W S__** :rainbow: ")
        msg2.set_image(url="https://i.imgur.com/rItq9Ph.gifv")
        await client.edit_message(b, embed=msg2)
        await asyncio.sleep(float(2))
    
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
    
''' COMMANDS FOR EVERYONE '''
    
#EMOTE

mocklinks = ["https://media1.tenor.com/images/e92185e00b00c8b2ef4199164e130d27/tenor.gif?itemid=8665747"]

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

# FUN MESSAGES
@client.event
async def on_message(message):
    if message.content.lower().startswith('v!test'):
        await client.send_message(message.channel, "Testing 1 2 3...")

    if message.content.lower().startswith('v!coin'): #Coinflip 50/50% chance kopf oder zahl
        choice = random.randint(1,2)
        if choice == 1:
            await client.add_reaction(message, '🌑')
        if choice == 2:
            await client.add_reaction(message, '🌕')
                    
    if message.content.lower().startswith('who is huskie'):
        await client.send_message(message.channel, "Cough cough... who do you think he is, it clearly says 'Huskie', is that enough proof to show how awesome he is?? ")
                    
    if message.content.lower().startswith('who is seven'):
        await client.send_message(message.channel, "Stacey's one and only. Don't touch him! :stuck_out_tongue:")
                    
    if message.content.lower().startswith('who is stacey'):
        await client.send_message(message.channel, "Claimed by Huskie and Seven. Dun be mean to Stacey or you get a whack on ya head.")
                    
    if message.content.lower().startswith('who is vanessa'):
        await client.send_message(message.channel, "Tbh no one knows... she is mysterious and never speaks... lmao jk she's fucking greaaat!")
        
    if message.content.lower().startswith('who is respect'):
        await client.send_message(message.channel, "Listen to this song... just do it... https://www.youtube.com/watch?v=6EEW-9NDM5k")
        
    if message.content.lower().startswith('who is maly'):
        await client.send_message(message.channel, "Well... so... um... she's Maly..?")
        
    if message.content.lower().startswith('who is stefan'):
        await client.send_message(message.channel, "The most retarded ugly looking ass kid here, but he got memes")
        
    if message.content.lower().startswith('who is kelly'):
        await client.send_message(message.channel, "Thicc")
                        
    if message.content.lower().startswith('who is feez'):
        await client.send_message(message.channel, "A ghost that lives in shadows... *that's a bit dark*...")
                        
    if message.content.lower().startswith('who is oggy'):
        await client.send_message(message.channel, "Oggy is a guy who makes weird autistic noices from his mouth, he is a child with bad humor and ofc ugly, he destroys seven at TF2 ofc... gg")      
                
    if message.content.lower().startswith('who is yami'):
        await client.send_message(message.channel, "Hikari's")
                        
    if message.content.lower().startswith('who is hikari'):
        await client.send_message(message.channel, "Yami's")
                        
    if message.content.lower().startswith('who is marcy'):
        await client.send_message(message.channel, "The useless owner")
        
    if message.content.lower().startswith('who is kasper'):
        await client.send_message(message.channel, "Useless admin")
        
    if message.content.lower().startswith('who is worgen'):
        await client.send_message(message.channel, "The dumb guy with no life 24/7 on discord")
                                
    if message.content.lower().startswith('who is tredll'):
        await client.send_message(message.channel, "Shut up. Shut the fuck up. Shut up! Shut the fuck up! Shut up! Shut up. This what I do, This what I do! This what I do. Shut the fuck up! Shut up! All you don't nobody goin' nowhere. Nobody goin' nowhere. Don't nobody going nowhere. You wanna stop? YOU WANNA STOP?! Stop. So if I get up somebody gon' hold 'im? Nobody touch me. Nobody touch me. Nobody touch me. You got blood on me, right? Got blood on me, right?! You got blood, use a tissue! You got-...You got blood on me? You got blood on me, right? Come on bro. Get your shit. What's up, bruh? Don't touch me. Don't touch me. You wanna fight, right? Don't touch me. Don't touch me. You wanna fight, right? Tell 'em turn the cameras off. Smack up. Don't say my name out on these cameras!")
        
    if message.content.lower().startswith('whalecum'):
        b = ["Stop saying that shit.", "just why", "(╯°□°）╯︵ ┻━┻", "boi", "fucking pervert"]
        await client.send_message(message.channel, "{}".format(random.choice(b)))
        
    if message.content.lower().startswith('i love you'):
        await client.send_message(message.channel, "Mind if I third wheel for a sec..? Just saying, love you too <3")
        
    if message.content.lower().startswith('i love you too viola'):
        await client.send_message(message.channel, "Nawww, that's sweet.")
                
    if message.content.lower().startswith('i love viola'):
        await client.send_message(message.channel, "Thanks, at least someone loves me ;(")
                
    if message.content.lower().startswith('love you viola'):
        await client.send_message(message.channel, "LOVE YA TOO BABES")        
    else:
        await client.process_commands(message)
            
            
# v!hug <user>
@client.command(pass_context=True)
async def hug(ctx, user: discord.Member = None):
    author = ctx.message.author
    msg = discord.Embed(colour=0x51cbdb, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if user == None:
        msg.add_field(name=error_img, value="Please mention someone you want to hug.")
    else:
        msg.set_image(url="{}".format(random.choice(huglinks)))
        msg.add_field(name=":small_blue_diamond: EMOTE :small_blue_diamond:", value="<@{}> got a hug from <@{}>! Nawww.".format(user.id, author.id))
    await client.say(embed=msg)
    
# v!mock <user>
@client.command(pass_context=True)
async def mock(ctx, user: discord.Member = None):
    author = ctx.message.author
    msg = discord.Embed(colour=0x51cbdb, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if user == None:
        msg.add_field(name=error_img, value="Please mention someone you want to mock.")
    else:
        msg.set_image(url="{}".format(random.choice(mocklinks)))
        msg.add_field(name=":small_blue_diamond: EMOTE :small_blue_diamond:", value="<@{}> iS mOcKiNg <@{}>!".format(author.id, user.id))
    await client.say(embed=msg)

# v!kiss <user>
@client.command(pass_context=True)
async def kiss(ctx, user: discord.Member = None):
    author = ctx.message.author
    msg = discord.Embed(colour=0x51cbdb, description= "")
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
    msg = discord.Embed(colour=0x51cbdb, description= "")
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
    msg = discord.Embed(colour=0x51cbdb, description= "")
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
    msg = discord.Embed(colour=0x51cbdb, description= "")
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
    msg = discord.Embed(colour=0x51cbdb, description= "")
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
    msg = discord.Embed(colour=0x51cbdb, description= "")
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
    msg = discord.Embed(colour=0x51cbdb, description= "")
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
    msg = discord.Embed(colour=0x51cbdb, description= "")
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
    msg = discord.Embed(colour=0x51cbdb, description= "")
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
    msg = discord.Embed(colour=0x51cbdb, description= "")
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
    msg = discord.Embed(colour=0x51cbdb, description= "")
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
    msg = discord.Embed(colour=0x51cbdb, description= "")
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
    msg = discord.Embed(colour=0x51cbdb, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    msg.set_image(url="{}".format(random.choice(facepalmlinks)))
    msg.add_field(name=":small_blue_diamond: EMOTE :small_blue_diamond:", value="<@{}> facepalmed. <_<".format(author.id))
    await client.say(embed=msg)
    
# v!fart
@client.command(pass_context=True)
async def fart(ctx):
    author = ctx.message.author
    msg = discord.Embed(colour=0x51cbdb, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    msg.add_field(name=":small_blue_diamond: EMOTE :small_blue_diamond:", value="<@{}> farted... can you smell the love? <_<".format(author.id))
    await client.say(embed=msg)

# v!spank <user>
@client.command(pass_context=True)
async def spank(ctx, user: discord.Member = None):
    author = ctx.message.author
    msg = discord.Embed(colour=0x51cbdb, description= "")
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
    msg = discord.Embed(colour=0x51cbdb, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if user == None:
        msg.add_field(name=error_img, value="Please mention someone you want to lick.")
    else:
        msg.set_image(url="{}".format(random.choice(licklinks)))
        msg.add_field(name="**:small_blue_diamond: EMOTE :small_blue_diamond: **", value="<@{}> licked <@{}>! Uhm...".format(author.id, user.id))
    await client.say(embed=msg)
    
#FUN
# }kill <user>
@client.command(pass_context=True)
async def kill(ctx, user: discord.Member = None):
    author = ctx.message.author
    msg = discord.Embed(colour=0x51cbdb, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if user == None:
        msg.add_field(name=error_img, value="Please mention the user you want to kill.")
    else:
        msgs = ["On a beautiful, sunny day, <@{}> went to the store. As they walked in to the store, they slipped and the doors cut off their head.".format(user.id),
                "<@{}> was sitting on a tree, but because of their weight, the branch broke and they fell right on their head.".format(user.id),
                "On a beautiful morning <@{}> suddenly jumped out of bed and started running towards the bathroom. However, they slipped on a banana and fell out of the window.".format(user.id),
                "<@{}> watched the Emoji movie. The next day they died from too much cringe.".format(user.id),
                "<@{}> was browsing the web one day. They accidentaly clicked on a pop-up saying 'DIE FOR FREE!'.".format(user.id),
                "<@{}> got caught watching hentai. They had no choice but to kill themselves in order to wash away their sins.".format(user.id),
                "All of <@{}>'s memes got stolen! They couldn't live for more than 0.420 seconds without memes.".format(user.id),
                "<@{}> was walking down the village when all of a sudden a piano fell on top of them, crashing all their bones.".format(user.id),
                "Long time ago <@{}> lived in peace and harmony, until the fire nation attacked. Now <@{}> is pretty much dead.".format(user.id, user.id),
                "<@{}> died a virgin. LMAO what a loser.".format(user.id),
                "<@{}> was playing hopscotch on a landmine field. You can tell how that went.".format(user.id),
                "<@{}> was playing the Sims. Their computer crashed and they got a heart attack.".format(user.id),
                "Wait, <@{}> died? Oh well.".format(user.id),
                "<@{}> commited suicide. I guess it's a way of saying 'You can't fire me! I quit!' to God.".format(user.id),
                "<@{}> gave their heart to <@{}>... Literally.".format(user.id, author.id),
                "There hasn't been rain around the whole world, plants are dying and the temperatures are very high. <@{}> was a vegan.".format(user.id),
                "<@{}> decided to go on the moon. However they forgot their space suit. All the kids wanted to hear about the corpse on the moon...".format(user.id),
                "One day <@{}> was chilling with their friends. All of them were bored, they didn't have anything to do. One of them said 'So gentlemen, what do we do now?', <@{}> replied: 'We die.'. Yeah, they were really bored.".format(user.id, user.id),
                "<@{}> tried to lay an egg. Humans can't do that, nor can bots!".format(user.id),
                "All of <@{}>'s diamonds were stolen on their Christian minecraft server. Out of anger they said 'heck' and got killed instantly.".format(user.id),
                "<@{}> forgot how to breathe.".format(user.id),
                "<@{}> saw <@{}>'s face and instantly died.".format(user.id, author.id),
                "...and then <@{}> said: I don't feel so good...".format(user.id),
                "<@{}> livedn't.".format(user.id),
                "<@{}> had a lot of mental disorders and couldn't live with them anymore. They commited suicide by cutting a deep wound on their chest with a kitchen knife.".format(user.id),
                "<@{}> drowned <@{}> in a glass of water.".format(author.id, user.id),
                "<@{}> threw <@{}> in a pool with sharks.".format(author.id, user.id),
                "<@{}> spammed <@{}>'s DMs and they died from all the notifications they got.".format(author.id, user.id),
                "<@{}> stole all of <@{}>'s chocolate. <@{}> simply couldn't live without their chocolate and decided that their life is not worth living anymore.".format(author.id, user.id, user.id),
                "<@{}>'s toaster was hacked by <@{}>. They couldn't live with no toast.".format(user.id, author.id),
                "<@{}> watched furry porn and died from what they saw.".format(user.id),
                "<@{}> 'accidentally' fell off a building.".format(user.id),
                "<@{}> may have ate food with cyanide.".format(user.id),
                "<@{}> starved in a fast food restaurant. What a fucking idiot.".format(user.id),
                "...And <@{}> died happily ever after... Wait no, I messed it up!".format(user.id),
                "<@{}> joined this server and died. Oh well, that's not a first.".format(user.id),
                "<@{}> was gay in Iran.".format(user.id),
                "<@{}> choked on a banana ( ͡° ͜ʖ ͡°) and died.".format(user.id),
                "<@{}> drove off a cliff and survived, but died from shock when they saw the high price of the hospital bill.".format(user.id),
                "<@{}> listened to Justin Beiber for more than 0.69 seconds.".format(user.id),
                "<@{}> drank too much anti-freeze.".format(user.id),
                "<@{}> got stabbed with a cucumber by <@{}>.".format(user.id, author.id),
                "<@{}> died from a heatstroke in the artic.".format(user.id),
                "<@{}> tried to fly. It worked till they hit the ground.".format(user.id),
                "<@{}> wanted to get a haircut in a faster way. They thought setting their hair on fire would do the trick.".format(user.id),
                "On a peaceful night. The moon was shining and everyone was sleeping and enjoying their dreams while <@{}> suffocated in their pillow.".format(user.id),
                "<@{}> got run over by a boat. A fricking boat!".format(user.id),
                "What's that smell? It smells like toast... Hey, <@{}>! Don't take out the toast with a fork- too late...".format(user.id),
                "<@{}> got a paper cut on both of their eyes, walked off a cliff and died. I guess books are evil.".format(user.id),
                "<@{}> tried putting out fire with gasoline.".format(user.id),
                "<@{}>'s head exploded while they were sitting on the toilet and pressing.".format(user.id),
                "<@{}> died of laughter. No I mean they actually died.".format(user.id),
                "<@{}> got locked in a refrigerator and died of hunger.".format(user.id),
                "<@{}> drowned in their own tears after losing a game of Fortnite.".format(user.id),
                "<@{}> got beat up by their imaginary friends.".format(user.id),
                "<@{}> played My Little Ponny for too long.".format(user.id),
                "<@{}> choked on air.".format(user.id),
                "<@{}> got poked by Chuck Norris.".format(user.id),
                "<@{}> took a selfie with a gun.".format(user.id),
                "<@{}>'s brain exploded after <@{}> saying 'What if dolphins had legs?'.".format(user.id, author.id),
                "<@{}> died after eating their favourite snack, tide pods.".format(user.id),
                "<@{}> survived the biggest waves then tripped on a rock and died.".format(user.id),
                "<@{}> ate white chocolate. Who the fuck eats white chocolate?".format(user.id),
                "<@{}> demonstrated how to die and then had a heart attack. How ironic.".format(user.id),
                "<@{}> fell in a toilet and then got flushed.".format(user.id),
                "<@{}> got stuck in a vending machine.".format(user.id),
                "<@{}> choked on their toothbrush and died.".format(user.id),
                "<@{}> found their butthole and died from excitement.".format(user.id),
                "<@{}> died. That's it. They just died.".format(user.id)]
        msg.add_field(name=":newspaper2: ", value="{}".format(random.choice(msgs)))
    await client.say(embed=msg)
    
# v!battle <user>
@client.command(pass_context=True)
async def battle(ctx, userName: discord.Member = None):
    author = ctx.message.author
    msg = discord.Embed(colour=0x51cbdb, description= "")
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
    msg = discord.Embed(colour=0x51cbdb, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if args == None:
        msg.add_field(name=error_img, value="Please give 2 things you want to ship.\nExample: `v!ship Hikari and Yami`.")
    else:
        if len(str(args)) > 400:
            msg.add_field(name=error_img, value="The ship cannot be longer than 400 characters.")
        else:
            if " and " in str(args):
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
    msg = discord.Embed(colour=0x51cbdb, description= "")
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
    msg = discord.Embed(colour=0x51cbdb, description= "")
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
    msg = discord.Embed(colour=0x51cbdb, description= "")
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
    msg = discord.Embed(colour=0x51cbdb, description= "")
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

# }apply <helper/mod/admin/manager/adbot>
@client.command(pass_context=True)
async def apply(ctx, option = None):
    author = ctx.message.author
    msg = discord.Embed(colour=0x51cbdb, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if option == None:
        msg.add_field(name=error_img, value="No option given.\nOptions: `moderator`, `pm`.\n \nExample: `v!apply pm`.")
    else:
        if option == "pm":
            try:
                mg = "***__PARTNERSHIP MANAGER APPLICATION TEMPLATE__***"
                mg += "\n:exclamation: Before applying make sure you met all the requirements."
                mg += "\n`-` You must be 15+"
                mg += "\n`-` You must be level 15+"
                mg += "\n```fix"
                mg += "\n===================================="
                mg += "\n```"
                mg += "\n:grey_question: How to apply:"
                mg += "\n`-` Once you meet the requirements, copy the template below and answer all the questions."
                mg += "\n`-` When you finish answering the questions, send them to either Huskie or Saw."
                mg += "\n```fix"
                mg += "\n===================================="
                mg += "\n```"
                mg += "\n`-` What is your discord username? Example: Huskie#9999"
                mg += "\n`-` How old are you?"
                mg += "\n`-` For how long have you been in this server?"
                mg += "\n`-` Why do you want to become a partnership manager?"
                mg += "\n`-` How many partnerships can you do a day?."
                mg += "\n`-` How active can you be (example: 1 hour a day, 3 times a week per 2 hours, etc.)?"
                mg += "\n`-` What would you do if the server is being raided?"
                mg += "\n`-` What would you do if a staff member is abusing their powers?"
                mg += "\n`-` What would you do if someone is being rude towards you?"
                mg += "\n`-` Do you know any of the staff members? If yes, please tag them."
                mg += "\n`-` Have you been or are you a partnership manager on another server?"
                await client.send_message(author, mg)
                msg.add_field(name=":pencil: ", value="The `partnership manager` template has been sent to your DMs!")
            except:
                msg.add_field(name=error_img, value="I was unable to DM you, please try again once you allowed DMs from me.")
        elif option == "moderator":
            try:
                mg = "***__MODERATOR APPLICATION TEMPLATE__***"
                mg += "\n:exclamation: Before applying make sure you met all the requirements."
                mg += "\n`-` You must be 15+"
                mg += "\n`-` You must be level 15+"
                mg += "\n```fix"
                mg += "\n===================================="
                mg += "\n```"
                mg += "\n:grey_question: How to apply:"
                mg += "\n`-` Once you meet the requirements, copy the template below and answer all the questions."
                mg += "\n`-` When you finish answering the questions, send them to either Huskie or Saw."
                mg += "\n```fix"
                mg += "\n===================================="
                mg += "\n```"
                mg += "\n`-` How old are you?"
                mg += "\n`-` For how long have you been in this server?"
                mg += "\n`-` Why do you want to become a moderator?"
                mg += "\n`-` Rate your knowledge of discord and the Viola Bot (from 1-10 for both)."
                mg += "\n`-` How active can you be (example: 1 hour a day, 3 times a week per 2 hours, etc)?"
                mg += "\n`-` What would you do if the server is being raided?"
                mg += "\n`-` What would you do if a staff member is abusing their powers?"
                mg += "\n`-` What would you do if someone is being rude towards you?"
                mg += "\n`-` Do you know any of the staff members? If yes, please tag them."
                mg += "\n`-` Have you been or are you a staff member on another server? If yes, what role do you have?"
                mg += "\n`-` Do you know how partnerships work on this server?"
                await client.send_message(author, mg)
                msg.add_field(name=":pencil: ", value="The `moderator` template has been sent to your DMs!")
            except:
                msg.add_field(name=error_img, value="I was unable to DM you, please try again once you allowed DMs from me.")
        else:
            msg.add_field(name=error_img, value="Invalid option given.\nOptions: `moderator`, `pm`.\n \nExample: `v!apply moderator`.")
    await client.say(embed=msg)
    
# }invite
@client.command(pass_context=True)
async def invite(ctx):
    msg = discord.Embed(colour=0x51cbdb, url=default_invite, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    msg.add_field(name=":link: ", value="Here is the default server invite:\n{}".format(default_invite))
    await client.say(embed=msg)
    
# }suggest <suggestion>
@client.command(pass_context=True)
async def suggest(ctx, *, args = None):
    author = ctx.message.author
    channel = client.get_channel('457604410344865814')
    msg = discord.Embed(colour=0x51cbdb, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if args == None:
        msg.add_field(name=error_img, value="Please give a suggestion.\nExample: `v!suggest Create a new role called Huskie's Servant.`.")
    else:
        if len(str(args)) > 500:
            msg.add_field(name=error_img, value="The suggestion cannot be longer than 500 characters.")
        else:
            m = discord.Embed(colour=0x51cbdb, description= "")
            m.title = ""
            m.set_footer(text=footer_text)
            m.add_field(name=":speech_balloon: ", value="{}".format(args))
            m.add_field(name="===============", value="Suggested by: `{}` ### `{}`\nIf you like this suggestion, react with :white_check_mark: and if you don't like it, react with :x:.".format(author, author.id))
            await client.send_message(channel, embed=m)
            async for message in client.logs_from(channel):
                if len(message.reactions) == 0:
                    await client.add_reaction(message, '\u2611')
                    await client.add_reaction(message, '\u2716')
                    break
                else:
                    print("")
            msg.add_field(name=":speech_balloon: ", value="Suggestion sent!\nYou can see it in <#457604410344865814>.")
    await client.say(embed=msg)

# }userinfo <user>
@client.command(pass_context=True)
async def userinfo(ctx, userName: discord.Member = None):
    punish = discord.utils.get(ctx.message.server.roles, name='Muted')
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
            msg.add_field(name="MUTED:", value="False", inline=True)
    await client.say(embed=msg)
    
# }serverinfo
@client.command(pass_context=True)
async def serverinfo(ctx):
    msg = discord.Embed(colour=0x51cbdb, description= "")
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
    msg = discord.Embed(colour=0x51cbdb, description= "")
    msg.title = "MEMBER COUNT"
    msg.set_footer(text=footer_text)
    msg.add_field(name="Members", value="`{}`".format(len(ctx.message.server.members)), inline=True)
    await client.say(embed=msg)

#MODERATOR COMMANDS

# }p <user>
@client.command(pass_context=True)
async def partner(ctx, userName: discord.Member = None):
    author = ctx.message.author
    helper = discord.utils.get(ctx.message.server.roles, name='Jr. Mod')
    mod = discord.utils.get(ctx.message.server.roles, name='Moderator')
    admin = discord.utils.get(ctx.message.server.roles, name='Administrator')
    manager = discord.utils.get(ctx.message.server.roles, name='Co-Owner')
    owner = discord.utils.get(ctx.message.server.roles, name='Owner')
    partner = discord.utils.get(ctx.message.server.roles, name='Partners')
    pmanager = discord.utils.get(ctx.message.server.roles, name='Partnership Manager')
    msg = discord.Embed(colour=0x51cbdb, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    chnl = client.get_channel('470464384725024768')
    l = client.get_channel(logs)
    if helper in author.roles or mod in author.roles or admin in author.roles or manager in author.roles or owner in author.roles or pmanager in author.roles:
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

# v!bc
@client.command(pass_context=True)
async def bc(ctx):
    author = ctx.message.author
    chnl = ctx.message.channel
    msg = discord.Embed(colour=0x51cbdb, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    x = discord.utils.get(ctx.message.server.roles, name='Viola')
    helper = discord.utils.get(ctx.message.server.roles, name='Jr. Mod')
    mod = discord.utils.get(ctx.message.server.roles, name='Moderator')
    admin = discord.utils.get(ctx.message.server.roles, name='Administrator')
    manager = discord.utils.get(ctx.message.server.roles, name='Co-Owner')
    owner = discord.utils.get(ctx.message.server.roles, name='Owner')
    a = []
    if helper in author.roles or mod in author.roles or admin in author.roles or manager in author.roles or owner in author.roles:
        async for i in client.logs_from(chnl):
            if len(a) < 50:
                if i.author.bot:
                    await client.delete_message(i)
                    a.append("+1")
                else:
                    print("")
            else:
                break
        msg.add_field(name="**Bot Clear**", value="<@{}> removed the latest messages sent by bots.".format(author.id))
    else:
        msg.add_field(name=error_img, value="This command can only be used by the staff!")
    await client.say(embed=msg)

# v!kick <user> [reason]
@client.command(pass_context=True)
async def kick(ctx, user: discord.Member = None, *, args = None):
    author = ctx.message.author
    x = discord.utils.get(ctx.message.server.roles, name='Viola')
    helper = discord.utils.get(ctx.message.server.roles, name='Jr. Mod')
    mod = discord.utils.get(ctx.message.server.roles, name='Moderator')
    admin = discord.utils.get(ctx.message.server.roles, name='Administrator')
    manager = discord.utils.get(ctx.message.server.roles, name='Co-Owner')
    owner = discord.utils.get(ctx.message.server.roles, name='Owner')
    msg = discord.Embed(colour=0x51cbdb, description= "")
    if owner in author.roles or admin in author.roles or manager in author.roles or mod in author.roles:
        if user == None:
            msg.add_field(name=error_img, value="No target given.\nExamples:\n`v!kick @Huskie Being a dog.`.\n`v!kick @Huskie`.")
        else:
            if owner in user.roles or manager in user.roles or admin in user.roles or mod in user.roles or helper in user.roles or x in user.roles:
                msg.add_field(name=error_img, value="You cannot kick other staff.\nStaff can only be kicked manualy.")
            else:
                chnl = client.get_channel('470464384725024768')
                m = "```diff"
                m += "\n- KICK -"
                m += "\n+ Author: {} ### {}".format(author, author.id)
                m += "\n+ Target: {} ### {}".format(user, user.id)
                if args == None:
                    m += "\n+ Reason: [No Reason Given]"
                    m += "\n```"
                    msg.add_field(name="**Kick**", value="<@{}> kicked **{}**!\nNo reason given.".format(author.id, user))
                    await client.kick(user)
                    await client.send_message(chnl, m)
                else:
                    if len(str(args)) > 1000:
                        msg.add_field(name=error_img, value="The reason cannot be longer than 1000 characters.")
                    else:
                        m += "\n+ Reason:"
                        m += "\n```"
                        m += "\n{}".format(args)
                        msg.add_field(name=":boot: Kicking Boot", value="<@{}> kicked **{}**!\nReason:\n{}".format(author.id, user, args))
                        await client.kick(user)
                        await client.send_message(chnl, m)
    else:
        msg.add_field(name=error_img, value="This command can only be used by Moderators, Administrators, Co-Owners and Owners.")
    await client.say(embed=msg)
    
# v!idban <id> <reason>
@client.command(pass_context=True)
async def hackban(ctx, target = None, *, args = None):
    author = ctx.message.author
    server = ctx.message.server
    x = discord.utils.get(ctx.message.server.roles, name='Viola')
    helper = discord.utils.get(ctx.message.server.roles, name='Jr. Mod')
    mod = discord.utils.get(ctx.message.server.roles, name='Moderator')
    admin = discord.utils.get(ctx.message.server.roles, name='Administrator')
    manager = discord.utils.get(ctx.message.server.roles, name='Co-Owner')
    owner = discord.utils.get(ctx.message.server.roles, name='Owner')
    msg = discord.Embed(colour=0x51cbdb, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if owner in author.roles or manager in author.roles:
        if target == None or args == None:
            msg.add_field(name=error_img, value="Not all arguments were given.\nExample: `v!hackban 244042996129988608 Being a human being.`.")
        else:
            try:
                a = await client.get_user_info(target)
                await client.http.ban(target, server.id, 0)
                msg.add_field(name="**Hack Ban**", value="<@{}> ID banned **{}**.\nReason:\n{}".format(author.id, a, args))
                m = "```diff"
                m += "\n- ID BAN -"
                m += "\n+ Author: {} ### {}".format(author, author.id)
                m += "\n+ Target: {} ### {}".format(a, a.id)
                m += "\n+ Reason:"
                m += "\n```"
                m += "\n{}".format(args)
                chnl = client.get_channel('470464384725024768')
                await client.send_message(chnl, m)
            except:
                msg.add_field(name=error_img, value="There was an error while trying to ID ban that user.\nEither the user cannot be banned or the ID you specified doesn't exist.")
    else:
        msg.add_field(name=error_img, value="This command can only be used by Co-Owners and Owners.")
    await client.say(embed=msg)
    
# v!unban <user id>
@client.command(pass_context=True)
async def unban(ctx, userID = None):
    author = ctx.message.author
    x = discord.utils.get(ctx.message.server.roles, name='Viola')
    helper = discord.utils.get(ctx.message.server.roles, name='Jr. Mod')
    mod = discord.utils.get(ctx.message.server.roles, name='Moderator')
    admin = discord.utils.get(ctx.message.server.roles, name='Administrator')
    manager = discord.utils.get(ctx.message.server.roles, name='Co-Owner')
    owner = discord.utils.get(ctx.message.server.roles, name='Owner')
    msg = discord.Embed(colour=0x51cbdb, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if owner in author.roles or admin in author.roles or manager in author.roles or mod in author.roles:
        if userID == None:
            msg.add_field(name=error_img, value="No user ID given.\nExample: `v!unban 440770699259281408`.")
        else:
            banned_users = await client.get_bans(ctx.message.server)
            try:
                user = discord.utils.get(banned_users,id=userID)
                await client.unban(ctx.message.server, user)
                msg.add_field(name=":tools: ", value="<@{}> unbanned **{}** ( `{}` ).".format(author.id, user, userID))
                m = "```diff"
                m += "\n- UNBAN -"
                m += "\n+ Author: {} ### {}".format(author, author.id)
                m += "\n+ Target: {} ### {}".format(user, user.id)
                m += "\n```"
                chnl = client.get_channel('470464384725024768')
                await client.send_message(chnl, m)
            except:
                msg.add_field(name=error_img, value="There was an error while trying to unban that ID.\nEither the ID you specified doesn't exist or it isn't banned.")
    else:
        msg.add_field(name=error_img, value="This command can only be used by Moderators, Administrators, Co-Owners and Owners.")
    await client.say(embed=msg)
    
# }ban <user> [reason]
@client.command(pass_context=True)
async def ban(ctx, user: discord.Member = None, *, args = None):
    author = ctx.message.author
    x = discord.utils.get(ctx.message.server.roles, name='Viola')
    helper = discord.utils.get(ctx.message.server.roles, name='Jr. Mod')
    mod = discord.utils.get(ctx.message.server.roles, name='Moderator')
    admin = discord.utils.get(ctx.message.server.roles, name='Administrator')
    manager = discord.utils.get(ctx.message.server.roles, name='Co-Owner')
    owner = discord.utils.get(ctx.message.server.roles, name='Owner')
    msg = discord.Embed(colour=0x51cbdb, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if owner in author.roles or admin in author.roles or manager in author.roles or mod in author.roles:
        if user == None:
            msg.add_field(name=error_img, value="No target given.\nExamples:\n`v!ban @Huskie Barking.`.\n`v!ban @Huskie`.")
        else:
            if owner in user.roles or manager in user.roles or admin in user.roles or mod in user.roles or helper in user.roles or x in user.roles:
                msg.add_field(name=error_img, value="You cannot ban other staff.\nStaff can only be banned manualy.")
            else:
                chnl = client.get_channel('470464384725024768')
                m = "```diff"
                m += "\n- BAN -"
                m += "\n+ Author: {} ### {}".format(author, author.id)
                m += "\n+ Target: {} ### {}".format(user, user.id)
                if args == None:
                    m += "\n+ Reason: [No Reason Given]"
                    m += "\n```"
                    msg.add_field(name=":hammer: Ban Hammer", value="<@{}> banned **{}**!\nNo reason given.".format(author.id, user))
                    await client.ban(user)
                    await client.send_message(chnl, m)
                else:
                    if len(str(args)) > 1000:
                        msg.add_field(name=error_img, value="The reason cannot be longer than 1000 characters.")
                    else:
                        m += "\n+ Reason:"
                        m += "\n```"
                        m += "\n{}".format(args)
                        msg.add_field(name=":hammer: Ban Hammer", value="<@{}> banned **{}**!\nReason:\n{}".format(author.id, user, args))
                        await client.ban(user)
                        await client.send_message(chnl, m)
    else:
        msg.add_field(name=error_img, value="This command can only be used by Moderators, Administrators, Co-Owners and Owners.")
    await client.say(embed=msg)
    
# v!purge <number>
@client.command(pass_context=True)
async def purge(ctx, number = None):
    author = ctx.message.author
    x = discord.utils.get(ctx.message.server.roles, name='Viola')
    helper = discord.utils.get(ctx.message.server.roles, name='Jr. Mod')
    mod = discord.utils.get(ctx.message.server.roles, name='Moderator')
    admin = discord.utils.get(ctx.message.server.roles, name='Administrator')
    manager = discord.utils.get(ctx.message.server.roles, name='Co-Owner')
    owner = discord.utils.get(ctx.message.server.roles, name='Owner')
    punished = discord.utils.get(ctx.message.server.roles, name='Muted')
    msg = discord.Embed(colour=0x51cbdb, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if owner in author.roles or admin in author.roles or manager in author.roles or mod in author.roles or helper in author.roles:
        if number == None:
            msg.add_field(name=error_img, value="Please specify the number of messages you want to delete.")
        else:
            try:
                testnumber = int(number)
                number2 = testnumber * 0
                await asyncio.sleep(float(number2))
                try:
                    deleted = await client.purge_from(ctx.message.channel, limit=testnumber)
                    if len(deleted) < testnumber:
                        msg.add_field(name="**Purge**", value="<@{}> tried to delete {} messages.\n{} messages were deleted.".format(author.id, number, len(deleted)))
                    else:
                        msg.add_field(name="**Purge**", value="<@{}> deleted {} messages.".format(author.id, len(deleted)))
                    chnl = client.get_channel('470464384725024768')
                    m = "```diff"
                    m += "\n- PURGE -"
                    m += "\n+ Author: {} ### {}".format(author, author.id)
                    m += "\n+ In: {} ### {}".format(ctx.message.channel.name, ctx.message.channel.id)
                    m += "\n+ Number: {}".format(number)
                    m += "\n+ Deleted: {}".format(len(deleted))
                    m += "\n```"
                    await client.send_message(chnl, m)
                except:
                    msg.add_field(name=error_img, value="There has been an error while trying to purge messages.")
            except:
                msg.add_field(name=error_img, value="*Sigh*, a number is a number, not a letter...")
    else:
        msg.add_field(name=error_img, value="This command can only be used by the staff.")
    await client.say(embed=msg)
    
# v!say <text>
@client.command(pass_context=True)
async def say(ctx, *, args = None):
    author = ctx.message.author
    vip = discord.utils.get(ctx.message.server.roles, name='Moderator')
    legend = discord.utils.get(ctx.message.server.roles, name='Administrator')
    msg = discord.Embed(colour=0x51cbdb, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if vip in author.roles or legend in author.roles:
        if args == None:
            msg.add_field(name=error_img, value="Please give a message that you want the bot to say.")
            await client.say(embed=msg)
        else:
            if len(str(args)) > 1990:
                msg.add_field(name=error_img, value="The message cannot be longer than 1990 characters.")
                await client.say(embed=msg)
            else:
                await client.say("{}".format(args))
                await client.delete_message(ctx.message)
    else:
        msg.add_field(name=error_img, value="This command can only be used by Moderators and Admins!")
        await client.say(embed=msg)
        
# v!warn <user> <reason>
@client.command(pass_context=True)
async def warn(ctx, user: discord.Member = None, *, args = None):
    author = ctx.message.author
    x = discord.utils.get(ctx.message.server.roles, name='Viola')
    helper = discord.utils.get(ctx.message.server.roles, name='Jr. Mod')
    mod = discord.utils.get(ctx.message.server.roles, name='Moderator')
    admin = discord.utils.get(ctx.message.server.roles, name='Administrator')
    manager = discord.utils.get(ctx.message.server.roles, name='Co-Owner')
    owner = discord.utils.get(ctx.message.server.roles, name='Owner')
    punished = discord.utils.get(ctx.message.server.roles, name='Muted')
    msg = discord.Embed(colour=0x51cbdb, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if owner in author.roles or admin in author.roles or manager in author.roles or mod in author.roles or helper in author.roles:
        if user == None or args == None:
            msg.add_field(name=error_img, value="Not all arguments were given.\nExample: `v!warn @Huskie Ear Rape in Music (aka his singing).`.")
            await client.say(embed=msg)
        else:
            if len(str(args)) > 1000:
                msg.add_field(name=error_img, value="The reason cannot be longer than 1000 characters.")
                await client.say(embed=msg)
            else:
                msg2 = discord.Embed(colour=0x51cbdb, description= "")
                msg2.title = ""
                msg2.set_footer(text=footer_text)
                msg2.add_field(name=":warning: ", value="Hello, <@{}>.\nYou have been warned by <@{}> ( **{}** ).\nReason:\n{}".format(user.id, author.id, author, args))
                try:
                    await client.send_message(user, embed=msg2)
                    msg.add_field(name=":warning: ", value="<@{}> warned <@{}>.\nReason:\n{}".format(author.id, user.id, args))
                    await client.say(embed=msg)
                except:
                    msg.add_field(name=":warning: ", value="<@{}> warned <@{}>.\nReason:\n{}".format(author.id, user.id, args))
                    await client.say("<@{}>".format(user.id), embed=msg)
                chnl = client.get_channel('470464384725024768')
                chnl2 = client.get_channel('480177377343963138')
                p = []
                async for i in client.logs_from(chnl2):
                    p.append("+1")
                m2 = "{} | {} ### {} | {} ### {} | {}".format(len(p) + 1, author, author.id, user, user.id, args)
                await client.send_message(chnl2, m2)
                m = "```diff"
                m += "\n- WARN -"
                m += "\n+ Author: {} ### {}".format(author, author.id)
                m += "\n+ Target: {} ### {}".format(user, user.id)
                m += "\n+ Reason:"
                m += "\n```"
                m += "\n{}".format(args)
                await client.send_message(chnl, m)
    else:
        msg.add_field(name=error_img, value="This command can only be used by the staff.")
        await client.say(embed=msg)
        
# v!check <user>
@client.command(pass_context=True)
async def check(ctx, user: discord.Member = None):
    author = ctx.message.author
    x = discord.utils.get(ctx.message.server.roles, name='Viola')
    helper = discord.utils.get(ctx.message.server.roles, name='Jr. Mod')
    mod = discord.utils.get(ctx.message.server.roles, name='Moderator')
    admin = discord.utils.get(ctx.message.server.roles, name='Administrator')
    manager = discord.utils.get(ctx.message.server.roles, name='Co-Owner')
    owner = discord.utils.get(ctx.message.server.roles, name='Owner')
    punished = discord.utils.get(ctx.message.server.roles, name='Muted')
    msg = discord.Embed(colour=0x51cbdb, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if owner in author.roles or admin in author.roles or manager in author.roles or mod in author.roles or helper in author.roles:
        if user == None:
            msg.add_field(name=error_img, value="Please mention someone you want to run a check on.")
            await client.say(embed=msg)
        else:
            msg2 = discord.Embed(colour=0x51cbdb, description= "")
            msg2.title = ""
            msg2.set_footer(text=footer_text)
            chnl = client.get_channel('480177377343963138')
            await client.send_typing(ctx.message.channel)
            m = ""
            async for i in client.logs_from(chnl):
                a = str(i.content)
                if user.id in a:
                    b = i.content.split(' | ')
                    m += "\n**__Warn number: {}__**\n`Warned by:` {}\n`Reason:` {}".format(b[0], b[1], b[3])
                else:
                    print("")
            msg2.add_field(name=":warning: ***__Warning list for {} ### {}__***".format(user, user.id), value=m)
            try:
                await client.send_message(author, embed=msg2)
                msg.add_field(name=":mag: Warnings Check", value="<@{}>, please check your DMs!".format(author.id), inline=True)
                await client.say(embed=msg)
            except:
                msg.add_field(name=error_img, value="I cannot send you DMs. Please try again once you let me slide in your DMs.")
                await client.say(embed=msg)
                    
    else:
        msg.add_field(name=error_img, value="This command can only be used by the staff.")
        await client.say(embed=msg)
        
# }punish <user> <time> [reason]
@client.command(pass_context=True)
async def mute(ctx, user: discord.Member = None, time4 = None, *, args = None):
    author = ctx.message.author
    x = discord.utils.get(ctx.message.server.roles, name='Viola')
    helper = discord.utils.get(ctx.message.server.roles, name='Jr. Mod')
    mod = discord.utils.get(ctx.message.server.roles, name='Moderator')
    admin = discord.utils.get(ctx.message.server.roles, name='Administrator')
    manager = discord.utils.get(ctx.message.server.roles, name='Co-Owner')
    owner = discord.utils.get(ctx.message.server.roles, name='Owner')
    punished = discord.utils.get(ctx.message.server.roles, name='Muted')
    msg = discord.Embed(colour=0x51cbdb, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if owner in author.roles or admin in author.roles or manager in author.roles or mod in author.roles or helper in author.roles:
        if user == None or time4 == None:
            msg.add_field(name=error_img, value="Not all required arguments were given.\nExamples:\n`v!mute @Huskie 15 Spamming.`.\n`v!mute @Huskie 15`.")
            await client.say(embed=msg)
        else:
            if punished in user.roles:
                msg.add_field(name=error_img, value="That user is already muted.")
                await client.say(embed=msg)
            else:
                if owner in user.roles or manager in user.roles or admin in user.roles or mod in user.roles or helper in user.roles or x in user.roles:
                    msg.add_field(name=error_img, value="Other staff cannot be muted.")
                    await client.say(embed=msg)
                else:
                    try:
                        time = int(time4)
                        if time > 600:
                            msg.add_field(name=error_img, value="The time cannot be longer than 600 minutes (10 hours).")
                            await client.say(embed=msg)
                        else:
                            testtime = time * 0
                            try:
                                await asyncio.sleep(float(testtime))
                                time2 = time * 60
                                chnl = client.get_channel('470464384725024768')
                                msg2 = discord.Embed(colour=0x51cbdb, description= "")
                                msg2.title = ""
                                msg2.set_footer(text=footer_text)
                                await client.add_roles(user, punished)
                                if args == None:
                                    msg.add_field(name=":speak_no_evil: ", value="<@{}> muted <@{}> for {} minute(s).\nNo reason given.".format(author.id, user.id, time4))
                                    await client.say(embed=msg)
                                    m = "```diff"
                                    m += "\n- MUTE -"
                                    m += "\n+ Author: {} ### {}".format(author, author.id)
                                    m += "\n+ Target: {} ### {}".format(user, user.id)
                                    m += "\n+ Time: {}".format(time4)
                                    m += "\n+ Reason: [No Reason Given]"
                                    m += "\n```"
                                    await client.send_message(chnl, m)
                                    await asyncio.sleep(float(time2))
                                    await client.remove_roles(user, punished)
                                    msg2.add_field(name=":monkey: ", value="<@{}> has been automatically unmuted.".format(user.id))
                                    await client.say(embed=msg2)
                                else:
                                    if len(str(args)) > 1000:
                                        msg.add_field(name=error_img, value="The reason cannot be longer than 1000 characters.")
                                    else:
                                        msg.add_field(name=":speak_no_evil: ", value="<@{}> muted <@{}> for {} minute(s).\nReason:\n{}".format(author.id, user.id, time4, args))
                                        await client.say(embed=msg)
                                        m = "```diff"
                                        m += "\n- MUTE -"
                                        m += "\n+ Author: {} ### {}".format(author, author.id)
                                        m += "\n+ Target: {} ### {}".format(user, user.id)
                                        m += "\n+ Time: {}".format(time4)
                                        m += "\n+ Reason:"
                                        m += "\n```"
                                        m += "\n{}".format(args)
                                        await client.send_message(chnl, m)
                                        await asyncio.sleep(float(time2))
                                        if punished in user.roles:
                                            await client.remove_roles(user, punished)
                                            msg2.add_field(name=":monkey: ", value="<@{}> has been automatically unmuted.".format(user.id))
                                            await client.say(embed=msg2)
                                        else:
                                            print("")
                            except:
                                msg.add_field(name=error_img, value="There has been an error while trying to punish that user.")
                                await client.say(embed=msg)
                    except:
                        msg.add_field(name=error_img, value="The time has to be a number.\nExample: `v!mute @Huskie 10` will mute Sarah for 10 minutes.")
                        await client.say(embed=msg)
    else:
        msg.add_field(name=error_img, value="This command can only be used by the staff.")
        await client.say(embed=msg)
        
# v!unmute <user>
@client.command(pass_context=True)
async def unmute(ctx, user: discord.Member = None):
    author = ctx.message.author
    x = discord.utils.get(ctx.message.server.roles, name='Viola')
    helper = discord.utils.get(ctx.message.server.roles, name='Jr. Mod')
    mod = discord.utils.get(ctx.message.server.roles, name='Moderator')
    admin = discord.utils.get(ctx.message.server.roles, name='Administrator')
    manager = discord.utils.get(ctx.message.server.roles, name='Co-Owner')
    owner = discord.utils.get(ctx.message.server.roles, name='Owner')
    punished = discord.utils.get(ctx.message.server.roles, name='Muted')
    msg = discord.Embed(colour=0x51cbdb, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if owner in author.roles or admin in author.roles or manager in author.roles or mod in author.roles or helper in author.roles:
        if user == None:
            msg.add_field(name=error_img, value="Please mention someone you want to unmute.\nExample: `v!unmute @Huskie`.")
        else:
            if punished in user.roles:
                await client.remove_roles(user, punished)
                msg.add_field(name=":monkey_face: ", value="<@{}> unmuted <@{}>.".format(author.id, user.id))
                chnl = client.get_channel('470464384725024768')
                m = "```diff"
                m += "\n- UNMUTE -"
                m += "\n+ Author: {} ### {}".format(author, author.id)
                m += "\n+ Target: {} ### {}".format(user, user.id)
                m += "\n```"
                await client.send_message(chnl, m)
            else:
                msg.add_field(name=error_img, value="That user isn't muted.")
    else:
        msg.add_field(name=error_img, value="This command can only be used by the staff.")
    await client.say(embed=msg)
    
# }takerole <user> <role>
@client.command(pass_context=True)
async def take(ctx, user: discord.Member = None, *, args = None):
    author = ctx.message.author
    owner = discord.utils.get(ctx.message.server.roles, name='Owner')
    admin = discord.utils.get(ctx.message.server.roles, name='Administrator')
    manager = discord.utils.get(ctx.message.server.roles, name='Co-Owner')
    msg = discord.Embed(colour=0x51cbdb, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if admin in author.roles or manager in author.roles or owner in author.roles:
        if user == None or args == None:
            msg.add_field(name=error_img, value="Not all arguments were given.\nExample: `v!take @Huskie Moderator`.")
        else:
            try:
                rolename2 = discord.utils.get(ctx.message.server.roles, name='{}'.format(args))
                if author.top_role == rolename2 or author.top_role < rolename2:
                    msg.add_field(name=error_img, value="You cannot remove a role that is the same or higher than your top role.")
                else:
                    try:
                        await client.remove_roles(user, rolename2)
                        msg.add_field(name=":outbox_tray: ", value="<@{}> removed `{}` from <@{}>.".format(author.id, args, user.id))
                    except:
                        msg.add_field(name=error_img, value="Either I can't edit that user's role or the role you specified is higher than Co-Owner.")
            except:
                msg.add_field(name=error_img, value="The specified role was not found. Make sure to check spelling and capitalization.")
    else:
        msg.add_field(name=error_img, value="This command can only be used by Administrators, Co-Owners and Owners.")
    await client.say(embed=msg)
    
# }giverole <user> <role>
@client.command(pass_context=True)
async def give(ctx, user: discord.Member = None, *, args = None):
    author = ctx.message.author
    owner = discord.utils.get(ctx.message.server.roles, name='Owner')
    admin = discord.utils.get(ctx.message.server.roles, name='Administrator')
    manager = discord.utils.get(ctx.message.server.roles, name='Co-Owner')
    msg = discord.Embed(colour=0x51cbdb, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if admin in author.roles or manager in author.roles or owner in author.roles:
        if user == None or args == None:
            msg.add_field(name=error_img, value="Not all arguments were given.\nExample: `v!give @Huskie Moderator`.")
        else:
            try:
                rolename2 = discord.utils.get(ctx.message.server.roles, name='{}'.format(args))
                if author.top_role == rolename2 or author.top_role < rolename2:
                    msg.add_field(name=error_img, value="You cannot add a role that is the same or higher than your top role.")
                else:
                    try:
                        await client.add_roles(user, rolename2)
                        msg.add_field(name=":inbox_tray: ", value="<@{}> added `{}` to <@{}>.".format(author.id, args, user.id))
                    except:
                        msg.add_field(name=error_img, value="Either I can't edit that user's role or the role you specified is higher than Co-Owner.")
            except:
                msg.add_field(name=error_img, value="The specified role was not found.")
    else:
        msg.add_field(name=error_img, value="This command can only be used by Administrators, Co-Owners and Owners.")
    await client.say(embed=msg)
##################################
client.run(os.environ['BOT_TOKEN'])
