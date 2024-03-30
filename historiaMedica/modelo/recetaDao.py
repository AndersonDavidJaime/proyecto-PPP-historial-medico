from tkinter import messagebox
from .conexion import ConexionDB

def listarRecetas(idHistoriaMedica):
    conexion = ConexionDB()
    listaRecetas = []
    sql = f"SELECT * FROM Receta WHERE idHistoriaMedica = {idHistoriaMedica}"
    
    try:
        conexion.cursor.execute(sql)
        listaRecetas = conexion.cursor.fetchall()
        conexion.cerrarConexion()
    except:
        title = 'Listar Recetas'
        mensaje = 'Error al listar las recetas'
        messagebox.showerror(title, mensaje)
    return listaRecetas

def guardarReceta(idHistoriaMedica, fechaReceta, especialidadServicio, prescriptorNombre, viasAdministracion, dosis, frecuencia, duracion, manana, meidodia, tarde, noche):
    conexion = ConexionDB()
    sql = f"""INSERT INTO Receta (idHistoriaMedica, fechaReceta, especialidadServicio, prescriptorNombre, viasAdministracion, dosis, frecuencia, duracion, manana, meidodia, tarde, noche) 
            VALUES ({idHistoriaMedica}, '{fechaReceta}', '{especialidadServicio}', '{prescriptorNombre}', '{viasAdministracion}', '{dosis}', '{frecuencia}', '{duracion}', '{manana}', '{meidodia}', '{tarde}', '{noche}')"""
    try:
        conexion.cursor.execute(sql)
        conexion.cerrarConexion()
        title = 'Guardar Receta'
        mensaje = 'Receta guardada exitosamente'
        messagebox.showinfo(title, mensaje)
    except:
        title = 'Guardar Receta'
        mensaje = 'Error al guardar la receta'
        messagebox.showerror(title, mensaje)

def eliminarReceta(idReceta):
    conexion = ConexionDB()
    sql = f"DELETE FROM Receta WHERE idReceta = {idReceta}"
    try:
        conexion.cursor.execute(sql)
        conexion.cerrarConexion()
        title = 'Eliminar Receta'
        mensaje = 'Receta eliminada exitosamente'
        messagebox.showinfo(title, mensaje)
    except:
        title = 'Eliminar Receta'
        mensaje = 'Error al eliminar la receta'
        messagebox.showerror(title, mensaje)

def editarReceta(idReceta, fechaReceta, especialidadServicio, prescriptorNombre, viasAdministracion, dosis, frecuencia, duracion, manana, meidodia, tarde, noche):
    conexion = ConexionDB()
    sql = f"""UPDATE Receta SET fechaReceta = '{fechaReceta}', especialidadServicio = '{especialidadServicio}', prescriptorNombre = '{prescriptorNombre}', viasAdministracion = '{viasAdministracion}', 
            dosis = '{dosis}', frecuencia = '{frecuencia}', duracion = '{duracion}', manana = '{manana}', meidodia = '{meidodia}', tarde = '{tarde}', noche = '{noche}' WHERE idReceta = {idReceta}"""
    try:
        conexion.cursor.execute(sql)
        conexion.cerrarConexion()
        title = 'Editar Receta'
        mensaje = 'Receta editada exitosamente'
        messagebox.showinfo(title, mensaje)
    except:
        title = 'Editar Receta'
        mensaje = 'Error al editar la receta'
        messagebox.showerror(title, mensaje)
