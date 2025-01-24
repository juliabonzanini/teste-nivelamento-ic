-- 3. TESTE DE BANCO DE DADOS
-- 3.3. Crie queries para estruturar tabelas necessárias para o arquivo csv.
CREATE DATABASE IF NOT EXISTS demonstracoes_contabeis_database;
USE demonstracoes_contabeis_database;

-- Criação da tabela
CREATE TABLE IF NOT EXISTS demonstracoes_contabeis (
    data_data DATE NOT NULL,
    reg_ans VARCHAR(10) NOT NULL,
    cd_conta_contabil VARCHAR(15) NOT NULL,
    descricao VARCHAR(255),
    vl_saldo_inicial DOUBLE,
    vl_saldo_final DOUBLE,
    PRIMARY KEY (data_data, reg_ans, cd_conta_contabil) -- Chave primária composta
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Índices para melhorar performance de consultas futuras
CREATE INDEX idx_data_reg_ans ON demonstracoes_contabeis_database.demonstracoes_contabeis (data_data, reg_ans);
CREATE INDEX idx_descricao_data ON demonstracoes_contabeis_database.demonstracoes_contabeis (descricao, data_data);

-- 3.4. Elabore queries para importar o conteúdo dos arquivos preparados, atentando para o encoding correto.
-- A importação é feita com o comando LOAD DATA INFILE, configurando corretamente o encoding, delimitadores e tratamento de linhas

LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/1T2023.csv' -- Caminho do arquivo
INTO TABLE demonstracoes_contabeis
CHARACTER SET utf8mb4 		-- Encoding UTF-8
FIELDS TERMINATED BY ';' 	-- Delimitador dos campos
ENCLOSED BY '"'				-- Valores entre aspas
LINES TERMINATED BY '\r\n'  -- Quebra de linha Windows (CRLF)
IGNORE 1 ROWS 				-- Ignorar cabeçalho
(data_data, reg_ans, cd_conta_contabil, descricao, @vl_saldo_inicial, @vl_saldo_final) -- Mapear colunas
SET 
    vl_saldo_inicial = REPLACE(@vl_saldo_inicial, ',', '.'), -- Substituir ',' por '.' para valores decimais
    vl_saldo_final = REPLACE(@vl_saldo_final, ',', '.');

LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/1T2024.csv'
INTO TABLE demonstracoes_contabeis
CHARACTER SET utf8mb4
FIELDS TERMINATED BY ';'
ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 ROWS
(data_data, reg_ans, cd_conta_contabil, descricao, @vl_saldo_inicial, @vl_saldo_final)
SET 
    vl_saldo_inicial = REPLACE(@vl_saldo_inicial, ',', '.'),
    vl_saldo_final = REPLACE(@vl_saldo_final, ',', '.');

LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/2t2023.csv'
INTO TABLE demonstracoes_contabeis
CHARACTER SET utf8mb4
FIELDS TERMINATED BY ';'
ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 ROWS
(data_data, reg_ans, cd_conta_contabil, descricao, @vl_saldo_inicial, @vl_saldo_final)
SET 
    vl_saldo_inicial = REPLACE(@vl_saldo_inicial, ',', '.'),
    vl_saldo_final = REPLACE(@vl_saldo_final, ',', '.');

LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/2T2024.csv'
INTO TABLE demonstracoes_contabeis
CHARACTER SET utf8mb4
FIELDS TERMINATED BY ';'
ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 ROWS
(data_data, reg_ans, cd_conta_contabil, descricao, @vl_saldo_inicial, @vl_saldo_final)
SET 
    vl_saldo_inicial = REPLACE(@vl_saldo_inicial, ',', '.'),
    vl_saldo_final = REPLACE(@vl_saldo_final, ',', '.');

LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/3T2023.csv'
INTO TABLE demonstracoes_contabeis
CHARACTER SET utf8mb4
FIELDS TERMINATED BY ';'
ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 ROWS
(data_data, reg_ans, cd_conta_contabil, descricao, @vl_saldo_inicial, @vl_saldo_final)
SET 
    vl_saldo_inicial = REPLACE(@vl_saldo_inicial, ',', '.'),
    vl_saldo_final = REPLACE(@vl_saldo_final, ',', '.');

LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/3T2024.csv'
INTO TABLE demonstracoes_contabeis
CHARACTER SET utf8mb4
FIELDS TERMINATED BY ';'
ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 ROWS
(data_data, reg_ans, cd_conta_contabil, descricao, @vl_saldo_inicial, @vl_saldo_final)
SET 
    vl_saldo_inicial = REPLACE(@vl_saldo_inicial, ',', '.'),
    vl_saldo_final = REPLACE(@vl_saldo_final, ',', '.');

LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/4T2023.csv'
INTO TABLE demonstracoes_contabeis
CHARACTER SET utf8mb4
FIELDS TERMINATED BY ';'
-- Sem enclosed
LINES TERMINATED BY '\r\n'
IGNORE 1 ROWS
(@data_data, reg_ans, cd_conta_contabil, descricao, @vl_saldo_inicial, @vl_saldo_final)
SET 
    data_data = STR_TO_DATE(@data_data, '%d/%m/%Y'), -- Converte data para formato DATE
    vl_saldo_inicial = REPLACE(@vl_saldo_inicial, ',', '.'),
    vl_saldo_final = REPLACE(@vl_saldo_final, ',', '.');

-- Verifica os dados importados
SELECT * FROM demonstracoes_contabeis_database.demonstracoes_contabeis LIMIT 10000;

