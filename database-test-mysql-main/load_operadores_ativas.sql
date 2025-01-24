-- 3. TESTE DE BANCO DE DADOS
-- 3.3. Crie queries para estruturar tabelas necessárias para o arquivo csv.

-- Verifica se o banco de dados já existe e, se não, cria o banco
CREATE DATABASE IF NOT EXISTS operadoras_ativas_database;
USE operadoras_ativas_database;

-- Criação da tabela 'operadoras' com tipos e tamanho de dados adequados
CREATE TABLE IF NOT EXISTS operadoras (
    registro_ans VARCHAR(20) NOT NULL, 
    cnpj VARCHAR(18) NOT NULL, 
    razao_social VARCHAR(255) NOT NULL, 
    nome_fantasia VARCHAR(255), 
    modalidade VARCHAR(100),
    logradouro VARCHAR(255), 
    numero VARCHAR(20),
    complemento VARCHAR(100), 
    bairro VARCHAR(100), 
    cidade VARCHAR(100), 
    uf CHAR(2),
    cep VARCHAR(10),
    ddd VARCHAR(3),
    telefone VARCHAR(50), 
    fax VARCHAR(15), 
    endereco_eletronico VARCHAR(100), 
    representante VARCHAR(255), 
    cargo_representante VARCHAR(100),
    regiao_de_comercializacao CHAR(2), 
    data_registro_ans DATE, 
    PRIMARY KEY (registro_ans)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4; -- Define InnoDB como mecanismo de armazenamento e  garante que caracteres especiais sejam corretamente armazenados

-- Índices para melhorar performance de consultas futuras
CREATE INDEX idx_cnpj ON operadoras (cnpj);
CREATE INDEX idx_cidade_uf ON operadoras (cidade, uf);
CREATE INDEX idx_modalidade ON operadoras (modalidade);

-- 3.4. Elabore queries para importar o conteúdo dos arquivos preparados, atentando para o encoding correto.
-- A importação é feita com o comando LOAD DATA INFILE, configurando corretamente o encoding, delimitadores e tratamento de linhas

LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/Relatorio_cadop.csv' 
INTO TABLE operadoras
CHARACTER SET utf8mb4	  -- Define o encoding como UTF-8MB4
FIELDS TERMINATED BY ';'  -- Delimitador de campos
ENCLOSED BY '"'           -- Caracter que envolve os campos
LINES TERMINATED BY '\n'  -- Delimitador de linhas
IGNORE 1 ROWS             -- Ignora o cabeçalho
(
    registro_ans, 
    cnpj, 
    razao_social, 
    nome_fantasia, 
    modalidade, 
    logradouro, 
    numero, 
    complemento, 
    bairro, 
    cidade, 
    uf, 
    cep, 
    ddd, 
    telefone, 
    fax, 
    endereco_eletronico, 
    representante, 
    cargo_representante, 
    regiao_de_comercializacao, 
    data_registro_ans
);

-- Verifica os dados importados
SELECT * FROM operadoras_ativas_database.operadoras; 

