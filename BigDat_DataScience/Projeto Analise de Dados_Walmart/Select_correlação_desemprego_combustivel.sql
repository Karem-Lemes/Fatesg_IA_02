

SELECT 
    id_loja,
    CORR(ipc, preco_combustivel) as Correlacao_Combustivel,
    CORR(vendas_semanais, taxa_desemprego) as Correlacao_Desemprego,
    AVG(ipc) as Media_Vendas
FROM public.bd_walmart
GROUP BY id_loja
HAVING ABS(CORR(ipc, preco_combustivel)) > 0.5 
   OR ABS(CORR(vendas_semanais, taxa_desemprego)) > 0.5
ORDER BY Media_Vendas DESC

