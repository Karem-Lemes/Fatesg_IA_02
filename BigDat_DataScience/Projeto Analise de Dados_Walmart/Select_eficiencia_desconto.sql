
SELECT 
    id_loja,
    AVG(desconto1) AS media_desconto_aplicado,
    AVG(vendas_semanais) AS media_vendas_semanal
FROM bd_walmart
WHERE desconto1 > 0
GROUP BY id_loja
ORDER BY media_vendas_semanal DESC, media_desconto_aplicado ASC;