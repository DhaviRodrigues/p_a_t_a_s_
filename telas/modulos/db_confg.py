import mysql.connector
from mysql.connector import Error

# --- INFORMAÇÕES DE CONEXÃO ---
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Ciente2020#', 
    'database': 'patas_db'
}

def get_db_connection():
    """
    Cria e retorna um objeto de conexão com o banco de dados MySQL.
    Retorna None se a conexão falhar.
    """
    conn = None  # Inicia a variável de conexão como None
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        if conn.is_connected():
            return conn
            
    except Error as e:
        print(f"Erro ao conectar ao MySQL: {e}")
        # Em caso de erro, a função retornará None, pois 'conn' não foi alterado.
        return None

# --- Bloco de teste ---
# Este código só será executado se você rodar este ficheiro diretamente (ex: python db_config.py)
if __name__ == '__main__':
    print("A testar a conexão com o banco de dados...")
    connection = get_db_connection()
    if connection:
        print("-> Conexão estabelecida com sucesso!")
        connection.close()
        print("-> Conexão de teste fechada.")
    else:
        print("-> Falha ao estabelecer conexão.")