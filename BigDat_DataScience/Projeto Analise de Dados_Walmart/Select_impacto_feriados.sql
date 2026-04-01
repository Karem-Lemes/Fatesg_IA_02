SELECT 
    CASE WHEN eh_feriado = TRUE THEN 'Feriado' ELSE 'Dia Comum' END AS status_semana,
    AVG(vendas_semanais) AS media_vendas
FROM public.bd_walmart
GROUP BY eh_feriado;