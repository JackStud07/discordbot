# use: python3 desktop\bot.py in terminal before
import discord
import requests
import json

def get_meme():
  response = requests.get('https://meme-api.com/gimme')
  json_data = json.loads(response.text)
  return json_data['url']

class MyClient(discord.Client):
  async def on_ready(self):
    print('Logged on as {0}!'.format(self.user))
  
  async def on_message(self, message):
    if message.author == self.user:
      return

    if message.content.startswith('$meme'):
      await message.channel.send(get_meme())

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run('MTQ2NjUyODk3MTcxMjYzMTA2NQ.G-EdYZ.ReSHWFK2A02cas6mAXUhIBRZlo18CL8djTSnCw') # My token
