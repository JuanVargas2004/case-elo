SELECT id, nome, YEAR(data_contratacao) AS ano_contratacao, salario, 
	   ROW_NUMBER() OVER (PARTITION BY ano_contratacao ORDER BY salario DESC) AS ranking
FROM funcionarios
;



WITH auxiliar AS (
SELECT id, nome, YEAR(data_contratacao) AS ano_contratacao, salario, 
	   ROW_NUMBER() OVER (PARTITION BY ano_contratacao ORDER BY salario DESC) AS ranking
FROM funcionarios
) SELECT id, nome, ano_contratacao, salario
FROM auxiliar
WHERE ranking = 1
;