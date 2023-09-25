############################################################
#Programa model.Administradores
#AUTOR.......: Daniel Marinho 
#DATA........: 24/09/2023
#DESCRICAO...: class Administradores  
############################################################


class Administradores:
    
    def __init__(self, nome, telefone, email, site, cnpj):
        self._nome = nome 
        self._telefone = telefone
        self._email = email
        self._site = site
        self._cnpj = cnpj
        
        
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
    
    def set_cnpj(self, cnpj):
        self._cnpj = cnpj            
            