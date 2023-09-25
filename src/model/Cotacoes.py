from datetime import time
from model.fundos import Fundo

############################################################
#Programa model.Cotacoes
#AUTOR.......: Daniel Marinho 
#DATA........: 18/10/2022 24/09/2023
#DESCRICAO...: class Cotacao  
############################################################

class Cotacoes():

    def __init__(self, ticker:str, Data:str, Cota_Atual:int, fechamento:int, 
                       cota_minimo:int, cota_maximo:int, valorizacao:int, mes:time, rendimento_atual:str)  -> None:
        self._ticker = ticker
        self._Data = Data
        self._Cota_Atual = Cota_Atual
        self._cota_minimo = cota_minimo
        self._cota_maximo = cota_maximo
        self._valorizacao = valorizacao
        self._mes:time = mes
        self._rendimento_atual = rendimento_atual


    def get_Abertura(self) -> int:
        return self.abertura

    def get_Fechamento(self):
        return self.fechamento

    def get_Minimo(self):
        return self.minimo

    def get_Maximo(self):
        return self.maximo
    
    def get_Volume_Cotas(self):
        return self.volume_cotas

    def get_Mes(self):
        return self.mes
    
    def set_Fundo(self, fundo:Fundo) -> Fundo:
        self.fundo = fundo
    
    def set_Abertura(self, abertura):
        self.abertura = abertura

    def set_Fechamento(self, fechamento):
        self.fechamento = fechamento

    def set_Minimo(self, minimo):
        self.minimo = minimo

    def set_Maximo (self, maximo):
        self.maximo = maximo 

    def set_Volume_Cotas(self, volume_cotas):
        self.volume_cotas = volume_cotas

    def set_Mes(self, mes):
        self.mes = mes