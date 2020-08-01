import os

import requests
from bs4 import BeautifulSoup

url = 'http://www.ans.gov.br/prestadores/tiss-troca-de-informacao-de-saude-suplementar/'

print("\nAcessando site da Agência Nacional de Saúde Suplementar:")
print(url)
response = requests.get(url)
page = response.content
soup = BeautifulSoup(page, 'html.parser')

ANS = soup.find('a', target='_self').attrs['href']
url_especifica = 'http://www.ans.gov.br' + ANS
print("\nAcessando link da versão atualizado:")
print(url_especifica)

response_especifica = requests.get(url_especifica)
page_especifica = response_especifica.content
soup = BeautifulSoup(page_especifica, 'html.parser')

print("Procurando arquivo mais recente do Padrão para Troca de Informação de Saúde Suplementar - (TISS) em PDF \n")
aPdfHref = soup.find('a', target='_self').attrs['href']
r = requests.get('http://www.ans.gov.br' + aPdfHref)
file = aPdfHref[aPdfHref.rfind('/') + 1:]

if file.endswith('.pdf'):
    with open(fr'\Users\{os.getlogin()}\Desktop\{file}', 'wb') as file:
        file.write(r.content)
        file.close()
    print("Arquivo encontrado e salvo em:", file.name, "\n")
else:
    print("Não encontramos o arquivo solicitado")
