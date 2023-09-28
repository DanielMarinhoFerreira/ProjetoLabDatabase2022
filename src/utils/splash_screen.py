from connection.oracle_queries import OracleQueries

class SplashScreen:

    def __init__(self):
        self.created_by = 'DANIEL MARINHO FERREIRA DE SOUZA,EMANUEL SIQUEIRA LANNES' 
        self.created_by2 = 'ERICK ANTONIO PIMENTEL MERCADO, GABRIEL VASCONCELOS SANTOS e VITOR DORNELA MASCARENHAS'
        self.professor = "Prof. M.Sc. Howard Roatti"
        self.disciplina = "Banco de Dados"
        self.semestre = "2023/2"
        self.oracle = OracleQueries()

    def get_total_fundos(self):
        orac = self.oracle
        orac.connect()
        return orac.sqlToDataFrame('select count(1) as total_fundos from FUNDOS')["total_fundos"].values[0]

    def get_total_admin(self):
        orac = self.oracle
        orac.connect()
        return orac.sqlToDataFrame('select count(1) as total_admin from Administradores')["total_admin"].values[0]

    def get_total_cotacoes(self):
        orac = self.oracle
        orac.connect()
        return orac.sqlToDataFrame('select count(1) as total_contas from Cotacoes')["total_contas"].values[0]
    
    def get_total_Dividendos(self):
        orac = self.oracle
        orac.connect()
        return orac.sqlToDataFrame('select count(1) as total_dvidandos from Dividendos')["total_dvidandos"].values[0]

    def get_updated_screen(self):
        return f"""
        ########################################################
        #                   SISTEMA DE VENDAS                     
        #                                                         
        #  TOTAL DE REGISTROS:                                    
        #      1 - : Administradores : {str(self.get_total_admin()).rjust(5)}
        #      2 - : Cotacoes : {str(self.get_total_cotacoes()).rjust(5)}
        #      3 - : Dividendos : {str(self.get_total_Dividendos()).rjust(5)}
        #      4 - : Fundos : {str(self.get_total_fundos()).rjust(5)}
        #
        #  CRIADO POR: {self.created_by}
        #               {self.created_by2}
        #  PROFESSOR:  {self.professor}
        #
        #  DISCIPLINA: {self.disciplina}
        #              {self.semestre}
        ########################################################
        """