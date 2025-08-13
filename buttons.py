from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

def download_button(url):
    buttons = [
        [InlineKeyboardButton("⬇ Download Now", url=url)]
    ]
    return InlineKeyboardMarkup(buttons)
