 -- SITE PARA PEGAR AS INFORMAÇÕES: https://fiis.com.br/ OU https://www.fundsexplorer.com.br/ranking

INSERT INTO ADMINISTRADORES (NOME, TELEFONE, EMAIL,URL_SITE, CNPJ_ADMIN)
WITH DATA_ADMINISTRADORES AS (

    SELECT 'PLANNER CORRETORA DE VALORES SA', '1121722667', 'inforegulatorio@planner.com.br', 'www.planner.com.br','00806535000154' FROM DUAL UNION ALL
    SELECT 'RJI CORRETORA DE TÍTULOS E VALORES MOBILIÁRIOS LTDA', '213500450021','backoffice.adm@rjicv.com.br','www.rjicv.com.br','42066258000130' FROM DUAL UNION ALL
    SELECT 'BTG PACTUAL SERVIÇOS FINANCEIROS S/A DTVM', '1133833102','ri.fundoslistados@btgpactual.com','www.btgpactual.com','59281253000123' FROM DUAL UNION ALL
    SELECT 'OLIVEIRA TRUST DTVM S.A.', '2135140000', 'ger2.fundos@oliveiratrust.com.br','www.oliveiratrust.com.br','36113876000191' FROM DUAL 
    )
    SELECT * FROM DATA_ADMINISTRADORES;
    
    commit;
     
INSERT INTO FUNDOS (TICKER, TIPO_ABBIMA, SEGMENTO, CONTA_EMIT, NUM_COTAS, RAZAO_SOCIAL, CNPJ, NOME_PREGAO, PRAZO_DURACAO, TIPO_GESTAO, CNPJ_ADMIN)
    WITH DATA_FUNDOS AS (

    SELECT 'AAZQ11','Tílos e Valores Mobiliarios','Indefinido','24037284','18095', 'AZ QUEST SOLE FDO DE INV','44625826000111','FIAGRO AAZQ','Indeterminado','ativa','59281253000123'FROM DUAL UNION ALL
    SELECT 'ABCP11','Renda','Shoppings','4709082','17747','Grand Plaza Shopping','01201140000190','Grand Plaza Shopping','Indeterminado','Passiva','00806535000154'FROM DUAL UNION ALL
    SELECT  'AFHI11','Tílos e Valores Mobiliarios','Papel','3343095','23891','AF INVEST CRI','36642293000158','FII AFHI CRI','Indeterminado','Ativa','42066258000130' FROM DUAL UNION ALL
    SELECT  'LVBI11','Renda','Imóveis Industriais e Logísticos','1363338408','11775177','AF INVEST CRI','36642293000158','FII VBI LOG','Indeterminado','Ativa','59281253000123' FROM DUAL UNION ALL
    SELECT  'SNCI11','Títulos e Valores Mobiliários','Indefinido','413274896','4200000','SUNO RECEBÍVEIS IMOBILIÁRIOS FDO DE INV IMOB','41076710000182','FII SUNO CRI','Indeterminado','Ativa','59281253000123' FROM DUAL UNION ALL    
    SELECT  'AIEC11','Renda','Lajes Corporativas','4824987','15564','AUTONOMY EDIF̓IOS CORPORATIVOS','35765826000126','FII AUTONOMY','Indeterminado','Ativa','36113876000191' FROM DUAL
    
    )
    SELECT * FROM DATA_FUNDOS;
    
    commit;

    
