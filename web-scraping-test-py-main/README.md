# Web Scraping para Download e Compactação de Anexos usando Python

Este script realiza o processo de web scraping para acessar uma página específica do site **gov.br**, extrair links para os anexos "Anexo I" e "Anexo II" em formato PDF, e depois compactar todos os anexos baixados em um arquivo ZIP.

## Funcionalidade

O script realiza as seguintes operações:

1. **Acesso ao site**: O script acessa a página [Atualização do Rol de Procedimentos](https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos) para buscar os anexos.
2. **Download dos Anexos**: Após acessar a página, o script localiza os links para os anexos "Anexo I" e "Anexo II" (em formato PDF) e os baixa.
3. **Compactação dos Arquivos**: Todos os arquivos PDF baixados são então compactados em um único arquivo ZIP para facilitar o armazenamento ou envio.

## Pré-requisitos

Para executar este script, você precisará de:

- Python (versão usada: 3.12)
- Bibliotecas Python: `requests`, `beautifulsoup4`, `pathlib`, `zipfile`, `logging`

Você pode instalar as bibliotecas necessárias usando o seguinte comando:

```bash
pip install requests beautifulsoup4
```

## Estrutura do Código

### Funções Principais:

- **`extract_links(url)`**: Extrai os links dos anexos "Anexo I" e "Anexo II" da página informada.
- **`download_attachments(links)`**: Baixa os arquivos PDF dos links encontrados.
- **`compress_files(directory, zip_filename)`**: Compacta os arquivos PDF baixados em um único arquivo ZIP.

### Bibliotecas Utilizadas:

- **`requests`**: Usada para fazer requisições HTTP e obter o conteúdo das páginas da web.
- **`beautifulsoup4`**: Usada para analisar o HTML da página e extrair os links dos anexos.
- **`pathlib`**: Usada para manipulação de caminhos de arquivos e criação de diretórios.
- **`zipfile`**: Usada para compactar os arquivos baixados em um arquivo ZIP.
- **`logging`**: Usada para registrar mensagens de log durante a execução do script (como o progresso e possíveis erros).

### Diretórios e Arquivos:

- **`files/`**: Diretório onde os arquivos PDF serão salvos.
- **`attachments.zip`**: Arquivo ZIP gerado com os anexos.

## Logs

O script faz uso de logs para monitorar o progresso do download e compactação dos arquivos. As mensagens de log indicam o status de cada etapa (acesso ao site, download dos arquivos e compactação).

### Exemplos de logs:

```bash
2025-01-23 10:00:00 - INFO - Starting web scraping process.
2025-01-23 10:01:00 - INFO - Accessing URL: https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos
2025-01-23 10:02:00 - INFO - Downloading Anexo I from https://example.com/anexo1.pdf...
2025-01-23 10:03:00 - INFO - Files successfully compressed into attachments.zip.
```

## Contato
- E-mail: juliavbonzanini@gmail.com
