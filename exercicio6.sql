SELECT departamento, nome, salario, 
	   RANK() OVER (PARTITION BY departamento ORDER BY salario DESC) AS ranking,
       COUNT(*) OVER (PARTITION BY departamento) AS total_funcionarios,
       ROUND(AVG(salario) OVER (PARTITION BY departamento), 2) AS media_salarial
FROM funcionarios
;