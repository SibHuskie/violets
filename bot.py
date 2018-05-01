import discord
from discord.ext import commands
import logging
import asyncio
import random
import time
import os

client = commands.Bot(command_prefix="")
footer_text = "Violets™"

@client.event
async def on_ready():
    print("Logged in as:")
    print(client.user.name)
    print(client.user.id)
    print("---------------")
    await client.change_presence(game=discord.Game(name='wit a God (Huskie)'))

@client.command()
async def testing():
    await client.say("Testing? Testing...")

@client.command(pass_context = True)
async def <kill(ctx, *, member : discord.Member = None):
    if member is None:
        await client.say(ctx.message.author.mention + ", I can't kill someone unless you tell me who you want to kill! :dagger:")
        return

    if member.id == "429932831314280448":
        await client.say(ctx.message.author.mention + ", you can't kill me if I kill you first! :smiling_imp:")
    elif member.id == "299761993382887425":
        await client.say(ctx.message.author.mention + ", why do you want me to kill my master?")
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

#RAPE
@client.command(pass_context = True)
async def <rape(ctx, *, member : discord.Member = None):
    if member is None:
        await client.say(ctx.message.author.mention + ", you need to find someone to rape.")
    else:
        await client.say(member.mention + " has been raped by " + ctx.message.author.mention + "! :fearful: ")

#COOKIE
@client.command(pass_context = True)
async def <cookie(ctx, *, member : discord.Member = None):
    if member is None:
        await client.say(ctx.message.author.mention + ", give cookies to other members! :laughing:")
    else:
        await client.say(member.mention + " was given a cookie by " + ctx.message.author.mention + "! :cookie:")

# }ban <user> [reason]
@client.command(pass_context=True)
async def <ban(ctx, userName: discord.Member = None, *, args = None):
    staff_role = discord.utils.get(ctx.message.server.roles, name='Staff')
    author = ctx.message.author
    msg = discord.Embed(colour=0x871485, description= "")
    msg.title = ""
    if staff_role in author.roles or staff_role in author.roles or staff_role.role in author.roles or staff_role in author.roles or staff_role in author.roles:
        if userName == None:
            msg.add_field(name=":octagonal_sign: ", value="`<ban <user> [reason]`")
        elif staff_role in userName.roles or staff_role in userName.roles or staff_role in userName.roles or staff_role.role in userName.roles or staff_role in userName.roles or staff_role in userName.roles:
            msg.add_field(name=":warning: ", value="`You can't ban other staff!`")
        elif args == None:
            msg.add_field(name=":hammer: Ban Hammer", value="`{} banned {}!`\n`Reason: ?`".format(author.display_name, userName.display_name))
            await client.ban(userName)
        else:
            msg.add_field(name=":hammer: Ban Hammer", value="`{} banned {}!`\n`Reason: {}`".format(author.display_name, userName.display_name, args))
            await client.ban(userName)
    else:
        msg.add_field(name=":octagonal_sign: ", value="`This command can only be used by Staff!`")
    await client.say(embed=msg)
    print("============================================================")
    print("}ban <user> [reason]")
    print("{} ### {}".format(author, author.id))
    print("============================================================")

# }tempban <user> <time> [reason]
@client.command(pass_context=True)
async def <tempban(ctx, userName: discord.Member = None, time: int = None, *, args = None):
    staff_role = discord.utils.get(ctx.message.server.roles, name='Staff')
    author = ctx.message.author
    msg = discord.Embed(colour=0x871485, description= "")
    msg.title = ""
    if staff_role in author.roles or staff_role in author.roles or staff_role in author.roles or staff_role in author.roles:
        if userName == None or time == None:
            msg.add_field(name=":octagonal_sign: ", value="`<tempban <user> <time> [reason]`")
            await client.say(embed=msg)
        else:
            if staff_role in userName.roles or staff_role in userName.roles or staff_role in userName.roles or staff_role in userName.roles or staff_role in userName.roles:
                msg.add_field(name=":octagonal_sign: ", value="`You can't ban other staff!`")
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
        msg.add_field(name=":octagonal_sign: ", value="`This command can only be used by Staff!`")
        await client.say(embed=msg)
    print("============================================================")
    print("}tempban <user> <time> [reason]")
    print("{} ### {}".format(author, author.id))
    print("============================================================")

