from pyrogram import Client, filters
from pymongo import MongoClient
import os
from terabox import get_direct_link
from buttons import download_button

# Bot credentials (Fixed values)
API_ID = 20517170
API_HASH = "f09e5c91dd864f01063ff63827832137"
BOT_TOKEN = "8348010277:AAGOQ7Z5HtO7JiyoCz0HZmm0vD9uyALWNr4"
DATABASE_URL = "mongodb+srv://mkxcloud123:jc6PH2BdnK6orvoj@cluster0.mnwmku3.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Connect to MongoDB
mongo_client = MongoClient(DATABASE_URL)
db = mongo_client["terabox_bot"]
users_col = db["users"]

# Initialize bot
app = Client(
    "terabox_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

@app.on_message(filters.command("start"))
async def start(client, message):
    user_id = message.from_user.id
    if not users_col.find_one({"_id": user_id}):
        users_col.insert_one({"_id": user_id, "username": message.from_user.username})
    await message.reply("👋 Hi! Send me a TeraBox link, I'll give you the direct download button.")

@app.on_message(filters.text & ~filters.command("start"))
async def terabox_handler(client, message):
    link = message.text.strip()
    try:
        dl_link = get_direct_link(link)
        await message.reply(
            "✅ **Direct Download Link Generated!**",
            reply_markup=download_button(dl_link)
        )
    except Exception as e:
        await message.reply(f"❌ Error: {e}")

app.run()
