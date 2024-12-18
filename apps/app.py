from flask import Flask, request, jsonify
import mysql.connector
from mysql.connector import Error
from config import DB_CONFIG

app = Flask(__name__)

def get_db_connection():
    try:
        connection = mysql.connector.connect(**DB_CONFIG)
        if connection.is_connected():
            return connection
    except Error as e:
        print(f"Error: {e}")
        return None

@app.route('/insert', methods=['POST'])
def insert_data():
    data = request.json
    name = data.get('name')

    connection = get_db_connection()
    if not connection:
        return jsonify({"error": "Database connection failed"}), 500

    cursor = connection.cursor()
    try:
        cursor.execute("INSERT INTO test_table (name) VALUES (%s)", (name,))
        connection.commit()
        return jsonify({"message": "Data inserted successfully"}), 201
    except Error as e:
        return jsonify({"error": str(e)}), 500
    finally:
        cursor.close()
        connection.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
