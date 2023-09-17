import discord
import logging
from dotenv import dotenv_values

config = dotenv_values(".env")
BOT_TOKEN = config['KEY']
CELUI_A_FAIRE_CHIER = config['CELUI_A_FAIRE_CHIER']
MESSAGE_QUI_FAIT_CHIER = config['MESSAGE_QUI_FAIT_CHIER']
LE_SANG= config['LE_SANG']
MESSAGE_AU_SANG=config['MESSAGE_AU_SANG']


logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

intents = discord.Intents.default()
client = discord.Client(intents=intents)

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    logger.info(f"Received message from {message.author}: {message.content}")

    if message.author.id == CELUI_A_FAIRE_CHIER:
        await message.author.send(f'{MESSAGE_QUI_FAIT_CHIER}')
        logger.info(f"Sending {MESSAGE_QUI_FAIT_CHIER} to {message.author}")
    if message.author.id == LE_SANG:
        await message.author.send(f'{MESSAGE_AU_SANG}')
        logger.info(f"Sending {MESSAGE_AU_SANG} to {message.author}")

client.run(f'{BOT_TOKEN}')