# }unban <user id>
@client.command(pass_context=True)
async def <unban(ctx, userID = None):
    staff_role = discord.utils.get(ctx.message.server.roles, name='Staff')
    author = ctx.message.author
    msg = discord.Embed(colour=0x871485, description= "")
    msg.title = ""
    if staff_role in author.roles or staff_role in author.roles or staff_role in author.roles or staff_role in author.roles:
        if userID == None:
            msg.add_field(name=":octagonal_sign: ", value="`<unban (user id)`")
        else:
            banned_users = await client.get_bans(ctx.message.server)
            user = discord.utils.get(banned_users,id=userID)
            if user is not None:
                await client.unban(ctx.message.server, user)
                msg.add_field(name=":tools: ", value="`{} unbanned the user with the following ID: {}!`".format(author.display_name, userID))
            else:
                msg.add_field(name=":smiley: ", value="`The ID you specified is not banned! ID: {}`".format(userID))
    else:
        msg.add_field(name=":warning: ", value="`This command can only be used by Staff!`")
    await client.say(embed=msg)
    print("============================================================")
    print("}unban <user>")
    print("{} ### {}".format(author, author.id))
    print("============================================================")

# serverinfo
@client.command(pass_context=True)
async def <serverinfo(ctx):
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
    msg.add_field(name="RELEASE DATE:", value="23th of March 2018", inline=True)
    await client.say(embed=msg)
    print("============================================================")
    print("<serverinfo")
    print("{} ### {}".format(author, author.id))
    print("============================================================")

# serverinfo
@client.command(pass_context=True)
async def <mc(ctx):
    author = ctx.message.author
    msg = discord.Embed(colour=0x871485, description= "")
    msg.title = ":closed_book: Member Count :closed_book:"
    msg.add_field(name="MEMBERS", value=(len(ctx.message.server.members)), inline=True)
    await client.say(embed=msg)

