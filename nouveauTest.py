import os
import discord
from dotenv import load_dotenv
load_dotenv(dotenv_path="../config")


default_intents = discord.Intents.default()
default_intents.members = True
client = discord.Client(intents=default_intents)
id_bot = client.user
@client.event
async def on_ready():
    print('Le bot est prêt, sous le nom {} !'.format(client.user))

@client.event
async def on_message(message):
    if message.content.startswith("!del"):
        number = int(message.content.split()[1])
        messages = await message.channel.history(limit=number + 1).flatten()
        for each_message in messages:
            await each_message.delete()

    if message.content.startswith("!re"):
        emojis = ['❤','❌']
        await message.channel.send("Ton message va être soumis au sondage du public ! :eyes:")
        for emoji in emojis:
            await message.add_reaction(emoji)

    if message.content.lower()== "ping":
        await message.channel.send("Pong")
        print("pong")

@client.event
async def on_reaction_add(reaction, user):
    channel = reaction.message.channel
    if (reaction.me != id_bot):
        await channel.send('{} a ajouté la réaction :  {} au message : "{}" écrit par {}'.format(user.name, reaction.emoji, reaction.message.content, reaction.message.author))

@client.event
async def on_raw_reaction_remove(payload):
    print("Je l'ai vu gros nullos")
    salon = payload.channel_id
    channel = client.get_channel(salon)
    await channel.send('{} a retiré la réaction : {} au message'.format(payload.message_id,payload.emoji))


@client.event
async def on_member_join(member):
    general_channel: discord.TextChannel = client.get_channel(801259914969874465)
    await general_channel.send(content="Bienvenue sur le serveur {member.display_name} !")
    


client.run(os.getenv("TOKEN"))