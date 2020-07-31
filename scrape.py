import requests
from bs4 import BeautifulSoup

url = 'http://www.ans.gov.br/prestadores/tiss-troca-de-informacao-de-saude-suplementar/'

print("\nAcessando site da Agência Nacional de Saúde Suplementar: ", url)
response = requests.get(url)
page = response.content
soup = BeautifulSoup(page, 'html.parser')

ANS = soup.find('a', target='_self').attrs['href']
url_especifica = 'http://www.ans.gov.br' + ANS
print("\nAcessando url da versão atualizado:", url_especifica)

response_especifica = requests.get(url_especifica)
page_especifica = response_especifica.content
soup = BeautifulSoup(page_especifica, 'html.parser')

print("Procurando arquivo em PDF do Padrão para Troca de Informação de Saúde Suplementar - (TISS)\n")
aPdfHref = soup.find('a', target='_self').attrs['href']
r = requests.get('http://www.ans.gov.br' + aPdfHref)
file = aPdfHref[aPdfHref.rfind('/') + 1:]

if file.endswith('.pdf'):
    print("Arquivo encontrado:", file, "e feito download.")
    open(file, 'wb').write(r.content)
else:
    print("Não encontramos o arquivo solicitado")
