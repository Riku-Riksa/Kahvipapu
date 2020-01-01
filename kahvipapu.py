#Discord.py requirements and essentials.
from discord.ext import commands 

from discord.utils import get

import discord

import asyncio

import random

import praw

import youtube_dl (Not really necessary yet!)


#Set bot as active.
bot = commands.Bot(command_prefix="!", status=discord.Status.idle, actvity=discord.Game(name="Booting.."))

#Define reddit praw requirements
reddit = praw.Reddit(client_id='reddit app id here',client_secret = 'reddit app id secret here', user_agent ='How reddit sees activity')

#Bot essentials (game and status.)

@bot.event

async def on_ready():

    print("Ready to go!")

    print(f"Serving: {len(bot.guilds)} guilds.")

    await bot.change_presence(status=discord.Status.online, activity=discord.Game(name="!commands"))

  


#Command 1: Bot ping command.
@bot.command()

async def ping(ctx):

    ping_ = bot.latency

    ping = round(ping_ * 1000)

    await ctx.channel.send(f"My ping is {ping}ms")

#Command 2: Get basic user info (Name, join date and role.)

@bot.command()

async def user(ctx, member:discord.Member = None):

    if member == None:

        member = ctx.message.author

        pronoun = "Your"

        prono = "You"

    else:

        pronoun = "Their"

        prono = "They"

    name = f"{member.name}#{member.discriminator}"

    status = member.status

    joined = member.joined_at

    role = member.top_role

    await ctx.channel.send(f"{pronoun} name is {name}. {pronoun} status is {status}. {prono} joined at {joined}. {pronoun} highest rank is {role}.")

#Command 3: Ban user from server. Only admins can do this.
@bot.command()
@commands.has_role("")
#checks role.


async def kick(ctx, member:discord.Member = None, reason = None):

    if member == None or member == ctx.message.author:

        await ctx.channel.send ("You cannot kick yourself!")

        return

    if reason == None:

        reason = "you did fuckery."


    message = f"You have been kicked from {ctx.guild.name} for {reason}!"

    await member.send(message)

    await member.kick(reason=reason)

    await ctx.channel.send(f"{member} has been kicked!")


#Command 4: Unban user from server. Only admins can do this.
@bot.command()

@commands.has_role("")

async def unban(ctx, member:discord.Member = None, reason = None):

    if member == None or member == ctx.message.author:

        await ctx.channel.send ("You cannot unban yourself!")

        return

    if reason == None:

        reason = "Ylivaltias myönsi sinulle uuden mahdollisuuden"

    message = f"You have been unbanned from {ctx.guild.name} for {reason}"

    await member.send(message)

    await ctx.channel.send(f"{member} has been unbanned")

#Command 5: When a member joins, auto-assign a role and send them a message
@bot.event

async def on_member_join(member):
    role = get(member.guild.roles, name="Your default role")
    await member.add_roles(role)
    await member.send("Hi! Welcome to the server!")
    print (f"{member} was given a role: {role} ")
    
    
#Command 6: Just a greeting.
@bot.command()
async def greet(ctx):
    await ctx.send("Hello?")

#Command 7: Shrugs.

@bot.command()
async def shrug(ctx):
    await ctx.send(" ¯\_(ツ)_/¯")

#Command 8: Clear latest 100 messages from the text channel where the command was initiated

@bot.command()
@commands.has_role("")
async def clear(ctx, amount = 99):
    await ctx.message.channel.purge(limit=amount+1)
    await ctx.message.channel.send(f"Messages deleted")

#Command 9: Post IT-Ankka comics using imgur urls

@bot.command()
async def ankka(ctx):
    kuvat = ["https://i.redd.it/hmwo7swmdiu11.jpg","https://i.imgur.com/AFYWLOt.jpg","https://i.imgur.com/BWcr1sJ.jpg","https://i.redd.it/141l5ify2b511.jpg","https://i.redd.it/2qlfo4zvei511.jpg","https://i.redd.it/vhujpcqngmm31.jpg","https://i.redd.it/razkd181dw221.png","https://i.redd.it/bxb1jq9q1lu11.png","https://i.redd.it/meyilf5otdu31.png"]
    valittu = random.choice(kuvat)
    await ctx.send(valittu)

#Command 10: Post top 10 memes at random from r/memes

@bot.command()
async def meme(ctx):
    memes_submissions = reddit.subreddit('memes').hot()
    post_to_pick = random.randint(1, 10)
    for i in range(0, post_to_pick):
        submission = next(x for x in memes_submissions if not x.stickied)


    await ctx.channel.send(submission.url)

#Command 11: Show all available commands

@bot.command()
async def commands(ctx):
    embed=discord.Embed(title="Commands", url="https://i.ylilauta.org/f4/897e34b8.jpg", description="All available commands!", color=0x00ff00)
    embed.set_thumbnail(url="https://i.ylilauta.org/f4/897e34b8.jpg")
    embed.add_field(name="!commands", value="Displays commands... duh.    ", inline=False)
    embed.add_field(name="!user @example#0000", value="Information about the requested user.", inline=False)
    embed.add_field(name="!ping", value="Bots ping.", inline=False)
    embed.add_field(name="!kick @example#0000", value="Kicks the user.", inline=False)
    embed.add_field(name="!ankka", value="IT-Ankka comics.", inline=False)
    embed.add_field(name="!meme", value="Top 10 memes from trending in reddit.", inline=False)
    embed.add_field(name="!clear", value="Purge 100 messages from the channel.", inline=False)
    embed.add_field(name="!bitethedust", value ="BITO ZA DUSTO aka fancy clear", inline=False)
    embed.add_field(name="!juice", value = "Shows a dead rapper", inline=False)
    embed.set_footer(text="What can I say except your welcome!")
    await ctx.send(embed=embed)

#Command 12: Shows Juice world. RIP

@bot.command()
async def juice(ctx):
    imageURL = "https://scontent-bru2-1.cdninstagram.com/v/t51.2885-15/sh0.08/e35/s750x750/71178603_163311328099885_5945200428367304836_n.jpg?_nc_ht=scontent-bru2-1.cdninstagram.com&_nc_cat=101&oh=30e11cd18fe6d0c49c6f47614b86d994&oe=5E89411C&ig_cache_key=MjE4NDA5MDQ1Nzc3NTM1ODYyNw%3D%3D.2"
    embed = discord.Embed()
    embed.set_image(url=imageURL)
    await ctx.send(embed = embed)

#Command 13: Clears the latest message in style!

@bot.command()
async def bitethedust(ctx, amount = 2):
    await ctx.send("https://tenor.com/view/killer-queen-go-back-fuck-go-back-bite-the-dust-bite-za-dusto-gif-13939608")
    await asyncio.sleep(1)
    await ctx.message.channel.purge(limit=amount+1)
    await ctx.send(f"https://tenor.com/view/jojo-idid-it-gif-15129632")
    await asyncio.sleep(4)
    await ctx.message.channel.purge(limit=1)



bot.run("TOKEN HERE")
