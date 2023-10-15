from model.dividendos import Dividendos
from connection.oracle_queries import OracleQueries

class Controller_Dividendos():
   
    def __init__(self):
        pass
    
    def inserir_Dividendos(self) -> None:

        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries(can_write=True)
        oracle.connect()

        # Solicita ao usuário o código do fundo a ser alterado
        div_ticker = input("informe o ticker do fundo: ")
        while self.verifica_existencia(oracle, valor=div_ticker, tabela='DIVIDENDOS', coluna=['TICKER','TICKER']):
            div_ticker = input("informe o ticker do fundo: ")

        divid = self.cadastrar_dividendos(ticker=div_ticker)
        
        if self.verifica_existencia(oracle, valor=[divid.get_ticker(),divid.get_data_pag()], tabela='DIVIDENDOS', coluna=['ID','TICKER','DATA_PAG']):
            #Inserir o cadastro do Fundo
            oracle.write(divid.get_insert())
                
            # Recupera os dados do novo ticker criado transformando em um DataFrame
            df_div = oracle.sqlToDataFrame(f"""SELECT TICKER, DATA_PAG FROM DIVIDENDOS  WHERE TICKER = '{divid.get_ticker()}' AND DATA_PAG ='{divid.get_data_pag()}'""")
            print(df_div.ticker.values[0], df_div.data_pag.values[0])
        else:
            print("Já existe divindendo com essa informações cadastrado no sistema.")
        return
    
    def atualizar_Dividendos(self):

        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries(can_write=True)
        oracle.connect()

        # Solicita ao usuário o código do fundo a ser alterado
        div_ticker = input("informe o ticker do fundo: ")
        data_pag = input("Informe Data pagamento (Novo): ")
        while self.verifica_existencia(oracle, valor=[div_ticker,data_pag], tabela='DIVIDENDOS', coluna=['ID','TICKER','DATA_PAG']):
            div_ticker = input("informe o ticker do fundo: ")
            data_pag = input("Informe Data pagamento (Novo): ")

        df_div = oracle.sqlToDataFrame(f"""SELECT ID,TICKER, DATA_PAG FROM DIVIDENDOS  WHERE TICKER = '{div_ticker}' AND DATA_PAG ='{data_pag}'""")
        
        atual_div = self.cadastrar_dividendos(ticker=div_ticker, data_pag=data_pag)

        dict_div = atual_div.__dict__
        aux_dict = {}
        query = (f"UPDATE DIVIDENDOS SET ")

        for inf in dict_div:
                if dict_div[inf] !='':
                    aux_dict.update({inf:dict_div[inf]})
 
        if len(aux_dict) != 0:   
            aux_cont = 1
            aux = len(aux_dict)
            
            for i in aux_dict:
                if aux == 1: # Monta primeira possição somente um registro
                    query += f""" {i} = '{aux_dict[i]}' """
                elif aux != 1 and  aux_cont <= (aux-1): # Monta primeira possição varios registro
                    query += f"""{i} = '{aux_dict[i]}', """
                    aux_cont += 1
                elif aux_cont == aux:
                    query += f""" {i} = '{aux_dict[i]}' """ # Mota ultimo
                    aux_cont += 1
                            
            query += f""" WHERE TICKER ='{atual_div.get_ticker()}' AND ID= '{df_div.id.values[0]}'"""
            oracle.write(query)

            df_div = oracle.sqlToDataFrame(f"""SELECT TICKER, DATA_PAG, COTA_BASE, ULT_DIVID, RENDIMENTO, DIV_YIELD FROM DIVIDENDOS  WHERE TICKER = '{atual_div.get_ticker()}' AND DATA_PAG ='{atual_div.get_data_pag()}'""")
            print("Atualizado!")
            df_div.head()
        else:
            print("Não foi Informado registro para alteração")
        return
    
    def deletar_Dividendos(self):

        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries(can_write=True)
        oracle.connect()

        # Solicita ao usuário o código do fundo a ser alterado
        div_ticker = input("informe o ticker do fundo: ")
        data_pag = input("Informe Data pagamento (Novo): ")
        
        while self.verifica_existencia(oracle, valor=[div_ticker,data_pag], tabela='DIVIDENDOS', coluna=['ID','TICKER','DATA_PAG']):
            div_ticker = input("informe o ticker do fundo: ")
            data_pag = input("Informe Data pagamento (Novo): ")

        df_div = oracle.sqlToDataFrame(f"""SELECT ID, TICKER, DATA_PAG, COTA_BASE, ULT_DIVID, RENDIMENTO, DIV_YIELD FROM DIVIDENDOS  WHERE TICKER = '{div_ticker}' AND DATA_PAG ='{data_pag}'""")

        if not df_div.empty:
            query = f""" DELETE FROM DIVIDENDOS WHERE TICKER = '{df_div.ticker.values[0]}' AND DATA_PAG ='{df_div.data_pag.values[0]}' AND ID='{df_div.id.values[0]}'"""
            oracle.write(query)
        else:
            print("Registro informado Não encontrado")
        return
    
    def cadastrar_dividendos(self, ticker:str='', data_pag:str='') -> Dividendos:
        
        dividendo = Dividendos()
        
        while ticker == '' or data_pag =='':
            ticker = input("Fundos (Novo): ")
            data_pag = input("Informe Data pagamento (Novo): ")

        dividendo.set_ticker(ticker=ticker)
        dividendo.set_data_pag(data_pag=data_pag)
        dividendo.set_div_yield(div_yield= input("Informe Dividend Yield (Novo): "))
        dividendo.set_cota_base(cota_base= input("Informe cotação (Novo): "))
        dividendo.set_rendimento(rendimento= input("Informe Rendimento dividendo (Novo): "))
        dividendo.set_ult_divid(ult_divid= input("Informe porcentagem do Dy.Ult (Novo): "))
        
        return dividendo
    
    def verifica_existencia(self, oracle:OracleQueries, valor:list=None, tabela:str=None, coluna:list=None) -> bool:
            
            if valor != '' and len(valor) == 2:
                df_cliente = oracle.sqlToDataFrame(f"""select {coluna[0]} from {tabela} where {coluna[1]} ='{valor[0]}' AND {coluna[2]} ='{valor[1]}'""")
                return df_cliente.empty
            elif valor !='' and len(valor) ==1:
                df_cliente = oracle.sqlToDataFrame(f"""select {coluna[0]} from {tabela} where {coluna[1]} ='{valor[0]}'""")
                return df_cliente.empty
    