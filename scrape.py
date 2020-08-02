import os
import re
import time

import requests
from bs4 import BeautifulSoup


def main():
    start_time = time.time()

    url = 'http://www.ans.gov.br/prestadores/tiss-troca-de-informacao-de-saude-suplementar/'
    home_url = 'http://www.ans.gov.br'

    def acessa_site_ans():
        print("\nAcessando site da Agência Nacional de Saúde Suplementar:")
        print(url)
        response = requests.get(url)
        page = response.content
        return BeautifulSoup(page, 'html.parser')

    def acessa_link_com_versao_atualizada():
        link = acessa_site_ans().find('a', href=re.compile('padrao')).attrs['href']
        print("\nAcessando link da versão atualizado:", home_url + link)
        return home_url + link

    def pagina_especifica_versao_atualizada():
        response_especifica = requests.get(acessa_link_com_versao_atualizada())
        page_especifica = response_especifica.content
        return BeautifulSoup(page_especifica, 'html.parser')

    pdf_link = pagina_especifica_versao_atualizada().find('a', href=re.compile('Padrao')).attrs['href']
    r = requests.get(home_url + pdf_link)

    file = pdf_link[pdf_link.rfind('/') + 1:]

    if file.endswith('.pdf'):
        open(file, 'wb').write(r.content)
        print("TISS mais recente salvo em:", os.path.realpath(file), "\n")
    else:
        print("Não encontramos o arquivo solicitado")

    print("My program took", time.time() - start_time, "to run")


if __name__ == "__main__":
    main()
