from datetime import time
from model.fundos import Fundos

############################################################
#Programa model.Cotacoes
#AUTOR.......: Daniel Marinho 
#DATA........: 18/10/2022 24/09/2023
#DESCRICAO...: class Cotacao  
############################################################

class Cotacoes():


    def __init__(self, ticker:str, Data:str, Cota_Atual:int, fechamento:int, abertura:int,volume_cotas:int, 
                       cota_minimo:int, cota_maximo:int, valorizacao:int, mes:time, rendimento_atual:str)  -> None:
        self._ticker = ticker
        self._Data = Data
        self._Cota_Atual = Cota_Atual
        self._cota_minimo = cota_minimo
        self._cota_maximo = cota_maximo
        self._valorizacao = valorizacao
        self._fechamento = fechamento
        self._abertura = abertura
        self._volume_cotas = volume_cotas
        self._mes:time = mes
        self._rendimento_atual = rendimento_atual

    def get_Ticker(self):
        return self._ticker

    def get_Abertura(self) -> int:
        return self._abertura

    def get_Fechamento(self):
        return self._fechamento

    def get_Minimo(self):
        return self._cota_minimo

    def get_Maximo(self):
        return self._cota_maximo
    
    def get_Volume_Cotas(self):
        return self._volume_cotas

    def get_Mes(self):
        return self._mes