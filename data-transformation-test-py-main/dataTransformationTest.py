# 2. TESTE DE TRANSFORMAÇÃO DE DADOS
import pdfplumber
import requests
from io import BytesIO
from zipfile import ZipFile
import pandas as pd
import logging

# Constantes
PDF_URL = 'https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos/Anexo_I_Rol_2021RN_465.2021_RN624_RN625.2024.pdf'  # URL do PDF a ser baixado
CSV_FILENAME = 'tabelaAnexoI.csv'  # Nome do arquivo CSV para salvar a tabela extraida
ZIP_FILENAME = 'Teste_Julia_Bonzanini.zip'  # Nome do arquivo ZIP que vai ser gerado

# Configuração do logger
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


# Função main
def main():
    logging.info('Starting the process of downloading PDF, extracting table, and creating ZIP file.')

    # Baixa o PDF para a memoria (buffer)
    pdf_file = download_pdf(PDF_URL)
    if pdf_file:
        logging.info('PDF downloaded successfully into memory (buffer).')

        # Extrai a tabela do PDF
        table_data = extract_table(pdf_file)
        if table_data:
            logging.info('Table extracted successfully from the PDF.')

            # Salva os dados extraidos em um arquivo CSV
            save_table_to_csv(table_data, CSV_FILENAME)

            # Substitui abreviações no CSV
            replace_abbreviations_in_csv(CSV_FILENAME)

            # Cria um arquivo ZIP contendo o arquivo CSV gerado
            create_zip_from_csv(CSV_FILENAME, ZIP_FILENAME)
            logging.info('Process completed successfully.')
        else:
            logging.warning('No table data found in PDF.')
    else:
        logging.error('Failed to download the PDF.')


# Função que recebe a URL do PDF por parametro para baixar e armazenar na memória
def download_pdf(pdf_url):
    try:
        logging.info(f'Downloading PDF from {pdf_url} into memory buffer.')
        # Realiza a requisição HTTP para baixar o arquivo PDF da URL
        response = requests.get(pdf_url, timeout=10)
        response.raise_for_status()  # Verifica se a requisição foi bem-sucedida

        # Verifica se o conteudo retornado é realmente um PDF
        if 'application/pdf' not in response.headers.get('Content-Type', ''):
            raise ValueError('The content is not a PDF.')

        # Retorna o conteudo do PDF como um buffer de memória utilizando BytesIO
        return BytesIO(response.content)
    except requests.exceptions.RequestException as e:
        logging.error(f'Error downloading the PDF: {e}')
    except ValueError as e:
        logging.error(f'Error: {e}')
    return None

# 2.1. Extraia os dados da tabela Rol de Procedimentos e Eventos em Saúde do PDF do Anexo I do teste 1 (todas as páginas)
# Função que recebe o PDF por parametro para extrair a tabela dele usando o pdfplumber
def extract_table(pdf_file):
    try:
        logging.info('Extracting table from the downloaded PDF.')
        # Abre o arquivo PDF usando pdfplumber
        with pdfplumber.open(pdf_file) as pdf:
            all_data = []  # Lista para armazenar todas as linhas da tabela
            for page_number, page in enumerate(pdf.pages, start=1):
                # Extrai a tabela da página atual
                table = page.extract_table()
                if table:
                    if not all_data:
                        all_data.append(table[0])  # Adiciona o cabeçalho na primeira iteração
                    all_data.extend(table[1:])  # Adiciona as linhas da tabela
                else:
                    logging.warning(f'No table found on page {page_number}.')  # Caso não haja tabela na página (No caso desse PDF, nas 2 primeiras páginas não há tabela)
            return all_data if all_data else None  # Retorna os dados da tabela ou None caso não tenha sido encontrada nenhuma tabela
    except Exception as e:
        logging.error(f'Error extracting table from PDF: {e}')
    return None

# 2.2. Salve os dados em uma tabela estruturada, em formato csv.
# Função que recebe os dados extraidos da tabela e o nome do arquivo CSV por parametro
# e salva os dados nesse arquivo
def save_table_to_csv(table_data, output_csv):
    try:
        logging.info(f'Saving extracted table to {output_csv}.')
        # Converte a lista de dados extraidos para um DataFrame do Pandas
        df = pd.DataFrame(table_data[1:], columns=table_data[0])  # Usa a primeira linha como cabeçalho
        # Salva o DataFrame em um arquivo CSV
        df.to_csv(output_csv, index=False, encoding='utf-8')
        logging.info('CSV file saved successfully.')
    except Exception as e:
        logging.error(f'Error saving table to CSV: {e}')

# 2.4. Substitua as abreviações das colunas OD e AMB pelas descrições completas, conforme a legenda no rodapé.
# Substitui também as abreviações de HCO, HSO, REF e PAC pelas descrições completas
# Função que recebe o nome do arquivo CSV por parametro e substitui as abreviações nele
def replace_abbreviations_in_csv(input_csv):
    try:
        logging.info('Replacing abbreviations in the CSV.')
        # Le o CSV gerado para substituição de abreviações
        df = pd.read_csv(input_csv, encoding='utf-8')

        # Dicionário com as abreviações
        replacements = {
            'OD': 'Seg. Odontológica',
            'AMB': 'Seg. Ambulatorial',
            'HCO': 'Seg. Hospitalar Com Obstetrícia',
            'HSO': 'Seg. Hospitalar Sem Obstetrícia',
            'REF': 'Plano Referência',
            'PAC': 'Procedimento de Alta Complexidade'
        }

        # Substitui as abreviações no DataFrame
        for col, full_name in replacements.items():
            if col in df.columns:
                df[col] = df[col].replace({col: full_name})  # Substitui as abreviações pelas versões completas

        # Salva o CSV com as substituições
        df.to_csv(input_csv, index=False, encoding='utf-8')
        logging.info('Abbreviations replaced and CSV updated successfully.')
    except Exception as e:
        logging.error(f'Error replacing abbreviations: {e}')

# 2.3. Compacte o csv em um arquivo denominado "Teste_{seu_nome}.zip".
# Função que recebe o nome do arquivo CSV e do ZIP por parametro
# e cria um arquivo ZIP com este nome contendo o arquivo CSV gerado
def create_zip_from_csv(csv_filename, zip_filename):
    try:
        logging.info(f'Creating ZIP file {zip_filename}.')
        # Cria um arquivo ZIP e adiciona o CSV a ele
        with ZipFile(zip_filename, 'w') as zipf:
            zipf.write(csv_filename)  # Adiciona o arquivo CSV ao ZIP
        logging.info(f'ZIP file {zip_filename} created successfully.')
    except Exception as e:
        logging.error(f'Error creating ZIP file: {e}')


# Inicio do script
if __name__ == '__main__':
    main()
