from pyrogram import Client, filters
import os
from terabox import get_direct_link

API_ID = int(os.getenv("20517170"))
API_HASH = os.getenv("f09e5c91dd864f01063ff63827832137")
BOT_TOKEN = os.getenv("8348010277:AAGOQ7Z5HtO7JiyoCz0HZmm0vD9uyALWNr4")

app = Client("terabox_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@app.on_message(filters.command("start"))
async def start(client, message):
    await message.reply("Hᴇʟʟᴏ Sᴇɴᴅ Mᴇ A TᴇʀᴀBᴏx Lɪɴᴋ Tᴏ Gᴇᴛ Tʜᴇ Dɪʀᴇᴄᴛ Dᴏᴡɴʟᴏᴀᴅ Lɪɴᴋ !!! 😍")

@app.on_message(filters.text & ~filters.command("start"))
async def terabox_handler(client, message):
    link = message.text.strip()
    try:
        dl_link = get_direct_link(link)
        await message.reply(f"Hᴇʀᴇ Iꜱ Yᴏᴜʀ Dɪʀᴇᴄᴛ Lɪɴᴋ :\n{dl_link}")
    except Exception as e:
        await message.reply(f"Error: {e}")

app.run()