INSERT INTO COTACOES (TICKER, DATA_COTA, COTA_ATUAL, RENDIMENTO_ATUAL, MINIMO_COTA, MAXIMO_COTA, ABERTURA, VOLUME_COTAS, MES, P_VP)
WITH DATA_COTACOES AS (

    SELECT  'AAZQ11',   '03/10/2023',   '09.25',    '1.28',     '09.28',    '09.95',   '09.29',     '24037284',    '04/10/2023', '1.2'  FROM DUAL UNION ALL
    SELECT  'ABCP11',   '03/10/2023',   '66.81',    '0.89',     '63.47',    '109.7',    '66.84',    '4709082',     '04/10/2023', '1.0'   FROM DUAL UNION ALL
    SELECT  'AFHI11',   '03/10/2023',   '95.70',    '1.07',     '90.30',    '103.70',   '95.98',    '3343095',     '04/10/2023', '1.2'   FROM DUAL UNION ALL
    SELECT  'AIEC11',   '03/10/2023',   '63.16',    '1.16',     '60.52',    '70.86',    '63.63',    '4824987',     '04/10/2023', '1.3'   FROM DUAL UNION ALL

    SELECT  'AAZQ11',   '13/10/2023',   '09.35',    '0.11',     '09.32',    '09.36',   '09.34',     '24037284',    '13/10/2023', '0.97'  FROM DUAL UNION ALL
    SELECT  'ABCP11',   '13/10/2023',   '67.80',    '-0.31',     '67.68',    '68.01',    '68.01',    '4709082',     '13/10/2023','0.74'   FROM DUAL UNION ALL
    SELECT  'AFHI11',   '13/10/2023',   '98.19',    '0.051',     '97.75',    '98.73',   '98.14',    '3343095',     '13/10/2023','1.03'   FROM DUAL UNION ALL
    SELECT  'AIEC11',   '13/10/2023',   '62.40',    '0.22',     '62.40',    '63.10',    '62.54',    '4824987',     '13/10/2023','0.66'   FROM DUAL UNION ALL

    SELECT  'SNCI11',   '13/10/2023',   '100.42',    '0.45',     '99.90',    '100.54',    '99.97',    '4200000',     '13/10/2023','1.02'   FROM DUAL UNION ALL
    SELECT  'LVBI11',   '13/10/2023',   '118.04',    '0.68',     '117.03',    '118.07',   '117.96',    '11775177',     '13/10/2023','1.02'   FROM DUAL 
    )
    SELECT * FROM DATA_COTACOES;

    commit;
    

INSERT INTO DIVIDENDOS (TICKER, DATA_PAG, COTA_BASE, ULT_DIVID, RENDIMENTO, DIV_YIELD)
WITH DATA_DIVIDENDOS AS (

    SELECT 'AAZQ11' , '05/11/2023',  '9.32' ,  '1.28' ,  '0.12' , '12.47' FROM DUAL UNION ALL
    SELECT 'ABCP11' , '06/11/2023' , '66.95' , '0.89',   '0.60' , '8.59' FROM DUAL UNION ALL
    SELECT 'AFHI11' , '05/11/2023' , '95.80' , '1.07',   '1.05' , '13.03' FROM DUAL UNION ALL
    SELECT 'AIEC11' , '05/11/2023' , '63.31' , '1.16',   '0.76' , '14.38' FROM DUAL UNION ALL

    SELECT 'AAZQ11' , '16/10/2023',  '9.40' ,  '1.28' ,  '0.12' , '12.42' FROM DUAL UNION ALL
    SELECT 'ABCP11' , '06/10/2023' , '67.24' , '0.89',   '0.60' , '8.45' FROM DUAL UNION ALL
    SELECT 'AFHI11' , '22/09/2023' , '98.23' , '1.07',   '1.05' , '12.69' FROM DUAL UNION ALL
    SELECT 'AIEC11' , '09/10/2023' , '65.69' , '1.16',   '0.76' , '14.57' FROM DUAL UNION ALL
    
    SELECT 'SNCI11' , '25/10/2023' , '100.48' , '1.00',   '1.00' , '13.32' FROM DUAL UNION ALL    
    SELECT 'LVBI11' , '06/10/2023' , '118.69' , '0.67',   '0.79' , '7.75' FROM DUAL

    )
    SELECT * FROM DATA_DIVIDENDOS;

    commit;  
    

