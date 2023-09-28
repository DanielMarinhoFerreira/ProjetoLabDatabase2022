############################################################
#Programa model.Fundos
#AUTOR.......: Daniel Marinho 
#DATA........: 18/10/2022 as 24/09/2023
#DESCRICAO...: class Fundo  
############################################################

class Fundos:
    """
    class de Obj fundos:
    
    """

    def __init__(self, ticker:str, tipo_abbima:str, segmento:str, conta_emit:int, razao_social:str, cnpj:int, nome_pregao:str, prazo_doracao:str, tipo_gestao:str, cnpj_admin:int) -> None:
        self.ticker = ticker        
        self.tipo_abbima = tipo_abbima
        self.segmento = segmento
        self.conta_emit:int = conta_emit
        self.razao_social = razao_social
        self.cnpj:int = cnpj
        self.nome_pregao = nome_pregao
        self.prazo_doracao = prazo_doracao
        self.tipo_gestao:str = tipo_gestao
        self.cnpj_admin:int = cnpj_admin
        
        
    def set_insert(self):
        return f'''
                insert into Fundos values ('{self.get_Ticker}', 
                                        '{self.get_tipo_abbima}',
                                        '{self.get_segmento}',
                                        '{self.get_razao_social}'
                                        '{self.get_cnpj}'
                                        '{self.get_nome_pregao}'
                                        '{self.get_prazo_doracao}'
                                        '{self.get_tipo_gestao}'
                                        '{self.get_cnpl_admin}')")
                '''
        
    def get_Ticker(self):
        return self.ticker

    def get_tipo_abbima(self):
        return self.tipo_abbima
    
    def get_segmento(self):
        return self.segmento
    
    def get_conta_emit(self):
        return self.conta_emit
    
    def get_razao_social(self):
        return self.razao_social
    
    def get_cnpj(self):
        return self.cnpj
    
    def get_nome_pregao(self):
        return self.nome_pregao

    def get_prazo_doracao(self):
        return self.prazo_doracao
    
    def get_tipo_gestao(self):
        return self.tipo_gestao
    
    def get_cnpl_admin(self):
        return self.cnpj_admin
    
    def set_cnpl_admin(self, cnpj):
        self.cnpj_admin = cnpj