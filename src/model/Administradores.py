############################################################
#Programa model.Administradores
#AUTOR.......: Daniel Marinho 
#DATA........: 24/09/2023
#DESCRICAO...: class Administradores  
############################################################


class Administradores:
    
    def __init__(self, nome:str='', telefone:str='', email:str='', site:str='', cnpj:str=''):
        self._nome = nome 
        self._telefone = telefone
        self._email = email
        self._site = site
        self._cnpj = cnpj

    #(NOME, TELEFONE, EMAIL,URL_SITE, CNPJ_ADMIN)
    def set_insert_admin(self):
        admin_insert = f"""insert into ADMINISTRADORES (NOME, TELEFONE, EMAIL, URL_SITE, CNPJ_ADMIN) values ('{self._nome}','{self._telefone}','{self._email}','{self._site}','{self._cnpj}')"""
        return  admin_insert
    
    def get_nome(self):
        return self._nome
    
    def get_telefone(self):
        return self._telefone
    
    def get_email(self):
        return self._email
        
    def get_site(self):
        return self._site
    
    def get_cnpj(self):
        return self._cnpj
    
    def set_nome(self, nome):
        self._nome = nome
    
    def set_telefone(self,telefone):
        self._telefone = telefone
    
    def set_email(self,  email):
        self._email = email
        
    def set_site(self, site):
        self._site = site 
    
    def set_cnpj(self, cnpj):
        self._cnpj = cnpj            
            