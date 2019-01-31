from lineData import LineData
from storage import DatabaseConnection
import sys

if len(sys.argv) < 4:
    print('Parametrização inválida: parse.py <linha_inicio> <usuário_bd> <senha_bd>')
else:
    db = DatabaseConnection(sys.argv[2], sys.argv[3])
    fh = open('./F.K032001K.D81106A', 'r')
    count = 0
    while True:
        line = fh.readline()
        if not line:
            break
        if count > int(sys.argv[1]):
            ld = LineData(count, line)
            
            if ld.tipo_de_registro == '1' or ld.tipo_de_registro == '2' or ld.tipo_de_registro == '6':
                db.insert(ld)
            
            if count > 0 and count % 50 == 0:
                db.commit()
                print('Commited line: ' + str(count))
        count += 1
    db.commit()
    db.close()
    fh.close()
    print('Total='+str(count))
