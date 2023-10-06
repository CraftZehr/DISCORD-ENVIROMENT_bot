import discord, random, os
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def maccasstuff(ctx):
    await ctx.send(f'x')

@bot.command()
async def mcdjp(ctx):
    await ctx.send(f'c')

@bot.command()
async def ok(ctx):
    await ctx.send(f'n b')

@bot.command()
async def mcd(ctx):
    await ctx.send(f'c')

@bot.command()
async def wat(ctx):
    await ctx.send(f'This bot is created by CraftZehr')

@bot.command()
async def credits(ctx):
    await ctx.send(f'me')


@bot.command()
async def qdo(ctx):
    await ctx.send(f'c')

@bot.command()
async def qproblem(ctx):
    await ctx.send(f'c')


@bot.command()
async def qemit(ctx):
    await ctx.send(f'c')

@bot.command()
async def qpollution(ctx):
    await ctx.send(f'c')



@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def spam(ctx, count_4h = 100):
    await ctx.send("wow " * count_4h)

@bot.command()
async def kicr(ctx):
    await ctx.send("rickroll")




@bot.command()
async def ide_sampah(ctx):
    img_name = random.choice(os.listdir('kerajinan'))
    with open(f'kerajinan/{img_name}', 'rb') as f:
        picture = discord.File(f)
        f.close()
    await ctx.send(file=picture)


@bot.command()
async def lol(ctx):
    img_name = random.choice(os.listdir('rdm'))
    with open(f'rdm/{img_name}', 'rb') as f:
        picture = discord.File(f)
        f.close()
    await ctx.send(file=picture)




bot.run("tokehere")

