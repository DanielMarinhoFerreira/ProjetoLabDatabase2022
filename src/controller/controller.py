from model.Fundos import Fundos
from model.Administradores import Administradores 
from model.Cotacoes import Cotacoes
from model.dividendos import Dividendos
from connection.oracle_queries import OracleQueries
from time import sleep

class Controller_fundos:
    def __init__(self):
        pass

    def inserir_fundos(self) -> None:
        ''' Ref.: https://cx-oracle.readthedocs.io/en/latest/user_guide/plsql_execution.html#anonymous-pl-sql-blocks'''
        
        contin = ''
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries(can_write=True)
        oracle.connect()
        
        # Solicita ao usuario o cadastro do Fundo
        fundo = self.cadastro_fundo()

        if self.verifica_existencia(oracle, fundo.get_Ticker(), tabela='FUNDOS',coluna=['ticker', 'ticker']): #Verificar se exista no banco na tabela fondos 
            
            if not self.verifica_existencia(oracle, valor=fundo.get_cnpl_admin(), tabela="ADMINISTRADORES", coluna=['CNPJ','CNPJ']):
                #Inserir o cadastro do Fundo
                oracle.write(fundo.set_insert())
                
                # Recupera os dados do novo ticker criado transformando em um DataFrame
                df_fundo = oracle.sqlToDataFrame(f"select ticker, nome from ticker where ticker = '{fundo.get_Ticker()}'")
                print(df_fundo.ticker.values[0], df_fundo.nome.values[0])
            else:
                contin = input("Administrador não cadastrado, deseja cadastrar administrador ? Digite S ou N")
                
                while contin.upper != 'S' or contin.upper !='N':
                     contin = input("Informe um valor valido. Digite S ou N : ")
                     
                if contin.upper != 'S':
                    print("serar finalizado sem realizar o cadastro do fundo")
                else:
                    admin = self.cadastrar_admin()
                    if not self.verifica_existencia(oracle, valor=admin.get_cnpj(), tabela="ADMINISTRADORES", coluna=['CNPJ','CNPJ']):
                        #Inserir o cadastro do admin
                        oracle.write(admin.set_insert()) 
                        
                        # Recupera os dados do novo admin criado transformando em um DataFrame
                        df_admin = oracle.sqlToDataFrame(f"SELECT CNPJ FROM ADMINISTRADORES WHERE CNPJ='{admin.get_cnpj()}'")
                        print(df_admin.cnpj.values[0])
                        
                        #Alterar CNJ do admin no Fundo 
                        fundo.set_cnpl_admin(admin.get_cnpj())
                        
                        #Inserir o cadastro do Fundo
                        oracle.write(admin.set_insert())
                        
                        # Recupera os dados do novo ticker criado transformando em um DataFrame
                        df_fundo = oracle.sqlToDataFrame(f"select ticker, nome from ticker where ticker = '{fundo.get_Ticker()}'")
                        print(df_fundo.ticker.values[0], df_fundo.nome.values[0])
                    else:
                        print("Erro na verificação da existencia do cadastro admin")
        else:
            print(f"O ticker: {fundo.get_Ticker()} desse fundo já está cadastrado.")
            return None 
        
    def atualizar_fundos(self) -> None:
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries(can_write=True)
        oracle.connect()

        # Solicita ao usuário o código do fundo a ser alterado
        ticker = int(input("informe o ticker do fundo: "))

        # Verifica se o fundo existe na base de dados
        if not self.verifica_existencia(oracle, ticker, tabela='FUNDOS',coluna=['ticker', 'ticker']):
            # Solicita a nova descrição do cliente
            novo_segmento = input("Segmento (Novo): ")
            # Atualiza o nome do cliente existente
            oracle.write(f"UPDATE FUNDOS SET SEGMENTO ='{novo_segmento}' WHERE TICKER ='{ticker}'")
            # Recupera os dados do novo cliente criado transformando em um DataFrame
            df_fundos = oracle.sqlToDataFrame(f" SELECT TICKER, SEGMENTO FROM FUNDOS WHERE TICKER = '{ticker}'")
            # Cria um novo objeto cliente
            print(df_fundos.ticker.values[0], df_fundos.nome.values[0])
        else:
            print(f"O ticker do fundos {ticker} não existe.")
            return None
    
    # Realizar cadastro do fundo 
    def cadastro_fundo(self) -> Fundos:
            ticker = input("Fundos (Novo): ")
            tipo_abbima = input("tipo_abbima (Novo): ")
            segmento = input("segmento (Novo): ")
            conta_emit = input("conta emitidas (Novo): ")
            razao_social = input("razão social (Novo): ")
            
            sleep(1) #ms
            cnpj = input("cnpj (Novo): ")
            while (len(cnpj) < 14):
                cnpj = input("cnpj (Novo): ")
                
            nome_pregao = input("nome pregão (Novo): ")
            prazo_doracao = input("prazo doracao (Novo): ")
            tipo_gestao = input("tipo gestao (Novo): ")
            cnpj_admin = input("cnpj administrador do fundo (Novo): ")
            
            fundos = Fundos(ticker=ticker, tipo_abbima=tipo_abbima, segmento=segmento, conta_emit=conta_emit, razao_social=razao_social, cnpj=cnpj, 
                                nome_pregao= nome_pregao, prazo_doracao=prazo_doracao, tipo_gestao=tipo_gestao, cnpj_admin=cnpj_admin)
            
            return fundos
    
    '''Criar class para esses cadastro'''
    def cadastrar_admin(self) -> Administradores:
        nome = input("nome (Novo): ")
        telefone = input("Telefone (Novo): ")
        email = input("E-mail (Novo): ")
        site = input("Site (Novo): ")
        cnpj = input("Cnpj (Novo): ")
        admin = Administradores(nome=nome, telefone=telefone, email=email, site=site, cnpj=cnpj)
        return admin
    
    def cadastrar_cotacao(self) -> Cotacoes:
        ticker = input("Ticker (Novo): ")
        data_cota = input("Data cotação (Novo): ")
        cota_atual = input("Cotação Atual (Novo): ")
        rendimento_atual = input("Rendimento (Novo): ")
        minimo_cota = input("Cota minima (Novo): ")
        maximo_cota = input("Cota maxima (Novo): ")
        abertura = input("Abertura (Novo): ")
        fechamento = input("Ferchamento (Novo): ")
        volume_cotas = input("Valume Cotas (Novo): ")
        mes = input("Mês (Novo): ")
        cotacao = Cotacoes(ticker=ticker, Data=data_cota, Cota_Atual=cota_atual, rendimento_atual=rendimento_atual, cota_minimo=minimo_cota, cota_maximo=maximo_cota, mes=mes)
        return cotacao 
    
    def cadastrar_dividendos() -> Dividendos:
        
        return
    
    '''Terminar de criar codigo de excluir fundo'''
    def excluir_fundos(self):
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries(can_write=True)
        oracle.connect()
        
        # Solicita ao usuário o código do fundo a ser alterado
        ticker = int(input("informe o ticker do fundo: "))
        
        # Verifica se o cliente existe na base de dados
        if not self.verifica_existencia_fundos(oracle, ticker):            
            # Recupera os dados do novo cliente criado transformando em um DataFrame
            df_cliente = oracle.sqlToDataFrame(f"select ticker, nome from fundos where ticker = {ticker}")
            # Revome o cliente da tabela
            oracle.write(f"delete from fundos where ticker = {ticker}")   
            oracle.white(f"delete from empreendimento where = {ticker}")
            # Cria um novo objeto Cliente para informar que foi removido
            fundo_excluido = Fundo(df_cliente.ticker.values[0], df_cliente.nome.values[0])
            # Exibe os atributos do cliente excluído
            print("Cliente Removido com Sucesso!")
            print(fundo_excluido.toString())
        else:
            print(f"O ticker do fundo {ticker} não existe.")

    def verifica_existencia(self, oracle:OracleQueries, valor:str=None, tabela:str=None, coluna:list=None) -> bool:
        '''
            Recupera os dados de uma tabela.
            seguindo a instrução:
            fundos: string -> valor de pesquisa
            tabela: string -> tabela de pesquisa 
            coluna: dict  -> colunas das tabela e seguencia
            exemplo:
                    select coluna[0]
                        from tabela 
                        where coluna[1] = fundos  
        
        '''
        df_cliente = oracle.sqlToDataFrame(f'''
                                           " 
                                            select {tabela} 
                                                from {coluna[1]}
                                            where {coluna[0]} = {valor}
                                           "
                                           ''')
        return df_cliente.empty