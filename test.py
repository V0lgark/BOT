from discord.ext import commands

bot = commands.Bot(command_prefix="!")


@bot.event
async def on_ready():
    print("MY BODY IS READY")

@bot.command(name='del')
async def delete(ctx, number_of_messages: int):
    messages = await ctx.channel.history(limit=number_of_messages + 1).flatten()
    for each_message in messages:
            await each_message.delete()

bot.run('ODAxMjU5NDQ2NDgzNDE5MTc4.YAeFAg.1A5-0URDYfoAe1z5ctGZL5Xqua8')