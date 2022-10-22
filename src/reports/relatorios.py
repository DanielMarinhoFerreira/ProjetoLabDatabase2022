from connection.oracle_queries import OracleQueries
#
# Implementar 
# Base montada 
# #
class Relatorio:
    def __init__(self):
        with open("src/sql/relatorio_fundos.sql") as f:
            self.query_relatorio_fundos = f.read()

    def get_relatorio_fundos(self):
        oracle = OracleQueries()
        oracle.connect()
        print(oracle.sqlToDataFrame(self.query_relatorio_fundos))
        input("Pressione Enter para Sair do Relatório de ")