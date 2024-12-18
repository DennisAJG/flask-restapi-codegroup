import mysql.connector
from mysql.connector import Error

try:
    # Conexão com o banco de dados MySQL
    connection = mysql.connector.connect(
        host='databaseprojectappscodegroup.cly6g06qycbq.us-east-1.rds.amazonaws.com',
        user='root',
        password='CodeGroup2024'
    )
    
    if connection.is_connected():
        print("Conectado ao MySQL com sucesso!")

        # Criar um cursor para executar os comandos SQL
        cursor = connection.cursor()
        
        # Comandos SQL
        create_database_query = "CREATE DATABASE IF NOT EXISTS test_db;"
        use_database_query = "USE test_db;"
        create_table_query = """
        CREATE TABLE IF NOT EXISTS test_table (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255)
        );
        """
        
        # Executando os comandos
        cursor.execute(create_database_query)
        cursor.execute(use_database_query)
        cursor.execute(create_table_query)
        
        print("Banco de dados e tabela criados com sucesso!")

except Error as e:
    print(f"Erro ao conectar ao MySQL: {e}")
finally:
    # Fechando a conexão
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("Conexão com MySQL fechada.")
