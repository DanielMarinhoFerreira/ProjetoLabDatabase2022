############################################################
#Programa model.dividendos
#AUTOR.......: Daniel Marinho 
#DATA........:  24/09/2023
#DESCRICAO...: class dividendos  
############################################################


class Dividendos:
    
    
    def __init__(self, ticker, data, conta_atual, ult_divid, dy_ult_div, div_acao, div_yield):
        self._ticker = ticker
        self._data = data
        self._conta_atual = conta_atual
        self._ult_divid = ult_divid
        self._dy_ult_div = dy_ult_div
        self._div_acao = div_acao
        self._div_yield = div_yield
        
    def get_ticker(self):
        return self._ticker

    def get_data(self):
        return self._data

    def get_conta_atual(self):
        return self._conta_atual

    def get_ult_divid(self):
        return self._ult_divid

    def get_dy_ult_div(self):
        return self._dy_ult_div

    def get_div_acao(self):
        return self._div_acao

    def get_div_yield(self):
        return self._div_yield   

        
