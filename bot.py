import discord
import datetime
import json
from discord import option
from datetime import timedelta
bot = discord.Bot(intents=discord.Intents.all())

#傳參數用等於

@bot.event
async def on_ready():
#定義一個function for bot變數
    print(bot.user)

@bot.event
async def on_message(msg):
    pass #函數不能為空

@bot.slash_command(name="timeout", description="禁言機器寶寶") #slash指令
@option(
    "member", #the name of the option
    discord.Member, #the type to traget
    description= "the member to timeout", 
    required= False #必要選項 or not
)

@option(
    "minutes",
    int,
    description= "the time for timeout",
    required= False
)
@option(
    "hours",
    int,
    required= False
)
async def timeout_members(
    ctx: discord.ApplicationContext, member: discord.Member, hours: int, minutes: int
):
    duration = datetime.timedelta(minutes=minutes, hours=hours)
    await member.timeout_for(duration)
    await ctx.respond("Successfully timed out.")

@bot.slash_command(name="kick", description="把陳宥輔踢掉")
@option(
    "陳宥輔",
    discord.Member,
    description = "仇恨陳宥輔",
    required = True
)

@option(
    "沒有原因",
    str,
    required= False
)
async def kick_members(
    ctx: discord.ApplicationContext, member: discord.Member, reason: str
):
    await member.kick(reason=reason)
    await ctx.respond("Successfully kicked ou/t.")

@bot.slash_command(name="role", description = "鷄鷄")
@option(
    "name",
    str,
    required = True
)
async def role(ctx,name,):
    await ctx.guild.create_role(name=name)
    await ctx.respond("Successfully created")

@bot.slash_command(name="purge", description= "delete some messages")
async def purge(ctx,amount:int):
    await ctx.channel.purge(limit=amount)
    await ctx.respond("Successfully deleted")

@bot.slash_command(name="bots")
async def bots(ctx):
    for member in ctx.guild.members:
        if member.bot == True:
            await ctx.respond(f'{member.name} is a bot')

@bot.slash_command(name="feedback_setup")
async def feedback_setup(ctx, channel: discord.TextChannel):
    with open("sus.json", "r") as f:
        data = json.load(f)
        data['feedback'] = channel.id
    with open("sus.json", "w") as f: #用read開啓
        json.dump(data, f) #把新的資料填上去
    await ctx.respond("feedback setup complete")

@bot.slash_command(name="feedback")
async def feedback(ctx, feedback):
    with open("sus.json", "r") as f: #用read開啓
        data = json.load(f) #獲取json内容
    channel = bot.get_channel(data["feedback"])
    await channel.send(feedback)
    await ctx.respond("Successfully sent.")

@bot.slash_command(name="say", description="Echoes back your message.")
@option(
    "message",
    str,  
    description="The message to echo back",
    required=True
)
async def say(ctx, message: str):
    await ctx.send(message)


