import discord
from discord.ext import commands
import logging
import asyncio
import random
import time
import os
import os.path
import requests
import json

client = commands.Bot(command_prefix="v!")
footer_text = "Violets™"

@client.event
async def on_ready():
    print("Logged in as:")
    print(client.user.name)
    print(client.user.id)
    print("---------------")
    await client.change_presence(game=discord.Game(name='on Violets™'))

@client.command()
async def testing():
    await client.say("Testing? Testing...")

@client.command(pass_context = True)
async def kill(ctx, *, member : discord.Member = None):
    if member is None:
        await client.say(ctx.message.author.mention + ", I can't kill someone unless you tell me who you want to kill! :dagger:")
        return

    if member.id == "440770699259281408":
        await client.say(ctx.message.author.mention + ", you can't kill me if I kill you first! :smiling_imp:")
    elif member.id == "424838833633361921":
        await client.say(ctx.message.author.mention + ", I have been told under strict instructions not to kill her... that's Huskie's sister!")
    elif member.id == "299761993382887425":
        await client.say(ctx.message.author.mention + ", why do you want me to kill my master?")
    elif member.id == "208183328942194689":
        await client.say(ctx.message.author.mention + ", don't bother... she's dead inside.")
    elif member.id == ctx.message.author:
        await client.say(ctx.message.author.mention + " why do you want me to kill you?")
    else:
        random.seed(time.time())
        chosenResponse = killResponses[random.randrange(0, len(killResponses) - 1)] % member.mention
        await client.say(" " + chosenResponse)

killResponses = ["%s 'accidentaly' fell into a ditch, rip...",
               "I poisened the food of %s... This should be fun to watch :smiling_imp:",
               "It has been done, %s was stabbed in the back.",
               "I accidentaly let go of the rope... Sorry %s",
                 "%s was lit... literally...",
                 "I see everything, but I **DEFINITELY** didn't see %s get hit by a car :rolling_eyes:",
               "Somehow a toaster fell into %s's bath...",
               "%s's remains can still be seen to this day",
               "%s has ebola, they will be gone soon"]
default_invite = 'https://discord.gg/GnkADTA'

#RAPE
@client.command(pass_context = True)
async def rape(ctx, *, member : discord.Member = None):
    if member is None:
        await client.say(ctx.message.author.mention + ", you need to find someone to rape.")
    else:
        await client.say(member.mention + " has been raped by " + ctx.message.author.mention + "! :fearful: ")

