from connection.oracle_queries import OracleQueries

class SplashScreen:

    def __init__(self):
        self.qry_total_fundos = "select count(1) as total_fundos from FUNDOS" 
        self.created_by = "Daniel Marinho, Isaque Silva"
        self.professor = "Prof. M.Sc. Howard Roatti"
        self.disciplina = "Banco de Dados"
        self.semestre = "2022/2"

    def get_total_fundos(self):
        oracle = OracleQueries()
        oracle.connect()
        return oracle.sqlToDataFrame(self.qry_total_fundos)["total_fundos"].values[0]



    def get_updated_screen(self):
        return f"""
        ########################################################
        #                   SISTEMA DE VENDAS                     
        #                                                         
        #  TOTAL DE REGISTROS:                                    
        #      1 - : Fundos   {str(self.get_total_fundos()).rjust(1)}
        #
        #  CRIADO POR: {self.created_by}
        #
        #  PROFESSOR:  {self.professor}
        #
        #  DISCIPLINA: {self.disciplina}
        #              {self.semestre}
        ########################################################
        """