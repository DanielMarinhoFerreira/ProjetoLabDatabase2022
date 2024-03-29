/*
drop table COTACOES;
drop table DIVIDENDOS;
drop table FUNDOS;
drop table ADMINISTRADORES;
drop SEQUENCE ADMINISTRADORES_ID_SEQ;
drop SEQUENCE DIVIDENDOS_ID_SEQ;
drop SEQUENCE COTACOES_ID_SEQ;
*/

CREATE SEQUENCE ADMINISTRADORES_ID_SEQ;

CREATE TABLE ADMINISTRADORES (
                ID NUMBER GENERATED ALWAYS AS IDENTITY NOT NULL,
                CNPJ_ADMIN NUMBER(14) NOT NULL,
                NOME VARCHAR2(80) NOT NULL,
                TELEFONE NUMBER(12),
                EMAIL VARCHAR2(80),
                URL_SITE VARCHAR2(80),
                CONSTRAINT ADMINISTRADORES_PK PRIMARY KEY (CNPJ_ADMIN)
);


CREATE TABLE FUNDOS (
                TICKER VARCHAR2(6) NOT NULL,
                TIPO_ABBIMA VARCHAR2(64) NOT NULL,
                SEGMENTO VARCHAR2(62),
                CONTA_EMIT NUMERIC(38) NOT NULL,
                NUM_COTAS NUMERIC(38) NOT NULL,
                RAZAO_SOCIAL VARCHAR2(80) NOT NULL,
                CNPJ NUMBER(14) NOT NULL,
                NOME_PREGAO VARCHAR2(80),
                PRAZO_DURACAO VARCHAR2(80) NOT NULL,
                TIPO_GESTAO VARCHAR2(60) NOT NULL,
                CNPJ_ADMIN NUMBER(14) NOT NULL,
                CONSTRAINT FUNDOS_PK PRIMARY KEY (TICKER)
);


CREATE SEQUENCE DIVIDENDOS_ID_SEQ;


CREATE TABLE DIVIDENDOS (
                ID NUMBER GENERATED ALWAYS AS IDENTITY NOT NULL,
                TICKER VARCHAR2(6) NOT NULL,
                DATA_PAG VARCHAR2(10) NOT NULL,
                COTA_BASE NUMERIC(6,2) NOT NULL,
                ULT_DIVID NUMERIC(6,2),
                RENDIMENTO NUMERIC(6,2),
                DIV_YIELD NUMERIC(6,2),
                CONSTRAINT DIVIDENDOS_PK PRIMARY KEY (ID)
);


CREATE SEQUENCE COTACOES_ID_SEQ;


CREATE TABLE COTACOES (
                ID NUMBER GENERATED ALWAYS AS IDENTITY NOT NULL,
                TICKER VARCHAR2(6) NOT NULL,
                DATA_COTA VARCHAR2(10) NOT NULL,
                COTA_ATUAL NUMERIC(6,2) NOT NULL,
                RENDIMENTO_ATUAL NUMERIC(6,2) NOT NULL,
                MINIMO_COTA NUMERIC(6,2) NOT NULL,
                MAXIMO_COTA NUMERIC(6,2) NOT NULL,
                ABERTURA NUMERIC(6,2) NOT NULL,
                VOLUME_COTAS NUMERIC(15,4) NOT NULL,
                MES VARCHAR2(10) NOT NULL,
                P_VP NUMERIC(6,2)NOT NULL,
                CONSTRAINT COTACOES_PK PRIMARY KEY (ID)
);


ALTER TABLE FUNDOS ADD CONSTRAINT ADMINISTRADORES_FUNDOS_FK
FOREIGN KEY (CNPJ_ADMIN)
REFERENCES ADMINISTRADORES (CNPJ_ADMIN);

ALTER TABLE COTACOES ADD CONSTRAINT FUNDOS_COTACOES_FK
FOREIGN KEY (TICKER)
REFERENCES FUNDOS (TICKER);

ALTER TABLE DIVIDENDOS ADD CONSTRAINT FUNDOS_DIVIDENDOS_FK
FOREIGN KEY (TICKER)
REFERENCES FUNDOS (TICKER);
