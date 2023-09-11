#Acesta este puzzle master

import asyncio
from meteo_info.api_meteo import get_weather_temp
from meteo_info.telegram_funcs import telegram_send_message
from datetime import datetime
from meteo_info.configsx import oras, chat_id_constantin, ora_specificata



#Daca este ora X, trimite mesaj pe telegram cu temp de afara din orasul mentionat in configs
#!!!
async def main():
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    raportul = await get_weather_temp(oras)
    await telegram_send_message(chat_id= chat_id_constantin,
                                textx= raportul)
    #print(raportul)
    return raportul

if __name__ == "__main__":
    ora = datetime.now().hour
    # print(int(ora))
    if ora == ora_specificata:
        rap = asyncio.run(main())
        print(f"rap = {rap}")
    else:
        print(f"Programul este rulat in afara orei specificate {ora_specificata}")