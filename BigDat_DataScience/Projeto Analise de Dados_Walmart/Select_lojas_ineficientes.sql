

SELECT 
    id_loja, 
    tipo_loja, 
    tamanho_loja,
    SUM(vendas_semanais) / tamanho_loja AS venda_por_metro_quadrado,
    RANK() OVER(
        PARTITION BY tipo_loja 
        ORDER BY (SUM(vendas_semanais) / tamanho_loja) ASC
    ) AS rank_pior_eficiencia
FROM bd_walmart
GROUP BY id_loja, tipo_loja, tamanho_loja
ORDER BY tipo_loja, venda_por_metro_quadrado ASC;
