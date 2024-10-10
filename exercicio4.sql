SELECT data_contratacao, salario, SUM(salario) OVER(ORDER BY data_contratacao) AS soma_acumulativa
FROM funcionarios
ORDER BY data_contratacao
;