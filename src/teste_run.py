from connection.oracle_queries import OracleQueries



db = OracleQueries()


db_select = db.sqlToDataFrame('SELECT CNPJ FROM ADMINISTRADORES;')['CNPJ'].values()

print(db_select)