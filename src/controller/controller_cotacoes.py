from model.Cotacoes import Cotacoes
from connection.oracle_queries import OracleQueries

class Controller_Cotacoes():
    
    def __init__(self):
        pass
    
    def inserir_cotacoes(self) -> None:
        
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries(can_write=True)
        oracle.connect()
        
        # Solicita ao usuario o cadastro do cotacoes
        cotas = self.cadastrar_cotacao()
        
        if self.verifica_existencia(oracle, valor=[{cotas.get_Ticker()},{cotas.get_Mes()}], tabela='COTACOES', coluna=['ID','TICKER','MES']):
            if not self.verifica_existencia(oracle, valor=[{cotas.get_Ticker()}], tabela='FUNDOS', coluna=['TICKER']):

                #Inserir o cadastro do Fundo
                oracle.write(cotas.set_insert())
                
                # Recupera os dados do novo ticker criado transformando em um DataFrame
                df_fundo = oracle.sqlToDataFrame(f"SELECT TICKER, MES FROM TICKER  WHERE TICKER = '{cotas.get_Ticker()}'")
                print(df_fundo.ticker.values[0], df_fundo.nome.values[0])
            else:
                print('Fundo informado não existe!')
        else: 
            print('já existe uma cota cadastrada desse mês')
        return
    
    def atualizar_cotacoes(self):
        
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries(can_write=True)
        oracle.connect()
        
        ticker = input("informe o ticker da cota : ")
        novo_mes = input("informe mês: ")
        
        if not self.verifica_existencia(oracle, valor=[ticker], tabela='FUNDOS', coluna=['TICKER']):
            if not self.verifica_existencia(oracle, valor=[{ticker},{novo_mes}], tabela='COTACOES', coluna=['ID','TICKER','MES']):
                
                novo_mes = input("Mes (Novo):")
                while self.verifica_existencia(oracle, valor=[{ticker},{novo_mes}], tabela='COTACOES', coluna=['ID','TICKER','MES']):
                    novo_mes = input("Mes Já cadastrado (Novo):")
                cota_atual = input("Cota Atual (Novo):")
                
                #Inserir o cadastro do Fundo
                oracle.write(f"UPDATE COTACOES SET MES ='{novo_mes}', CONTA_ATUAL='{cota_atual}' WHERE TICKER ='{ticker}'")
                
                # Recupera os dados do novo ticker criado transformando em um DataFrame
                df_fundo = oracle.sqlToDataFrame(f"SELECT TICKER, MES FROM COTACOES  WHERE TICKER = '{ticker}'")
                print(df_fundo.ticker.values[0], df_fundo.nome.values[0])
            else:
                print('já existe uma cota cadastrada desse mês')
        else: 
            print('Ticker do Fundo informado não existe!')
        return
    
    '''falta realizar deleção'''
    def deletar_cotacoes(self):
        return
    
    def cadastrar_cotacao(self) -> Cotacoes:
        mes:str = ''
        
        ticker = input("Ticker (Novo): ")
        data_cota = input("Data cotação (Novo): ")
        cota_atual = input("Cotação Atual (Novo): ")
        rendimento_atual = input("Rendimento (Novo): ")
        minimo_cota = input("Cota minima (Novo): ")
        maximo_cota = input("Cota maxima (Novo): ")
        abertura = input("Abertura (Novo): ")
        fechamento = input("Ferchamento (Novo): ")
        volume_cotas = input("Valume Cotas (Novo): ")
        
        while mes =='' and mes.isdecimal:
            mes = input("Mês (Novo): ")
            
        cotacao = Cotacoes(ticker=ticker, Data=data_cota, Cota_Atual=cota_atual, rendimento_atual=rendimento_atual, 
                           cota_minimo=minimo_cota, cota_maximo=maximo_cota, mes=mes, fechamento=fechamento, abertura=abertura, volume_cotas=volume_cotas )
        return cotacao 
    
    def verifica_existencia(self, oracle:OracleQueries, valor:list=None, tabela:str=None, coluna:list=None) -> bool:
            
            if valor != '' and len(valor) == 2:
                df_cliente = oracle.sqlToDataFrame(f'''
                                                " 
                                                    select {coluna[0]} 
                                                        from {tabela}
                                                    where {coluna[1]} ='{valor[0]}'
                                                        AND {coluna[2]} ='{valor[1]}' 
                                                "
                                                ''')
                return df_cliente.empty
            elif valor !='' and len(valor) ==1:
                df_cliente = oracle.sqlToDataFrame(f'''
                                                " 
                                                    select {coluna[0]} 
                                                        from {tabela}
                                                    where {coluna[1]} ='{valor[0]}'
                                                "
                                                ''')
                return df_cliente.empty
                