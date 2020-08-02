import re
import requests
from bs4 import BeautifulSoup

home = 'http://www.ans.gov.br/'


def sopa(url):
    resposta = requests.get(url)
    pagina = resposta.content
    return BeautifulSoup(pagina, 'html.parser')


def caminho(texto, url, url_padrao=home):
    return url_padrao + sopa(url).find('a', href=re.compile(texto)).attrs['href']

