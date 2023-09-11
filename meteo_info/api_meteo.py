# import the module
import python_weather
import asyncio
import os


async def get_weather_temp(city):
    # declare the client. the measuring unit used defaults to the metric system (celcius, km/h, etc.)
    async with python_weather.Client(unit=python_weather.METRIC) as client:
        # fetch a weather forecast from a city
        weather = await client.get(city)

        # returns the current day's forecast temperature (int)
        temp = weather.current.temperature
        raport = f"In {city} temperatura acum este {temp} grade Celsius"

        return raport

if __name__ == '__main__':
    # see https://stackoverflow.com/questions/45600579/asyncio-event-loop-is-closed-when-getting-loop
    # for more details

    #pt Windows
    oras = "Cairo"
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    raportul = asyncio.run(get_weather_temp(oras))
    print(raportul)