import sqlite3

class Data_base:
    def __init__(self, name='empresa.db'):
        self.name = name

    def connect(self):
        self.connection = sqlite3.connect(self.name)

    def close_connection(self):
        try:
            self.connection.close()
        except Exception as e:
            print(f"Erro ao fechar a conexão: {e}")

    def create_table_clientes(self):
        cursor = self.connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Clientes (
                Id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome_cli TEXT,
                cpf_cli TEXT
            )
        """)

    def cadastro_cliente(self, fullDataSet):
        campo_tabela = ('nome_cli', 'cpf_cli')
        placeholders = ", ".join(["?"] * len(campo_tabela))
        sql = f"INSERT INTO Clientes ({', '.join(campo_tabela)}) VALUES ({placeholders})"

        cursor = self.connection.cursor()
        try:
            cursor.execute(sql, fullDataSet)
            self.connection.commit()
            return "ok"
        except Exception as e:
            print(f"Erro ao cadastrar cliente: {e}")
            return "erro"
                
    def pesquisa_cliente(self, cpf=None):
        cursor = self.connection.cursor()

        if cpf is None:
            cursor.execute("SELECT nome_cli,cpf_cli FROM Clientes")
        else:
            cursor.execute("SELECT nome_cli,cpf_cli FROM Clientes WHERE cpf_cli = ?", (cpf,))

        result = cursor.fetchall()  # Retorna todos os resultados
        return result  # Retorna uma lista de tuplas com os dados dos clientes
    
    def alterar_cliente(self, cpf, nome_cli, cpf_cli):
        cursor = self.connection.cursor()

        try:
            cursor.execute("UPDATE Clientes SET nome_cli = ?, cpf_cli = ? WHERE cpf_cli = ?", (nome_cli, cpf_cli, cpf))
            self.connection.commit()
            return True
        except Exception as e:
            print(f"Erro ao alterar cliente: {e}")
            return False
        
    def excluir_cliente(self, cpf):
        cursor = self.connection.cursor()

        try:
            cursor.execute("DELETE FROM Clientes WHERE cpf_cli = ?", (cpf,))
            self.connection.commit()
            return True
        except Exception as e:
            print(f"Erro ao excluir cliente: {e}")
            return False