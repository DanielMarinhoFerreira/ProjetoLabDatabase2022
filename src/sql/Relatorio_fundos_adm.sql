select  FUN.TICKER, FUN.NOME, EMPRE.SEGMENTO, adm.CNPJ_ADMIN, adm.NOME
from FUNDOS fun
join Administradores adm on adm.CNPJ = fun.CNPJ_ADMIN
where TICKER !=''
    GROUP BY fun.CNPJ_ADMIN