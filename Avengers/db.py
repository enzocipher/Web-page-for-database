import pyodbc as dbms

def conectar():
    conn = dbms.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};'
        'SERVER=localhost;'
        'DATABASE=policia_arequipa;'
        'Trusted_Connection=yes;'
    )
    return conn

def ejecutar_funcion(nombre_funcion, parametros):
    conn = conectar()
    cursor = conn.cursor()
    placeholder = ', '.join(['?' for _ in parametros])
    # Si tu función es de tabla, usa SELECT * FROM ...
    sql = f"SELECT * FROM dbo.{nombre_funcion}({placeholder})"
    cursor.execute(sql, parametros)
    columns = [column[0] for column in cursor.description]
    resultados = [dict(zip(columns, row)) for row in cursor.fetchall()]
    cursor.close()
    conn.close()
    return resultados
