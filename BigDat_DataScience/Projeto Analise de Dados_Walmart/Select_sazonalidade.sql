
SELECT 
    mes, 
    AVG(vendas_semanais) AS media_vendas_mensal,
    SUM(vendas_semanais) AS faturamento_total_mes
FROM bd_walmart 
GROUP BY mes 
ORDER BY media_vendas_mensal DESC;
