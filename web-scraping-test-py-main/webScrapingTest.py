# 1. TESTE DE WEB SCRAPING
from bs4 import BeautifulSoup
import requests
from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED
import logging

# Constantes
BASE_URL = 'https://www.gov.br'  # URL base do site
PAGE_URL = f'{BASE_URL}/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos'  # Página para acessar os anexos
DOWNLOAD_DIR = Path('files')  # Diretorio onde os arquivos vão ser salvos
ZIP_FILENAME = 'attachments.zip'  # Nome do arquivo ZIP que vai ser criado

# Configuração do logger
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Função main
def main():
    logging.info('Starting web scraping process.')

    # Extrai os links dos anexos da página
    links = extract_links(PAGE_URL)

    # Verifica se foram encontrados links validos
    if not links:
        logging.warning('No valid links found.')
        return

    # Baixa os anexos encontrados
    download_attachments(links)

    # Compacta os arquivos baixados em um único arquivo ZIP
    compress_files(DOWNLOAD_DIR, ZIP_FILENAME)

    logging.info('Process successfully completed.')

# 1.1. Acesso ao site: https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos
# Função extract_links que recebe a URL por parametro para extrair os links da pagina
def extract_links(url):
    try:
        logging.info(f'Accessing URL: {url}')

        # Faz a requisiçao HTTP para obter o HTML da página
        response = requests.get(url)
        response.raise_for_status()  # Verifica se a requisição foi bem-sucedida

        # Analisa o HTML usando BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Procura links com texto que contenham "Anexo I" ou "Anexo II"
        links = soup.find_all('a', string=lambda text: text and ('Anexo I' in text or 'Anexo II' in text))
        logging.info(f'{len(links)} links found.')

        return links
    except requests.RequestException as e:
        logging.error(f'Error accessing the URL: {e}')
        return []

# 1.2. Download dos Anexos I e II em formato PDF
# Função download_attachments que recebe os links por parametro para baixar os anexos encontrados
def download_attachments(links):
    DOWNLOAD_DIR.mkdir(exist_ok=True)  # Cria o diretorio para salvar os arquivos, caso não exista

    for link in links:
        download_url = link.get('href')  # Pega o atributo href do link
        if not download_url:  # Verifica se o link é válido
            continue

        # Ajusta a URL caso ela nao seja absoluta
        if not download_url.startswith('http'):
            download_url = f'{BASE_URL}{download_url}'

        # Verifica se o link aponta para um arquivo PDF
        if download_url.endswith('.pdf'):
            # Gera o nome do arquivo com base no texto do link
            filename = DOWNLOAD_DIR / f"{link.text.split('(')[0].strip().replace(' ', '_').rstrip('.')}.pdf"

            try:
                logging.info(f'Downloading {filename} from {download_url}...')

                # Faz o download do arquivo
                response = requests.get(download_url)
                response.raise_for_status()

                # Salva o conteudo do arquivo
                filename.write_bytes(response.content)
                logging.info(f'{filename} downloaded successfully.')
            except requests.RequestException as e:
                logging.error(f'Error downloading {filename}: {e}')


# 1.3. Compactação de todos os anexos em um único arquivo (formatos ZIP, RAR, etc.).
# Função compress_files que recebe o diretorio onde os arquivos estão baixados e o nome do arquivo
# zip por parametro para compactar os anexos baixados
def compress_files(directory, zip_filename):
    try:
        # Cria um arquivo ZIP e adiciona os arquivos do diretorio
        with ZipFile(zip_filename, "w", ZIP_DEFLATED) as zip_file:
            for file in directory.rglob("*"):  # Itera por todos os arquivos no diretório
                zip_file.write(file, file.relative_to(directory))  # Adiciona o arquivo ao ZIP
        logging.info(f'Files successfully compressed into {zip_filename}.')
    except Exception as e:
        logging.error(f'Error compressing files: {e}')


# Inicio do script
if __name__ == '__main__':
    main()
