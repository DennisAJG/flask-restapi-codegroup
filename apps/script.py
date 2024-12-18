import mysql.connector
from mysql.connector import Error
import os

# Configuração do banco de dados
DATABASE_CONFIG = {
    'host': os.getenv('DB_HOST', 'localhost'),
    'user': os.getenv('DB_USER', 'root'),
    'password': os.getenv('DB_PASSWORD', ''),
    'database': os.getenv('DB_NAME', 'test_db')
}

try:
    # Conectando ao banco de dados MySQL
    connection = mysql.connector.connect(
        host=DATABASE_CONFIG['host'],
        user=DATABASE_CONFIG['user'],
        password=DATABASE_CONFIG['password']
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
    try:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("Conexão com MySQL fechada.")
    except NameError:
        print("Nenhuma conexão foi aberta para fechar.")
