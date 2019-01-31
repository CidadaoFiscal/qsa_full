import pyodbc
from lineData import LineData
from datetime import datetime

class DatabaseConnection():
    def __init__(self, username, password):
        server = 'cidadaofiscal.database.windows.net'
        database = 'rawdata'
        driver= '{ODBC Driver 13 for SQL Server}'
        cnxn = pyodbc.connect('Driver='+driver+';Server=tcp:'+server+',1433;Database='+database+';Uid='+username+';Pwd='+ password+';Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;')
        self.cursor = cnxn.cursor()
        pass

    def insert(self, lineData):
        sql = 'INSERT INTO '
        if (lineData.tipo_de_registro == '1'):
            sql += 'qsa_dados_cadastrais '
            
        elif (lineData.tipo_de_registro == '2'):
            sql += 'qsa_socios'

        elif (lineData.tipo_de_registro == '6'):
            sql += 'qsa_cnaes_secundarios'
            
        keys = '('
        values = 'VALUES ('
        for item in vars(lineData).items():
            key = item[0]
            value = item[1]

            if value and key != 'tipo_de_registro':
                if isinstance(value, str): 
                    keys += key + ','
                    values += '\'' + value.replace('\'', '\'\'') + '\','
                elif isinstance(value, datetime):
                    keys += key + '_ano,' + key + '_mes,' + key + '_dia,' 
                    values += str((value).year) + ',' + str((value).month) + ',' + str((value).day) + ','
                else: 
                    keys += key + ','
                    values += str(value) + ','
        keys = keys[:-1] + ') '
        values = values[:-1] + ')'

        sql += keys + values
        try:
            self.cursor.execute(sql)
        except pyodbc.DataError:
            print(sql)
            raise
        pass

    def commit(self):
        self.cursor.commit()
        pass

    def close(self):
        self.cursor.close()
        pass
    pass