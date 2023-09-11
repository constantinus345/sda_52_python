import asyncio
import telegram
from meteo_info.configsx import bot_key , chat_id_constantin
# print(chat_id_constantin)

#docs telegram https://core.telegram.org/

#send message
async def telegram_send_message(chat_id, textx):
    bot = telegram.Bot(token=bot_key)
    async with bot:
        await bot.send_message(chat_id = chat_id, text= textx)

async def main():
    #pentru a gasi id-ul vostru de telegram, accesati https://t.me/raw_info_bot
    await telegram_send_message(chat_id= chat_id_constantin, textx="Salut test")

if __name__ == "__main__":
    asyncio.run(main())