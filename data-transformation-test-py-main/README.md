# Teste de Transformação de Dados usando Python

Este script em Python realiza a extração de dados de um arquivo PDF (Anexo I do Rol de Procedimentos e Eventos em Saúde), converte esses dados em uma tabela estruturada e os salva em formato CSV. Em seguida, o script substitui as abreviações de colunas no CSV conforme especificado e compacta o arquivo CSV gerado em um arquivo ZIP.

## Funcionalidade

O script realiza as seguintes operações:

1. **Baixar o PDF**: O script baixa o arquivo PDF do Anexo I do Rol de Procedimentos e Eventos em Saúde.
2. **Extrair Dados da Tabela**: Após baixar o PDF, o script extrai os dados da tabela presente no documento.
3. **Salvar Dados em CSV**: Os dados extraídos são salvos em formato CSV.
5. **Substituir Abreviações**: As abreviações presentes nas colunas da tabela (OD, AMB, HCO, HSO, REF, PAC) são substituídas pelas descrições completas.
5. **Compactar em ZIP**: O arquivo CSV é compactado em um arquivo ZIP.

## Pré-requisitos

Para executar este script, você precisará de:

- Python (versão usada: 3.12)
- Bibliotecas Python: `requests`, `pdfplumber`, `BytesIO`, `pandas`, `zipfile`, `logging`

Você pode instalar as bibliotecas necessárias usando o seguinte comando:

```bash
pip install requests pdfplumber pandas
```
## Estrutura do Código

### Funções Principais:

- `download_pdf(pdf_url)`: Baixa o arquivo PDF a partir da URL fornecida.
- `extract_table(pdf_file)`: Extrai a tabela do PDF utilizando a biblioteca `pdfplumber`.
- `save_table_to_csv(table_data, output_csv)`: Salva os dados extraídos em um arquivo CSV.
- `replace_abbreviations_in_csv(input_csv)`: Substitui as abreviações no CSV pelas descrições completas.
- `create_zip_from_csv(csv_filename, zip_filename)`: Compacta o arquivo CSV em um arquivo ZIP.

### Bibliotecas Utilizadas:

- **requests**: Para fazer requisições HTTP e baixar o PDF.
- **pdfplumber**: Para extrair a tabela do PDF.
- **BytesIO**: Usado para carregar o conteúdo do PDF em memória, permitindo a extração sem a necessidade de salvar o PDF em disco.
- **pandas**: Para manipulação e salvamento dos dados extraídos em formato CSV.
- **zipfile**: Para compactar o arquivo CSV em um arquivo ZIP.
- **logging**: Para registrar mensagens de log durante a execução do script.

## Arquivos Gerados:

- **tabelaAnexoI.csv**: Arquivo CSV gerado com os dados extraídos do PDF.
- **Teste_Julia_Bonzanini.zip**: Arquivo ZIP contendo o arquivo CSV.

## Logs

O script utiliza logs para monitorar o progresso de cada etapa do processo, como o download do PDF, a extração da tabela, o salvamento no CSV, a substituição das abreviações e a criação do arquivo ZIP.

### Exemplos de Logs:

```bash
2025-01-23 10:00:00 - INFO - Starting the process of downloading PDF, extracting table, and creating ZIP file.
2025-01-23 10:01:00 - INFO - PDF downloaded successfully into memory (buffer).
2025-01-23 10:02:00 - INFO - Table extracted successfully from the PDF.
2025-01-23 10:03:00 - INFO - CSV file saved successfully.
2025-01-23 10:04:00 - INFO - Abbreviations replaced and CSV updated successfully.
2025-01-23 10:05:00 - INFO - ZIP file Teste_Julia_Bonzanini.zip created successfully.
```

## Contato
- E-mail: juliavbonzanini@gmail.com