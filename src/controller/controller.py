from model.fundos import Fundos
from connection.oracle_queries import OracleQueries

class Controller_fundos:
    def __init__(self):
        pass
        
    def inserir_fundos(self) -> None:
        ''' Ref.: https://cx-oracle.readthedocs.io/en/latest/user_guide/plsql_execution.html#anonymous-pl-sql-blocks'''
        
        contin = ''
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries(can_write=True)
        oracle.connect()

        # Informa um novo Fundo 
        ticker = input("Fundos (Novo): ")

        if self.verifica_existencia(oracle, ticker, tabela='fundos',coluna=['ticker', 'ticker']): #Verificar se exista no banco na tabela fondos 
            # Solicita ao usuario o novo nome
            tipo_abbima = input("tipo_abbima (Novo): ")
            segmento = input("segmento (Novo): ")
            conta_emit = input("conta emitidas (Novo): ")
            razao_social = input("razão social (Novo): ")
            
            cnpj = input("cnpj (Novo): ")
            while (len(cnpj) < 14):
                cnpj = input("cnpj (Novo): ")
                
            nome_pregao = input("nome pregão (Novo): ")
            prazo_doracao = input("prazo doracao (Novo): ")
            tipo_gestao = input("tipo gestao (Novo): ")
            
            cnpj_admin = input("cnpj administrador do fundo (Novo): ")
            if self.verifica_existencia_fundos(oracle, tabela=cnpj_admin, coluna=['cnpj','cnpj']):
                fundos = Fundos(ticker=ticker, tipo_abbima=tipo_abbima, segmento=segmento, conta_emit=conta_emit, razao_social=razao_social, cnpj=cnpj, 
                                nome_pregao= nome_pregao, prazo_doracao=prazo_doracao, tipo_gestao=tipo_gestao, cnpj_admin=cnpj_admin)
                
                # Insere e persiste o novo cliente
                oracle.write(fundos.set_insert())
                
                # Recupera os dados do novo cliente criado transformando em um DataFrame
                df_fundo = oracle.sqlToDataFrame(f"select ticker, nome from ticker where ticker = '{ticker}'")
                
                print(df_fundo.ticker.values[0], df_fundo.nome.values[0])
            else:
                contin = input("Administrador não cadastrado, deseja cadastrar mesmo assim ? Digite S ou N")
                if contin.upper != 'S':
                    contin = input("Tem certeza de não deseja continuar ? Digite S ou N")
                    if contin.upper == 'S':
                        fundos = Fundos(ticker=ticker, tipo_abbima=tipo_abbima, segmento=segmento, conta_emit=conta_emit, razao_social=razao_social, cnpj=cnpj, 
                                nome_pregao= nome_pregao, prazo_doracao=prazo_doracao, tipo_gestao=tipo_gestao)
                        oracle.write(fundos.set_insert())
                else:
                    # chama classe de cadastro do administrador 
                    print("chama class adminstrador")     
        else:
            print(f"O ticker: {ticker} desse fundo já está cadastrado.")
            return None

    def atualizar_fundos(self) -> None:
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries(can_write=True)
        oracle.connect()

        # Solicita ao usuário o código do fundo a ser alterado
        ticker = int(input("informe o ticker do fundo: "))

        # Verifica se o fundo existe na base de dados
        if not self.verifica_existencia_fundos(oracle, ticker):
            # Solicita a nova descrição do cliente
            novo_nome = input("Nome (Novo): ")
            # Atualiza o nome do cliente existente
            oracle.write(f"update fundo set nome = '{novo_nome}' where ticker = {ticker}")
            # Recupera os dados do novo cliente criado transformando em um DataFrame
            df_fundos = oracle.sqlToDataFrame(f"select ticker, nome from fundos where ticker = {ticker}")
            # Cria um novo objeto cliente
            nome_fundos_atualizado = Fundo(df_fundos.ticker.values[0], df_fundos.nome.values[0])
            # Exibe os atributos do novo cliente
            print(nome_fundos_atualizado.toString())
            # Retorna o objeto cliente_atualizado para utilização posterior, caso necessário
            return nome_fundos_atualizado
        else:
            print(f"O ticker do fundos {ticker} não existe.")
            return None

    def excluir_fundos(self):
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries(can_write=True)
        oracle.connect()

        # Solicita ao usuário o CPF do Cliente a ser alterado
        ticker = int(input("ticker do fundo que irá excluir: "))        

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