import requests
from bs4 import BeautifulSoup

url = 'http://www.ans.gov.br/prestadores/tiss-troca-de-informacao-de-saude-suplementar/'
response = requests.get(url)
page = response.content
soup = BeautifulSoup(page, 'html.parser')

ans = soup.find('a', target='_self').attrs['href']
r1 = requests.get('http://www.ans.gov.br' + ans)
url_especifica = 'http://www.ans.gov.br' + ans

response_especifica = requests.get(url_especifica)
page_especifica = response_especifica.content
soup = BeautifulSoup(page_especifica, 'html.parser')

divPdf = soup.find('div', class_='table-responsive')
aPdfHref = divPdf.find('a', target='_self').attrs['href']
r = requests.get('http://www.ans.gov.br' + aPdfHref)
file = aPdfHref[aPdfHref.rfind('/') + 1:]
open(file, 'wb').write(r.content)
