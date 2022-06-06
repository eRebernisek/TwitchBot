import os
from pynput.keyboard import Key, Controller
import socket
import os
from os.path import join, dirname
from twitchio.ext import commands
import time
from ahk import AHK

#Download Autohotkey at https://www.autohotkey.com/ and provide the address to
#AutoHotkey.exe below!
ahk = AHK(executable_path='C:\\Program Files\\AutoHotkey\\AutoHotkey.exe')

keyboard = Controller()

# credentials
TMI_TOKEN=""
CLIENT_ID=""
BOT_NICK="MyOwnBot"
BOT_PREFIX="!"
CHANNEL=""

bot = commands.Bot(
    token=TMI_TOKEN,
    client_id=CLIENT_ID,
    nick=BOT_NICK,
    prefix=BOT_PREFIX,
    initial_channels=[CHANNEL]
)

@bot.event()
async def event_message(message):
    # the bot should not react to itself
    if message.author.name.lower() == BOT_NICK.lower():
        return
    # relay message to command callbacks
    await bot.handle_commands(message)

    comando = message.content.lower()
    
    # time.sleep(1)
    
    if len(comando)==1:
        ahk.key_press(comando)
        # keyboard.press(comando)

if __name__ == "__main__":
    # launch bot
    os.system('cls')
    bot.run()