import os
import time
import requests
from sopa import caminho, home


def main():
    start_time = time.time()

    ans = caminho('tiss', home)
    page_tiss = caminho('padrao', ans)
    page_pdf = caminho('Padrao', page_tiss)

    requisicao = requests.get(page_pdf)
    arquivo = page_pdf[page_pdf.rfind('/') + 1:]

    if arquivo.endswith('.pdf'):
        open(arquivo, 'wb').write(requisicao.content)
        print("\nTISS mais recente salvo em:", os.path.realpath(arquivo), "\n")
    else:
        print("Não encontramos o arquivo solicitado")

    print("O script demorou", time.time() - start_time, "para rodar")


if __name__ == "__main__":
    main()