# }chocolate <user> <number>
@client.command(pass_context=True)
async def chocolate(ctx, userName: discord.Member = None, number: int = None):
    author = ctx.message.author
    msg = discord.Embed(colour=0x871485, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if userName == None or number == None:
        msg.add_field(name=":warning: ", value="`v!chocolate (user) (amount)`")
    else:
        if number > 100:
            msg.add_field(name=":warning: ", value="`You can't give over 100 chocolates to someone! They gon get real fat...`")
        else:
            msg.add_field(name=":smiley: ", value="`{} gave {}` :chocolate_bar: `to {}!`\n`Be like {}!`".format(author.display_name, number, userName.display_name, author.display_name))
    await client.say(embed=msg)
    print("============================================================")
    print("}chocolate <user> <number>")
    print("{} ### {}".format(author, author.id))
    print("============================================================")

# }cookie <user> <number>
@client.command(pass_context=True)
async def cookie(ctx, userName: discord.Member = None, number: int = None):
    author = ctx.message.author
    msg = discord.Embed(colour=0x871485, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if userName == None or number == None:
        msg.add_field(name=":warning: ", value="`v!cookie (user) (amount)`")
    else:
        if number > 100:
            msg.add_field(name=":warning: ", value="`You can't give over 100 cookie to someone! Tryna give them diabetes?!`")
        else:
            msg.add_field(name=":smiley: ", value="`{} gave {}` :cookie: `to {}!`\n`Be like {}!`".format(author.display_name, number, userName.display_name, author.display_name))
    await client.say(embed=msg)
    print("============================================================")
    print("}chocolate <user> <number>")
    print("{} ### {}".format(author, author.id))
    print("============================================================")

# }ban <user> [reason]
@client.command(pass_context=True)
async def ban(ctx, userName: discord.Member = None, *, args = None):
    helper_role = discord.utils.get(ctx.message.server.roles, name='Moderator')
    mod_role = discord.utils.get(ctx.message.server.roles, name='Administrator')
    admin_role = discord.utils.get(ctx.message.server.roles, name='Co Owner')
    manager_role = discord.utils.get(ctx.message.server.roles, name='Co Owner')
    owner_role = discord.utils.get(ctx.message.server.roles, name='Owner')
    author = ctx.message.author
    msg = discord.Embed(colour=0x871485, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if mod_role in author.roles or admin_role in author.roles or manager_role in author.roles or owner_role in author.roles:
        if userName == None:
            msg.add_field(name=":warning: ", value="`v!ban <user> [reason]`")
        elif helper_role in userName.roles or mod_role in userName.roles or admin_role in userName.roles or manager_role in userName.roles or owner_role in userName.roles:
            msg.add_field(name=":warning: ", value="`You can't ban other staff!`")
        elif args == None:
            msg.add_field(name=":hammer: Ban Hammer", value="`{} banned {}!`\n`Reason: ?`".format(author.display_name, userName.display_name))
            await client.ban(userName)
        else:
            msg.add_field(name=":hammer: Ban Hammer", value="`{} banned {}!`\n`Reason: {}`".format(author.display_name, userName.display_name, args))
            await client.ban(userName)
    else:
        msg.add_field(name=":warning: ", value="`This command can only be used by Moderators, Administrators, Co Owners and Owners!`")
    await client.say(embed=msg)
    print("============================================================")
    print("}ban <user> [reason]")
    print("{} ### {}".format(author, author.id))
    print("============================================================")

# }tempban <user> <time> [reason]
@client.command(pass_context=True)
async def tempban(ctx, userName: discord.Member = None, time: int = None, *, args = None):
    helper_role = discord.utils.get(ctx.message.server.roles, name='Moderator')
    mod_role = discord.utils.get(ctx.message.server.roles, name='Moderator')
    admin_role = discord.utils.get(ctx.message.server.roles, name='Administrator')
    manager_role = discord.utils.get(ctx.message.server.roles, name='Co Owner')
    owner_role = discord.utils.get(ctx.message.server.roles, name='Owner')
    author = ctx.message.author
    msg = discord.Embed(colour=0x871485, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if mod_role in author.roles or admin_role in author.roles or manager_role in author.roles or owner_role in author.roles:
        if userName == None or time == None:
            msg.add_field(name=":warning: ", value="`v!tempban <user> <time> [reason]`")
            await client.say(embed=msg)
        else:
            if helper_role in userName.roles or mod_role in userName.roles or admin_role in userName.roles or manager_role in userName.roles or owner_role in userName.roles:
                msg.add_field(name=":warning: ", value="`You can't ban other staff!`")
                await client.say(embed=msg)
            else:
                time2 = time * 60
                user_id = userName.id
                if args == None:
                    msg.add_field(name=":hammer: Ban Hammer", value="`{} banned {} for {} minute(s)!`\n`Reason: ?`".format(author.display_name, userName.display_name, time))
                    await client.say(embed=msg)
                    await client.ban(userName)
                    await asyncio.sleep(float(time2))
                    banned_users = await client.get_bans(ctx.message.server)
                    user = discord.utils.get(banned_users,id=user_id)
                    await client.unban(ctx.message.server, user)
                    await client.say("```diff\n- The user with the following ID has been unbanned: {} ({} minute(s) are up!)\n```".format(user_id, time))
                else:
                    msg.add_field(name=":hammer: Ban Hammer", value="`{} banned {} for {} minute(s)!`\n`Reason: {}`".format(author.display_name, userName.display_name, time, args))
                    await client.say(embed=msg)
                    await client.ban(userName)
                    await asyncio.sleep(float(time2))
                    banned_users = await client.get_bans(ctx.message.server)
                    user = discord.utils.get(banned_users,id=user_id)
                    await client.unban(ctx.message.server, user)
                    await client.say("```diff\n- The user with the following ID has been unbanned: {} ({} minute(s) are up!)\n```".format(user_id, time))
    else:
        msg.add_field(name=":warning: ", value="`This command can only be used by Moderators, Administrators and Owners!`")
        await client.say(embed=msg)
    print("============================================================")
    print("}tempban <user> <time> [reason]")
    print("{} ### {}".format(author, author.id))
    print("============================================================")

# }unban <user id>
@client.command(pass_context=True)
async def unban(ctx, userID = None):
    mod_role = discord.utils.get(ctx.message.server.roles, name='Administrator')
    admin_role = discord.utils.get(ctx.message.server.roles, name='Senior Administrator')
    manager_role = discord.utils.get(ctx.message.server.roles, name='Co Owner')
    owner_role = discord.utils.get(ctx.message.server.roles, name='Owner')
    author = ctx.message.author
    msg = discord.Embed(colour=0x871485, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if mod_role in author.roles or admin_role in author.roles or manager_role in author.roles or owner_role in author.roles:
        if userID == None:
            msg.add_field(name=":warning: ", value="`i!unban <user id>`")
        else:
            banned_users = await client.get_bans(ctx.message.server)
            user = discord.utils.get(banned_users,id=userID)
            if user is not None:
                await client.unban(ctx.message.server, user)
                msg.add_field(name=":tools: ", value="`{} unbanned the user with the following ID: {}!`".format(author.display_name, userID))
            else:
                msg.add_field(name=":warning: ", value="`The ID you specified is not banned! ID: {}`".format(userID))
    else:
        msg.add_field(name=":warning: ", value="`This command can only be used by Moderators, Administrators and Owners!`")
    await client.say(embed=msg)
    print("============================================================")
    print("}unban <user>")
    print("{} ### {}".format(author, author.id))
    print("============================================================")

# serverinfo
@client.command(pass_context=True)
async def serverinfo(ctx):
    author = ctx.message.author
    msg = discord.Embed(colour=0x871485, description= "")
    msg.title = ":closed_book: Server Information :closed_book:"
    msg.add_field(name="MEMBERS", value=(len(ctx.message.server.members)), inline=True)
    msg.add_field(name="CHANNELS", value=(len(ctx.message.server.channels)), inline=True)
    msg.add_field(name="EMOJIS", value=(len(ctx.message.server.emojis)), inline=True)
    msg.add_field(name="ID", value=(ctx.message.server.id), inline=True)
    msg.add_field(name="REGION", value=(ctx.message.server.region), inline=True)
    msg.add_field(name="ROLES", value=(len(ctx.message.server.roles)), inline=True)
    msg.add_field(name="OWNER", value=(ctx.message.server.owner), inline=True)
    msg.add_field(name="RELEASE DATE:", value="23rd of March 2018", inline=True)
    await client.say(embed=msg)
    print("============================================================")
    print("<serverinfo")
    print("{} ### {}".format(author, author.id))
    print("============================================================")

# serverinfo
@client.command(pass_context=True)
async def mc(ctx):
    author = ctx.message.author
    msg = discord.Embed(colour=0x871485, description= "")
    msg.title = ":closed_book: Member Count :closed_book:"
    msg.add_field(name="MEMBERS", value=(len(ctx.message.server.members)), inline=True)
    await client.say(embed=msg)

# }userinfo <user>
@client.command(pass_context=True)
async def userinfo(ctx, userName: discord.Member = None):
    member_role = discord.utils.get(ctx.message.server.roles, name='Member')
    staff_role = discord.utils.get(ctx.message.server.roles, name='Commanding Officers')
    author = ctx.message.author
    msg = discord.Embed(colour=0x871485, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if member_role in author.roles or staff_role in author.roles:
        if userName == None:
            msg.title = ""
            msg.add_field(name="       :warning: ", value="`v!userinfo <user>`")
        else:
            imageurl = userName.avatar_url
            msg.title = ":closed_book: USER INFORMATION"
            msg.set_thumbnail(url=imageurl)
            msg.add_field(name="NAME:", value=(userName), inline=True)
            msg.add_field(name="ID:", value=(userName.id), inline=True)
            msg.add_field(name="CREATED AT:", value=(userName.created_at), inline=True)
            msg.add_field(name="JOINED AT:", value=(userName.joined_at), inline=True)
            msg.add_field(name="STATUS:", value=(userName.status), inline=True)
            msg.add_field(name="IS BOT:", value=(userName.bot), inline=True)
            msg.add_field(name="GAME:", value="Playing {}".format(userName.game), inline=True)
            msg.add_field(name="NICKNAME:", value=(userName.nick), inline=True)
            msg.add_field(name="TOP ROLE:", value=(userName.top_role), inline=True)
            msg.add_field(name="VOICE CHANNEL:", value=(userName.voice_channel), inline=True)
    await client.say(embed=msg)
    print("============================================================")
    print("<userinfo <user>")
    print("{} ### {}".format(author, author.id))
    print("============================================================")

# <lick <user>
@client.command(pass_context=True)
async def lick(ctx, userName: discord.Member = None):
    author = ctx.message.author
    msg = discord.Embed(colour=0x871485, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if userName == None:
        msg.add_field(name=":warning: ", value="`v!lick <user>`")
    else:
        msg.set_image(url="{}".format(random.choice(licklinks)))
        msg.add_field(name=":tongue: Emotes :tongue:", value="`{} licked {}!`".format(author.display_name, userName.display_name), inline=True)
    await client.say(embed=msg)
    print("============================================================")
    print("}lick <user>")
    print("{} ### {}".format(author, author.id))
    print("============================================================")

licklinks = ["https://i.imgur.com/QkRz1GJ.gif",
             "https://i.imgur.com/ObCPKYV.gif",
             "https://i.imgur.com/7fWrYqd.gif",
             "https://i.imgur.com/O8CNVUL.gif",
             "https://i.imgur.com/4QIlJtC.gif",
             "https://i.imgur.com/LptJIi1.gif",
             "https://i.imgur.com/THGgRJz.gif"]

# <takerole <user> <role name>
@client.command(pass_context=True)
async def takerole(ctx, userName: discord.Member = None, *, args = None):
    admin_role = discord.utils.get(ctx.message.server.roles, name='Administrator')
    coowner_role = discord.utils.get(ctx.message.server.roles, name='Co Owner')
    owner_role = discord.utils.get(ctx.message.server.roles, name='Owner')
    author = ctx.message.author
    msg = discord.Embed(colour=0x871485, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    serverroles = [ctx.message.server.roles]
    if admin_role in author.roles or coowner_role in author.roles or owner_role in author.roles:
        if userName == None or args == None:
            msg.add_field(name=":warning: ", value="`v!takerole <user> <role name>`")
        else:
            rolename2 = discord.utils.get(ctx.message.server.roles, name='{}'.format(args))
            if rolename2 == None:
                msg.add_field(name=":warning: ", value="`That role has not been found!`")
            elif author.top_role == rolename2 or author.top_role < rolename2:
                msg.add_field(name=":warning: ", value="`You cannot remove a role that is the same or higher than your top role!`")
            else:
                await client.remove_roles(userName, rolename2)
                msg.add_field(name=":outbox_tray: ", value="`{} removed {} from {}!`".format(author.display_name, args, userName.display_name))
    else:
        msg.add_field(name=":warning: ", value="`This command can only be used by Administrators, Co Owners and Owners!`")
    await client.say(embed=msg)
    print("============================================================")
    print("<takerole <user> <role name>")
    print("{} ### {}".format(author, author.id))
    print("============================================================")

# <giverole <user> <role name>
@client.command(pass_context=True)
async def giverole(ctx, userName: discord.Member = None, *, args = None):
    admin_role = discord.utils.get(ctx.message.server.roles, name='Administrator')
    coowner_role = discord.utils.get(ctx.message.server.roles, name='Co Owner')
    owner_role = discord.utils.get(ctx.message.server.roles, name='Owner')
    author = ctx.message.author
    msg = discord.Embed(colour=0x871485, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    serverroles = [ctx.message.server.roles]
    if admin_role in author.roles or coowner_role in author.roles or owner_role in author.roles:
        if userName == None or args == None:
            msg.add_field(name=":warning: ", value="`v!giverole <user> <role name>`")
        else:
            rolename2 = discord.utils.get(ctx.message.server.roles, name='{}'.format(args))
            if rolename2 == None:
                msg.add_field(name=":warning: ", value="`That role has not been found!`")
            elif author.top_role == rolename2 or author.top_role < rolename2:
                msg.add_field(name=":warning: ", value="`You cannot give a role that is the same or higher than your top role!`")
            else:
                await client.add_roles(userName, rolename2)
                msg.add_field(name=":inbox_tray: ", value="`{} gave {} to {}!`".format(author.display_name, args, userName.display_name))
    else:
        msg.add_field(name=":warning: ", value="`This command can only be used by Administrators, Co Owners and Owners!`")
    await client.say(embed=msg)
    print("============================================================")
    print("<giverole <user> <role name>")
    print("{} ### {}".format(author, author.id))
    print("============================================================")


# <echo <text>
@client.command(pass_context=True)
async def echo(ctx, *, args=None): 
    staff_role = discord.utils.get(ctx.message.server.roles, name='Staff')
    author = ctx.message.author
    msg = discord.Embed(colour=0x871485, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if staff_role in author.roles or staff_role in author.roles:
        if args == None:
            msg.add_field(name=":warning: ", value="v!say <text>")
            await client.say(embed=msg)
        else:
            await client.say("{}".format(args))
            await client.delete_message(ctx.message)
    else:
        msg.add_field(name=":warning: ", value="`This command can only be used by staff!`")
        await client.say(embed=msg)

# <hug <user>
@client.command(pass_context=True)
async def hug(ctx, userName: discord.Member = None):
    author = ctx.message.author
    msg = discord.Embed(colour=0x871485, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if userName == None:
        msg.add_field(name=":warning: ", value="`v!hug (user)`")
    else:
        msg.set_image(url="{}".format(random.choice(huglinks)))
        msg.add_field(name=":tongue: Emotes:tongue:", value="`{}, you got a hug from {}!`".format(userName.display_name, author.display_name), inline=True)
    await client.say(embed=msg)
    print("============================================================")
    print("}hug <user>")
    print("{} ### {}".format(author, author.id))
    print("============================================================")

huglinks = ["https://media1.tenor.com/images/7a72691a20eaefe593007f592544bbf1/tenor.gif?itemid=7931494",
            "https://media1.tenor.com/images/5cd23c906465474946375ad0414f94e5/tenor.gif?itemid=8739843",
            "http://68.media.tumblr.com/cb06ea17e532d49f71130dc47d26f971/tumblr_oku2wjbegP1vvvk86o1_500.gif",
            "https://media1.tenor.com/images/6f52c38f13fc5bc4ea671e14f6762f5a/tenor.gif?itemid=7768372",
            "http://gifimage.net/wp-content/uploads/2017/10/couple-hug-gif-8.gif",
            "https://78.media.tumblr.com/6610fb5c0d4a081556d4d758c372617f/tumblr_nj3i4byjfr1r7eta3o1_500.gif",
            "https://vignette.wikia.nocookie.net/riverdalearchie/images/3/38/Bughead_Hug.gif/revision/latest?cb=20170410021955"]

# <cuddle <user>
@client.command(pass_context=True)
async def cuddle(ctx, userName: discord.Member = None):
    author = ctx.message.author
    msg = discord.Embed(colour=0x871485, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if userName == None:
        msg.add_field(name=":warning: ", value="`v!cuddle (user)`")
    else:
        msg.set_image(url="{}".format(random.choice(cuddlelinks)))
        msg.add_field(name=":tongue: Emotes :tongue:", value="`{}, you got a cuddle from {}!`".format(userName.display_name, author.display_name), inline=True)
    await client.say(embed=msg)
    print("============================================================")
    print("}cuddle <user>")
    print("{} ### {}".format(author, author.id))
    print("============================================================")

cuddlelinks = ["https://media.giphy.com/media/MRdtc4yAr3gBO/giphy.gif",
               "https://thumbs.gfycat.com/WarmFlippantKilldeer-size_restricted.gif",
               "https://media.giphy.com/media/o5LfImOrM728w/giphy.gif",
               "https://i.gifer.com/TSO2.gif"]

# <pat <user>
@client.command(pass_context=True)
async def pat(ctx, userName: discord.Member = None):
    author = ctx.message.author
    msg = discord.Embed(colour=0x871485, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if userName == None:
        msg.add_field(name=":warning: ", value="`v!pat (user)`")
    else:
        msg.set_image(url="{}".format(random.choice(patlinks)))
        msg.add_field(name=":tongue: Emotes :tongue:", value="`{}, you got a pat from {}!`".format(userName.display_name, author.display_name), inline=True)
    await client.say(embed=msg)
    print("============================================================")
    print("}pat <user>")
    print("{} ### {}".format(author, author.id))
    print("============================================================")

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
            "https://i.imgur.com/y3La9yP.gif",
           "https://i.imgur.com/u7kxk2Y.mp4"]

# <kiss <user>
@client.command(pass_context=True)
async def kiss(ctx, userName: discord.Member = None):
    author = ctx.message.author
    msg = discord.Embed(colour=0x871485, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if userName == None:
        msg.add_field(name=":warning: ", value="`v!kiss (user)`")
    else:
        msg.set_image(url="{}".format(random.choice(kisslinks)))
        msg.add_field(name=":tongue: Emotes :tongue:", value="`{}, you got kissed by {}!`".format(userName.display_name, author.display_name), inline=True)
    await client.say(embed=msg)
    print("============================================================")
    print("}kiss <user>")
    print("{} ### {}".format(author, author.id))
    print("============================================================")

kisslinks = ["https://media1.tenor.com/images/9c92434bdeea2df04d67710f338b212d/tenor.gif?itemid=5223535",
             "https://media1.tenor.com/images/e88bcd916c0da114a8dcac8d9babc77c/tenor.gif?itemid=5052769",
             "https://m.popkey.co/96c6ee/4QVgR_s-200x150.gif",
             "https://i.gifer.com/9NC8.gif",
             "http://gifimage.net/wp-content/uploads/2017/10/morning-kiss-gif-11.gif",
             "https://thumbs.gfycat.com/LateAchingHoatzin-max-1mb.gif",
             "https://media1.tenor.com/images/b7cf0d7ff5c2bb274e8cdc6d5a87d91d/tenor.gif?itemid=5636758"]

# EVENT - JOIN / LEAVE
@client.async_event
async def on_member_join(member):
    joins = [" **Welcome to Violets™ {}! :sparkles: \n Please make sure to read the rules and if you want to partner, contact any of the staff with the role Partnership Manager :smiley:\n Also don't forget to get roles and colors in the <#440562714989821982> and the <#427124007377305611> channels :wink: \n Enjoy your stay :sparkling_heart:**".format(member.mention)]
    await client.send_message(client.get_channel("426680388585521163"), "{}".format(random.choice(joins)))
    print("============================================================")
    print("JOIN EVENT")
    print("{} ### {}".format(userName, userName.id))
    print("============================================================")

@client.async_event
async def on_member_remove(userName: discord.User):
    leaves = ["Cya `{}` :wave:".format(userName)]
    await client.send_message(client.get_channel("426680388585521163"), "{}".format(random.choice(leaves)))
    print("============================================================")
    print("LEAVE EVENT")
    print("{} ### {}".format(userName, userName.id))
    print("============================================================")

# <eightball <yes or no question>
@client.command(pass_context=True)
async def eightball(ctx, *, args=None):
    author = ctx.message.author
    msg = discord.Embed(colour=0x871485, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if args == None:
        msg.add_field(name="warning: ", value="`v!eightball (yes or no question)`")
    else:
        msg.add_field(name="Magic Eight Ball", value=":question: **Question:**\n`{}`\n \n:8ball: **Answer:**\n`{}`".format(args, random.choice(eightballmsgs)))
    await client.say(embed=msg)
    print("============================================================")
    print("<eightball <yes or no question>")
    print("{} ### {}".format(author, author.id))
    print("============================================================")

eightballmsgs = ["Yes!",
                 "No!",
                 "Probably!",
                 "Most likely!",
                 "Probably not!",
                 "Definitely!",
                 "Definitely not!",
                 "Of course!",
                 "Of course not!",
                 "WTF no!",
                 "Hell yeah!"]

# <poke <user>
@client.command(pass_context=True)
async def poke(ctx, userName: discord.Member = None):
    author = ctx.message.author
    msg = discord.Embed(colour=0x871485, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if userName == None:
        msg.add_field(name=":warning: ", value="`v!poke (user)`")
    else:
        msg.set_image(url="{}".format(random.choice(pokelinks)))
        msg.add_field(name=":tongue: Emotes :tongue:", value="`{}, you got poked by {}!`".format(userName.display_name, author.display_name), inline=True)
    await client.say(embed=msg)
    print("============================================================")
    print("}poke <user>")
    print("{} ### {}".format(author, author.id))
    print("============================================================")

pokelinks = ["https://i.imgur.com/HAAktbl.gif",
             "https://i.imgur.com/Fmd0Rsu.gif",
             "https://i.imgur.com/1rObSM3.gif",
             "https://i.imgur.com/Wo2fc94.gif",
             "https://i.imgur.com/rtTucBW.gif",
             "https://i.imgur.com/4c2mC5d.gif",
             "https://i.imgur.com/1DVD84G.gif"]

# <spank <user>
@client.command(pass_context=True)
async def spank(ctx, userName: discord.Member = None):
    author = ctx.message.author
    msg = discord.Embed(colour=0x871485, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if userName == None:
        msg.add_field(name=":warning: ", value="`v!spank (user)`")
    else:
        msg.set_image(url="{}".format(random.choice(spanklinks)))
        msg.add_field(name=":tongue: Emotes :tongue:", value="`{} spanked {}!`".format(author.display_name, userName.display_name), inline=True)
    await client.say(embed=msg)
    print("============================================================")
    print("}spank <user>")
    print("{} ### {}".format(author, author.id))
    print("============================================================")

spanklinks = ["https://i.imgur.com/dt1TTQu.gif",
              "https://i.imgur.com/ZsTbDvh.gif",
              "https://i.imgur.com/4LHwG60.gif",
              "https://i.imgur.com/xLOoHKP.gif",
              "https://i.imgur.com/UShywVv.gif",
              "https://i.imgur.com/RE3mnrA.gif"]

# }calculator <math problem>
@client.command(pass_context=True)
async def calculator(ctx, *, args=None):
    author = ctx.message.author
    msg = discord.Embed(colour=0x871485, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if args == None:
        msg.add_field(name=":warning: ", value="`v!calculator (math problem)`")
    else:
        answer = str(eval(args))
        msg.add_field(name=":fax: Calculator", value= "`Problem: {}`\n \n`Answer: {}`".format(args, answer), inline=True)
    await client.say(embed=msg)
    print("============================================================")
    print("}calculator <math problem>")
    print("{} ### {}".format(author, author.id))
    print("============================================================")

# <battle <user>
@client.command(pass_context=True)
async def battle(ctx, userName: discord.Member = None):
    attacker = random.randint(0, 301)
    attacked = random.randint(0, 301)
    attackerhealth = 300 - attacked
    attackedhealth = 300 - attacker
    author = ctx.message.author
    msg = discord.Embed(colour=0x871485, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if userName == None:
        msg.add_field(name=":warning: ", value="`v!battle (user)`")
    else:
        msg.add_field(name= ":crossed_swords: B A T T LE :crossed_swords: ", value= "**~~=================================~~**\n`{}` :vs: `{}`\n**~~=================================~~**\n:small_orange_diamond: `{}`\n \n:arrow_forward: {}\n \n:fast_forward: {} DMG\n**~~=================================~~**\n:small_orange_diamond: `{}`\n \n:arrow_forward: {}\n \n:fast_forward: {} DMG\n**~~=================================~~**\n:small_orange_diamond: `{}`\n:hearts: {} HP\n \n:small_orange_diamond: `{}`\n:hearts: {} HP\n**~~=================================~~**".format(author.display_name, userName.display_name, author.display_name, random.choice(attacks), attacker, userName.display_name, random.choice(attacks), attacked, author.display_name, attackerhealth, userName.display_name, attackedhealth), inline=True)
        if attacker == attacked:
            msg.add_field(name= ":diamonds: N O  W I N N E R :diamonds:", value= "**~~=================================~~**\n`{}`\n`{}`\n**~~=================================~~**".format(author.display_name, userName), inline=True)
        elif attacker > attacked:
            msg.add_field(name= ":diamonds: W I N N E R :diamonds:", value= "**~~=================================~~**\n`{}`\n**~~=================================~~**".format(author.display_name), inline=True)
        else:
            msg.add_field(name= ":diamonds: W I N N E R :diamonds:", value= "**~~=================================~~**\n`{}`\n**~~=================================~~**".format(userName.display_name), inline=True)
    await client.say(embed=msg)
    print("============================================================")
    print("}battle <user>")
    print("{} ### {}".format(author, author.id))
    print("============================================================")

attacks = ["Punches the opponent :punch: ", "Kicks the opponent :boot: ", "Throws the opponent :raised_hands: ", "Stabs the opponent :dagger: ", "Shoots the opponent :gun: ",
           "Sets the opponent on fire :fire: ", "Poisons the opponent :syringe: ", "Throws a bomb at the opponent :bomb: ", "Uses a shield to deal damage with the same attack as the opponent's :shield: ", "Chokes the opponent using chains :chains: ",
           "Cuts the opponent :knife: ", "Hits the opponent's head with a hammer :hammer: ", "Uses dark magic to attack the opponent :skull_crossbones: ", "Casts a spell on the opponent :sparkles: ", "Pukes at the opponent :nauseated_face: ",
           "Scares the opponent :ghost: ", "Summons a demon to attack the opponent :smiling_imp: ", "Transforms into a robot to attack the opponent :robot: ", "Farts at the opponent :dash: ", "Summons a tornado near the opponent :cloud_tornado: ",
           "Summons a meteor and hits the opponent with it :comet: ", "Hits the opponent with lightning :zap: ", "Freezes the opponent :snowflake: ", "Cripples the opponent :boom: ", "Shoots the opponent using a bow and arrow :bow_and_arrow: ",
           "Drives over the opponent :red_car: ", "Chops off the opponent's leg :crossed_swords: ", "Drains some of the opponent's life :broken_heart: ", "Steals the opponent's soul :black_heart: ", "Stuns the opponent :octagonal_sign: ",
           "Uses nuclear energy to attack the opponent :radioactive: ", "Blinds the opponent :eye: ", "Deafens the opponent :ear: ", "Uses mind control on the opponent :alien: ", "Summons minions to attack the opponent :busts_in_silhouette: ",
           "Traps the opponent :spider_web: "] 

@client.command(pass_context=True)
async def dice(ctx):
    r=random.randint(1,6)
    await client.send_message(ctx.message.channel, "You rolled a " + str(r) + "!")
    
# <matchmake <user1> <user2>
@client.command(pass_context=True)
async def ship(ctx, userName1: discord.Member = None, userName2: discord.Member = None):
    percent = random.randint(0, 101)
    author = ctx.message.author
    msg = discord.Embed(colour=0x871485, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if userName1 == None or userName2 == None:
        msg.add_field(name=":warning: ",value="`v!ship (user1) (user2)`")
    else:
        if percent >= 1 and percent <= 10:
            msg.add_field(name=":heartpulse: Matchmaking... :heartpulse: ", value=":small_red_triangle_down: **{}**\n:small_red_triangle: **{}**\n```fix\n{}% - No point\n```\n:sob: ".format(userName1.display_name, userName2.display_name, percent))
        elif percent >= 11 and percent <= 20:
            msg.add_field(name=":heartpulse: Matchmaking... :heartpulse: ", value=":small_red_triangle_down: **{}**\n:small_red_triangle: **{}**\n```fix\n{}% - Trash\n```\n:cry: ".format(userName1.display_name, userName2.display_name, percent))
        elif percent >= 21 and percent <= 30:
            msg.add_field(name=":heartpulse: Matchmaking... :heartpulse: ", value=":small_red_triangle_down: **{}**\n:small_red_triangle: **{}**\n```fix\n{}% - Just don't\n```\n:frowning2: ".format(userName1.display_name, userName2.display_name, percent))
        elif percent >= 31 and percent <= 40:
            msg.add_field(name=":heartpulse: Matchmaking... :heartpulse: ", value=":small_red_triangle_down: **{}**\n:small_red_triangle: **{}**\n```fix\n{}% - The opposite to good\n```\n:slight_frown: ".format(userName1.display_name, userName2.display_name, percent))
        elif percent >= 41 and percent <= 50:
            msg.add_field(name=":heartpulse: Matchmaking... :heartpulse: ", value=":small_red_triangle_down: **{}**\n:small_red_triangle: **{}**\n```fix\n{}% - 50/50 ish\n```\n:neutral_face: ".format(userName1.display_name, userName2.display_name, percent))
        elif percent >= 51 and percent <= 60:
            msg.add_field(name=":heartpulse: Matchmaking... :heartpulse: ", value=":small_red_triangle_down: **{}**\n:small_red_triangle: **{}**\n```fix\n{}% - Good\n```\n:slight_smile: ".format(userName1.display_name, userName2.display_name, percent))
        elif percent >= 61 and percent <= 70:
            msg.add_field(name=":heartpulse: Matchmaking... :heartpulse: ", value=":small_red_triangle_down: **{}**\n:small_red_triangle: **{}**\n```fix\n{}% - Very Good\n```\n:smiley: ".format(userName1.display_name, userName2.display_name, percent))
        elif percent >= 71 and percent <= 80:
            msg.add_field(name=":heartpulse: Matchmaking... :heartpulse: ", value=":small_red_triangle_down: **{}**\n:small_red_triangle: **{}**\n```fix\n{}% - Fantastic\n```\n:blush: ".format(userName1.display_name, userName2.display_name, percent))
        elif percent >= 81 and percent <= 90:
            msg.add_field(name=":heartpulse: Matchmaking... :heartpulse: ", value=":small_red_triangle_down: **{}**\n:small_red_triangle: **{}**\n```fix\n{}% - Amazing\n```\n:heart_eyes: ".format(userName1.display_name, userName2.display_name, percent))
        else:
            msg.add_field(name=":heartpulse: Matchmaking... :heartpulse: ", value=":small_red_triangle_down: **{}**\n:small_red_triangle: **{}**\n```fix\n{}% - Get a room you two\n```\n:revolving_hearts: ".format(userName1.display_name, userName2.display_name, percent))
    await client.say(embed=msg)
    
@client.command(pass_context=True)
async def warn(ctx, userName: discord.Member = None, *, args = None):
    helper_role = discord.utils.get(ctx.message.server.roles, name='Partnership Manager')
    mod_role = discord.utils.get(ctx.message.server.roles, name='Moderator')
    admin_role = discord.utils.get(ctx.message.server.roles, name='Administrator')
    manager_role = discord.utils.get(ctx.message.server.roles, name='Co Owner')
    owner_role = discord.utils.get(ctx.message.server.roles, name='Owners')
    author = ctx.message.author
    msg = discord.Embed(colour=0x871485, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    msg2 = discord.Embed(colour=0x871485, description= "")
    msg2.title = ""
    msg2.set_footer(text=footer_text)
    if helper_role in author.roles or mod_role in author.roles or admin_role in author.roles or manager_role in author.roles or owner_role in author.roles:
        if userName == None or args == None:
            msg.add_field(name=":warning: ", value="`v!warn (user) (reason)`")
            await client.say(embed=msg)
        else:
            if helper_role in userName.roles or mod_role in userName.roles or admin_role in userName.roles or manager_role in userName.roles or owner_role in userName.roles:
                msg.add_field(name=":warning: ", value="`You cannot warn other staff!`")
                await client.say(embed=msg)
            else:
                msg2.add_field(name=":pencil: ", value="`You have been warned by {} in Violets!`\n`Reason: {}`".format(author.display_name, args))
                msg.add_field(name=":pencil: ", value="`{} warned {}!`\n`Reason: {}`".format(author.display_name, userName.display_name, args))
                await client.say(embed=msg)
                await client.send_message(userName, embed=msg2)
    else:
        msg.add_field(name=":warning: ", value="`This command can only be used by staff!`")
        await client.say(embed=msg)
        
# <kick <user> [reason]
@client.command(pass_context=True)
async def kick(ctx, userName: discord.Member = None, *, args = None):
    helper_role = discord.utils.get(ctx.message.server.roles, name='Partnership Manager')
    mod_role = discord.utils.get(ctx.message.server.roles, name='Moderators')
    admin_role = discord.utils.get(ctx.message.server.roles, name='Administrator')
    manager_role = discord.utils.get(ctx.message.server.roles, name='Co Owner')
    owner_role = discord.utils.get(ctx.message.server.roles, name='Owner')
    author = ctx.message.author
    msg = discord.Embed(colour=0x871485, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if mod_role in author.roles or admin_role in author.roles or manager_role in author.roles or owner_role in author.roles:
        if userName == None:
            msg.add_field(name=":warning: ", value="`v!kick (user) (reason)`")
        elif helper_role in userName.roles or mod_role in userName.roles or admin_role in userName.roles or manager_role in userName.roles or owner_role in userName.roles:
            msg.add_field(name=":warning: ", value="`You can't kick other staff!`")
        elif args == None:
            msg.add_field(name=":boot: Kicker", value="`{} kicked {}!`\n`Reason: ?`".format(author.display_name, userName.display_name))
            await client.kick(userName)
        else:
            msg.add_field(name=":boot: Kicker", value="`{} kicked {}!`\n`Reason: {}`".format(author.display_name, userName.display_name, args))
            await client.kick(userName)
    else:
        msg.add_field(name=":octagonal_sign: ", value="`This command can only be used by Moderators, Administrators, Co Owners and Owners!`")
    await client.say(embed=msg)
    
# }punish <user> <time> [reason]
@client.command(pass_context=True)
async def tempmute(ctx, userName: discord.Member = None, time: int = None, *, args = None):
    member_role = discord.utils.get(ctx.message.server.roles, name ='Members')
    punished_role = discord.utils.get(ctx.message.server.roles, name='Muted')
    helper_role = discord.utils.get(ctx.message.server.roles, name='Helper')
    mod_role = discord.utils.get(ctx.message.server.roles, name='Moderator')
    admin_role = discord.utils.get(ctx.message.server.roles, name='Administrator')
    manager_role = discord.utils.get(ctx.message.server.roles, name='Co Owner')
    owner_role = discord.utils.get(ctx.message.server.roles, name='Owner')
    author = ctx.message.author
    msg = discord.Embed(colour=0x871485, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if helper_role in author.roles or mod_role in author.roles or admin_role in author.roles or manager_role in author.roles or owner_role in author.roles:
        if userName == None or time == None:
            msg.add_field(name=":warning: ", value="`v!tempmute (user) (time) (reason)`")
            await client.say(embed=msg)
        elif helper_role in userName.roles or mod_role in userName.roles or admin_role in userName.roles or manager_role in userName.roles or owner_role in userName.roles:
            msg.add_field(name=":warning: ", value="`You can't punish other staff!`")
            await client.say(embed=msg)
        elif punished_role in userName.roles:
            msg.add_field(name=":warning: ", value="`That user is already muted!`")
            await client.say(embed=msg)
        else:
            time2 = time * 60
            if args == None:
                await client.add_roles(userName, punished_role)
                await client.remove_roles(userName, member_role)
                msg.add_field(name=":speak_no_evil: ", value="`{} has been temporarily muted by {}! for {} minute(s)!`\n`Reason: ?`".format(userName.display_name, author.display_name, time))
                await client.say(embed=msg)
                await asyncio.sleep(float(time2))
                await client.remove_roles(userName, punished_role)
                await client.say("```diff\n- Removed {}'s mute! ({} minute(s) are up.)\n```".format(userName.display_name, time))
            else:
                await client.add_roles(userName, punished_role)
                msg.add_field(name=":speak_no_evil: ", value="`{} has been muted by {} for {} minute(s)!`\n`Reason: {}`".format(userName.display_name, author.display_name, time, args))
                await client.say(embed=msg)
                await asyncio.sleep(float(time2))
                await client.remove_roles(userName, punished_role)
                await client.say("```diff\n- Removed {}'s mute! ({} minute(s) are up.)\n```".format(userName.display_name, time))
    else:
        msg.add_field(name=":warning: ", value="`This command can only be used by staff!`")
        await client.say(embed=msg)
        
# }partner <user>
@client.command(pass_context=True)
async def partner(ctx, userName: discord.Member = None):
    partner_role = discord.utils.get(ctx.message.server.roles, name='Partners')
    pm_role = discord.utils.get(ctx.message.server.roles, name ='Partnership Manager')
    mod_role = discord.utils.get(ctx.message.server.roles, name='Moderator')
    admin_role = discord.utils.get(ctx.message.server.roles, name='Administrator')
    manager_role = discord.utils.get(ctx.message.server.roles, name='Co Owner')
    owner_role = discord.utils.get(ctx.message.server.roles, name='Owner')
    author = ctx.message.author
    msg = discord.Embed(colour=0x871485, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if pm_role in author.roles or mod_role in author.roles or admin_role in author.roles or manager_role in author.roles or owner_role in author.roles:
        if userName == None:
            msg.add_field(name=":warning: ", value="`v!partner <user>`")
        else:
            if partner_role in userName.roles:
                await client.remove_roles(userName, partner_role)
                msg.add_field(name=":credit_card: ", value="`{} removed the partnership with {}!`".format(author.display_name, userName.display_name))
            else:
                await client.add_roles(userName, partner_role)
                msg.add_field(name=":credit_card: ", value="`{} partnered with {}!`".format(author.display_name, userName.display_name))
    else:
        msg.add_field(name=":warning: ", value="`This command can only be used by Moderators, Administrators, Co-Owners and Owners!`")
    await client.say(embed=msg)
    print("============================================================")
    print("}partner <user>")
    print("{} ### {}".format(author, author.id))
    print("============================================================")
    
# }purge <number>
@client.command(pass_context=True)
async def purge(ctx, number: int = None):
    helper_role = discord.utils.get(ctx.message.server.roles, name='Moderator')
    mod_role = discord.utils.get(ctx.message.server.roles, name='Moderator')
    admin_role = discord.utils.get(ctx.message.server.roles, name='Administrator')
    manager_role = discord.utils.get(ctx.message.server.roles, name='Co Owner')
    owner_role = discord.utils.get(ctx.message.server.roles, name='Owner')
    author = ctx.message.author
    msg = discord.Embed(colour=0x871485, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if helper_role in author.roles or mod_role in author.roles or admin_role in author.roles or manager_role in author.roles or owner_role in author.roles:
        if number == None:
            msg.add_field(name=":warning: ", value="`v!purge <number>`")
        else:
            deleted = await client.purge_from(ctx.message.channel, limit=number)
            if len(deleted) < number:
                msg.add_field(name=":wastebasket: ", value="`{} tried to delete {} messages!`\n`Deleted {} message(s)!`".format(author.display_name, number, len(deleted)))
            else:
                msg.add_field(name=":wastebasket: ", value="`{} deleted {} message(s)!`".format(author.display_name, len(deleted)))
    else:
        msg.add_field(name=":warning: ", value="`This command can only be used by staff!`")
    await client.say(embed=msg)
    print("============================================================")
    print("}purge <number>")
    print("{} ### {}".format(author, author.id))
    print("============================================================")
    
# }help
client.remove_command('help')
@client.command(pass_context=True)
async def help(ctx):
    author = ctx.message.author
    msg = discord.Embed(colour=0x871485, description= "")
    msg.title = ""
    msg.add_field(name=":incoming_envelope: ", value="`You can see all commands in the #viola-commands channel!`")
    msg.set_footer(text=footer_text)
    await client.say(embed=msg)
    print("============================================================")
    print("}help")
    print("{} ### {}".format(author, author.id))
    print("============================================================")
    
# <sorry <user>
@client.command(pass_context=True)
async def sorry(ctx, userName: discord.Member = None):
    author = ctx.message.author
    msg = discord.Embed(colour=0x871485, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if userName == None:
        msg.add_field(name=":warning: ", value="`v!sorry (user)`")
    else:
        msg.set_image(url="{}".format(random.choice(sorrylinks)))
        msg.add_field(name=":tongue: Emotes :tongue:", value="`{}, {} is saying sorry!`".format(userName.display_name, author.display_name), inline=True)
    await client.say(embed=msg)
    print("============================================================")
    print("}hug <user>")
    print("{} ### {}".format(author, author.id))
    print("============================================================")

sorrylinks = ["https://i.imgur.com/9f2FsAQ.gif",
            "https://i.imgur.com/9f2FsAQ.gif",
            "https://i.imgur.com/9f2FsAQ.gif"]

# %annoy <user> [text]
@client.command(pass_context=True)
async def annoy(ctx, userName: discord.Member = None, *, args = None):
    author = ctx.message.author
    msg = discord.Embed(colour=0x871485, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if userName == None:
        msg.add_field(name=":warning: ", value="`v!annoy (user) (text)`")
        await client.say(embed=msg)
    else:
        if args == None:
            msg.add_field(name=":drooling_face: ", value="`Sending a beautiful video to {}...`".format(userName.display_name))
            await client.say(embed=msg)
            await client.send_message(userName, "{}".format(random.choice(rickrolls)))
        else:
            msg.add_field(name=":drooling_face: ", value="`Sliding in {}'s DMs...`".format(userName.display_name))
            await client.say(embed=msg)
            await client.send_message(userName, "{}".format(args))
    print("============================================================")
    print("}rickroll <user>")
    print("{} ### {}".format(author, author.id))
    print("============================================================")
    
rickrolls = ["https://www.youtube.com/watch?v=V-_O7nl0Ii0",
             "https://www.youtube.com/watch?v=ID_L0aGI9bg",
             "https://www.youtube.com/watch?v=yBLdQ1a4-JI",
             "https://www.youtube.com/watch?v=6-HUgzYPm9g",
             "https://www.youtube.com/watch?v=Gc2u6AFImn8",
             "https://www.youtube.com/watch?v=4n7_Il1dft0",
             "https://www.youtube.com/watch?v=OL7B2z56ziQ",
             "https://www.youtube.com/watch?v=li7qFeHI5KM",
             "https://www.youtube.com/watch?v=wvWX-jWhLBI",
             "https://youtu.be/ByC8sRdL-Ro",
             "https://www.youtube.com/watch?v=HoWcnTsc5s8",
             "hi lol",
             "https://www.youtube.com/watch?v=E9DlT_DS0wA",
             "https://youtu.be/rp8hvyjZWHs",
             "https://www.youtube.com/watch?v=3HfnLwopb58"]

# }idban <user id> [reason]
@client.command(pass_context=True)
async def idban(ctx, userID: int = None, *, args = None):
    manager_role = discord.utils.get(ctx.message.server.roles, name='Co Owner')
    owner_role = discord.utils.get(ctx.message.server.roles, name='Administrator')
    author = ctx.message.author
    guild = ctx.message.server
    user = guild.get_member(userID)
    msg = discord.Embed(colour=0x871485, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if manager_role in author.roles or owner_role in author.roles:
        if userID == None:
            msg.add_field(name=":warning: ", value="`v!idban (userID) (reason)`")
        elif user == None and args is not None:
            msg.add_field(name=":tools: ", value="`{} ID-Banned the following ID: {}!`\n`Reason: {}`".format(author.display_name, userID, args))
            await client.http.ban(userID, guild.id, 0)
        elif user == None and args == None:
            msg.add_field(name=":tools: ", value="`{} ID-Banned the following ID: {}!`\n`Reason: ?`".format(author.display_name, userID))
            await client.http.ban(userID, guild.id, 0)
        else:
            msg.add_field(name=":warning: ", value="`Unknown error!`")
    else:
        msg.add_field(name=":warning: ", value="`This command can only be used by Administrators+!`")
    await client.say(embed=msg)
    print("============================================================")
    print("}idban <user id> [reason]")
    print("{} ### {}".format(author, author.id))
    print("============================================================")
    
# }report <user> <reason>
@client.command(pass_context=True)
async def report(ctx, userName: discord.Member = None, *, args = None):
    author = ctx.message.author
    msg = discord.Embed(colour=0x871485, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    msg2 = discord.Embed(colour=0x871485, description= "")
    msg2.title = ""
    msg2.set_footer(text=footer_text)
    if userName == None or args == None:
        msg.add_field(name=":warning: ", value="`v!report <user> <reason>`")
    else:
        msg.add_field(name=":clipboard: REPORT", value="`{} has reported {}!`".format(author.display_name, userName.display_name))
        msg2.add_field(name=":clipboard: REPORT", value="`Reporter:`\n`{} ### {}`\n`Reported:`\n`{} ### {}`\n`Reason:`\n`{}`".format(author, author.id, userName, userName.id, args))
        channel = client.get_channel('444087235197927424')
        await client.send_message(channel, embed=msg2)
    await client.say(embed=msg)
    print("============================================================")
    print("}report <user> <reason>")
    print("{} ### {}".format(author, author.id))
    print("============================================================")
    
# }rate <text>
@client.command(pass_context=True)
async def rate(ctx, *, args = None):
    author = ctx.message.author
    msg = discord.Embed(colour=0x871485, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if args == None:
        msg.add_field(name=":warning: ", value="`v!rate <text>`")
    else:
        msg.add_field(name=":scales:", value="`I'd rate {} a {}/10`".format(args, random.randint(0, 11)))
    await client.say(embed=msg)
    print("============================================================")
    print("}rate <text>")
    print("{} ### {}".format(author, author.id))
    print("============================================================")
    
# }partner <user>
@client.command(pass_context=True)
async def mute(ctx, userName: discord.Member = None):
    muted_role = discord.utils.get(ctx.message.server.roles, name='Muted')
    pm_role = discord.utils.get(ctx.message.server.roles, name ='Moderator')
    mod_role = discord.utils.get(ctx.message.server.roles, name='Moderator')
    admin_role = discord.utils.get(ctx.message.server.roles, name='Administrator')
    manager_role = discord.utils.get(ctx.message.server.roles, name='Co Owner')
    owner_role = discord.utils.get(ctx.message.server.roles, name='Owner')
    author = ctx.message.author
    msg = discord.Embed(colour=0x871485, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if pm_role in author.roles or mod_role in author.roles or admin_role in author.roles or manager_role in author.roles or owner_role in author.roles:
        if userName == None:
            msg.add_field(name=":warning: ", value="`v!mute <user>`")
        else:
            if muted_role in userName.roles:
                await client.remove_roles(userName, muted_role)
                msg.add_field(name=":speak_no_evil: ", value="`{} unmuted {}!`".format(author.display_name, userName.display_name))
            else:
                await client.add_roles(userName, muted_role)
                msg.add_field(name=":speak_no_evil: ", value="`{} muted {}!`".format(author.display_name, userName.display_name))
    else:
        msg.add_field(name=":warning: ", value="`This command can only be used by Moderators, Administrators, Co-Owners and Owners!`")
    await client.say(embed=msg)
    print("============================================================")
    print("}partner <user>")
    print("{} ### {}".format(author, author.id))
    print("============================================================")
    
# }nick <user> [nickname]
@client.command(pass_context=True)
async def nick(ctx, userName: discord.Member = None, *, args = None):
    helper_role = discord.utils.get(ctx.message.server.roles, name='Moderator')
    mod_role = discord.utils.get(ctx.message.server.roles, name='Administrator')
    admin_role = discord.utils.get(ctx.message.server.roles, name='Administrator')
    manager_role = discord.utils.get(ctx.message.server.roles, name='Co Owner')
    owner_role = discord.utils.get(ctx.message.server.roles, name='Owner')
    author = ctx.message.author
    msg = discord.Embed(colour=0x871485, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if helper_role in author.roles or mod_role in author.roles or admin_role in author.roles or manager_role in author.roles or owner_role in author.roles:
        if userName == None:
            msg.add_field(name=":warning: ", value="`v!nick (user) (nickname)`")
        elif args == None:
            nickname = args
            await client.change_nickname(userName, nickname)
            msg.add_field(name=":label: ", value="`{} removed {}'s nickname!`".format(author.display_name, userName.display_name))
        else:
            nickname = args
            msg.add_field(name=":label: ", value="`{} changed {}'s nickname to {}!`".format(author.display_name, userName.display_name, args))
            await client.change_nickname(userName, nickname)
    else:
        msg.add_field(name=":warning: ", value="`This command can only be used by staff!`")
    await client.say(embed=msg)
    print("============================================================")
    print("}nick <user> <nickname>")
    print("{} ### {}".format(author, author.id))
    print("============================================================")
    
# }cry
@client.command(pass_context=True)
async def cry(ctx):
    author = ctx.message.author
    msg = discord.Embed(colour=0x871485, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    msg.set_image(url="{}".format(random.choice(crylinks)))
    msg.add_field(name=":tongue: Emotes :tongue:", value="`{} is crying! *Pat pat pat*`".format(author.display_name), inline=True)
    await client.say(embed=msg)
    print("============================================================")
    print("}cry")
    print("{} ### {}".format(author, author.id))
    print("============================================================")
    
# }fart
@client.command(pass_context=True)
async def fart(ctx):
    author = ctx.message.author
    msg = discord.Embed(colour=0x871485, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    msg.add_field(name=":tongue: Emotes :tongue:", value="{} Just farted, clear out the area... :dancer: :dash:".format(author.display_name), inline=True)
    await client.say(embed=msg)
    print("============================================================")
    print("}cry")
    print("{} ### {}".format(author, author.id))
    print("============================================================")
    
crylinks = ["https://media1.giphy.com/media/ROF8OQvDmxytW/giphy-downsized.gif",
            "https://media1.tenor.com/images/06ae6bbe852471939cf61a81e5a9eb23/tenor.gif?itemid=5370823",
            "https://78.media.tumblr.com/e9fb46144efc579746e57bcaebd3350a/tumblr_olrmy4djBG1tydz8to1_500.gif",
            "http://i.imgur.com/k5B1CBd.jpg",
            "https://media.giphy.com/media/hyU0RHvlS3iQU/giphy.gif",
            "https://media1.tenor.com/images/5912cbe4bc0dec511b5e0996a2ad9b6f/tenor.gif?itemid=8620704",
            "https://s9.favim.com/orig/131225/an-anime-anime-gif-anime-guy-Favim.com-1182388.gif",
            "https://media1.tenor.com/images/06ae6bbe852471939cf61a81e5a9eb23/tenor.gif?itemid=5370823",
            "https://media.tenor.com/images/d571f86a5adcb4545444e9d1dc4638f9/tenor.gif",
            "https://i.pinimg.com/originals/73/3d/59/733d5948098702b0d6f156819143b581.gif",
            "https://67.media.tumblr.com/aa7766807df523677bb9c73da94ee049/tumblr_npwxeb2dPp1u7ltf6o1_500.gif",
            "https://static2.fjcdn.com/thumbnails/comments/I+actually+dont+remember+i+think+because+of+the+horns+_78025db895d293c2765eaace345742f0.gif"]

# }slap <user>
@client.command(pass_context=True)
async def slap(ctx, userName: discord.Member = None):
    author = ctx.message.author
    msg = discord.Embed(colour=0x871485, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if userName == None:
        msg.add_field(name=":warning: ", value="`v!slap (user)`")
    else:
        msg.set_image(url="{}".format(random.choice(slaplinks)))
        msg.add_field(name=":tongue: Emotes :tongue: ", value="`{}, you got slapped by {}! Ouch...`".format(userName.display_name, author.display_name), inline=True)
    await client.say(embed=msg)
    print("============================================================")
    print("}slap <user>")
    print("{} ### {}".format(author, author.id))
    print("============================================================")
    
slaplinks = ["https://i.imgur.com/EAF42MG.gif",
             "https://i.imgur.com/tLTT9Q4.gif",
             "https://i.imgur.com/tEWjg7v.gif",
             "https://i.imgur.com/MlkLTjv.gif",
             "https://i.imgur.com/hoTYJZP.gif",
             "https://i.imgur.com/Pthhs3Y.gif"]

# }hide
@client.command(pass_context=True)
async def hide(ctx):
    author = ctx.message.author
    msg = discord.Embed(colour=0x871485, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    msg.set_image(url="{}".format(random.choice(hidelinks)))
    msg.add_field(name=":tongue: Emotes :tongue:", value="`{} is hiding!`".format(author.display_name), inline=True)
    await client.say(embed=msg)
    print("============================================================")
    print("}cry")
    print("{} ### {}".format(author, author.id))
    print("============================================================")

hidelinks = ["http://www.gifbin.com/bin/012011/1295259460_cat-hides-in-box.gif",
             "https://www.cat-gifs.com/w3/Funny-Cat-GIF-Weird-Black-Cat-with-big-round-eyes-tries-to-hide-in-his-small-green-box.gif",
             "http://www.letssmiletoday.com/uploads/images/9642-Quick_hide_in_the_box_20.04.2012.gif",
             "https://i.gifer.com/VfBm.gif",
             "https://i.imgur.com/gFMNHyA.gif",
             "https://i.imgur.com/UXSe4sQ.gif",
             "https://i.chzbgr.com/full/7074625536/hD0F6F5CE/"]
    
@client.event
async def on_message(message, timeout=10,):
    await client.process_commands(message)
    if message.content.lower().startswith('who is huskie'):
        await client.send_message(message.channel, "Da best")
        
    if message.content.lower().startswith('who is seven'):
        await client.send_message(message.channel, "A person who likes to make drum noises out of his eating hole.")
        
    if message.content.lower().startswith('who is zemm'):
        await client.send_message(message.channel, "Satan's wife")
        
    if message.content.lower().startswith('who is stacey'):
        await client.send_message(message.channel, "Claimed by Huskie, he do the protec")
        
    if message.content.lower().startswith('who is yami'):
        await client.send_message(message.channel, "Claimed by Hikari.")
        
    if message.content.lower().startswith('who is hikari'):
        await client.send_message(message.channel, "Claimed by Yami.")
        
    if message.content.lower().startswith('gay'):
        await client.send_message(message.channel, "Uno reverse card has been played")
        
    if message.content.lower().startswith('no u'):
        await client.send_message(message.channel, "Aww, no us <3")
              
    if message.content.lower().startswith('who is zebro'):
        await client.send_message(message.channel, "She is a moist slut, and tsundere for pala")
        
    if message.content.lower().startswith('huskie'):
        await client.send_message(message.channel, "<@299761993382887425>")
        
    if message.content.lower().startswith('vwelc'):
        await client.send_message(message.channel, "Welcome to Violets! \n To assign your self colors go to <#427124007377305611> \n and to assign yourself other Roles go to <#440562714989821982> \n Enjoy your stay, Thanks :)")

    if message.content.lower().startswith('v!coin'): #Coinflip 50/50% chance kopf oder zahl
        choice = random.randint(1,2)
        if choice == 1:
            await client.add_reaction(message, '🌑')
        if choice == 2:
            await client.add_reaction(message, '🌕')
            
    if message.content.lower().startswith('can i'):
        await client.send_message(message.channel, "Would you like fries with that?")
                                  
    if message.content.lower().startswith('goodnight'):
        await client.send_message(message.channel, "꒰´ ु-௰ू-॰`꒱⋆｡˚✩ɢ∞פ ɴⅈɢhт ༘*ೄ˚")
                                  
    if message.content.lower().startswith('good night'):
        await client.send_message(message.channel, "꒰´ ु-௰ू-॰`꒱⋆｡˚✩ɢ∞פ ɴⅈɢhт ༘*ೄ˚")
            
# }rps <rock/paper/scissors>
@client.command(pass_context=True)
async def rps(ctx, args=None):
    choice = random.choice(choices)
    author = ctx.message.author
    msg = discord.Embed(colour=0x871485, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if args == None:
        msg.add_field(name=":warning: ", value="`v!rps <rock/paper/scissors>`")
    elif args == "rock" or args == "paper" or args == "scissors":
        msg.add_field(name=":fist: :raised_hand: :v: ROCK PAPER SCISSORS :v: :raised_hand: :fist: ", value="**~~=================================~~**\n:arrow_forward: `{}`: {}\n:arrow_forward: `BOT`: {}\n**~~=================================~~**".format(author.display_name, args, choice), inline=True)
        if args == "rock" and choice == "scissors":
            msg.add_field(name=":diamonds: W I N N E R :diamonds: ", value="`{}`\n**~~=================================~~**".format(author.display_name), inline=True)
        elif args == "paper" and choice == "rock":
            msg.add_field(name=":diamonds: W I N N E R :diamonds: ", value="`{}`\n**~~=================================~~**".format(author.display_name), inline=True)
        elif args == "scissors" and choice == "paper":
            msg.add_field(name=":diamonds: W I N N E R :diamonds: ", value="`{}`\n**~~=================================~~**".format(author.display_name), inline=True)
        elif args == "rock" and choice == "paper":
            msg.add_field(name=":diamonds: W I N N E R :diamonds: ", value="`BOT`\n**~~=================================~~**", inline=True)
        elif args == "paper" and choice == "scissors":
            msg.add_field(name=":diamonds: W I N N E R :diamonds: ", value="`BOT`\n**~~=================================~~**", inline=True)
        elif args == "scissors" and choice == "rock":
            msg.add_field(name=":diamonds: W I N N E R :diamonds: ", value="`BOT`\n**~~=================================~~**", inline=True)
        elif args == "rock" and choice == "rock":
            msg.add_field(name=":diamonds: W I N N E R :diamonds: ", value="It's a tie!\n**~~=================================~~**", inline=True)
        elif args == "paper" and choice == "paper":
            msg.add_field(name=":diamonds: W I N N E R :diamonds: ", value="It's a tie!\n**~~=================================~~**", inline=True)
        else:
            msg.add_field(name=":diamonds: W I N N E R :diamonds: ", value="It's a tie!\n**~~=================================~~**", inline=True)
    else:
        msg.add_field(name=":warning: ", value="`v!rps <rock/paper/scissors>`")
    await client.say(embed=msg)
    print("============================================================")
    print("}rps <rock/paper/scissors>")
    print("{} ### {}".format(author, author.id))
    print("============================================================")
    
choices = ["rock", "paper", "scissors"]

# <punch <user>
@client.command(pass_context=True)
async def punch(ctx, userName: discord.Member = None):
    author = ctx.message.author
    msg = discord.Embed(colour=0x871485, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if userName == None:
        msg.add_field(name=":warning: ", value="`v!punch (user)`")
    else:
        msg.set_image(url="{}".format(random.choice(punchlinks)))
        msg.add_field(name=":tongue: Emotes :tongue:", value="`{}, you got a punch from by {}! Ouch...`".format(userName.display_name, author.display_name), inline=True)
    await client.say(embed=msg)
    print("============================================================")
    print("}kiss <user>")
    print("{} ### {}".format(author, author.id))
    print("============================================================")
    
punchlinks = ["http://www.reactiongifs.com/wp-content/uploads/2013/11/punch.gif",
              "https://media.giphy.com/media/7Nsu3HCWLRVgQ/giphy.gif",
              "https://media1.tenor.com/images/3aa0da04ef714f758c9ed215e629c161/tenor.gif?itemid=4902916",
              "https://i.pinimg.com/originals/f6/d9/1c/f6d91c1f8a29b0131d448bad244dbeba.gif"]

# }invite
@client.command(pass_context=True)
async def invite(ctx):
    msg = discord.Embed(colour=0x871485, url=default_invite, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    msg.add_field(name=":link: ", value="Here is the default server invite:\n{}".format(default_invite))
    await client.say(embed=msg)
client.run(os.environ['BOT_TOKEN'])
