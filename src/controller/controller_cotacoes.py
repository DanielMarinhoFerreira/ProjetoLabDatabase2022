from model.Cotacoes import Cotacoes
from connection.oracle_queries import OracleQueries

class Controller_Cotacoes():
    
    def __init__(self):
        pass
    
    def inserir_cotacoes(self) -> None:
        
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries(can_write=True)
        oracle.connect()
        
        # Solicita ao usuário o código do fundo a ser alterado
        ticker = input("informe o ticker do fundo: ")
        while self.verifica_existencia(oracle, valor=[ticker], tabela='FUNDOS', coluna=['TICKER','TICKER']):
            ticker = input("informe o ticker do fundo: ")
        
        # Solicita ao usuario o cadastro do cotacoes
        cota = self.cadastrar_cotacao(ticker=ticker)

        if self.verifica_existencia(oracle, valor=[cota.get_ticker(),cota.get_mes()], tabela='COTACOES', coluna=['ID','TICKER','MES']):
            
            #Inserir o cadastro do Fundo
            oracle.write(cota.set_insert())
                
            # Recupera os dados do novo ticker criado transformando em um DataFrame
            df_fundo = oracle.sqlToDataFrame(f"SELECT TICKER, MES FROM COTACOES  WHERE TICKER = '{cota.get_ticker()}' AND MES ='{cota.get_mes()}'")
            print(df_fundo.ticker.values[0], df_fundo.mes.values[0])
        else: 
            print('já existe uma cota cadastrada desse mês')
        return
    
    def atualizar_cotacoes(self):
        
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries(can_write=True)
        oracle.connect()
        
        # Solicita ao usuário o código do fundo a ser alterado
        ticker = input("informe o ticker do fundo: ")
        mes = input("informe mês: ")
        while self.verifica_existencia(oracle, valor=[ticker, mes], tabela='COTACOES', coluna=['ID','TICKER','MES']):
            ticker = input("informe o ticker do fundo: ")
            mes = input("informe mês: ")
        
        df_cota = oracle.sqlToDataFrame(f"select ID, TICKER, MES FROM COTACOES WHERE MES ='{mes}' AND TICKER='{ticker}'")
        
        if not df_cota.empty:
            
            cotacao = Cotacoes()
            cotacao.set_cota_atual(cota_atual = input("Cotação Atual (Novo): "))
            cotacao.set_rendimento_atual(rendimento = input("Rendimento (Novo): "))
            cotacao.set_minimo(minimo_cota = input("Cota minima (Novo): "))
            cotacao.set_maximo(maximo_cota= input("Cota maxima (Novo): "))
            cotacao.set_abertura(abertura= input("Abertura (Novo): "))
            cotacao.set_volume_cotas(volume_cotas= input("Valume Cotas (Novo): "))
            cotacao.set_p_vp(p_vp= input("P_VP (Novo): "))

            dict_cota = cotacao.__dict__
            aux_dict = {}
            query = (f"UPDATE COTACOES SET ")
           
            for inf in dict_cota:
                if dict_cota[inf] !='':
                    aux_dict.update({inf:dict_cota[inf]})
            
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
                            

                query += f""" WHERE TICKER ='{ticker}' AND ID= '{df_cota.id.values[0]}'"""
                oracle.write(query)
            else:
                print("Não foi informado informações pra alteração")    
        else: 
            print('Ticker do Fundo informado não existe!')
        return
    
    '''falta realizar deleção'''
    def deletar_cotacoes(self):
        
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries(can_write=True)
        oracle.connect()
        
        # Solicita ao usuário o código do fundo a ser alterado
        ticker = input("informe o ticker do fundo: ")
        mes = input("informe mês: ")
        while self.verifica_existencia(oracle, valor=[ticker, mes], tabela='COTACOES', coluna=['ID','TICKER','MES']):
            ticker = input("informe o ticker do fundo: ")
            mes = input("informe mês: ")
        
        df_cota = oracle.sqlToDataFrame(f"select ID, TICKER, MES COTACOES FROM WHERE MES ='{mes}' AND TICKER='{ticker}'")

        if not df_cota.empty:

            #Inserir o cadastro do Fundo
            oracle.write(f"DELETE FROM COTACOES WHERE TICKER ='{ticker}' AND ID= '{df_cota.id.values[0]}'")

        return
    
    def cadastrar_cotacao(self, ticker:str='') -> Cotacoes:
        mes:str = ''
        cotacao = Cotacoes()

         # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries(can_write=True)
        oracle.connect()
        
        if ticker == '':
            ticker = input("Ticker (Novo): ")
            while self.verifica_existencia(oracle, valor=[ticker], tabela='FUNDOS', coluna=['TICKER','TICKER']):
                ticker = input("informe o ticker do fundo: ")
        
        cotacao.set_ticker(ticker)
        cotacao.set_data_cota(data_atual = input("Data cotação (Novo): "))
        cotacao.set_cota_atual(cota_atual = input("Cotação Atual (Novo): "))
        cotacao.set_rendimento_atual(rendimento = input("Rendimento (Novo): "))
        cotacao.set_minimo(cota_minima= input("Cota minima (Novo): "))
        cotacao.set_maximo(cota_maxima= input("Cota maxima (Novo): "))
        cotacao.set_abertura(abertura= input("Abertura (Novo): "))
        cotacao.set_volume_cotas(volume_cotas= input("Valume Cotas (Novo): "))
        
        mes= input("Mês cotação (Novo): ")
        
        while not self.verifica_existencia(oracle, valor=[cotacao.get_ticker(),mes], tabela='COTACOES', coluna=['ID','TICKER','MES']):
            mes = input("Mês cotação (Novo): ")

        cotacao.set_mes(mes)
        cotacao.set_p_vp(p_vp= input("P_VP (Novo): "))
  
        return cotacao 
    
    def verifica_existencia(self, oracle:OracleQueries, valor:list=None, tabela:str=None, coluna:list=None) -> bool:
            
            if valor != '' and len(valor) == 2:
                df_cliente = oracle.sqlToDataFrame(f"""select {coluna[0]} from {tabela} where {coluna[1]} ='{valor[0]}' AND {coluna[2]} ='{valor[1]}'""")
                return df_cliente.empty
            elif valor !='' and len(valor) ==1:
                df_cliente = oracle.sqlToDataFrame(f"""select {coluna[0]} from {tabela} where {coluna[1]} ='{valor[0]}'""")
                return df_cliente.empty
                