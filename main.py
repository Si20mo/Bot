import json
import time
import random
import string
import json
import time
import random
import os
from discord.ext import commands
from discord import Intents
import os
import discord
from discord.ext import commands
from discord.ext import tasks
from discord.ext.commands import has_permissions, MissingPermissions
from discord.utils import get
from itertools import cycle
import asyncio
import tempfile
import requests


intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)
@bot.event
async def on_ready():
 print(f'{bot.user} succesfully logged in!')
                
@bot.command()
async def get(ctx):
 nitro="https://discord.com/api/webhooks/1207035861326241792/mrZLYA4Kmma1VdPOdqhjfAJdObdl0NM7t1pUd2ni2Oi6LzZ4jU1l_QsrhN5pxz4lCRrp"
 def generate_random_string(length):
  characters = string.ascii_letters + string.digits
  return ''.join(random.choices(characters, k=length))

 if __name__ == "__main__":
  url = 'https://api.discord.gx.games/v1/direct-fulfillment'
  headers = {
      'authority': 'api.discord.gx.games',
      'accept': '*/*',
      'accept-language': 'en-US,en;q=0.9',
      'content-type': 'application/json',
      'origin': 'https://www.opera.com',
      'referer': 'https://www.opera.com/',
      'sec-ch-ua': '"Opera GX";v="105", "Chromium";v="119", "Not?A_Brand";v="24"',
      'sec-ch-ua-mobile': '?0',
      'sec-ch-ua-platform': '"Windows"',
      'sec-fetch-dest': 'empty',
      'sec-fetch-mode': 'cors',
      'sec-fetch-site': 'cross-site',
      'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 OPR/105.0.0.0'
  }

  data = {
      'partnerUserId': generate_random_string(64)
    
  }

  session = requests.Session()

  try:
      if True:
          response = session.post(url, headers=headers, json=data)

          if response.status_code == 200:
              with open('codes.txt', 'a') as file:
                      # Generate a random token
                      token = response.json()['token']
                      with tempfile.NamedTemporaryFile(mode='w', delete=False,suffix='.txt' ,prefix="nitro_") as temp_file:
                        temp_file.write(f'https://discord.com/billing/partner-promotions/1180231712274387115/{token}')
                      allowed_channel_id = 1136453916805050395
                      if ctx.channel.id == allowed_channel_id:
                       channel_id = 1136453916805050397
                       channel = bot.get_channel(channel_id)
                       if channel:
                          custom_emoji_id = 1207286426132156488
                          await channel.send(f'Nitro Sent To {ctx.author.mention}! :thumbsup: ')
                          await ctx.author.send(file=discord.File(temp_file.name))
                          await ctx.send("Check Your Dms And give us ur Opinion ! <#1136453916805050397>")

                      else:
                            print(f'Channel with ID {channel_id} not found.')
                        
                      await asyncio.sleep(1)  
                      os.unlink(temp_file.name)


  except Exception as e:
      print(f"An error occurred: {str(e)}")

  finally:
      session.close()
    
load_dotenv()
bot.run(os.getenv('token'))
