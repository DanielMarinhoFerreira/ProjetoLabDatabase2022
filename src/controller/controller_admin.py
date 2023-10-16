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
        
       
        # Solicita CNPJ do administrador 
        admin = input("informe o Cnpj do Administrador: ")
            
        while not admin.isnumeric() or len(admin) > 14 or len(admin) <= 13:
            admin = input("informe o Cnpj do Administrador: ")
       

        if self.verifica_existencia(oracle, valor=admin, tabela='ADMINISTRADORES',coluna=['CNPJ_ADMIN', 'CNPJ_ADMIN']): #Verificar se exista no banco na tabela fondos 
            
            # solicita o restante do cadastro 
            admin = self.cadastrar_admin(cnpj_admin=admin)
            # Inserir o cadastro do Fundo
            oracle.write(admin.get_insert_admin())  
            # Recupera os dados do novo ticker criado transformando em um DataFrame
            df_admin = oracle.sqlToDataFrame(f"select CNPJ_ADMIN, NOME from ADMINISTRADORES where CNPJ_ADMIN = '{admin.get_cnpj_admin()}'")
            print("administrador do CNPJ: "+ str(df_admin.cnpj_admin.values[0]) +" : "+ df_admin.nome.values[0] +" Cadastrdo !")  
        else:
            print(f"Existe Administrador cadastrado com esse CNPJ {admin}")
            return None 
    
    def atualizar_admin(self):
        
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries(can_write=True)
        oracle.connect()

        # Solicita ao usuario o cadastro do Fundo
        admin = input("informe o Cnpj do Administrador: ")
        
        while not admin.isnumeric() or len(admin) > 14 or len(admin) <= 13:
            admin = input("informe o Cnpj do Administrador: ")


        # Verifica se o fundo existe na base de dados
        if not self.verifica_existencia(oracle, admin, tabela='ADMINISTRADORES',coluna=['CNPJ_ADMIN', 'CNPJ_ADMIN']):
            
        
            obj_admin = self.cadastrar_admin(cnpj_admin=admin)

            
            dict_div = obj_admin.__dict__
            aux_dict = {}
            query = (f"UPDATE ADMINISTRADORES SET ")

            for inf in dict_div:
                if dict_div[inf] !='' and inf != 'cnpj_admin':
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
                                
                query += f""" WHERE CNPJ_ADMIN ='{obj_admin.get_cnpj_admin()}'"""
                oracle.write(query)
            
            # Recupera os dados do novo cliente criado transformando em um DataFrame
            df_fundos = oracle.sqlToDataFrame(f"SELECT NOME, TELEFONE, EMAIL,URL_SITE, CNPJ_ADMIN FROM ADMINISTRADORES WHERE CNPJ_ADMIN = '{obj_admin.get_cnpj_admin()}'")
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
        admin = input("informe o Cnpj do Administrador: ")
        
        while not admin.isnumeric() or 14 < len(admin) or 15 <= len(admin):
            admin = input("informe o Cnpj do Administrador: ")
        
        if not self.verifica_existencia(oracle, admin, tabela='ADMINISTRADORES',coluna=['CNPJ_ADMIN', 'CNPJ_ADMIN']):
        
            if not self.verifica_existencia(oracle, admin, tabela='FUNDOS',coluna=['CNPJ_ADMIN', 'ticker']):            
                # Recupera os dados do fundo transformando em um DataFrame
                df_fundo = oracle.sqlToDataFrame(f"SELECT TICKER, CNPJ_ADMIN FROM FUNDOS WHERE CNPJ_ADMIN ='{admin}'")
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

                        oracle.write(f"delete from ADMINISTRADORES WHERE CNPJ_ADMIN ='{admin}'")     
                    else:
                        print("Não é possivel exlcuir Fundo sem excluir a suas cotações e dividendos")
                else:
                    # Se não existir dados nas tabela  COTACOES e DIVIDENDOS o sistema vai perguntar se deseja exluir esse fundo.
                    if "S" == input(f"Tem certezar que deseja excluir fundo: {df_fundo.ticker.values[0]} ? S OU N ").upper():
                        oracle.write(f"delete from FUNDOS WHERE TICKER ='{df_fundo.ticker.values[0]}'")

                        oracle.write(f"delete from ADMINISTRADORES WHERE CNPJ_ADMIN ='{admin}'")
                    else: 
                        print("Não relaizar processo de exclução")
            else: 
                if "S" == input(f"Tem certezar que deseja excluir esse administrador do Cnpj : {admin} ? S OU N ").upper():
                    oracle.write(f"delete from ADMINISTRADORES WHERE CNPJ_ADMIN ='{admin}'")
                else: 
                    print(f"processo de deletção abortado !")
        else:
            print("Não foi encontrado registro desse administrador")
                               
    def cadastrar_admin(self, cnpj_admin:str='') -> Administradores:
        
        admin = Administradores()

        if cnpj_admin == '' or not cnpj_admin.isnumeric():
        
            cnpj_admin = input("cnpj (Novo): ")
            while not cnpj_admin.isnumeric() or len(cnpj_admin) > 14 or len(cnpj_admin) <= 13:
                cnpj_admin = input("cnpj (Novo): ")
                
        admin.set_cnpj(cnpj_admin=cnpj_admin)
        admin.set_nome(nome = input("nome (Novo): "))
        admin.set_telefone(telefone = input("Telefone (Novo): "))
        admin.set_email(email = input("E-mail (Novo): "))
        admin.set_site(url_site = input("Site (Novo): "))
        
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