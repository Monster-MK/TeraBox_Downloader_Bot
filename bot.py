from pyrogram import Client, filters
import os
from terabox import get_direct_link

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")

app = Client("terabox_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@app.on_message(filters.command("start"))
async def start(client, message):
    await message.reply("Hi! Send me a TeraBox link to get the direct download link.")

@app.on_message(filters.text & ~filters.command("start"))
async def terabox_handler(client, message):
    link = message.text.strip()
    try:
        dl_link = get_direct_link(link)
        await message.reply(f"Here is your direct link:\n{dl_link}")
    except Exception as e:
        await message.reply(f"Error: {e}")

app.run()
