from dotenv import load_dotenv
import mysql.connector
from mysql.connector import Error
import os


load_dotenv()

try:
    
    connection = mysql.connector.connect(
        host=os.getenv('DB_HOST'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        database=os.getenv('DB_NAME')
    )
    
    if connection.is_connected():
        print("Conectado ao MySQL com sucesso!")

       
        cursor = connection.cursor()
        
        
        create_database_query = "CREATE DATABASE IF NOT EXISTS test_db;"
        use_database_query = "USE test_db;"
        create_table_query = """
        CREATE TABLE IF NOT EXISTS test_table (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255)
        );
        """
        
      
        cursor.execute(create_database_query)
        cursor.execute(use_database_query)
        cursor.execute(create_table_query)
        
        print("Banco de dados e tabela criados com sucesso!")

except Error as e:
    print(f"Erro ao conectar ao MySQL: {e}")
finally:
   
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("Conexão com MySQL fechada.")
