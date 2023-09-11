from time import sleep, perf_counter
from random import randint
import asyncio
from bs4 import BeautifulSoup as bs #parsing/citeste paginile web intr-un mod usor de procesat
import requests #accesez pagini web, fac rqusturi catre server

website_urls = ["https://ro.wikipedia.org/wiki/Rom%C3%A2nia",
               "https://ro.wikipedia.org/wiki/Dun%C4%83rea",
               "https://ro.wikipedia.org/wiki/P%C4%83durea_Neagr%C4%83",
               "https://ro.wikipedia.org/wiki/Baden-Baden",
               "https://ro.wikipedia.org/wiki/Imperiul_Roman"]


async def get_wiki_titlu(url):
    #trimit un request la server

    raspuns = requests.get(url)
    text_html = raspuns.text
    #soup transforma din text intr-un obiect usor de manipulat in python
    #exemplu: ca si cum as avea un dictionar ca string "{'cheie:valoare}" {"cheie":valoare}
    soup = bs(text_html, "html.parser")
    #id="firstHeading"
    titlu = soup.find(id = "firstHeading")

    return titlu.text

async def main():
    titluri = []
    for url in website_urls:
        titlu = await get_wiki_titlu(url)
        await asyncio.sleep(2) #semn de curtoazie sa nu facem requests hammering
        titluri.append(titlu)

    for title in titluri:
        print(title)

if __name__ == "__main__":
    asyncio.run(main())