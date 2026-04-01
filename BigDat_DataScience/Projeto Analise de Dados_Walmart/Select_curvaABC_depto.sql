WITH DeptSales AS (
    SELECT 
        cd.id_depto , 
        SUM(cd.vendas_semanais ) as Total_Dept_Sales
    FROM public.bd_walmart cd 
    GROUP BY id_depto
),
RunningSales AS (
    SELECT 
        id_depto, 
        Total_Dept_Sales,
        SUM(Total_Dept_Sales) OVER(ORDER BY Total_Dept_Sales DESC) as Cumulative_Sales,
        SUM(Total_Dept_Sales) OVER() as Grand_Total
    FROM DeptSales
)
SELECT 
    id_depto, 
    Total_Dept_Sales,
    (Cumulative_Sales / Grand_Total) * 100 as PCT_Acumulado,
    CASE 
        WHEN (Cumulative_Sales / Grand_Total) <= 0.80 THEN 'A'
        WHEN (Cumulative_Sales / Grand_Total) <= 0.95 THEN 'B'
        ELSE 'C'
    END as Categoria_ABC
FROM RunningSales
ORDER BY Total_Dept_Sales DESC;