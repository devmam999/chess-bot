from chessdotcom import get_player_stats
import discord
from discord.ext import commands

chessBot = commands.Bot(command_prefix="/", intents=discord.Intents.all())

@chessBot.event
async def on_ready():
  print("Chess Bot has connected to Discord")
@chessBot.command()
async def profile(ctx, arg):
  data = get_player_stats(arg).json
  await ctx.send("Blitz:")
  await ctx.send(f'{data["stats"]["chess_blitz"]["last"]["rating"]}')
  await ctx.send("Rapid:")
  await ctx.send(f'{data["stats"]["chess_rapid"]["last"]["rating"]}')
  await ctx.send("Bullet:")
  await ctx.send(f'{data["stats"]["chess_bullet"]["last"]["rating"]}')
  await ctx.send("Daily:")
  await ctx.send(f'{data["stats"]["chess_daily"]["last"]["rating"]}')
chessBot.run("MTA4OTcxMzQ5OTEzMjkyODAyMA.Ge2vaC.ceC9QbkBt8YmN6BaHjCZ3lZD1mHS1U6bqRLqNU")
