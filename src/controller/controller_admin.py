from model.Administradores import Administradores 
from connection.oracle_queries import OracleQueries
from time import sleep

class Controller_Admin():
    
    def __init__(self):
        pass

    def inserir_admin(self) -> None:

        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries(can_write=True)
        oracle.connect()
        
        # Solicita ao usuario o cadastro do Fundo
        admin = self.cadastrar_admin()

        if self.verifica_existencia(oracle, admin.get_cnpj(), tabela='ADMINISTRADORES',coluna=['CNPJ', 'CNPJ']): #Verificar se exista no banco na tabela fondos 
        
            #Inserir o cadastro do Fundo
            oracle.write(admin.set_insert())
                
            # Recupera os dados do novo ticker criado transformando em um DataFrame
            df_admin = oracle.sqlToDataFrame(f"select CNPJ, NOME from ADMINISTRADORES where CNPJ = '{admin.get_cnpj()}'")
            print("administrador do CNPJ: "+ df_admin.cnpj.values[0] +" : "+ df_admin.nome.values[0] +" Cadastrdo !")  
        else:
            print(f"O ticker: {df_admin.get_Ticker()} desse fundo já está cadastrado.")
            return None 
    
    def atualizar_admin(self):
        
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries(can_write=True)
        oracle.connect()

        # Solicita ao usuário o código do fundo a ser alterado
        admin = self.cadastrar_admin()

        # Verifica se o fundo existe na base de dados
        if not self.verifica_existencia(oracle, admin.get_cnpj(), tabela='ADMINISTRADORES',coluna=['CNPJ', 'CNPJ']):
            
            # Atualiza todos 
            if not admin.get_email() and admin.get_nome() and admin.get_site() and admin.get_telefone():
                oracle.write(f"UPDATE ADMINISTRADORES SET NOME='{admin.get_nome()}',TELEFONE='{admin.get_telefone()}',EMAIL='{admin.get_email()}',URL_TELEFONE='{admin.get_site}' WHERE CNPJ ='{admin.get_cnpj()}'")
            # Atualiza menos Email 
            elif admin.get_email() =='' and admin.get_nome() !='' and admin.get_site() !='' and admin.get_telefone() !='':
                oracle.write(f"UPDATE ADMINISTRADORES SET NOME='{admin.get_nome()}',TELEFONE='{admin.get_telefone()}',URL_TELEFONE='{admin.get_site}' WHERE CNPJ ='{admin.get_cnpj()}'")
            # Atualiza menos Email e NOME
            elif admin.get_email() =='' and admin.get_nome() =='' and admin.get_site() !='' and admin.get_telefone() !='':
                oracle.write(f"UPDATE ADMINISTRADORES SET TELEFONE='{admin.get_telefone()}',URL_TELEFONE='{admin.get_site}' WHERE CNPJ ='{admin.get_cnpj()}'")
            # Atualiza menos Email e NOME e SITE
            elif admin.get_email() =='' and admin.get_nome() =='' and admin.get_site() =='' and admin.get_telefone() !='':
                oracle.write(f"UPDATE ADMINISTRADORES SET TELEFONE='{admin.get_telefone()}' WHERE CNPJ ='{admin.get_cnpj()}'")
            
            # Recupera os dados do novo cliente criado transformando em um DataFrame
            df_fundos = oracle.sqlToDataFrame(f"SELECT NOME, TELEFONE, EMAIL,URL_SITE, CNPJ FROM ADMINISTRADORES WHERE CNPJ = '{admin.get_cnpj()}'")
            # Cria um novo objeto cliente
            print(df_fundos.head())
            admin.__delattr__
        else:
            print(f"O Cnpj {admin._cnpj} do Administrador informado não existe.")
            return None
        return
    
    '''Falta fazer '''
    def deletar_admin(self):
        return   

    def cadastrar_admin(self) -> Administradores:
        nome = input("nome (Novo): ")
        telefone = input("Telefone (Novo): ")
        email = input("E-mail (Novo): ")
        site = input("Site (Novo): ")
        cnpj = input("Cnpj (Novo): ")
        
        sleep(1) #ms
        cnpj = input("cnpj (Novo): ")
        while (len(cnpj) < 14):
            cnpj = input("cnpj (Novo): ")

        admin = Administradores(nome=nome, telefone=telefone, email=email, site=site, cnpj=cnpj)
        return admin
    
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
        df_cliente = oracle.sqlToDataFrame(f"""select {coluna[1]} from {tabela} where {coluna[0]} = '{valor}'""")
        return df_cliente.empty