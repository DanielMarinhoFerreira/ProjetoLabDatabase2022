select div.ticker, cot.p_vp, sum(div.rendimento) as rendimento_total
from dividendos div
join cotacoes cot on cot.ticker = div.ticker
where cot.p_vp >= '1'
group by div.ticker, cot.p_vp, div.rendimento