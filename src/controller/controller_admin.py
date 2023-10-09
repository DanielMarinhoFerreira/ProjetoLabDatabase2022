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

        # Solicita ao usuario o cadastro do Fundo
        admin = int(input("informe o Cnpj do Administrador: "))
        
        while 14 < admin or 15 >= admin or not admin.isnumeric():
            admin = int(input("informe o Cnpj do Administrador: "))


        # Verifica se o fundo existe na base de dados
        if not self.verifica_existencia(oracle, admin_cnpj.get_cnpj(), tabela='ADMINISTRADORES',coluna=['CNPJ', 'CNPJ']):
            
            admin_cnpj = Administradores()
            admin_cnpj.set_cnpj(clAd=admin_cnpj)
            admin = self.cadastrar_admin()

            
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
    
    
    def deletar_admin(self):
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries(can_write=True)
        oracle.connect()
        
        # Solicita ao usuario o cadastro do Fundo
        admin = int(input("informe o Cnpj do Administrador: "))
        
        while 14 < len(admin) or 15 >= len(admin) or not admin.isnumeric():
            admin = int(input("informe o Cnpj do Administrador: "))
        
        if not self.verifica_existencia(oracle, admin, tabela='ADMINISTRADORES',coluna=['CNPJ', 'CNPJ']):
        
            if not self.verifica_existencia(oracle, admin, tabela='FUNDOS',coluna=['CNPJ_ADMIN', 'ticker']):            
                # Recupera os dados do fundo transformando em um DataFrame
                df_fundo = oracle.sqlToDataFrame(f"SELECT TOCKER, CNPJ_ADMIN FROM FUNDOS WHERE CNPJ_ADMIN ='{admin}'")
                # Verificar se existe registro desse fundos na tabela cotações e dividendos
                if not self.verifica_existencia(oracle, df_fundo.ticker.values[0], tabela='COTACOES',coluna=['ticker', 'id']) and not self.verifica_existencia(oracle, df_fundo.ticker.values[0], tabela='DIVIDENDOS',coluna=['ticker', 'id']):
                
                    if "S" == input(f"Tem certezar que deseja excluir registro das cotações e dividandos desse fundo: {df_fundo.ticker.values[0]} ? S OU N").upper():
                        # Recupera os dados do COTACOES transformando em um DataFrame
                        df_cotas_fundo = oracle.sqlToDataFrame(f"SELECT ticker, id FROM COTACOES WHERE TICKER ='{df_fundo.ticker.values[0]}'")
                        # Recupera os dados do DIVIDENDOS transformando em um DataFrame
                        df_dividendos_fundos = oracle.sqlToDataFrame(f"SELECT ticker, id FROM DIVIDENDOS WHERE TICKER ='{df_fundo.ticker.values[0]}'")

                        for cota in df_cotas_fundo.size():
                            # deleta os registro da tebala COTACOES referente ao fundo 
                            ret = oracle.write(f"delete from COTACOES WHERE ID ='{cota.id.values()}'")
                            print(ret)        
                        for dividendo in df_dividendos_fundos.size():
                            # deleta os registro da tebala COTACOES referente ao fundo 
                            ret = oracle.write(f"delete from DIVIDENDOS WHERE ID ='{dividendo.id.values()}'")         
                    else:
                        print("Não é possivel exlcuir Fundo sem excluir a suas cotações e dividendos")
                else:
                    # Se não existir dados nas tabela  COTACOES e DIVIDENDOS o sistema vai perguntar se deseja exluir esse fundo.
                    if "S" == input(f"Tem certezar que deseja excluir fundo: {df_fundo.ticker.values[0]} ? S OU N").upper():
                        oracle.write(f"delete from FUNDOS WHERE TICKER ='{cota.id.values()}'")
                    else: 
                        print("Não relaizar processo de exclução")
            else: 
                if "S" == input(f"Tem certezar que deseja excluir esse administrador do Cnpj : {admin} ? S OU N").upper():
                    dl_admin = oracle.write(f"delete from ADMINISTRADORES WHERE CNPJ ='{admin}'")
                else: 
                    print(f"processo de deletção abortado !")
        else:
            print("Não foi encontrado registro desse administrador")
                               
    def cadastrar_admin(self, clAd:Administradores) -> Administradores:
        

        if clAd.admin.get_cnpj() != '':
            clAd.admin.set_nome(nome = input("nome (Novo): "))
            clAd.admin.set_nome(telefone = input("Telefone (Novo): "))
            clAd.admin.set_nome(adminemail = input("E-mail (Novo): "))
            clAd.admin.set_site(site = input("Site (Novo): "))
            return None
        else:
            admin = Administradores()
            sleep(1) #ms
            cnpj = input("cnpj (Novo): ")
            while len(cnpj) < 14 or not cnpj.isnumeric():
                cnpj = input("cnpj (Novo): ")

            admin.get_cnpj(cnpj=cnpj)
            admin.set_nome(nome = input("nome (Novo): "))
            admin.set_nome(telefone = input("Telefone (Novo): "))
            admin.set_nome(adminemail = input("E-mail (Novo): "))
            admin.set_site(site = input("Site (Novo): "))

        return admin 
    
    def verifica_existencia(self, oracle:OracleQueries, valor:str=None, tabela:str=None, coluna:list=None) -> bool:
        '''
            Recupera os dados de uma tabela.
            seguindo a instrução:
            fundos: string -> valor de pesquisa
            tabela: string -> tabela de pesquisa 
            coluna: dict  -> colunas das tabela e seguencia
            exemplo:
                    select coluna[1]
                        from tabela 
                        where coluna[0] = fundos  
        
        '''
        df_cliente = oracle.sqlToDataFrame(f"""select {coluna[1]} from {tabela} where {coluna[0]} = '{valor}'""")
        return df_cliente.empty