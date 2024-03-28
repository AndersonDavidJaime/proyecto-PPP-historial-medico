from sqlite3.dbapi2 import Cursor
from turtle import title
from .conexion import ConexionDB
from tkinter import messagebox

#ya esta
def listarHistoria(idPersona):
    conexion = ConexionDB()
    listaHistoria = []
    sql = f'SELECT h.idHistoriaMedica, p.nombres || " " || p.apellidos AS NombreCompleto, h.fechaHistoria, h.motivo, h.PA, h.FC, h.PESO, h.talla, h.IMC, h.examenAuxiliar, h.detalle FROM historiaMedic h INNER JOIN Persona p ON p.idPersona = h.idPersona WHERE p.idPersona = {idPersona}'

    try:
        conexion.cursor.execute(sql)
        listaHistoria = conexion.cursor.fetchall()
        conexion.cerrarConexion()
    except:
        title = 'LISTAR HISTORIA'
        mensaje = 'Error al listar historia medica'
        messagebox.showerror(title, mensaje)
    return listaHistoria



#ya esta 
def guardarHistoria(idPersona, fechaHistoria, PA, FC, PESO, talla, IMC, motivo, examenAuxiliar, detalle):
    if idPersona is None:
        print("Error: idPersona cannot be None")
        return

    conexion = ConexionDB()
    sql = f"""INSERT INTO historiaMedic (idPersona, fechaHistoria, PA, FC, PESO, talla, IMC, motivo, examenAuxiliar, detalle) VALUES
            ({idPersona},'{fechaHistoria}','{PA}','{FC}','{PESO}','{talla}','{IMC}','{motivo}','{examenAuxiliar}','{detalle}')"""
    try:
        conexion.cursor.execute(sql)
        conexion.cerrarConexion()
        title = 'Registro Historia Clinica'
        mensaje = 'Historia registrada exitosamente'
        messagebox.showinfo(title, mensaje)
    except:
        title = 'Registro Historia Clinica'
        mensaje = 'Error al registrar historia'
        messagebox.showerror(title, mensaje)


def eliminarHistoria(idHistoriaMedica):
    conexion = ConexionDB()
    sql = f'DELETE FROM historiaMedic WHERE idHistoriaMedica = {idHistoriaMedica}'

    try:
        conexion.cursor.execute(sql)
        conexion.cerrarConexion()
        title = 'Eliminar Historia'
        mensaje = 'Historia medica eliminada exitosamente'
        messagebox.showinfo(title, mensaje)
    except:
        title = 'Eliminar Historia'
        mensaje = 'Error al eliminar historia medica'
        messagebox.showerror(title, mensaje)

def editarHistoria(fechaHistoria, PA, FC, PESO, talla, IMC, motivo, examenAuxiliar, detalle, idHistoriaMedica):
    conexion = ConexionDB()
    sql = f"""UPDATE historiaMedic SET fechaHistoria = '{fechaHistoria}', PA = '{PA}', FC = '{FC}', PESO = '{PESO}', talla = '{talla}', IMC = '{IMC}', motivo = '{motivo}', examenAuxiliar = '{examenAuxiliar}', detalle = '{detalle}' WHERE idHistoriaMedica = {idHistoriaMedica}"""
    try:
        conexion.cursor.execute(sql)
        conexion.cerrarConexion()
        title = 'Editar Historia'
        mensaje = 'Historia medica editada exitosamente'
        messagebox.showinfo(title, mensaje)
    except:
        title = 'Editar Historia'
        mensaje = 'Error al editar historia medica'
        messagebox.showerror(title, mensaje)




#ya esta 
class historiaClinica:
    def __init__(self, idPersona, fechaHistoria, PA, FC, PESO, talla, IMC, motivo, examenAuxiliar, detalle):
        self.idHistoriaClinica = None
        self.idPersona = idPersona
        self.fechaHistoria = fechaHistoria
        self.PA = PA
        self.FC = FC
        self.PESO = PESO
        self.talla = talla
        self.IMC = IMC
        self.motivo = motivo
        self.examenAuxiliar = examenAuxiliar
        self.detalle = detalle

    def __str__(self):
        return f'historiaClinica[{self.idPersona}, {self.fechaHistoria}, {self.PA}, {self.FC}, {self.PESO}, {self.talla}, {self.IMC}, {self.motivo}, {self.examenAuxiliar}, {self.detalle}]'
    