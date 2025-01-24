-- 3.5. Desenvolva uma query analítica para responder:
USE demonstracoes_contabeis_database;

-- 1: Quais as 10 operadoras com maiores despesas em "EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR" no último trimestre?
SELECT 
    reg_ans AS operadora, 				  -- Identificador da operadora
    SUM(vl_saldo_final) AS total_despesas -- Soma do valor total das despesas por operadora
FROM 
    demonstracoes_contabeis_database.demonstracoes_contabeis 
WHERE 
    descricao = 'EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS  DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR ' 
    AND data_data >= '2024-07-01' -- Considera apenas despesas a partir de 1 de julho de 2024 (ultimo trimestre)
GROUP BY 
    reg_ans -- Agrupa os dados por operadora (identificada por reg_ans)
ORDER BY 
    total_despesas DESC -- Ordena os resultados pelas maiores despesas em ordem decrescente
LIMIT 10; -- Limita o resultado as 10 operadoras com maiores despesas

-- 2: Quais as 10 operadoras com maiores despesas nessa categoria no último ano?
SELECT 
    reg_ans AS operadora, 
    SUM(vl_saldo_final) AS total_despesas -- Soma do valor total das despesas por operadora
FROM 
    demonstracoes_contabeis_database.demonstracoes_contabeis
WHERE 
    descricao = 'EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS  DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR ' 
    AND data_data BETWEEN '2024-01-01' AND '2024-12-31' -- Considera despesas ocorridas entre 1 de janeiro e 31 de dezembro de 2024 (último ano)
GROUP BY 
    reg_ans -- Agrupa os dados por operadora (identificada por reg_ans)
ORDER BY 
    total_despesas DESC -- Ordena os resultados pelas maiores despesas em ordem decrescente
LIMIT 10; -- Limita o resultado as 10 operadoras com maiores despesas
