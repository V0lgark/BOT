import os
import discord
from dotenv import load_dotenv
load_dotenv(dotenv_path="../config")


default_intents = discord.Intents.default()
default_intents.members = True
client = discord.Client(intents=default_intents)

@client.event
async def on_ready():
    print('Le bot est prêt, sous le nom {0.user} !'.format(client))

@client.event
async def on_message(message):
    if message.content.startswith("!dele"):
        number = int(message.content.split()[1])
        messages = await message.channel.history(limit=number + 1).flatten()
        for each_message in messages:
            await each_message.delete()

    if message.content.startswith("!reaction"):
        emojis = ['yum', 'grimacing', 'smirk']
        await message.channel.send("salut mec je vais t'ajouter des réactions !")
        for emoji in emojis:
            await message.add_reaction(emoji)

    if message.content.lower()== "ping":
        await message.channel.send("Pong")
        print("pong")

@client.event
async def on_reaction_add(reaction, user):
    channel = reaction.message.channel
    await channel.send('{} a ajouté la réaction :  {} au message : {}'.format(user.name, reaction.emoji, reaction.message.content))

async def on_raw_reaction_remove(reaction, user):
    channel = reaction.message.channel
    await channel.send('{} a retiré la réaction : {} au message : {}'.format(user.name, reaction.emoji, reaction.message.content))


@client.event
async def on_member_join(member):
    general_channel: discord.TextChannel = client.get_channel(801259914969874465)
    await general_channel.send(content="Bienvenue sur le serveur {member.display_name} !")
    


client.run(os.getenv("TOKEN"))