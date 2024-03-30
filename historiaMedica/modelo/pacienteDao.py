from .conexion import ConexionDB
from tkinter import messagebox
import sqlite3

def editarDatoPaciente(persona, idPersona):
    conexion = ConexionDB()
    sql = f"""UPDATE Persona SET fechaRegistro ='{persona.fechaRegistro}', nombres = '{persona.nombres}', apellidos = '{persona.apellidos}', fechaNacimiento ='{persona.fechaNacimiento}', cedula ='{persona.cedula}', edad = '{persona.edad}', estadoCivil = '{persona.estadoCivil}', domicilio = '{persona.domicilio}', telefono = '{persona.telefono}', appp = '{persona.appp}', apf = '{persona.apf}', ago = '{persona.ago}', alergias = '{persona.alergias}', correo = '{persona.correo}', carrera = '{persona.carrera}', genero ='{persona.genero}', semestre ='{persona.semestre}', activo = 1 WHERE idPersona = {idPersona}"""
    try:
        conexion.cursor.execute(sql)
        conexion.cerrarConexion()
        title = 'Editar Paciente'
        mensaje = 'Paciente Editado Exitosamente'
        messagebox.showinfo(title, mensaje)
    except:
        title = 'Editar Paciente'
        mensaje = 'Error al editar paciente'
        messagebox.showinfo(title, mensaje)

def guardarDatosPaciente(persona):
    conexion = ConexionDB()
    sql = f"""INSERT INTO Persona(fechaRegistro, nombres, apellidos, cedula, fechaNacimiento, edad, estadoCivil, domicilio, telefono, appp, apf, ago, alergias, correo, carrera, genero, semestre, activo) VALUES 
                                    ('{persona.fechaRegistro}', '{persona.nombres}', '{persona.apellidos}', '{persona.cedula}', '{persona.fechaNacimiento}', '{persona.edad}', '{persona.estadoCivil}', '{persona.domicilio}', '{persona.telefono}', '{persona.appp}', '{persona.apf}', '{persona.ago}',
                                    '{persona.alergias}', '{persona.correo}', '{persona.carrera}', '{persona.genero}', '{persona.semestre}', 1)"""
    try:
        conexion.cursor.execute(sql)
        conexion.conexion.commit()  # Commit de la transacción
        conexion.cerrarConexion()
        title = 'Registrar Paciente'
        mensaje = 'Paciente Registrado Exitosamente'
        messagebox.showinfo(title, mensaje)
    except sqlite3.IntegrityError:
        title = 'Registrar paciente'
        mensaje = 'Error al registrar paciente: violación de la integridad de datos'
        messagebox.showerror(title, mensaje)
    except Exception as e:
        title = 'Registrar paciente'
        mensaje = f'Error al registrar paciente: {str(e)}'
        messagebox.showerror(title, mensaje)
    
def listar():
    conexion = ConexionDB()
    listaPersona = []
    sql = 'SELECT * FROM Persona WHERE activo = 1'
    try:
        conexion.cursor.execute(sql)
        listaPersona = conexion.cursor.fetchall()
        conexion.cerrarConexion()
    except:
        title = 'Datos'
        mensaje = 'Registros no existen'
        messagebox.showwarning(title, mensaje)
    return listaPersona

def listarCondicion(where):
    conexion = ConexionDB()
    listaPersona = []
    sql = f'SELECT * FROM Persona {where}'
    try:
        conexion.cursor.execute(sql)
        listaPersona = conexion.cursor.fetchall()
        conexion.cerrarConexion()
    except:
        title = 'Datos'
        mensaje = 'Registros no existen'
        messagebox.showwarning(title, mensaje)
    return listaPersona


def eliminarPaciente(idPersona):
    conexion = ConexionDB()
    sql = f"""UPDATE Persona SET activo = 0 WHERE idPersona = {idPersona}"""
    try:
        conexion.cursor.execute(sql)
        conexion.cerrarConexion()
        title = 'Eliminar Paciente'
        mensaje = 'Paciente eliminado exitosamente'
        messagebox.showinfo(title, mensaje)
    except:
        title = 'Eliminar Paciente'
        mensaje = 'Error al eliminar Paciente'
        messagebox.showwarning(title, mensaje)


class Persona:
    def __init__(self, fechaRegistro, nombres, apellidos, fechaNacimiento, cedula, edad, estadoCivil, 
                 domicilio, telefono, appp, apf, ago, alergias, correo, carrera, genero, semestre):
        self.fechaRegistro = fechaRegistro
        self.idPersona = None
        self.nombres = nombres
        self.apellidos = apellidos
        self.fechaNacimiento = fechaNacimiento
        self.cedula = cedula
        self.edad = edad
        self.estadoCivil = estadoCivil
        self.domicilio = domicilio
        self.telefono = telefono
        self.appp = appp
        self.apf = apf
        self.ago = ago
        self.alergias = alergias
        self.correo = correo
        self.carrera = carrera
        self.genero = genero
        self.semestre = semestre
    
    def __str__(self):
        return f'Persona[{self.fechaRegistro} ,{self.nombres}, {self.apellidos}, {self.fechaNacimiento}, {self.cedula}, {self.edad}, {self.estadoCivil}, {self.domicilio}, {self.telefono}, {self.appp}, {self.apf}, {self.ago}, {self.alergias}, {self.correo}, {self.carrera}, {self.genero}, {self.semestre}]'

