from flask import Flask, jsonify
import psycopg2
import psycopg2.extras

app = Flask(__name__)

# Configuration de la connexion à la base de données
DB_NAME = "mydb"
DB_USER = "postgres"
DB_PASS = "password"
DB_HOST = "db"  # Nom du conteneur pour la base de données

def get_db_connection():
    try:
        connection = psycopg2.connect(
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASS,
            host=DB_HOST,
            port="5432"
        )
        return connection
    except psycopg2.OperationalError as e:
        app.logger.error(f"Database connection error: {e}")
        return None

# Endpoint principal
@app.route('/')
def index():
    conn = get_db_connection()
    if conn is None:
        return jsonify({"error": "Unable to connect to the database"}), 500
    
    cur = conn.cursor()
    cur.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public';")
    tables = cur.fetchall()
    cur.close()
    conn.close()
    
    # Retourne la liste des tables dans une réponse JSON
    return jsonify({"Tables in public schema": [table[0] for table in tables]})

# Endpoint de liveness
@app.route('/health/live', methods=['GET'])
def liveness():
    return jsonify({"status": "alive"}), 200

# Endpoint de readiness
@app.route('/health/ready', methods=['GET'])
def readiness():
    conn = get_db_connection()
    if conn is None:
        return jsonify({"status": "not ready"}), 503
    
    conn.close()
    return jsonify({"status": "ready"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
