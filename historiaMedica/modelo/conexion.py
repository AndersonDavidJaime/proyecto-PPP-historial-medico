import sqlite3

class ConexionDB:
    def __init__(self):
        self.baseDatos = 'database/dbhistorial.db'
        self.conexion = sqlite3.connect(self.baseDatos)
        self.cursor = self.conexion.cursor()  # Inicializa el cursor
    
    def cerrarConexion(self):
        self.conexion.commit()
        self.conexion.close()