# }userinfo <user>
@client.command(pass_context=True)
async def <userinfo(ctx, userName: discord.Member = None):
    member_role = discord.utils.get(ctx.message.server.roles, name='Member')
    staff_role = discord.utils.get(ctx.message.server.roles, name='Staff')
    author = ctx.message.author
    msg = discord.Embed(colour=0x871485, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if member_role in author.roles or staff_role in author.roles:
        if userName == None:
            msg.title = ""
            msg.add_field(name="       :warning: ", value="`<userinfo <user>`")
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
async def <lick(ctx, userName: discord.Member = None):
    author = ctx.message.author
    msg = discord.Embed(colour=0x871485, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if userName == None:
        msg.add_field(name=":warning: ", value="`<lick <user>`")
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
async def <takerole(ctx, userName: discord.Member = None, *, args = None):
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
            msg.add_field(name=":warning: ", value="`<takerole <user> <role name>`")
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
async def <giverole(ctx, userName: discord.Member = None, *, args = None):
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
            msg.add_field(name=":warning: ", value="`<giverole <user> <role name>`")
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
async def <echo(ctx, *, args=None): 
    staff_role = discord.utils.get(ctx.message.server.roles, name='Staff')
    author = ctx.message.author
    msg = discord.Embed(colour=0x871485, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if staff_role in author.roles or staff_role in author.roles:
        if args == None:
            msg.add_field(name=":warning: ", value="<say <text>")
            await client.say(embed=msg)
        else:
            await client.say("{}".format(args))
            await client.delete_message(ctx.message)
    else:
        msg.add_field(name=":warning: ", value="`This command can only be used by Staff!`")
        await client.say(embed=msg)

# <hug <user>
@client.command(pass_context=True)
async def <hug(ctx, userName: discord.Member = None):
    author = ctx.message.author
    msg = discord.Embed(colour=0x871485, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if userName == None:
        msg.add_field(name=":warning: ", value="`<hug (user)`")
    else:
        msg.set_image(url="{}".format(random.choice(huglinks)))
        msg.add_field(name=":tongue: Emotes:tongue:", value="`{}, you got a hug from {}!`".format(userName.display_name, author.display_name), inline=True)
    await client.say(embed=msg)
    print("============================================================")
    print("}hug <user>")
    print("{} ### {}".format(author, author.id))
    print("============================================================")

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

# <cuddle <user>
@client.command(pass_context=True)
async def <cuddle(ctx, userName: discord.Member = None):
    author = ctx.message.author
    msg = discord.Embed(colour=0x871485, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if userName == None:
        msg.add_field(name=":warning: ", value="`<cuddle (user)`")
    else:
        msg.set_image(url="{}".format(random.choice(cuddlelinks)))
        msg.add_field(name=":tongue: Emotes :tongue:", value="`{}, you got a cuddle from {}!`".format(userName.display_name, author.display_name), inline=True)
    await client.say(embed=msg)
    print("============================================================")
    print("}cuddle <user>")
    print("{} ### {}".format(author, author.id))
    print("============================================================")

cuddlelinks = ["https://i.imgur.com/GWNWcLH.gif",
               "https://i.imgur.com/i3Eqqgz.gif",
               "https://i.imgur.com/GpFk6fE.gif",
               "https://i.imgur.com/mc3Z7wf.gif",
               "https://i.imgur.com/N5JYB5r.gif",
               "https://i.imgur.com/PGp8JYq.gif"]

# <pat <user>
@client.command(pass_context=True)
async def <pat(ctx, userName: discord.Member = None):
    author = ctx.message.author
    msg = discord.Embed(colour=0x871485, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if userName == None:
        msg.add_field(name=":warning: ", value="`<pat (user)`")
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
            "https://i.imgur.com/y3La9yP.gif"]

# <kiss <user>
@client.command(pass_context=True)
async def <kiss(ctx, userName: discord.Member = None):
    author = ctx.message.author
    msg = discord.Embed(colour=0x871485, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if userName == None:
        msg.add_field(name=":warning: ", value="`<kiss (user)`")
    else:
        msg.set_image(url="{}".format(random.choice(kisslinks)))
        msg.add_field(name=":tongue: Emotes :tongue:", value="`{}, you got kissed by {}!`".format(userName.display_name, author.display_name), inline=True)
    await client.say(embed=msg)
    print("============================================================")
    print("}kiss <user>")
    print("{} ### {}".format(author, author.id))
    print("============================================================")

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

# EVENT - JOIN / LEAVE
@client.async_event
async def on_member_join(userName: discord.User):
    joins = ["**Welcome to Violets™ @{}! :sparkles: Please make sure to read the rules and if you want to partner, contact any of the staff with the role Partnership Manager :smiley: Also don't forget to get roles and colors in the self role channel :wink: Enjoy your stay :sparkling_heart:**".format(userName)]
    await client.send_message(client.get_channel("426680388585521163"), "{}".format(random.choice(joins)))
    print("============================================================")
    print("JOIN EVENT")
    print("{} ### {}".format(userName, userName.id))
    print("============================================================")

@client.async_event
async def on_member_remove(userName: discord.User):
    leaves = ["Looks like `{}` wasn't good enough for Violets™! :wave:".format(userName)]
    await client.send_message(client.get_channel("426680388585521163"), "{}".format(random.choice(leaves)))
    print("============================================================")
    print("LEAVE EVENT")
    print("{} ### {}".format(userName, userName.id))
    print("============================================================")

# <eightball <yes or no question>
@client.command(pass_context=True)
async def <eightball(ctx, *, args=None):
    author = ctx.message.author
    msg = discord.Embed(colour=0x871485, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if args == None:
        msg.add_field(name="warning: ", value="`<eightball (yes or no question)`")
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
async def <poke(ctx, userName: discord.Member = None):
    author = ctx.message.author
    msg = discord.Embed(colour=0x871485, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if userName == None:
        msg.add_field(name=":warning: ", value="`<poke (user)`")
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
async def <spank(ctx, userName: discord.Member = None):
    author = ctx.message.author
    msg = discord.Embed(colour=0x871485, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if userName == None:
        msg.add_field(name=":warning: ", value="`<spank (user)`")
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
async def <calculator(ctx, *, args=None):
    author = ctx.message.author
    msg = discord.Embed(colour=0x871485, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if args == None:
        msg.add_field(name=":warning: ", value="`<calculator (math problem)`")
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
async def <battle(ctx, userName: discord.Member = None):
    attacker = random.randint(0, 301)
    attacked = random.randint(0, 301)
    attackerhealth = 300 - attacked
    attackedhealth = 300 - attacker
    author = ctx.message.author
    msg = discord.Embed(colour=0x871485, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if userName == None:
        msg.add_field(name=":warning: ", value="`<battle (user)`")
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
async def <dice(ctx):
    r=random.randint(1,6)
    await client.send_message(ctx.message.channel, "You rolled a " + str(r) + "!")
    
# <matchmake <user1> <user2>
@client.command(pass_context=True)
async def <ship(ctx, userName1: discord.Member = None, userName2: discord.Member = None):
    percent = random.randint(0, 101)
    author = ctx.message.author
    msg = discord.Embed(colour=0x871485, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if userName1 == None or userName2 == None:
        msg.add_field(name=":warning: ",value="`<ship (user1) (user2)`")
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
async def <warn(ctx, userName: discord.Member = None, *, args = None):
    helper_role = discord.utils.get(ctx.message.server.roles, name='Helper')
    mod_role = discord.utils.get(ctx.message.server.roles, name='Moderators')
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
            msg.add_field(name=":warning: ", value="`<warn (user) (reason)`")
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
async def <kick(ctx, userName: discord.Member = None, *, args = None):
    helper_role = discord.utils.get(ctx.message.server.roles, name='Helpers')
    mod_role = discord.utils.get(ctx.message.server.roles, name='Moderators')
    admin_role = discord.utils.get(ctx.message.server.roles, name='Administrator')
    manager_role = discord.utils.get(ctx.message.server.roles, name='Co Owner')
    owner_role = discord.utils.get(ctx.message.server.roles, name='Dark Lords (Owners)')
    author = ctx.message.author
    msg = discord.Embed(colour=0x871485, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if mod_role in author.roles or admin_role in author.roles or manager_role in author.roles or owner_role in author.roles:
        if userName == None:
            msg.add_field(name=":warning: ", value="`<kick (user) (reason)`")
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
async def <punish(ctx, userName: discord.Member = None, time: int = None, *, args = None):
    member_role = discord.utils.get(ctx.message.server.roles, name ='Members')
    punished_role = discord.utils.get(ctx.message.server.roles, name='Punished')
    helper_role = discord.utils.get(ctx.message.server.roles, name='Helpers')
    mod_role = discord.utils.get(ctx.message.server.roles, name='Moderators')
    admin_role = discord.utils.get(ctx.message.server.roles, name='Administrator')
    manager_role = discord.utils.get(ctx.message.server.roles, name='Co Owner')
    owner_role = discord.utils.get(ctx.message.server.roles, name='Owners')
    author = ctx.message.author
    msg = discord.Embed(colour=0x871485, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if helper_role in author.roles or mod_role in author.roles or admin_role in author.roles or manager_role in author.roles or owner_role in author.roles:
        if userName == None or time == None:
            msg.add_field(name=":warning: ", value="`<punish (user) (time) (reason)`")
            await client.say(embed=msg)
        elif helper_role in userName.roles or mod_role in userName.roles or admin_role in userName.roles or manager_role in userName.roles or owner_role in userName.roles:
            msg.add_field(name=":warning: ", value="`You can't punish other staff!`")
            await client.say(embed=msg)
        elif punished_role in userName.roles:
            msg.add_field(name=":warning: ", value="`That user is already punished!`")
            await client.say(embed=msg)
        else:
            time2 = time * 60
            if args == None:
                await client.add_roles(userName, punished_role)
                await client.remove_roles(userName, member_role)
                msg.add_field(name=":speak_no_evil: ", value="`{} has been punished by {}! for {} minute(s)!`\n`Reason: ?`".format(userName.display_name, author.display_name, time))
                await client.say(embed=msg)
                await asyncio.sleep(float(time2))
                await client.remove_roles(userName, punished_role)
                await client.say("```diff\n- Removed {}'s punishment! ({} minute(s) are up.)\n```".format(userName.display_name, time))
            else:
                await client.add_roles(userName, punished_role)
                msg.add_field(name=":speak_no_evil: ", value="`{} has been punished by {} for {} minute(s)!`\n`Reason: {}`".format(userName.display_name, author.display_name, time, args))
                await client.say(embed=msg)
                await asyncio.sleep(float(time2))
                await client.remove_roles(userName, punished_role)
                await client.say("```diff\n- Removed {}'s punishment! ({} minute(s) are up.)\n```".format(userName.display_name, time))
    else:
        msg.add_field(name=":warning: ", value="`This command can only be used by staff!`")
        await client.say(embed=msg)
client.run(os.environ['BOT_TOKEN'])
