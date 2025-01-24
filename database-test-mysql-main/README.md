# README

Este repositório contém três scripts SQL que executam a criação de tabelas, importação de dados e consultas analíticas para análise de operadoras de planos de saúde. O processo segue as etapas solicitadas para configurar o banco de dados, importar os arquivos necessários e realizar consultas analíticas sobre os dados financeiros das operadoras.

## Estrutura dos Arquivos

1. **load_operadoras_ativas.sql**
    - Criação da tabela `operadoras` no banco de dados.
    - Importação dos dados das operadoras ativas a partir de um arquivo CSV.
    - Estruturação da tabela com índices para otimizar as consultas.

2. **load_demonstracoes_contabeis.sql**
    - Criação da tabela `demonstracoes_contabeis` no banco de dados.
    - Importação de dados financeiros (demonstrativos contábeis) a partir de múltiplos arquivos CSV.
    - Utiliza a função `REPLACE` para ajustar a formatação de valores decimais e converte datas no formato adequado.

3. **query_analitica.sql**
    - Realiza consultas analíticas sobre as operadoras com maiores despesas na categoria "EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR", tanto para o último trimestre quanto para o último ano.

## Versão do Banco de Dados e Software

- **Versão do MySQL:** 8.0.41
- **Software Utilizado:** DBeaver 24.3.3

## Contato
- E-mail: juliavbonzanini@gmail.com