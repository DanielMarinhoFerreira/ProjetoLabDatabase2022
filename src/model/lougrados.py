from Empreendimentos import Empreendimento

############################################################
#Programa model.Emderecos
#AUTOR.......: Daniel Marinho 
#DATA........: 18/10/2022
#DESCRICAO...: class enderecos 
############################################################

class Endreco():

    def __init__(self, empreendimento:Empreendimento, endereco:str=None, bairro:str=None, cidade:str=None, area_bruta:float[9:3]=None) -> None:
        self.set_Empreendimento(empreendimento) #Class Empreendimento
        self.set_Endereco(endereco)
        self.set_Bairro(bairro)
        self.set_Cidade(cidade) 
        self.set_Area_Bruta(area_bruta)
        

    def get_Empreendimento(self) -> Empreendimento: #Class Empreendimento
        return self.empreendimento

    def get_Endereco(self):
        return self.endereco

    def get_Bairro(self):
        return self.bairro

    def get_Cidade(self):
        return self.cidade
    
    def get_Area_Bruta(self):
        return self.area_bruta

    def set_Empreendimento(self, empreendimento:Empreendimento)-> Empreendimento: #Class Empreendimento
        self.empreendimento = empreendimento

    def set_Endereco(self, endereco):
        self.endereco = endereco

    def set_Bairro(self, bairro):
        self.bairro = bairro

    def set_Cidade(self, cidade):
        self.cidade = cidade
    
    def set_Area_Bruta(self, area_bruta):
        self.area_bruta = area_bruta

    def toString(self):
        return f'Empreendimento: {self.empreendimento} Endereço {self.endereco} Bairro {self.bairro} Cidade: {self.cidade} Area Bruta: {self.area_bruta}'