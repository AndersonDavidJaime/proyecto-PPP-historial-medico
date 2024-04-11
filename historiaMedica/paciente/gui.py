import tkinter as tk
from fpdf import FPDF, TitleStyle
import sys
import subprocess


import webbrowser

from matplotlib import colors
from modelo.conexion import ConexionDB

from tkinter import *
from tkinter import Button, ttk, scrolledtext, Toplevel, LabelFrame
from tkinter import messagebox
from modelo.recetaDao import guardarReceta, listarReceta, ultimoId
from modelo.pacienteDao import Persona, eliminarPaciente, guardarDatosPaciente, listar, listarCondicion, editarDatoPaciente
from modelo.historiaMedicaDao import guardarHistoria, listarHistoria, eliminarHistoria, editarHistoria
import tkcalendar as tc
from tkcalendar import *
from tkcalendar import Calendar
from datetime import datetime, date
from tkinter import ttk, Toplevel
import re
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import sqlite3
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph, SimpleDocTemplate, TableStyle, Spacer 
from reportlab.lib.styles import getSampleStyleSheet
from PIL import Image

import os







class Frame(tk.Frame):
    def __init__(self, root):
        super().__init__(root, width=1300, height=750)
        self.root = root
        self.pack()
        self.config(bg='#1B7505')
        self.idPersona = None
        self.idPersonaHistoria =None
        self.idHistoriaMedica =None
        self.idHistoriaMedicaEditar =None
        self.idPERSONAPERS=None
        self.idHistoriaRec=None
        self.conexion_db = ConexionDB()  # Instancia de la clase ConexionDB
        self.pdf_process = None

        self.camposPaciente()
        self.create_encabezado()
        self.fill_current_date()
        self.deshabilitar()
        self.tablaPaciente()
        
    
    
    def create_encabezado(self):
        # Encabezado
        universidad_label = tk.Label(self, text='UNIVERSIDAD TÉCNICA ESTATAL DE QUEVEDO\n'
                                               'UNIDAD DE BIENESTRAR UNIVERSITARIO CENTRO MÉDICO',
                                    font=('Nexa', 12, 'bold'), bg='#1B7505', fg='white')
        universidad_label.grid(row=0, column=1, columnspan=6,  sticky='n', padx=(10, 0))
        

    def fill_current_date(self):
        current_date = datetime.now().strftime("%d-%m-%Y")  # Obtiene la fecha actual en formato YYYY-MM-DD
        self.svFecha.set(current_date)  # Establece la fecha actual en el campo de fecha


    
    def camposPaciente(self):
    #LABELS
    
    #fecha
        self.lblFechaRegistro = tk.Label(self, text='FECHA: ')
        self.lblFechaRegistro.config(font=('Nexa', 8, 'bold'), bg='#1B7505', fg='white')
        self.lblFechaRegistro.grid(column=1, row=1, padx=90, sticky='w')
    
    #CARRERA
        self.lblCarrera= tk.Label(self, text='CARRERA: ')
        self.lblCarrera.config(font=('Nexa', 8, 'bold'), bg='#1B7505', fg='white')
        self.lblCarrera.grid(column=2, row=1, sticky='w')  

    #SEMESTRE
        self.lblSemestre= tk.Label(self, text='SEMESTRE: ')
        self.lblSemestre.config(font=('Nexa', 8, 'bold'), bg='#1B7505', fg='white')
        self.lblSemestre.grid(column=3, row=1, sticky='w')

    #GENERO
        self.lblGenero = tk.Label(self, text='GÉNERO: ')
        self.lblGenero.config(font=('Nexa', 8, 'bold'), bg='#1B7505', fg='white')
        self.lblGenero.grid(column=1, row=2, padx=90, pady=5, sticky='w')

    #NOMBRE
        self.lblNombres = tk.Label(self, text='NOMBRES: ')
        self.lblNombres.config(font=('Nexa', 8, 'bold'), bg='#1B7505', fg='white')
        self.lblNombres.grid(column=1,row=3, padx=90, pady=1,  sticky='w')
    
    #APELLIDO
        self.lblApellidos = tk.Label(self, text='APELLIDOS: ')
        self.lblApellidos.config(font=('Nexa', 8, 'bold'), bg='#1B7505', fg='white')
        self.lblApellidos.grid(column=1,row=4, padx=90, pady=5, sticky='w')
    
    #Fecha de nacimiento
        self.lblFechNacimiento = tk.Label(self, text='FECHA NACIMIENTO: ')
        self.lblFechNacimiento.config(font=('Nexa', 8, 'bold'), bg='#1B7505', fg='white')
        self.lblFechNacimiento.grid(column=1,row=6, padx=90, pady=5, sticky='w')
    #CEDULA
        self.lblCedula = tk.Label(self, text='No. CÉDULA: ')
        self.lblCedula.config(font=('Nexa', 8, 'bold'), bg='#1B7505', fg='white')
        self.lblCedula.grid(column=1,row=5, padx=90, pady=5, sticky='w')


    #edad 
        self.lblEdad = tk.Label(self, text='EDAD: ')
        self.lblEdad.config(font=('Nexa', 8, 'bold'), bg='#1B7505', fg='white')
        self.lblEdad.grid(column=1,row=7, padx=90, pady=5, sticky='w')

        
    #ESTADO CIVIL
        self.lblFechNacimiento = tk.Label(self, text='ESTADO CIVIL: ')
        self.lblFechNacimiento.config(font=('Nexa', 8, 'bold'), bg='#1B7505', fg='white')
        self.lblFechNacimiento.grid(column=1,row=8, padx=90, pady=5, sticky='w')

    #DOMICILIO
        self.lblEdad = tk.Label(self, text='DOMICILIO: ')
        self.lblEdad.config(font=('Nexa', 8, 'bold'), bg='#1B7505', fg='white')
        self.lblEdad.grid(column=1,row=9, padx=90, pady=5, sticky='w')

    #TELEFINO:
        self.lblAntecedentes = tk.Label(self, text='TELÉFONO:')
        self.lblAntecedentes.config(font=('Nexa', 8, 'bold'), bg='#1B7505', fg='white')
        self.lblAntecedentes.grid(column=1,row=10, padx=90, pady=5, sticky='w')


    #CORREO:
        self.lblCorreo = tk.Label(self, text='CORREO:')
        self.lblCorreo.config(font=('Nexa', 8, 'bold'), bg='#1B7505', fg='white')
        self.lblCorreo.grid(column=1,row=11, padx=90, pady=5, sticky='w')
    
    #titulo
        self.lblFechaRegistro = tk.Label(self, text='ANTECEDENTES: ')
        self.lblFechaRegistro.config(font=('Nexa', 12, 'bold'), bg='#1B7505', fg='white')
        self.lblFechaRegistro.grid(column=3, row=7,  sticky='e')

    #APP
        self.lblFechaRegistro = tk.Label(self, text='APP: ')
        self.lblFechaRegistro.config(font=('Nexa', 8, 'bold'), bg='#1B7505', fg='white')
        self.lblFechaRegistro.grid(column=3, row=8,  sticky='w')
    
    #APF
        self.lblCarrera= tk.Label(self, text='APF: ')
        self.lblCarrera.config(font=('Nexa', 8, 'bold'), bg='#1B7505', fg='white')
        self.lblCarrera.grid(column=3, row=9, sticky='w')  
        

     #AGO7
        self.lblSemestre= tk.Label(self, text='AGO: ')
        self.lblSemestre.config(font=('Nexa', 8, 'bold'), bg='#1B7505', fg='white')
        self.lblSemestre.grid(column=3, row=10, sticky='w')
        
    
     #AGO7
        self.lblSemestre= tk.Label(self, text='ALERGIA: ')
        self.lblSemestre.config(font=('Nexa', 8, 'bold'), bg='#1B7505', fg='white')
        self.lblSemestre.grid(column=3, row=11, sticky='w')

       
    
    

        #ENTRYS

        #FECHA ENTRY
        self.svFecha = tk.StringVar()
        self.entryFecha = tk.Entry(self, textvariable=self.svFecha)
        self.entryFecha.config(width=16, font=('Nexa',8,'bold'))
        self.entryFecha.grid(column=1, row=1, padx=50, pady=25, sticky='e')


        #CARRERA ENTRY
        self.svCarrera = tk.StringVar()
        self.entryCarrera = tk.Entry(self, textvariable=self.svCarrera)
        self.entryCarrera.config(width=25, font=('Nexa',8,'bold'))
        self.entryCarrera.grid(column=2, row=1, padx=65)  

        #SEMESTRE
        self.svSemestre = tk.StringVar()
        self.entrySemestre = tk.Entry(self, textvariable=self.svSemestre)
        self.entrySemestre.config(width=20, font=('Nexa',8,'bold'))
        self.entrySemestre.grid(column=2,row=1, columnspan=2, pady=25, sticky='e') 

        #GÉNERO ENTRY
        self.svGenero = tk.StringVar()
        self.entryGenero = ttk.Combobox(self, textvariable=self.svGenero, state='readonly')
        self.entryGenero.config(values=['Masculino', 'Femenino', 'Otro'], width=33, font=('Nexa',8,'bold'))
        self.entryGenero.grid(column=2, row=2, columnspan=3, sticky='w')
 
        #NOMBRE
        self.svNombre = tk.StringVar()
        self.entryNombre = tk.Entry(self, textvariable=self.svNombre)
        self.entryNombre.config(width=35, font=('Nexa',8,'bold'))
        self.entryNombre.grid(column=2, row=3, columnspan=3, sticky='w')
        
        #APELLIDOS
        self.svApellidos = tk.StringVar()
        self.entryApellidos = tk.Entry(self, textvariable=self.svApellidos)
        self.entryApellidos.config(width=35, font=('Nexa',8,'bold'))
        self.entryApellidos.grid(column=2, row=4, columnspan=3, sticky='w')

        
        #CEDULA 
        self.svCedula = tk.StringVar()
        self.entryCedula = tk.Entry(self, textvariable=self.svCedula)
        self.entryCedula.config(width=35, font=('Nexa',8,'bold'))
        self.entryCedula.grid(column=2, row=5,  columnspan=3, sticky='w')

        
        #FECHA de nacimiento
        self.svFechaNacimiento = tk.StringVar()
        self.entryFechaNacimiento = tk.Entry(self, textvariable=self.svFechaNacimiento)
        self.entryFechaNacimiento.config(width=35, font=('Nexa',8,'bold'))
        self.entryFechaNacimiento.grid(column=2, row=6, columnspan=3, sticky='w')


        #edad
        self.svEdad = tk.StringVar()
        self.entryEdad = tk.Entry(self, textvariable=self.svEdad)
        self.entryEdad.config(width=35, font=('Nexa',8,'bold'))
        self.entryEdad.grid(column=2, row=7,  columnspan=2, sticky='w')
        


        #Estado civil
        self.svEstadoCivil = tk.StringVar()
        self.entryEstadoCivil = tk.Entry(self, textvariable=self.svEstadoCivil)
        self.entryEstadoCivil.config(width=35, font=('Nexa',8,'bold'))
        self.entryEstadoCivil.grid(column=2, row=8, columnspan=2, sticky='w')

        #DOMICILIO
        self.svDomicilio = tk.StringVar()
        self.entryDomicilio = tk.Entry(self, textvariable=self.svDomicilio)
        self.entryDomicilio.config(width=35, font=('Nexa',8,'bold'))
        self.entryDomicilio.grid(column=2, row=9,  columnspan=2, sticky='w')

        #TELEFONO
        self.svTelefono = tk.StringVar()
        self.entryTelefono = tk.Entry(self, textvariable=self.svTelefono)
        self.entryTelefono.config(width=35, font=('Nexa',8,'bold'))
        self.entryTelefono.grid(column=2, row=10, columnspan=3, sticky='w')

        #CORREO
        self.svCorreo = tk.StringVar()
        self.entryCorreo = tk.Entry(self, textvariable=self.svCorreo)
        self.entryCorreo.config(width=35, font=('Nexa',8,'bold'))
        self.entryCorreo.grid(column=2, row=11,  columnspan=3, sticky='w')
       
        #APP
        self.svApp = tk.StringVar()
        self.entryApp = tk.Entry(self, textvariable=self.svApp)
        self.entryApp.config(width=35, font=('Nexa',8,'bold'))
        self.entryApp.grid(column=3, row=8, padx=50, pady=5, columnspan=3)

        #APF
        self.svAPF = tk.StringVar()
        self.entryAPF = tk.Entry(self, textvariable=self.svAPF)
        self.entryAPF.config(width=35, font=('Nexa',8,'bold'))
        self.entryAPF.grid(column=3, row=9, padx=0, pady=5, columnspan=3)

        #AGO
        self.svAGO = tk.StringVar()
        self.entryAGO = tk.Entry(self, textvariable=self.svAGO)
        self.entryAGO.config(width=35, font=('Nexa',8,'bold'))
        self.entryAGO.grid(column=3, row=10, padx=0, pady=5, columnspan=3)

        #Alergia
        self.svAlergia = tk.StringVar()
        self.entryAlergia = tk.Entry(self, textvariable=self.svAlergia)
        self.entryAlergia.config(width=35, font=('Nexa',8,'bold'))
        self.entryAlergia.grid(column=3, row=11, padx=0, pady=5, columnspan=3)

        #BUSCADOR
        #LABEL BUSCADOR
        self.lblBuscarDni = tk.Label(self, text='BUSCAR CÉDULA: ')
        self.lblBuscarDni.config(font=('Nexa', 8, 'bold'), bg='#1B7505', fg='white')
        self.lblBuscarDni.grid(column=3, row=2,  sticky='w')

        self.lblBuscarApellido = tk.Label(self, text='BUSCAR APELLIDO: ')
        self.lblBuscarApellido.config(font=('Nexa', 8, 'bold'), bg='#1B7505', fg='white')
        self.lblBuscarApellido.grid(column=3, row=3, sticky='w')

        self.lblBuscarCarrera = tk.Label(self, text='CARRERA: ')
        self.lblBuscarCarrera.config(font=('Nexa', 8, 'bold'), bg='#1B7505', fg='white')
        self.lblBuscarCarrera.grid(column=3, row=4, sticky='w')
        #ENTRYS BUSCADOR
        self.svBuscarDni = tk.StringVar()
        self.entryBuscarDni = tk.Entry(self, textvariable=self.svBuscarDni)
        self.entryBuscarDni.config(width=25, font=('Nexa',8,'bold'))
        self.entryBuscarDni.grid(column=3, row=2, padx=150, pady=5, columnspan=3, sticky='w')

        self.svBuscarApellido = tk.StringVar()
        self.entryBuscarApellido = tk.Entry(self, textvariable=self.svBuscarApellido)
        self.entryBuscarApellido.config(width=25, font=('Nexa',8,'bold'))
        self.entryBuscarApellido.grid(column=3, row=3, padx=150, pady=5, columnspan=3, sticky='w')
        
        self.svBuscarCarrera = tk.StringVar()
        self.entryBuscarCarrera = tk.Entry(self, textvariable=self.svBuscarCarrera)
        self.entryBuscarCarrera.config(width=25, font=('Nexa',8,'bold'))
        self.entryBuscarCarrera.grid(column=3, row=4, padx=150, pady=5, columnspan=3, sticky='w')
        
        # BUTTON BUSCADOR
        self.btnBuscarCondicion = tk.Button(self, text='BUSCAR', command=self.buscarCondicion)
        self.btnBuscarCondicion.config(width=20, font=('Nexa',8,'bold'), fg='#DAD5D6', 
                                bg='#00396F', cursor='hand2',activebackground='#5B8DBD')
        self.btnBuscarCondicion.grid(column=3, row=5,sticky='w')

        self.btnLimpiarBuscador = tk.Button(self, text='LIMPIAR', command= self.limpiarBuscador)
        self.btnLimpiarBuscador.config(width=20, font=('Nexa',8,'bold'), fg='#DAD5D6', 
                                bg='#00396F', cursor='hand2',activebackground='#5B8DBD')
        self.btnLimpiarBuscador.grid(column=3, row=5, padx=40, pady=4, columnspan=3)  

        # FECHA - CALENDARIO 
        self.btnCalendario = tk.Button(self, text='CALENDARIO', command=self.show_calendar)
        self.btnCalendario.config(width=20, font=('Nexa',8,'bold'), fg='#DAD5D6', 
                                bg='#120061', cursor='hand2',activebackground='#7C6DC1')
        self.btnCalendario.grid(column=3, row=6, sticky='w')

   #BUTTONS
        self.btnNuevo = tk.Button(self, text='Nuevo', command=self.habilitar)
        self.btnNuevo.config(width=25, font=('ARIAL',8,'bold'), fg='#DAD5D6', 
                                bg='#158645', cursor='hand2',activebackground='#35BD6F')
        self.btnNuevo.grid(row=17, column=1, padx=10, pady=5)
             

        self.btnGuardar = tk.Button(self, text='Guardar', command=self.guardarPaciente)
        self.btnGuardar.config(width=30, font=('ARIAL',8,'bold'), fg='#DAD5D6', 
                                bg='#000000', cursor='hand2',activebackground='#5F5F5F')
        self.btnGuardar.grid(row=17, column=2, padx=10, pady=5)

            
        
        self.lblTitulo= tk.Label(self, text='TABLA PACIENTES: ')
        self.lblTitulo.config(font=('Nexa', 10, 'bold'), bg='#1B7505', fg='white')
        self.lblTitulo.grid(column=2, row=12, padx=10,sticky='e')  

        
        self.btnCancelar = tk.Button(self, text='Cancelar', command=self.deshabilitar)
        self.btnCancelar.config(width=20, font=('ARIAL',8,'bold'), fg='#DAD5D6', 
                                bg='#B00000', cursor='hand2',activebackground='#D27C7C')
        self.btnCancelar.grid(row=17, column=3, padx=10, pady=5)
        

        self.btnReportes = tk.Button(self, text='Reportes', command=self.venetanaReportes)
        self.btnReportes.config(width=20, font=('ARIAL',8,'bold'), fg='#DAD5D6', 
                                bg='#B00000', cursor='hand2',activebackground='#D27C7C')
        self.btnReportes.grid(row=17, column=4, padx=10, pady=5)
        
    def venetanaReportes(self):
        topVentanaReportes = tk.Toplevel()
        topVentanaReportes.title('REPORTES')
        topVentanaReportes.geometry("700x700")
         # Evitar redimensionamiento

        # Marco principal para contener el título y los botones
        marco_principal = tk.Frame(topVentanaReportes)
        marco_principal.pack(fill="both", expand=True)

        # Encabezado
        self.lblTitulo = tk.Label(marco_principal, text="Reportes", font=("Arial", 14, "bold"))
        self.lblTitulo.pack(pady=(10, 20))

        # Botones de selección de sección
        marco_botones = tk.Frame(marco_principal)
        marco_botones.pack(side="top", pady=(0, 10))

        self.btnHistoriaMedica = tk.Button(marco_botones, text="Historia Médica", command=self.mostrar_seccion_historia_medica, width=20, height=5)
        self.btnHistoriaMedica.pack(side="left", padx=10, pady=10)

        self.btnPacientes = tk.Button(marco_botones, text="Pacientes", command=self.mostrar_seccion_pacientes, width=20, height=5)
        self.btnPacientes.pack(side="left", padx=10, pady=10)

        self.btnRecetas = tk.Button(marco_botones, text="Recetas", command=self.mostrar_seccion_recetas, width=20, height=5)
        self.btnRecetas.pack(side="left", padx=10, pady=10)

        # Contenedor de la sección
        self.contenedor_seccion = tk.Frame(marco_principal)
        self.contenedor_seccion.pack(fill="both", expand=True, padx=10, pady=(0, 10))


#seccion historiaMedica reportes--------------------
    def mostrar_seccion_historia_medica(self):
        # Limpiar el contenedor
        for widget in self.contenedor_seccion.winfo_children():
            widget.destroy()

        # Crear un marco para contener la sección de búsqueda por historia médica
        marco_historia_medica = tk.Frame(self.contenedor_seccion)
        marco_historia_medica.grid(row=0, column=0, sticky="nsew")  # Hacemos que el marco se expanda en todas las direcciones

        # Etiqueta y Entry para la fecha de inicio
        lbl_desde = tk.Label(marco_historia_medica, text="Desde:(DD-MM-AAAA)")
        lbl_desde.grid(row=0, column=0, padx=5, pady=5)

        self.entry_desde = tk.Entry(marco_historia_medica)
        self.entry_desde.grid(row=0, column=1, padx=5, pady=5)

        # Etiqueta y Entry para la fecha de fin
        lbl_hasta = tk.Label(marco_historia_medica, text="Hasta:(DD-MM-AAAA)")
        lbl_hasta.grid(row=0, column=2, padx=5, pady=5)

        self.entry_hasta = tk.Entry(marco_historia_medica)
        self.entry_hasta.grid(row=0, column=3, padx=5, pady=5)

        # Botón para buscar pacientes por historia médica
        btn_buscar = tk.Button(marco_historia_medica, text="Buscar", command=self.buscar_pacientes_por_historia_medica)
        btn_buscar.grid(row=0, column=4, padx=5, pady=5)

        # Botón para generar el reporte en PDF
        btn_generar_reporte = tk.Button(marco_historia_medica, text="Generar Reporte", command=self.generar_reporte_historia_medica)
        btn_generar_reporte.grid(row=1, column=0, columnspan=5, padx=10, pady=10)

        # Marco para la tabla y las barras de desplazamiento
        marco_tabla = tk.Frame(marco_historia_medica)
        marco_tabla.grid(row=2, column=0, columnspan=5, padx=10, pady=10, sticky="nsew")  # Hacemos que el marco se expanda

        # Tabla de pacientes con encabezados
        self.tabla_pacientes_historia_medica = ttk.Treeview(marco_tabla, columns=('Cédula', 'Nombres', 'Apellidos','Carrera', 'Motivo' ,'Fecha de Historia Médica'), show='headings')
        self.tabla_pacientes_historia_medica.grid(row=0, column=0, sticky="nsew")

        # Agregar encabezados
        for col in ('Cédula', 'Nombres', 'Apellidos','Carrera', 'Motivo', 'Fecha de Historia Médica'):
            self.tabla_pacientes_historia_medica.heading(col, text=col)

        # Agregar barras de desplazamiento
        scroll_vertical = ttk.Scrollbar(marco_tabla, orient="vertical", command=self.tabla_pacientes_historia_medica.yview)
        scroll_vertical.grid(row=0, column=1, sticky="ns")

        scroll_horizontal = ttk.Scrollbar(marco_tabla, orient="horizontal", command=self.tabla_pacientes_historia_medica.xview)
        scroll_horizontal.grid(row=1, column=0, sticky="ew")

        # Configurar la tabla
        self.tabla_pacientes_historia_medica.configure(yscrollcommand=scroll_vertical.set, xscrollcommand=scroll_horizontal.set)

        # Ajustar el tamaño del contenedor principal
        self.contenedor_seccion.columnconfigure(0, weight=1)
        self.contenedor_seccion.rowconfigure(0, weight=1)

        # Ajustar el tamaño de las columnas en el marco de historia médica
        marco_historia_medica.columnconfigure(0, weight=1)
        marco_historia_medica.columnconfigure(1, weight=1)
        marco_historia_medica.columnconfigure(2, weight=1)
        marco_historia_medica.columnconfigure(3, weight=1)
        marco_historia_medica.columnconfigure(4, weight=1)


    def buscar_pacientes_por_historia_medica(self):
        # Limpiar tabla
        for item in self.tabla_pacientes_historia_medica.get_children():
            self.tabla_pacientes_historia_medica.delete(item)

        # Obtener fechas de inicio y fin
        desde = self.entry_desde.get()
        hasta = self.entry_hasta.get()

        # Consulta SQL para obtener pacientes con historias médicas en el rango de fechas especificado
        sql = f"SELECT Persona.cedula, Persona.nombres, Persona.apellidos, Persona.carrera, historiaMedic.motivo, historiaMedic.fechaHistoria FROM Persona INNER JOIN historiaMedic ON Persona.idPersona = historiaMedic.idPersona WHERE historiaMedic.fechaHistoria BETWEEN '{desde}' AND '{hasta}'"
        self.conexion_db.cursor.execute(sql)
        pacientes = self.conexion_db.cursor.fetchall()

        # Insertar datos en la tabla
        for paciente in pacientes:
            self.tabla_pacientes_historia_medica.insert('', 'end', values=paciente)


    def generar_reporte_historia_medica(self):
        # Obtener fechas de inicio y fin
        desde = self.entry_desde.get()
        hasta = self.entry_hasta.get()

        # Consulta SQL para obtener los pacientes con historias médicas en el rango de fechas especificado
        sql = f"SELECT Persona.cedula, Persona.nombres, Persona.apellidos, Persona.carrera, historiaMedic.motivo, historiaMedic.fechaHistoria FROM Persona INNER JOIN historiaMedic ON Persona.idPersona = historiaMedic.idPersona WHERE historiaMedic.fechaHistoria BETWEEN '{desde}' AND '{hasta}'"
        self.conexion_db.cursor.execute(sql)
        pacientes = self.conexion_db.cursor.fetchall()

        data = [['Cédula', 'Nombres', 'Apellidos','Carrea','Motivo','Fecha de Historia Médica']]
        for paciente in pacientes:
            data.append(list(paciente))

        # Obtener el estilo del encabezado
        estilo_encabezado = getSampleStyleSheet()["Heading1"]

        # Crear el documento PDF
        pdf_file = "Reporte_Historia_Medica_{}_{}.pdf".format(desde, hasta)
        pdf = SimpleDocTemplate(pdf_file, pagesize=letter)

        # Contenido del PDF
        contenido = []

        # Agregar encabezado al contenido del PDF
        encabezado = f"UNIVERSIDAD TÉCNICA ESTATAL DE QUEVEDO\n\nUNIDAD DE BIENESTAR CENTRO MÉDICO\n\n Reporte de historias médicas  desde {desde} hasta {hasta}\n"
        contenido.append(Paragraph(encabezado, estilo_encabezado))
        contenido.append(Spacer(1, 20))  # Agregar un espacio en blanco


        # Agregar la tabla de pacientes
        tabla_pacientes = Table(data)
        style = TableStyle([('BACKGROUND', (0, 0), (-1, 0), '#77D9D3'),
                            ('TEXTCOLOR', (0, 0), (-1, 0), '#FFFFFF'),
                            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                            ('BACKGROUND', (0, 1), (-1, -1), '#C1E8F4'),
                            ('GRID', (0, 0), (-1, -1), 1, '#000000')])
        
        tabla_pacientes.setStyle(style)
        contenido.append(tabla_pacientes)

        # Construir el PDF
        pdf.build(contenido)
        subprocess.Popen([pdf_file], shell=True)


#fin seccion historiaMedica reportes--------------------


#seccion pacientes reportes-------------------------------------
    def mostrar_seccion_pacientes(self):
        # Limpiar el contenedor
        for widget in self.contenedor_seccion.winfo_children():
            widget.destroy()
        
        # Crear un marco para contener los botones
        marco_botones = tk.Frame(self.contenedor_seccion)
        marco_botones.pack(fill="both", expand=True, padx=10, pady=10)

        # Crear y mostrar los botones de la sección de pacientes
        self.btnEdad = tk.Button(marco_botones, text="Edad", width=15, command=self.mostrar_seccion_edad)
        self.btnEdad.pack(side="left", fill="both", expand=True, padx=5, pady=(0, 5))

        btnCarrera = tk.Button(marco_botones, text="Carrera", width=15, command=self.mostrar_seccion_carrera)
        btnCarrera.pack(side="left", fill="both", expand=True, padx=5, pady=(0, 5))

        btnGenero = tk.Button(marco_botones, text="Género", width=15, command=self.mostrar_seccion_genero)
        btnGenero.pack(side="left", fill="both", expand=True, padx=5, pady=(0, 5))

        btnFechaRegistro = tk.Button(marco_botones, text="Fecha de Registro", width=15, command=self.mostrar_seccion_fecha_registro)
        btnFechaRegistro.pack(side="left", fill="both", expand=True, padx=5, pady=(0, 5))

        # Centrar los botones en la parte superior del contenedor
        marco_botones.pack(side="top", fill="x", anchor="n")


#paciente por fecha de registro____________
    def mostrar_seccion_fecha_registro(self):
        # Limpiar el contenedor
        for widget in self.contenedor_seccion.winfo_children():
            widget.destroy()

        # Crear un marco para contener la sección de búsqueda por fecha de registro
        marco_fecha_registro = tk.Frame(self.contenedor_seccion)
        marco_fecha_registro.grid(row=0, column=0, sticky="nsew")  # Hacemos que el marco se expanda en todas las direcciones

        # Etiqueta y Entry para la fecha de inicio
        lbl_desde = tk.Label(marco_fecha_registro, text="Desde: (DD-MM-AAAA)")
        lbl_desde.grid(row=0, column=0, padx=5, pady=5)

        self.entry_desde = tk.Entry(marco_fecha_registro)
        self.entry_desde.grid(row=0, column=1, padx=5, pady=5)

        # Etiqueta y Entry para la fecha de fin
        lbl_hasta = tk.Label(marco_fecha_registro, text="Hasta: (DD-MM-AAAA)")
        lbl_hasta.grid(row=0, column=2, padx=5, pady=5)

        self.entry_hasta = tk.Entry(marco_fecha_registro)
        self.entry_hasta.grid(row=0, column=3, padx=5, pady=5)

        # Botón para buscar pacientes por fecha de registro
        btn_buscar = tk.Button(marco_fecha_registro, text="Buscar", command=self.buscar_pacientes_por_fecha_registro)
        btn_buscar.grid(row=0, column=4, padx=5, pady=5)

        # Botón para generar el reporte en PDF
        btn_generar_reporte = tk.Button(marco_fecha_registro, text="Generar Reporte", command=self.generar_reporte_fecha_registro)
        btn_generar_reporte.grid(row=1, column=0, columnspan=5, padx=10, pady=10)

        # Marco para la tabla y las barras de desplazamiento
        marco_tabla = tk.Frame(marco_fecha_registro)
        marco_tabla.grid(row=2, column=0, columnspan=5, padx=10, pady=10, sticky="nsew")  # Hacemos que el marco se expanda

        # Tabla de pacientes con encabezados
        self.tabla_pacientes_fecha_registro = ttk.Treeview(marco_tabla, columns=('Cédula', 'Nombres', 'Apellidos', 'Edad', 'Carrera', 'Género', 'Fecha de Registro'), show='headings')
        self.tabla_pacientes_fecha_registro.grid(row=0, column=0, sticky="nsew")

        # Agregar encabezados
        for col in ('Cédula', 'Nombres', 'Apellidos', 'Edad', 'Carrera', 'Género', 'Fecha de Registro'):
            self.tabla_pacientes_fecha_registro.heading(col, text=col)

        # Agregar barras de desplazamiento
        scroll_vertical = ttk.Scrollbar(marco_tabla, orient="vertical", command=self.tabla_pacientes_fecha_registro.yview)
        scroll_vertical.grid(row=0, column=1, sticky="ns")

        scroll_horizontal = ttk.Scrollbar(marco_tabla, orient="horizontal", command=self.tabla_pacientes_fecha_registro.xview)
        scroll_horizontal.grid(row=1, column=0, sticky="ew")

        # Configurar la tabla
        self.tabla_pacientes_fecha_registro.configure(yscrollcommand=scroll_vertical.set, xscrollcommand=scroll_horizontal.set)

        # Ajustar el tamaño del contenedor principal
        self.contenedor_seccion.columnconfigure(0, weight=1)
        self.contenedor_seccion.rowconfigure(0, weight=1)

        # Ajustar el tamaño de las columnas en el marco de fecha de registro
        marco_fecha_registro.columnconfigure(0, weight=1)
        marco_fecha_registro.columnconfigure(1, weight=1)
        marco_fecha_registro.columnconfigure(2, weight=1)
        marco_fecha_registro.columnconfigure(3, weight=1)
        marco_fecha_registro.columnconfigure(4, weight=1)


    def buscar_pacientes_por_fecha_registro(self):
        # Limpiar tabla
        for item in self.tabla_pacientes_fecha_registro.get_children():
            self.tabla_pacientes_fecha_registro.delete(item)

        # Obtener fechas de inicio y fin
        desde = self.entry_desde.get()
        hasta = self.entry_hasta.get()

        # Consulta SQL para obtener pacientes registrados entre las fechas especificadas
        sql = f"SELECT cedula, nombres, apellidos, edad, carrera, genero, fechaRegistro FROM Persona WHERE fechaRegistro BETWEEN '{desde}' AND '{hasta} AND activo = 1'"
        self.conexion_db.cursor.execute(sql)
        pacientes = self.conexion_db.cursor.fetchall()

        # Insertar datos en la tabla
        for paciente in pacientes:
            self.tabla_pacientes_fecha_registro.insert('', 'end', values=paciente)


    def generar_reporte_fecha_registro(self):
        # Obtener fechas de inicio y fin
        desde = self.entry_desde.get()
        hasta = self.entry_hasta.get()

        # Consulta SQL para obtener los pacientes registrados entre las fechas especificadas
        sql = f"SELECT cedula, nombres, apellidos, edad, carrera, genero, fechaRegistro FROM Persona WHERE fechaRegistro BETWEEN '{desde}' AND '{hasta} AND activo = 1'"
        self.conexion_db.cursor.execute(sql)
        pacientes = self.conexion_db.cursor.fetchall()

        data = [['Cédula', 'Nombres', 'Apellidos', 'Edad', 'Carrera', 'Género', 'Fecha de Registro']]
        for paciente in pacientes:
            data.append(list(paciente))

        # Obtener el estilo del encabezado
        estilo_encabezado = getSampleStyleSheet()["Heading1"]

        # Crear el documento PDF
        pdf_file = "Reporte_Pacientes_Fecha_{}_{}_{}.pdf".format(desde, hasta, datetime.now().strftime("%Y-%m-%d_%H-%M-%S"))
        pdf = SimpleDocTemplate(pdf_file, pagesize=letter)

        # Contenido del PDF
        contenido = []

        # Agregar encabezado al contenido del PDF
        encabezado = f"UNIVERSIDAD TÉCNICA ESTATAL DE QUEVEDO\n\nUNIDAD DE BIENESTAR CENTRO MÉDICO\n\n Reporte de Pacientes registrados desde {desde} hasta {hasta}\n"
        contenido.append(Paragraph(encabezado, estilo_encabezado))
        contenido.append(Spacer(1, 20))  # Agregar un espacio en blanco

        # Agregar tabla al contenido del PDF
        tabla = Table(data)
        style = TableStyle([('BACKGROUND', (0, 0), (-1, 0), '#77D9D3'),
                            ('TEXTCOLOR', (0, 0), (-1, 0), '#FFFFFF'),
                            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                            ('BACKGROUND', (0, 1), (-1, -1), '#C1E8F4'),
                            ('GRID', (0, 0), (-1, -1), 1, '#000000')])
        tabla.setStyle(style)
        contenido.append(tabla)

        # Construir el PDF
        pdf.build(contenido)
        subprocess.Popen([pdf_file], shell=True)

#fin fecha de registro-------------------------------------

#paciente por genero_______________
    def mostrar_seccion_genero(self):
        # Limpiar el contenedor
        for widget in self.contenedor_seccion.winfo_children():
            widget.destroy()

        # Crear un marco para contener la sección de búsqueda por género
        marco_genero = tk.Frame(self.contenedor_seccion)
        marco_genero.grid(row=0, column=0, sticky="nsew")  # Hacemos que el marco se expanda en todas las direcciones

        # Etiqueta para la selección de género
        lbl_genero = tk.Label(marco_genero, text="Seleccione un género:")
        lbl_genero.grid(row=0, column=0, padx=5, pady=5, sticky="e")

        # Lista desplegable para seleccionar el género
        self.lista_generos = ttk.Combobox(marco_genero, state="readonly")
        self.lista_generos.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

        # Obtener los géneros disponibles y cargarlos en la lista desplegable
        generos = self.obtener_generos()
        self.lista_generos['values'] = generos

        # Botón para buscar pacientes por género
        btn_buscar = tk.Button(marco_genero, text="Buscar", command=self.buscar_pacientes_por_genero)
        btn_buscar.grid(row=0, column=2, padx=5, pady=5, sticky="w")

        # Botón para generar el reporte en PDF
        btn_generar_reporte = tk.Button(marco_genero, text="Generar Reporte", command=self.generar_reporte_genero)
        btn_generar_reporte.grid(row=1, column=0, columnspan=3, padx=10, pady=10, sticky="ew")

        # Marco para la tabla y las barras de desplazamiento
        marco_tabla = tk.Frame(marco_genero)
        marco_tabla.grid(row=2, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")  # Hacemos que el marco se expanda

        # Tabla de pacientes con encabezados
        self.tabla_pacientes_genero = ttk.Treeview(marco_tabla, columns=('Cédula', 'Nombres', 'Apellidos', 'Edad', 'Carrera', 'Género', 'Fecha de Registro'), show='headings')
        self.tabla_pacientes_genero.grid(row=0, column=0, sticky="nsew")

        # Agregar encabezados
        for col in ('Cédula', 'Nombres', 'Apellidos', 'Edad', 'Carrera', 'Género', 'Fecha de Registro'):
            self.tabla_pacientes_genero.heading(col, text=col)

        # Agregar barras de desplazamiento
        scroll_vertical = ttk.Scrollbar(marco_tabla, orient="vertical", command=self.tabla_pacientes_genero.yview)
        scroll_vertical.grid(row=0, column=1, sticky="ns")

        scroll_horizontal = ttk.Scrollbar(marco_tabla, orient="horizontal", command=self.tabla_pacientes_genero.xview)
        scroll_horizontal.grid(row=1, column=0, sticky="ew")

        # Configurar la tabla
        self.tabla_pacientes_genero.configure(yscrollcommand=scroll_vertical.set, xscrollcommand=scroll_horizontal.set)

        # Ajustar el tamaño del contenedor principal
        self.contenedor_seccion.columnconfigure(0, weight=1)
        self.contenedor_seccion.rowconfigure(0, weight=1)

        # Ajustar el tamaño de las columnas en el marco del género
        marco_genero.columnconfigure(0, weight=1)
        marco_genero.columnconfigure(1, weight=1)
        marco_genero.columnconfigure(2, weight=1)
    
    def obtener_generos(self):
        # Consulta SQL para obtener todas las carreras distintas
        sql = "SELECT DISTINCT genero FROM Persona WHERE activo = 1"
        self.conexion_db.cursor.execute(sql)
        generos = self.conexion_db.cursor.fetchall()
        generos = [genero[0] for genero in generos]
        return generos
    
    def buscar_pacientes_por_genero(self):
        # Limpiar tabla
        for item in self.tabla_pacientes_genero.get_children():
            self.tabla_pacientes_genero.delete(item)

        # Obtener género seleccionado
        genero = self.lista_generos.get()

        # Consulta SQL para obtener pacientes del género seleccionado
        sql = f"SELECT cedula, nombres, apellidos, edad, carrera, genero, fechaRegistro FROM Persona WHERE genero = '{genero}' AND activo = 1"
        self.conexion_db.cursor.execute(sql)
        pacientes = self.conexion_db.cursor.fetchall()

        # Insertar datos en la tabla
        for paciente in pacientes:
            self.tabla_pacientes_genero.insert('', 'end', values=paciente)


    def generar_reporte_genero(self):
        # Obtener el género seleccionado
        genero = self.lista_generos.get()

        # Consulta SQL para obtener los pacientes del género seleccionado
        sql = f"SELECT cedula, nombres, apellidos, edad, carrera, genero, fechaRegistro FROM Persona WHERE genero = '{genero}' AND activo = 1"
        self.conexion_db.cursor.execute(sql)
        pacientes = self.conexion_db.cursor.fetchall()

        data = [['Cédula', 'Nombres', 'Apellidos', 'Edad', 'Carrera', 'Género', 'Fecha de Registro']]
        for paciente in pacientes:
            data.append(list(paciente))

        # Obtener el estilo del encabezado
        estilo_encabezado = getSampleStyleSheet()["Heading1"]

        # Crear el documento PDF
        pdf_file = "Reporte_Pacientes_Genero_{}_{}.pdf".format(genero, datetime.now().strftime("%Y-%m-%d_%H-%M-%S"))
        pdf = SimpleDocTemplate(pdf_file, pagesize=letter)

        # Contenido del PDF
        contenido = []

        # Agregar encabezado al contenido del PDF
        encabezado = "UNIVERSIDAD TÉCNICA ESTATAL DE QUEVEDO\n\nUNIDAD DE BIENESTAR CENTRO MÉDICO\n\nReporte de Pacientes de Género: {}\n".format(genero)
        contenido.append(Paragraph(encabezado, estilo_encabezado))
        contenido.append(Spacer(1, 20))  # Agregar un espacio en blanco

        # Agregar tabla al contenido del PDF
        tabla = Table(data)
        style = TableStyle([('BACKGROUND', (0, 0), (-1, 0), '#77D9D3'),
                            ('TEXTCOLOR', (0, 0), (-1, 0), '#FFFFFF'),
                            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                            ('BACKGROUND', (0, 1), (-1, -1), '#C1E8F4'),
                            ('GRID', (0, 0), (-1, -1), 1, '#000000')])
        tabla.setStyle(style)
        contenido.append(tabla)

        # Construir el PDF
        pdf.build(contenido)
        subprocess.Popen([pdf_file], shell=True)


#fin paciente por genero-------------------------------------



#paciente por carrera----------------------------------------
    def mostrar_seccion_carrera(self):
        # Limpiar el contenedor
        for widget in self.contenedor_seccion.winfo_children():
            widget.destroy()

        # Crear un marco para contener la sección de búsqueda por carrera 

        marco_carrera = tk.Frame(self.contenedor_seccion)
        marco_carrera.grid(row=0, column=0, sticky="nsew")  # Hacemos que el marco se expanda en todas las direcciones

        # Etiqueta para la selección de carrera
        lbl_carrera = tk.Label(marco_carrera, text="Seleccione una carrera:")
        lbl_carrera.grid(row=0, column=0, padx=5, pady=5, sticky="e")

        # Lista desplegable para seleccionar la carrera
        self.lista_carreras = ttk.Combobox(marco_carrera, state="readonly")
        self.lista_carreras.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

        # Obtener las carreras disponibles y cargarlas en la lista desplegable
        carreras = self.obtener_carreras()
        self.lista_carreras['values'] = carreras

        # Botón para buscar pacientes por carrera
        btn_buscar = tk.Button(marco_carrera, text="Buscar", command=self.buscar_pacientes_por_carrera)
        btn_buscar.grid(row=0, column=2, padx=5, pady=5, sticky="w")

        # Botón para generar el reporte en PDF
        btn_generar_reporte = tk.Button(marco_carrera, text="Generar Reporte", command=self.generar_reporte_carrera)
        btn_generar_reporte.grid(row=1, column=0, columnspan=3, padx=10, pady=10, sticky="ew")

        # Marco para la tabla y las barras de desplazamiento
        marco_tabla = tk.Frame(marco_carrera)
        marco_tabla.grid(row=2, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")  # Hacemos que el marco se expanda

        # Tabla de pacientes con encabezados
        self.tabla_pacientes_carrera = ttk.Treeview(marco_tabla, columns=('Cédula', 'Nombres', 'Apellidos', 'Edad', 'Carrera', 'Género', 'Fecha de Registro'), show='headings')
        self.tabla_pacientes_carrera.grid(row=0, column=0, sticky="nsew")

        # Agregar encabezados
        for col in ('Cédula', 'Nombres', 'Apellidos', 'Edad', 'Carrera', 'Género', 'Fecha de Registro'):
            self.tabla_pacientes_carrera.heading(col, text=col)

        # Agregar barras de desplazamiento
        scroll_vertical = ttk.Scrollbar(marco_tabla, orient="vertical", command=self.tabla_pacientes_carrera.yview)
        scroll_vertical.grid(row=0, column=1, sticky="ns")

        scroll_horizontal = ttk.Scrollbar(marco_tabla, orient="horizontal", command=self.tabla_pacientes_carrera.xview)
        scroll_horizontal.grid(row=1, column=0, sticky="ew")

        # Configurar la tabla
        self.tabla_pacientes_carrera.configure(yscrollcommand=scroll_vertical.set, xscrollcommand=scroll_horizontal.set)

        # Ajustar el tamaño del contenedor principal
        self.contenedor_seccion.columnconfigure(0, weight=1)
        self.contenedor_seccion.rowconfigure(0, weight=1)

        # Ajustar el tamaño de las columnas en el marco de la carrera
        marco_carrera.columnconfigure(0, weight=1)
        marco_carrera.columnconfigure(1, weight=1)
        marco_carrera.columnconfigure(2, weight=1)


    def obtener_carreras(self):
        # Consulta SQL para obtener todas las carreras distintas
        sql = "SELECT DISTINCT carrera FROM Persona WHERE activo = 1"
        self.conexion_db.cursor.execute(sql)
        carreras = self.conexion_db.cursor.fetchall()
        carreras = [carrera[0] for carrera in carreras]
        return carreras

    def buscar_pacientes_por_carrera(self):
        # Limpiar tabla
        for item in self.tabla_pacientes_carrera.get_children():
            self.tabla_pacientes_carrera.delete(item)

        # Obtener la carrera seleccionada
        carrera = self.lista_carreras.get()

        # Consulta SQL para obtener pacientes de la carrera seleccionada
        sql = f"SELECT cedula, nombres, apellidos, edad, carrera, genero, fechaRegistro FROM Persona WHERE carrera = '{carrera}' AND activo = 1"
        self.conexion_db.cursor.execute(sql)
        pacientes = self.conexion_db.cursor.fetchall()

        # Insertar datos en la tabla
        for paciente in pacientes:
            self.tabla_pacientes_carrera.insert('', 'end', values=paciente)
    
    
    def generar_reporte_carrera(self):
        # Obtener la carrera seleccionada
        carrera = self.lista_carreras.get()

        # Consulta SQL para obtener los pacientes de la carrera seleccionada
        sql = f"SELECT cedula, nombres, apellidos, edad, carrera, genero, fechaRegistro FROM Persona WHERE carrera = '{carrera}' AND activo = 1"
        self.conexion_db.cursor.execute(sql)
        pacientes = self.conexion_db.cursor.fetchall()

        data = [['Cédula', 'Nombres', 'Apellidos', 'Edad', 'Carrera', 'Género', 'Fecha de Registro']]
        for paciente in pacientes:
            data.append(list(paciente))

        # Obtener el estilo del encabezado
        estilo_encabezado = getSampleStyleSheet()["Heading1"]

        # Crear el documento PDF
        pdf_file = "Reporte_Pacientes_Carrera_{}_{}.pdf".format(carrera, datetime.now().strftime("%Y-%m-%d_%H-%M-%S"))
        pdf = SimpleDocTemplate(pdf_file, pagesize=letter)

        # Contenido del PDF
        contenido = []

        # Agregar encabezado al contenido del PDF
        encabezado = "UNIVERSIDAD TÉCNICA ESTATAL DE QUEVEDO\n\nUNIDAD DE BIENESTAR CENTRO MÉDICO\n\nReporte de Pacientes de la Carrera: {}\n".format(carrera)
        contenido.append(Paragraph(encabezado, estilo_encabezado))
        contenido.append(Spacer(1, 20))  # Agregar un espacio en blanco

        # Agregar tabla al contenido del PDF
        tabla = Table(data)
        style = TableStyle([('BACKGROUND', (0, 0), (-1, 0), '#77D9D3'),
                            ('TEXTCOLOR', (0, 0), (-1, 0), '#FFFFFF'),
                            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                            ('BACKGROUND', (0, 1), (-1, -1), '#C1E8F4'),
                            ('GRID', (0, 0), (-1, -1), 1, '#000000')])
        tabla.setStyle(style)
        contenido.append(tabla)

        # Construir el PDF
        pdf.build(contenido)
        subprocess.Popen([pdf_file], shell=True)



#por paciente por edad--------------------------------------------------------
    def mostrar_seccion_edad(self):
        # Limpiar el contenedor
        for widget in self.contenedor_seccion.winfo_children():
            widget.destroy()

        # Crear un marco para contener la sección de búsqueda por edad
        marco_edad = tk.Frame(self.contenedor_seccion)
        marco_edad.grid(row=0, column=0, sticky="nsew")  # Hacemos que el marco se expanda en todas las direcciones

        # Etiquetas y Entry para el rango de edad
        lbl_desde = tk.Label(marco_edad, text="Desde:(años)")
        lbl_desde.grid(row=0, column=0, padx=5, pady=5)

        self.entry_desde = tk.Entry(marco_edad)
        self.entry_desde.grid(row=0, column=1, padx=5, pady=5)

        lbl_hasta = tk.Label(marco_edad, text="Hasta: (años)")
        lbl_hasta.grid(row=0, column=2, padx=5, pady=5)

        self.entry_hasta = tk.Entry(marco_edad)
        self.entry_hasta.grid(row=0, column=3, padx=5, pady=5)

        # Botón para buscar pacientes por rango de edad
        btn_buscar = tk.Button(marco_edad, text="Buscar", command=self.buscar_pacientes)
        btn_buscar.grid(row=0, column=4, padx=5, pady=5)

        # Marco para la tabla y las barras de desplazamiento
        marco_tabla = tk.Frame(marco_edad)
        marco_tabla.grid(row=1, column=0, columnspan=5, padx=10, pady=10, sticky="nsew")  # Hacemos que el marco se expanda

        # Tabla de pacientes con encabezados
        self.tabla_pacientes = ttk.Treeview(marco_tabla, columns=('Cédula', 'Nombres', 'Apellidos', 'Edad', 'Carrera', 'Género', 'Fecha de Registro'), show='headings')
        self.tabla_pacientes.grid(row=0, column=0, sticky="nsew")

        # Agregar encabezados
        for col in ('Cédula', 'Nombres', 'Apellidos', 'Edad', 'Carrera', 'Género', 'Fecha de Registro'):
            self.tabla_pacientes.heading(col, text=col)

        # Agregar barras de desplazamiento
        scroll_vertical = ttk.Scrollbar(marco_tabla, orient="vertical", command=self.tabla_pacientes.yview)
        scroll_vertical.grid(row=0, column=1, sticky="ns")

        scroll_horizontal = ttk.Scrollbar(marco_tabla, orient="horizontal", command=self.tabla_pacientes.xview)
        scroll_horizontal.grid(row=1, column=0, sticky="ew")

        # Configurar la tabla
        self.tabla_pacientes.configure(yscrollcommand=scroll_vertical.set, xscrollcommand=scroll_horizontal.set)

        # Botón para generar el reporte en PDF
        btn_generar_reporte = tk.Button(marco_edad, text="Generar Reporte", command=self.generar_reporte)
        btn_generar_reporte.grid(row=2, column=0, columnspan=5, padx=10, pady=10)

        # Ajustar el tamaño de las columnas y filas del marco
        marco_edad.columnconfigure(0, weight=1)  # Ajustamos la primera columna
        marco_edad.rowconfigure(1, weight=1)     # Ajustamos la segunda fila

        # Ajustar el tamaño del contenedor principal
        self.contenedor_seccion.columnconfigure(0, weight=1)
        self.contenedor_seccion.rowconfigure(0, weight=1)


#fin report---------------

    def buscar_pacientes(self):
        # Limpiar tabla
        for item in self.tabla_pacientes.get_children():
            self.tabla_pacientes.delete(item)

        # Obtener rango de edad
        desde = int(self.entry_desde.get())
        hasta = int(self.entry_hasta.get())

        # Consulta SQL para obtener pacientes dentro del rango de edad
        sql = f"SELECT cedula, nombres, apellidos, edad, carrera, genero, fechaRegistro FROM Persona WHERE edad BETWEEN {desde} AND {hasta} AND activo = 1"
        self.conexion_db.cursor.execute(sql)
        pacientes = self.conexion_db.cursor.fetchall()

        # Insertar datos en la tabla
        for paciente in pacientes:
            self.tabla_pacientes.insert('', 'end', values=paciente)

    def generar_reporte(self):
        # Obtener el rango de edad especificado
        desde = int(self.entry_desde.get())
        hasta = int(self.entry_hasta.get())

        # Consulta SQL para obtener los pacientes dentro del rango de edad especificado
        sql = f"SELECT cedula, nombres, apellidos, edad, carrera, genero, fechaRegistro FROM Persona WHERE edad BETWEEN {desde} AND {hasta} AND activo = 1"
        self.conexion_db.cursor.execute(sql)
        pacientes = self.conexion_db.cursor.fetchall()

        data = [['Cédula', 'Nombres', 'Apellidos', 'Edad', 'Carrera', 'Género', 'Fecha de Registro']]
        for paciente in pacientes:
            data.append(list(paciente))

        # Obtener el estilo del encabezado
        estilo_encabezado = getSampleStyleSheet()["Heading1"]

        # Crear el documento PDF
        pdf_file = "Reporte_Pacientes_{}.pdf".format(datetime.now()).replace(" ","-").replace(":",".")
        pdf = SimpleDocTemplate(pdf_file, pagesize=letter)

        # Contenido del PDF
        contenido = []

        # Agregar encabezado al contenido del PDF
        encabezado = "UNIVERSIDAD TÉCNICA ESTATAL DE QUEVEDO\n\nUNIDAD DE BIENESTAR CENTRO MÉDICO\n\nREPORTE DE PACIENTES POR EDAD\n\nDE: {}\n\nHASTA: {}".format(desde, hasta)
        contenido.append(Paragraph(encabezado, estilo_encabezado))
        contenido.append(Spacer(1, 20))  # Agregar un espacio en blanco

        # Agregar tabla al contenido del PDF
        tabla = Table(data)
        style = TableStyle([('BACKGROUND', (0, 0), (-1, 0), '#77D9D3'),
                            ('TEXTCOLOR', (0, 0), (-1, 0), '#FFFFFF'),
                            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                            ('BACKGROUND', (0, 1), (-1, -1), '#C1E8F4'),
                            ('GRID', (0, 0), (-1, -1), 1, '#000000')])
        tabla.setStyle(style)
        contenido.append(tabla)

        # Construir el PDF
        pdf.build(contenido)
        subprocess.Popen([pdf_file], shell=True)



    def generar_reporte(self):
        # Obtener el rango de edad especificado
        desde = int(self.entry_desde.get())
        hasta = int(self.entry_hasta.get())

        # Consulta SQL para obtener los pacientes dentro del rango de edad especificado
        sql = f"SELECT cedula, nombres, apellidos, edad, carrera, genero, fechaRegistro FROM Persona WHERE edad BETWEEN {desde} AND {hasta} AND activo = 1"
        self.conexion_db.cursor.execute(sql)
        pacientes = self.conexion_db.cursor.fetchall()

        data = [['Cédula', 'Nombres', 'Apellidos', 'Edad', 'Carrera', 'Género', 'Fecha de Registro']]
        for paciente in pacientes:
            data.append(list(paciente))

        # Obtener el estilo del encabezado
        estilo_encabezado = getSampleStyleSheet()["Heading1"]

        # Crear el documento PDF
        pdf_file = "Reporte_Pacientes_{}.pdf".format(datetime.now()).replace(" ","-").replace(":",".")
        pdf = SimpleDocTemplate(pdf_file, pagesize=letter)

        # Contenido del PDF
        contenido = []

        # Agregar encabezado al contenido del PDF
        encabezado = "UNIVERSIDAD TÉCNICA ESTATAL DE QUEVEDO\n\n   UNIDAD DE BIENESTAR CENTRO MÉDICO\n\nREPORTE DE PACIENTES POR EDAD \n\n DE: {} \n\n HASTA: {}".format(desde, hasta)
        contenido.append(Paragraph(encabezado, estilo_encabezado))  

        # Agregar tabla al contenido del PDF
        tabla = Table(data)
        style = TableStyle([('BACKGROUND', (0, 0), (-1, 0), '#77D9D3'),
                            ('TEXTCOLOR', (0, 0), (-1, 0), '#FFFFFF'),
                            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                            ('BACKGROUND', (0, 1), (-1, -1), '#C1E8F4'),
                            ('GRID', (0, 0), (-1, -1), 1, '#000000')])
        tabla.setStyle(style)
        contenido.append(tabla)

        # Construir el PDF
        pdf.build(contenido)
        subprocess.Popen([pdf_file], shell=True)

#seccion de reportes de recetas-------------------------------
    def mostrar_seccion_recetas(self):
        # Limpiar el contenedor
        for widget in self.contenedor_seccion.winfo_children():
            widget.destroy()

        # Crear un marco para contener la sección de búsqueda por recetas
        marco_recetas = tk.Frame(self.contenedor_seccion)
        marco_recetas.grid(row=0, column=0, sticky="nsew")  

        # Etiqueta y Entry para la fecha de inicio
        lbl_desde = tk.Label(marco_recetas, text="Desde (DD-MM-AAAA):")
        lbl_desde.grid(row=0, column=0, padx=5, pady=5)

        self.entry_desde_recetas = tk.Entry(marco_recetas)
        self.entry_desde_recetas.grid(row=0, column=1, padx=5, pady=5)

        # Etiqueta y Entry para la fecha de fin
        lbl_hasta = tk.Label(marco_recetas, text="Hasta (DD-MM-AAAA):")
        lbl_hasta.grid(row=0, column=2, padx=5, pady=5)

        self.entry_hasta_recetas = tk.Entry(marco_recetas)
        self.entry_hasta_recetas.grid(row=0, column=3, padx=5, pady=5)

        # Botón para buscar pacientes por recetas
        btn_buscar_recetas = tk.Button(marco_recetas, text="Buscar", command=self.buscar_pacientes_por_recetas)
        btn_buscar_recetas.grid(row=0, column=4, padx=5, pady=5)

        # Botón para generar el reporte en PDF
        btn_generar_reporte_recetas = tk.Button(marco_recetas, text="Generar Reporte", command=self.generar_reporte_recetas)
        btn_generar_reporte_recetas.grid(row=1, column=0, columnspan=5, padx=10, pady=10)

        # Marco para la tabla y las barras de desplazamiento
        marco_tabla_recetas = tk.Frame(marco_recetas)
        marco_tabla_recetas.grid(row=2, column=0, columnspan=5, padx=10, pady=10, sticky="nsew")  

        # Tabla de pacientes con encabezados
        self.tabla_pacientes_recetas = ttk.Treeview(marco_tabla_recetas, columns=('Cédula', 'Nombres', 'Apellidos', 'Fecha de Receta'), show='headings')
        self.tabla_pacientes_recetas.grid(row=0, column=0, sticky="nsew")

        # Agregar encabezados
        for col in ('Cédula', 'Nombres', 'Apellidos', 'Fecha de Receta'):
            self.tabla_pacientes_recetas.heading(col, text=col)

        # Agregar barras de desplazamiento
        scroll_vertical_recetas = ttk.Scrollbar(marco_tabla_recetas, orient="vertical", command=self.tabla_pacientes_recetas.yview)
        scroll_vertical_recetas.grid(row=0, column=1, sticky="ns")

        scroll_horizontal_recetas = ttk.Scrollbar(marco_tabla_recetas, orient="horizontal", command=self.tabla_pacientes_recetas.xview)
        scroll_horizontal_recetas.grid(row=1, column=0, sticky="ew")

        # Configurar la tabla
        self.tabla_pacientes_recetas.configure(yscrollcommand=scroll_vertical_recetas.set, xscrollcommand=scroll_horizontal_recetas.set)

        # Ajustar el tamaño del contenedor principal
        self.contenedor_seccion.columnconfigure(0, weight=1)
        self.contenedor_seccion.rowconfigure(0, weight=1)

        # Ajustar el tamaño de las columnas en el marco de recetas
        marco_recetas.columnconfigure(0, weight=1)
        marco_recetas.columnconfigure(1, weight=1)
        marco_recetas.columnconfigure(2, weight=1)
        marco_recetas.columnconfigure(3, weight=1)
        marco_recetas.columnconfigure(4, weight=1)

    def buscar_pacientes_por_recetas(self):
        # Limpiar tabla
        for item in self.tabla_pacientes_recetas.get_children():
            self.tabla_pacientes_recetas.delete(item)

        # Obtener fechas de inicio y fin
        desde_recetas = self.entry_desde_recetas.get()
        hasta_recetas = self.entry_hasta_recetas.get()

        # Consulta SQL para obtener pacientes con recetas en el rango de fechas especificado
        sql_recetas = f"SELECT Persona.cedula, Persona.nombres, Persona.apellidos, Receta.fechaReceta FROM Persona INNER JOIN historiaMedic ON Persona.idPersona = historiaMedic.idPersona INNER JOIN Receta ON historiaMedic.idHistoriaMedica = Receta.idHistoriaMedica WHERE Receta.fechaReceta BETWEEN '{desde_recetas}' AND '{hasta_recetas} AND Persona.activo = 1'"
        self.conexion_db.cursor.execute(sql_recetas)
        pacientes_recetas = self.conexion_db.cursor.fetchall()

        # Insertar datos en la tabla
        for paciente_receta in pacientes_recetas:
            self.tabla_pacientes_recetas.insert('', 'end', values=paciente_receta)

    def generar_reporte_recetas(self):
        # Obtener fechas de inicio y fin
        desde_recetas = self.entry_desde_recetas.get()
        hasta_recetas = self.entry_hasta_recetas.get()

        # Consulta SQL para obtener los pacientes con recetas en el rango de fechas especificado
        sql_recetas = f"SELECT Persona.cedula, Persona.nombres, Persona.apellidos, Receta.fechaReceta FROM Persona INNER JOIN historiaMedic ON Persona.idPersona = historiaMedic.idPersona INNER JOIN Receta ON historiaMedic.idHistoriaMedica = Receta.idHistoriaMedica WHERE Receta.fechaReceta BETWEEN '{desde_recetas}' AND '{hasta_recetas} AND Persona.activo = 1'"
        self.conexion_db.cursor.execute(sql_recetas)
        pacientes_recetas = self.conexion_db.cursor.fetchall()

        data_recetas = [['Cédula', 'Nombres', 'Apellidos', 'Fecha de Receta']]
        for paciente_receta in pacientes_recetas:
            data_recetas.append(list(paciente_receta))

        # Obtener el estilo del encabezado
        estilo_encabezado_recetas = getSampleStyleSheet()["Heading1"]

        # Crear el documento PDF para recetas
        pdf_file_recetas = "Reporte_Recetas_{}_{}.pdf".format(desde_recetas, hasta_recetas)
        pdf_recetas = SimpleDocTemplate(pdf_file_recetas, pagesize=letter)

        # Contenido del PDF para recetas
        contenido_recetas = []

        # Agregar encabezado al contenido del PDF para recetas
        encabezado_recetas = f"UNIVERSIDAD TÉCNICA ESTATAL DE QUEVEDO\n\nUNIDAD DE BIENESTAR CENTRO MÉDICO\n\n Reporte de recetas  desde {desde_recetas} hasta {hasta_recetas}\n"
        contenido_recetas.append(Paragraph(encabezado_recetas, estilo_encabezado_recetas))
        contenido_recetas.append(Spacer(1, 20))  # Agregar un espacio en blanco

        # Agregar la tabla de pacientes con recetas
        tabla_pacientes_recetas = Table(data_recetas)
        style_recetas = TableStyle([('BACKGROUND', (0, 0), (-1, 0), '#77D9D3'),
                                    ('TEXTCOLOR', (0, 0), (-1, 0), '#FFFFFF'),
                                    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                                    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                                    ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                                    ('BACKGROUND', (0, 1), (-1, -1), '#C1E8F4'),
                                    ('GRID', (0, 0), (-1, -1), 1, '#000000')])

        tabla_pacientes_recetas.setStyle(style_recetas)
        contenido_recetas.append(tabla_pacientes_recetas)

        # Construir el PDF para recetas
        pdf_recetas.build(contenido_recetas)
        subprocess.Popen([pdf_file_recetas], shell=True)


#fin reportes de recetas----------------------------------------
            
#trabajando en reportes--------------------------------    
    def guardarPaciente(self):
        persona = Persona(
            self.svFecha.get(), self.svNombre.get(), self.svApellidos.get(), self.svFechaNacimiento.get(), self.svCedula.get(), self.svEdad.get(), 
            self.svEstadoCivil.get(), self.svDomicilio.get(), self.svTelefono.get(), self.svApp.get(), self.svAPF.get(), self.svAGO.get(), 
            self.svAlergia.get(), self.svCorreo.get(), self.svCarrera.get(), self.svGenero.get(),self.svSemestre.get()
        )
       
        if self.idPersona ==None:
            guardarDatosPaciente(persona)
        else:
            editarDatoPaciente(persona, self.idPersona)
          
        self.deshabilitar()
        self.tablaPaciente()


    def buscarCondicion(self):
        if len(self.svBuscarDni.get()) > 0 or len(self.svBuscarApellido.get()) > 0 or len(self.svBuscarCarrera.get()) > 0:
            where = "WHERE 1=1"
            if len(self.svBuscarDni.get()) > 0:
                # Agrega la condición para buscar por cédula
                where += f" AND cedula = {self.svBuscarDni.get()} AND activo = 1"
            if len(self.svBuscarApellido.get()) > 0:
                # Agrega la condición para buscar por apellido
                where += f" AND apellidos LIKE '{self.svBuscarApellido.get()}%' AND activo = 1"
            if len(self.svBuscarCarrera.get()) > 0:
                # Agrega la condición para buscar por carrera
                where += f" AND carrera LIKE '{self.svBuscarCarrera.get()}%' AND activo = 1"
            self.tablaPaciente(where)
        else:
            self.tablaPaciente()





    def limpiarBuscador(self):
        self.svBuscarApellido.set('')
        self.svBuscarDni.set('')
        self.svBuscarCarrera.set('')
        self.tablaPaciente()


    def habilitar(self):

        # Actualizar l tabla de pacientes
        self.svCarrera.set('')
        self.svSemestre.set('')
        self.svGenero.set('')
        self.svNombre.set('')
        self.svApellidos.set('')
        self.svCedula.set('')
        self.svFechaNacimiento.set('')
        self.svEdad.set('')
        self.svEstadoCivil.set('')
        self.svDomicilio.set('')
        self.svTelefono.set('')
        self.svCorreo.set('')
        self.svApp.set('')
        self.svAPF.set('')
        self.svAGO.set('')
        self.svAlergia.set('')

        self.entryCarrera.config(state='normal')
        self.entrySemestre.config(state='normal')
        self.entryNombre.config(state='normal')
        self.entryApellidos.config(state='normal')
        self.entryCedula.config(state='normal')
        self.entryFechaNacimiento.config(state='normal')
        self.entryEdad.config(state='normal')
        self.entryEstadoCivil.config(state='normal')
        self.entryDomicilio.config(state='normal')
        self.entryTelefono.config(state='normal')
        self.entryCorreo.config(state='normal')
        self.entryApp.config(state='normal')
        self.entryAPF.config(state='normal')
        self.entryAGO.config(state='normal')
        self.entryAlergia.config(state='normal')
        self.btnGuardar.config(state='normal')
        self.btnCancelar.config(state='normal')

    def deshabilitar(self):
        self.idPersona =None
        self.svCarrera.set('')
        self.svSemestre.set('')
        self.svGenero.set('')
        self.svNombre.set('')
        self.svApellidos.set('')
        self.svCedula.set('')
        self.svFechaNacimiento.set('')
        self.svEdad.set('')
        self.svEstadoCivil.set('')
        self.svDomicilio.set('')
        self.svTelefono.set('')
        self.svCorreo.set('')
        self.svApp.set('')
        self.svAPF.set('')
        self.svAGO.set('')
        self.svAlergia.set('')


        self.entryCarrera.config(state='disabled')
        self.entrySemestre.config(state='disabled')
        self.entryNombre.config(state='disabled')
        self.entryApellidos.config(state='disabled')
        self.entryCedula.config(state='disabled')
        self.entryFechaNacimiento.config(state='disabled')
        self.entryEdad.config(state='disabled')
        self.entryEstadoCivil.config(state='disabled')
        self.entryDomicilio.config(state='disabled')
        self.entryTelefono.config(state='disabled')
        self.entryCorreo.config(state='disabled')
        self.entryApp.config(state='disabled')
        self.entryAPF.config(state='disabled')
        self.entryAGO.config(state='disabled')
        self.entryAlergia.config(state='disabled')


        self.btnGuardar.config(state='disabled')
        self.btnCancelar.config(state='disabled')
    

    def tablaPaciente(self, where=""):

        if len(where) > 0:
            self.listaPersona = listarCondicion(where)
        else:
            self.listaPersona = listar()
        
        self.tabla = ttk.Treeview(self, column=('Fecha_registro','Nombres', 'Apellidos', 'fecha_nacimiento', 'Cédula', 
                                                'edad','estado_civil','Domicilio','telefono','app', 'apf','ago','alergias',
                                                'correo','Carrera', 'Género', 'Semestre'))
        self.tabla.grid(column=1, row=18, columnspan=8, sticky='nsew')
        self.tabla.bind('<<TreeviewSelect>>', self.on_select_paciente)

        self.scroll = ttk.Scrollbar(self, orient='vertical', command=self.tabla.yview)
        self.scroll.grid(row=18, column=5, sticky='nse')
        
        self.tabla.configure(yscrollcommand=self.scroll.set, height=8)
        self.tabla.tag_configure('evenrow', background='#C5EAFE')

        self.tabla.heading('#0', text='ID')
        self.tabla.heading('Fecha_registro', text='Fecha_registro')
        self.tabla.heading('Nombres', text='Nombres')
        self.tabla.heading('Apellidos', text='Apellidos')
        self.tabla.heading('Cédula', text='Cédula')
        self.tabla.heading('fecha_nacimiento', text='fecha_nacimiento')
        self.tabla.heading('edad', text='edad')
        self.tabla.heading('estado_civil', text='estado_civil')
        self.tabla.heading('Domicilio', text='Domicilio')
        self.tabla.heading('telefono', text='telefono')
        self.tabla.heading('app', text='app')
        self.tabla.heading('apf', text='apf')
        self.tabla.heading('ago', text='ago')
        self.tabla.heading('alergias', text='alergias')
        self.tabla.heading('correo', text='correo')
        self.tabla.heading('Carrera', text='Carrera')
        self.tabla.heading('Género', text='Género')
        self.tabla.heading('Semestre', text='Semestre')

        self.tabla.column("#0", anchor=W, width=20)
        self.tabla.column("Fecha_registro", anchor=W, width=20)
        self.tabla.column("Nombres", anchor=W, width=20)
        self.tabla.column("Apellidos", anchor=W, width=20)
        self.tabla.column("Cédula", anchor=W, width=20)
        self.tabla.column("fecha_nacimiento", anchor=W, width=20)
        self.tabla.column("edad", anchor=W, width=20)
        self.tabla.column("estado_civil", anchor=W, width=20)
        self.tabla.column("Domicilio", anchor=W, width=20)
        self.tabla.column("telefono", anchor=W, width=20)
        self.tabla.column("app", anchor=W, width=20)
        self.tabla.column("apf", anchor=W, width=20)
        self.tabla.column("ago", anchor=W, width=20)
        self.tabla.column("alergias", anchor=W, width=20)
        self.tabla.column("correo", anchor=W, width=20)
        self.tabla.column("Carrera", anchor=W, width=20)
        self.tabla.column("Género", anchor=W, width=20)
        self.tabla.column("Semestre", anchor=W, width=20)

        # Insertar datos en la tabla
        for p in self.listaPersona:
            self.tabla.insert('', 0, text=p[0], values=(p[1],p[2], p[3], p[5],p[4],p[6],p[7],p[8],p[9],p[10],p[11],p[12],p[13], p[14],p[15], p[16], p[17]), tags=('evenrow',))

        # Configurar el tamaño de la fila para que la tabla ocupe la mitad del espacio disponible
        self.grid_rowconfigure(18, weight=1)

        # Agregar botones debajo de la tabla
        self.btnEditarPaciente = tk.Button(self, text='Editar Paciente', command=self.editarPaciente)
        self.btnEditarPaciente.config(width=20,font=('ARIAL',12,'bold'), fg='#DAD5D6', bg='#1E0075', activebackground='#9379E0', cursor='hand2')
        self.btnEditarPaciente.grid(row=20, column=1, padx=1, pady=3)
       
        self.btnEliminarPaciente = tk.Button(self, text='Eliminar Paciente', command= self.eliminarDatoPaciente )
        self.btnEliminarPaciente.config(width=20,font=('ARIAL',12,'bold'), fg='#DAD5D6', bg='#8A0000', activebackground='#D58A8A', cursor='hand2')
        self.btnEliminarPaciente.grid(row=20, column=2, padx=1, pady=3)

        self.btnHistorialPaciente = tk.Button(self, text='Historial Paciente', command=self.historiaMedica)
        self.btnHistorialPaciente.config(width=20,font=('ARIAL',12,'bold'), fg='#DAD5D6', bg='#007C79', activebackground='#99F2F0', cursor='hand2')
        self.btnHistorialPaciente.grid(row=20, column=3, padx=20, pady=3)

        self.btnSalir = tk.Button(self, text='Salir', command=self.root.destroy)
        self.btnSalir.config(width=20,font=('ARIAL',12,'bold'), fg='#DAD5D6', bg='#000000', activebackground='#5E5E5E', cursor='hand2')
        self.btnSalir.grid(row=20, column=4, padx=5, pady=3)


#agg aqui
    
        #hasta aca
#desde aqui la tabla
        
    
    def historiaMedica(self):
        try:
            if self.idPersona == None:
                self.idPersona = self.tabla.item(self.tabla.selection())['text']
                self.idPersonaHistoria = self.tabla.item(self.tabla.selection())['text']
                

            if (self.idPersona > 0):
                idPersona = self.idPersona
            
            self.topHistoriaMedica = Toplevel()
            self.topHistoriaMedica.title('HISTORIAL MEDICO')
            self.topHistoriaMedica.resizable(0,0)
            self.topHistoriaMedica.config(bg='#CDD8FF')

            self.listaHistoria = listarHistoria(idPersona)
            self.tablaHistoria = ttk.Treeview(self.topHistoriaMedica, column=('Nombre','Fecha Historia', 'PA', 'FC','PESO', 'Talla', 'IMC', 'Motivo', 'Examen auxiliar', 'Detalle'))
            self.tablaHistoria.grid(row=0, column=0, columnspan=11, sticky='nse')

            self.scrollHistoria = ttk.Scrollbar(self.topHistoriaMedica, orient='vertical', command=self.tablaHistoria.yview)
            self.scrollHistoria.grid(row=0, column=12, sticky='nse')

            self.tablaHistoria.configure(yscrollcommand=self.scrollHistoria.set)
            self.tablaHistoria.heading('#0', text='ID')
            self.tablaHistoria.heading('#1', text='Nombre')
            self.tablaHistoria.heading('#2', text='Fecha Historia')
            self.tablaHistoria.heading('#3', text='PA')
            self.tablaHistoria.heading('#4', text='FC')
            self.tablaHistoria.heading('#5', text='PESO')
            self.tablaHistoria.heading('#6', text='TALLA')
            self.tablaHistoria.heading('#7', text='IMC')
            self.tablaHistoria.heading('#8', text='MOTIVO')
            self.tablaHistoria.heading('#9', text='Examen auxiliar')
            self.tablaHistoria.heading('#10', text='Detalle')

            self.tablaHistoria.column('#0', anchor=W, width=50)
            self.tablaHistoria.column('#1', anchor=W, width=100)
            self.tablaHistoria.column('#2', anchor=W, width=100)
            self.tablaHistoria.column('#3', anchor=W, width=100)
            self.tablaHistoria.column('#4', anchor=W, width=100)
            self.tablaHistoria.column('#5', anchor=W, width=100)
            self.tablaHistoria.column('#6', anchor=W, width=100)
            self.tablaHistoria.column('#7', anchor=W, width=100)
            self.tablaHistoria.column('#8', anchor=W, width=100)
            self.tablaHistoria.column('#9', anchor=W, width=100)
            self.tablaHistoria.column('#10', anchor=W, width=100)

            for p in self.listaHistoria:
                self.tablaHistoria.insert('',0, text=p[0], values=(p[1],p[2],p[4],p[5],p[6],p[7],p[8],p[3],p[9],p[10]))
  
            #hasta aca la tabla
            self.btnGuardarHistoria = tk.Button(self.topHistoriaMedica, text='Agregar Historia', command=self.topAgregarHistoria)
            self.btnGuardarHistoria.config(width=20, font=('ARIAL', 12, 'bold'), fg='#DAD5D6', bg='#002771', cursor='hand2', activebackground='#7198E0')
            self.btnGuardarHistoria.grid(row=2, column=0, padx=10, pady=5)

            self.btnEditarHistoria = tk.Button(self.topHistoriaMedica, text='Editar Historia', command=self.topEditarHistorialMedico)
            self.btnEditarHistoria.config(width=20, font=('ARIAL', 12, 'bold'), fg='#DAD5D6', bg='#3A005D', cursor='hand2', activebackground='#B47CD6')
            self.btnEditarHistoria.grid(row=2, column=1, padx=10, pady=5)

            self.btnEliminarHistoria = tk.Button(self.topHistoriaMedica, text='Eliminar Historia', command=self.eliminarHistorialMedico)
            self.btnEliminarHistoria.config(width=20, font=('ARIAL', 12, 'bold'), fg='#DAD5D6', bg='#890011', cursor='hand2', activebackground='#DB939C')
            self.btnEliminarHistoria.grid(row=2, column=2, padx=10, pady=5)

            self.btnSalirHistoria = tk.Button(self.topHistoriaMedica, text='Salir', command=self.salirTop)
            self.btnSalirHistoria.config(width=20, font=('ARIAL', 12, 'bold'), fg='#DAD5D6', bg='#000000', cursor='hand2', activebackground='#6F6F6F')
            self.btnSalirHistoria.grid(row=2, column=6, padx=10, pady=5)
        
        except:
            title = 'Editar Historia'
            mensaje = 'Error al editar historia'
            messagebox.showerror(title, mensaje)

    def salirTop(self):
        if hasattr(self, 'topAHistoria'):
            self.topAHistoria.destroy()
        self.topHistoriaMedica.destroy()
        self.idPersona = None
        
    def on_select_paciente(self, event):
        self.idPersona = self.tabla.item(self.tabla.selection())['text']
        self.idPERSONAPERS=self.tabla.item(self.tabla.selection())['text']

    def topAgregarHistoria(self):
        self.topAHistoria = Toplevel()
        
        self.topAHistoria.title('AGREGAR HISTORIA')
        self.topAHistoria.resizable(0, 0)
        self.topAHistoria.config(bg='#CDD8FF')
        
        # FRAME 1
        self.frameDatosHistoria = tk.LabelFrame(self.topAHistoria)
        self.frameDatosHistoria.config(bg='#CDD8FF')
        self.frameDatosHistoria.pack(fill="both", expand="yes", pady=10, padx=20)

        # Signos Vitales
        self.lblSignosVitales = tk.Label(self.frameDatosHistoria, text='SIGNOS VITALES', font=('ARIAL', 12, 'bold'), bg='#CDD8FF')
        self.lblSignosVitales.grid(row=0, column=0, columnspan=4, pady=5)

        #PA
        self.lblPA = tk.Label(self.frameDatosHistoria, text='PA (sistolica/diastolica):', width=20, font=('ARIAL', 12, 'bold'), bg='#CDD8FF')
        self.lblPA.grid(row=1, column=0, pady=3, padx=0, sticky='w', columnspan=2)
        
        self.svPA = tk.StringVar()
        self.entryPA = tk.Entry(self.frameDatosHistoria, width=30, textvariable=self.svPA)
        self.entryPA.config(width=20, font=('Nexa',8,'bold'))
        self.entryPA.grid(row=1, column=0, pady=3,  sticky='e')

        #FC
        self.lblFC = tk.Label(self.frameDatosHistoria, text='FC (lpm):', width=15, font=('ARIAL', 12, 'bold'), bg='#CDD8FF')
        self.lblFC.grid(row=1, column=1, pady=3, sticky='w', columnspan=2)
        
        self.svFC = tk.StringVar()
        self.entryFC = tk.Entry(self.frameDatosHistoria, width=30, textvariable=self.svFC)
        self.entryFC.config(width=20, font=('Nexa',8,'bold'))
        self.entryFC.grid(row=1, column=1, pady=3, sticky='e')

        #PESO
        self.lblPeso = tk.Label(self.frameDatosHistoria, text='PESO (kg):', width=15, font=('ARIAL', 12, 'bold'), bg='#CDD8FF')
        self.lblPeso.grid(row=2, column=0, pady=2, sticky='w', columnspan=2)
        
        self.svPESO = tk.StringVar()
        self.entryPeso = tk.Entry(self.frameDatosHistoria, width=30, textvariable=self.svPESO)
        self.entryPeso.config(width=20, font=('Nexa',8,'bold'))
        self.entryPeso.grid(row=2, column=0, pady=3, sticky='e')

        #TALLA
        self.lblTalla = tk.Label(self.frameDatosHistoria, text='TALLA (CM):', width=15, font=('ARIAL', 12, 'bold'), bg='#CDD8FF')
        self.lblTalla.grid(row=2, column=1, pady=3, sticky='w', columnspan=2)

        self.svTalla = tk.StringVar()
        self.entryTalla = tk.Entry(self.frameDatosHistoria, width=30, textvariable=self.svTalla)
        self.entryTalla.config(width=20, font=('Nexa',8,'bold'))
        self.entryTalla.grid(row=2, column=1, pady=3, sticky='e')

        #IMC
        self.lblIMC = tk.Label(self.frameDatosHistoria, text='IMC:', width=15, font=('ARIAL', 12, 'bold'), bg='#CDD8FF')
        self.lblIMC.grid(row=3, column=0, pady=3, sticky='w', columnspan=2)

        self.svICM = tk.StringVar()
        self.entryIMC = tk.Entry(self.frameDatosHistoria, width=30, textvariable=self.svICM)
        self.entryIMC.config(width=20, font=('Nexa',8,'bold'))
        self.entryIMC.grid(row=3, column=0, pady=3, sticky='e')

      # Motivo de Consulta
        self.lblMotivoConsulta = tk.Label(self.frameDatosHistoria, text='MOTIVO DE CONSULTA:', font=('ARIAL', 12, 'bold'), bg='#CDD8FF')
        self.lblMotivoConsulta.grid(row=6, column=0, columnspan=2, pady=5, sticky='nsew')

        self.svMotivoConsulta = tk.StringVar()
        self.entryMotivoConsulta = tk.Entry(self.frameDatosHistoria, width=30, textvariable=self.svMotivoConsulta)
        self.entryMotivoConsulta.config(width=30, font=('Nexa',8,'bold'))
        self.entryMotivoConsulta.grid(row=7, column=0, columnspan=2, pady=5, sticky='nsew')

        # Notas de Evolución 
        self.lblNotasEvolucion = tk.Label(self.frameDatosHistoria, text='EXAMEN AUXILIAR:', font=('ARIAL', 12, 'bold'), bg='#CDD8FF')
        self.lblNotasEvolucion.grid(row=8, column=0, pady=5, sticky='nsew')
        
        self.svExamenAuxiliar = tk.StringVar()
        self.entryExamenAuxiliar = tk.Text(self.frameDatosHistoria, width=40, height=5)
        self.entryExamenAuxiliar.grid(row=9, column=0, pady=3, sticky='nsew')
        self.entryExamenAuxiliar.bind("<KeyRelease>", self.update_svExamenAuxiliar)

        #y Prescripción Médica
        self.lblPrescripcionMedica = tk.Label(self.frameDatosHistoria, text='DETALLE:', font=('ARIAL', 12, 'bold'), bg='#CDD8FF')
        self.lblPrescripcionMedica.grid(row=8, column=1, pady=5, sticky='nsew')

        self.svDetalle = tk.StringVar()       
        self.entryDetalle = tk.Text(self.frameDatosHistoria, width=40, height=5)
        self.entryDetalle.grid(row=9, column=1, pady=3, sticky='nsew')
        self.entryDetalle.bind("<KeyRelease>", self.update_svDetalle)

#FRAME 2
        self.frameFechaHistoria = tk.LabelFrame(self.topAHistoria)
        self.frameFechaHistoria.config(bg='#CDD8FF')
        self.frameFechaHistoria.pack(fill="both", expand="yes", padx=20,pady=20)

        #LABEL FECHA AGREGAR HISTORIA
        self.lblFechaHistoria = tk.Label(self.frameFechaHistoria, text='Fecha y Hora', width=20, font=('ARIAL', 15, 'bold'), bg='#CDD8FF')
        self.lblFechaHistoria.grid(row=1, column=0, padx=5, pady=3)
        
        #ENTRY FECHA AGREGAR HISTORIA
        self.svFechaHistoria = tk.StringVar()
        self.entryFechaHistoria = tk.Entry(self.frameFechaHistoria, textvariable=self.svFechaHistoria)
        self.entryFechaHistoria.config(width=17, font=('ARIAL', 15))
        self.entryFechaHistoria.grid(row=1, column=1, padx=5, pady=3)
        #TRAER FECHA Y HORA ACTUAL
        self.svFechaHistoria.set(datetime.today().strftime('%d-%m-%Y'))

        #BUTTONS AGREGA HISTORIA
        self.btnAgregarHistoria = tk.Button(self.frameFechaHistoria, text='Nueva consulta', command=self.agregaHistorialMedico)
        self.btnAgregarHistoria.config(width=17, font=('ARIAL', 12, 'bold'), fg='#DAD5D6', bg='#000992', cursor='hand2', activebackground='#4E56C6')
        self.btnAgregarHistoria.grid(row=2, column=0, padx=10, pady=5)

        self.btnSalirAgregarHistoria = tk.Button(self.frameFechaHistoria, text='Salir',command=self.topAHistoria.destroy)
        self.btnSalirAgregarHistoria.config(width=17, font=('ARIAL', 12, 'bold'), fg='#DAD5D6', bg='#000000', cursor='hand2', activebackground='#646464')
        self.btnSalirAgregarHistoria.grid(row=2, column=3, padx=10, pady=5)
        
        self.idPersona = None
    

#rectaaaaaaaaaaaaaaaaaaaaaaaaaaaa
    def abrirVentanaReceta(self):  
        self.topRecetas.destroy()
        self.ventana_receta = tk.Toplevel()
        self.ventana_receta.title("Receta Médica")
        self.ventana_receta.geometry("925x710")
        self.ventana_receta.config(bg='#CDD8FF')
        personabusqueda=listarCondicion('where idPersona={id}'.format(id=self.idPERSONAPERS))
        personabusqueda=personabusqueda[0]      
        nombres_paciente='{primernombre} {segundonombre}'.format(primernombre=personabusqueda[2],segundonombre=personabusqueda[3])
        cedula=personabusqueda[4]
        n_historia=self.idHistoriaRec
        edad=personabusqueda[6]
        sexo=personabusqueda[16]
        numero_receta = ultimoId(n_historia)
        numero_receta = numero_receta[0][0]
        # Frame de receta
        frame_receta = tk.Frame(self.ventana_receta, bg='#CDD8FF')
        frame_receta.pack(fill="both", expand="yes", padx=20, pady=10)
        # Título
        titulo_label = tk.Label(frame_receta, text="RECETA PARA ATENCIÓN AMBULATORIA", font=('Arial', 16, 'bold'), bg='#CDD8FF')
        titulo_label.grid(row=0, column=0, columnspan=4, pady=10)
        # Servicio/Especialidad
        servicio_label = tk.Label(frame_receta, text="Servicio/Especialidad:", font=('Arial', 12), bg='#CDD8FF')
        servicio_label.grid(row=1, column=0, sticky='w')

        self.servicio_entry = tk.Entry(frame_receta, width=30)
        self.servicio_entry.grid(row=1, column=1, sticky='w')
        self.servicio_entry.insert(0, "medicina general")


        # Fecha
        fecha_label = tk.Label(frame_receta, text="Fecha:", font=('Arial', 12), bg='#CDD8FF')
        fecha_label.grid(row=2, column=0, sticky='w')
        self.fecha_entry = tk.Entry(frame_receta, width=30)
        self.fecha_entry.grid(row=2, column=1, sticky='w')
        self.fill_current_date2()  # Llama a la función para establecer la fecha actual
        # Nombre del Paciente
        nombre_label = tk.Label(frame_receta, text="Nombre del Paciente:", font=('Arial', 12), bg='#CDD8FF')
        nombre_label.grid(row=3, column=0, sticky='w')      
        textEntry = tk.StringVar()
        textEntry.set(nombres_paciente)       
        self.nombres_paciente_entry = tk.Entry(frame_receta, width=30,textvariable=textEntry)
        self.nombres_paciente_entry.grid(row=3, column=1, sticky='w')
        # Cédula
        cedula_label = tk.Label(frame_receta, text="Cédula:", font=('Arial', 12), bg='#CDD8FF')
        cedula_label.grid(row=4, column=0, sticky='w')
        textEntry = tk.StringVar()
        textEntry.set(cedula)
        self.cedula_entry = tk.Entry(frame_receta, width=30,textvariable=textEntry)
        self.cedula_entry.grid(row=4, column=1, sticky='w')
        # Edad
        edad_label = tk.Label(frame_receta, text="Edad:", font=('Arial', 12), bg='#CDD8FF')
        edad_label.grid(row=5, column=0, sticky='w')
        textEntry = tk.StringVar()
        textEntry.set(edad)
        self.edad_entry = tk.Entry(frame_receta, width=30,textvariable=textEntry)
        self.edad_entry.grid(row=5, column=1, sticky='w')         
        # Sexo
        sexo_label = tk.Label(frame_receta, text="Sexo:", font=('Arial', 12), bg='#CDD8FF')
        sexo_label.grid(row=6, column=0, sticky='w')       
        textEntry = tk.StringVar()
        textEntry.set(sexo)
        self.sexo_entry = tk.Entry(frame_receta, width=30,textvariable=textEntry)
        self.sexo_entry.grid(row=6, column=1, sticky='w')
        # Número de Receta
        n_receta_label = tk.Label(frame_receta, text="Nº Receta:", font=('Arial', 12), bg='#CDD8FF')
        n_receta_label.grid(row=7, column=0, sticky='w')     
        textEntry = tk.StringVar()
        textEntry.set(numero_receta)
        self.RecetaN_entry = tk.Entry(frame_receta, width=30,textvariable=textEntry)
        self.RecetaN_entry.grid(row=7, column=1, sticky='w')   
        # Número de Historia Médica
        historia_medica_label = tk.Label(frame_receta, text="Nº Historia Médica:", font=('Arial', 12), bg='#CDD8FF')
        historia_medica_label.grid(row=8, column=0, sticky='w')       
        textEntry = tk.StringVar()
        textEntry.set(n_historia)
        self.historiaN_entry = tk.Entry(frame_receta, width=30,textvariable=textEntry)
        self.historiaN_entry.grid(row=8, column=1, sticky='w')
        # Agregar datos del prescriptor
        datos_prescriptor_label = tk.Label(frame_receta, text="DATOS PRESCRIPTOR", font=('Arial', 14, 'bold'), bg='#CDD8FF')
        datos_prescriptor_label.grid(row=9, column=0, columnspan=4, pady=10)
        self.datos_prescriptor_entry = tk.Text(frame_receta, width=105, height=2)
        self.datos_prescriptor_entry.grid(row=10, column=0, columnspan=4, sticky='n', padx=5, pady=5)
        # Lista de medicamentos
        medicamento_frame = tk.Frame(frame_receta, bg='#CDD8FF')
        medicamento_frame.grid(row=11, column=0, columnspan=4, pady=10, padx=10, sticky='w')
        tk.Label(medicamento_frame, text="MEDICAMENTOS", font=('Arial', 14, 'bold'), bg='#CDD8FF').grid(row=0, column=0, columnspan=2, sticky='n')
        # Lista de medicamentos agregados
        medicamentos_agregados_frame = tk.Frame(frame_receta, bg='#CDD8FF')
        medicamentos_agregados_frame.grid(row=11, column=2, columnspan=2, rowspan=4, padx=10, pady=10, sticky='nse')       
        tk.Label(medicamentos_agregados_frame, text="Medicamentos Agregados", font=('Arial', 12, 'bold'), bg='#CDD8FF').grid(row=0, column=0, sticky='n')
        tk.Label(medicamentos_agregados_frame, text="Cantidad", font=('Arial', 12, 'bold'), bg='#CDD8FF').grid(row=0, column=1, sticky='n')       
        tk.Label(medicamentos_agregados_frame, text="INDICACIONES", font=('Arial', 12, 'bold'), bg='#CDD8FF').grid(row=4, column=0, sticky='n')
        self.indicaciones_text = tk.Text(medicamentos_agregados_frame, width=30, height=3)
        self.indicaciones_text.grid(row=5, column=0, sticky='n')       
        tk.Label(medicamentos_agregados_frame, text="CIE 10:", font=('Arial', 12, 'bold'), bg='#CDD8FF').grid(row=6, column=0, sticky='n')
        self.cie_text = tk.Text(medicamentos_agregados_frame, width=30, height=2)
        self.cie_text.grid(row=7, column=0, sticky='n')
        
        tk.Label(medicamentos_agregados_frame, text="ADVERTENCIAS:", font=('Arial', 12, 'bold'), bg='#CDD8FF').grid(row=8, column=0, sticky='n')
        self.adver_text = tk.Text(medicamentos_agregados_frame, width=30, height=2)
        self.adver_text.grid(row=9, column=0, sticky='n')


        self.medicamentos_agregados_text = tk.Text(medicamentos_agregados_frame, width=30, height=3)
        self.medicamentos_agregados_text.grid(row=1, column=0, sticky='nse')
        # Caja de texto para mostrar las cantidades agregadas
        self.cantidades_agregadas_text = tk.Text(medicamentos_agregados_frame, width=10, height=3)
        self.cantidades_agregadas_text.grid(row=1, column=1, sticky='nse')
        # Columna de medicamentos
        tk.Label(medicamento_frame, text="Medicamento", font=('Arial', 12), bg='#CDD8FF').grid(row=1, column=0, sticky='n')
        self.medicamento_entry = tk.Entry(medicamento_frame, width=50)
        self.medicamento_entry.grid(row=2, column=0, sticky='w')
        # Columna de cantidades
        tk.Label(medicamento_frame, text="Cantidad", font=('Arial', 12), bg='#CDD8FF').grid(row=1, column=1, sticky='n')
        self.cantidad_entry = tk.Entry(medicamento_frame, width=25)
        self.cantidad_entry.grid(row=2, column=1, sticky='w')
        # Tabla de medicamentos
        datos_med_frame = tk.Frame(frame_receta, bg='#CDD8FF')
        datos_med_frame.grid(row=12, column=0, columnspan=4, pady=10, padx=10, sticky='w')      
        tk.Label(datos_med_frame, text="DATOS DE MEDICAMENTO", font=('Arial', 14, 'bold'), bg='#CDD8FF').grid(row=0, column=3, sticky='w', columnspan=5)
        # Nombres de las columnas de la tabla
        columnas = ["Medicamento","Via de \nAdministración", "Dosis", "Frecuencia", "Duración"]
        for i, col in enumerate(columnas):
            tk.Label(datos_med_frame, text=col, font=('Arial', 10), bg='#CDD8FF', width=10).grid(row=1, column=i+2, padx=2, pady=2, sticky='w')
        # Crear la tabla
        self.filas_tabla = []
        self.medicamento_entry2 = tk.Text(datos_med_frame, width=11, height=7)
        self.medicamento_entry2.grid(row=2, column=2, padx=0, pady=2, sticky='w')
        via_admin_entry = tk.Text(datos_med_frame, width=11, height=7)
        via_admin_entry.grid(row=2, column=3, padx=2, pady=2, sticky='w')
        self.filas_tabla.append([via_admin_entry])
        dosis_entry = tk.Text(datos_med_frame, width=11, height=7)
        dosis_entry.grid(row=2, column=4, padx=2, pady=2, sticky='w')
        self.filas_tabla[-1].append(dosis_entry)
        frecuencia_entry = tk.Text(datos_med_frame, width=11, height=7, )
        frecuencia_entry.grid(row=2, column=5, padx=2, pady=2, sticky='w')
        self.filas_tabla[-1].append(frecuencia_entry)
        duracion_entry = tk.Text(datos_med_frame, width=11, height=7)
        duracion_entry.grid(row=2, column=6, padx=2, pady=2, sticky='w')
        self.filas_tabla[-1].append(duracion_entry)
        btn_frame = tk.Frame(frame_receta, bg='#CDD8FF')
        btn_frame.grid(row=13, column=0, columnspan=4, pady=20)
        tk.Button(btn_frame, text="Guardar", font=('Arial', 12), command=self.guardarrecetadef).grid(row=0, column=0, padx=10)
        tk.Button(btn_frame, text="Imprimir", font=('Arial', 12), command=self.generar_pdf).grid(row=0, column=1, padx=10)
        tk.Button(btn_frame, text="Cancelar", font=('Arial', 12), command=self.cerrar_ventana_receta).grid(row=0, column=2, padx=10)
        tk.Button(btn_frame, text="Agregar", font=('Arial', 12), command=self.agregar_medicamento).grid(row=0, column=3, padx=10)
        # Lista para almacenar medicamentos y cantidades
        self.medicamentos_list = []
        self.habilitar()
        # Actualizar la tabla de pacientes
        self.tablaPaciente()

    def cerrar_ventana_receta(self):
        self.ventana_receta.destroy()

    def fill_current_date2(self):
        current_date = datetime.now().strftime("%d-%m-%Y")
        self.fecha_entry.insert(tk.END, current_date)

    def agregar_medicamento(self):
        medicamento = self.medicamento_entry.get()
        cantidad = self.cantidad_entry.get()
        if medicamento and cantidad:
            # Agregar medicamento y cantidad a las cajas de texto correspondientes
            self.medicamentos_agregados_text.insert(tk.END, f"{medicamento}\n")
            self.cantidades_agregadas_text.insert(tk.END, f"{cantidad}\n")           
            # Agregar medicamento también al campo medicamento_entry2
            self.medicamento_entry2.insert(tk.END, f"{medicamento}\n")
            # Agregar medicamento y cantidad a la lista
            self.medicamentos_list.append((medicamento, cantidad))
            # Limpiar los campos de entrada
            self.medicamento_entry.delete(0, tk.END)
            self.cantidad_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Por favor ingrese el nombre del medicamento y la cantidad.")

    def generar_pdf(self):
            # Obtener datos del paciente y la receta
            nombres_paciente = self.nombres_paciente_entry.get()
            cedula = self.cedula_entry.get()
            historia_medica = self.historiaN_entry.get()
            n_receta = self.RecetaN_entry.get()
            sexo = self.sexo_entry.get()
            fecha = self.fecha_entry.get()
            edad = self.edad_entry.get()
            servicio_especialidad = self.servicio_entry.get()
            indicaciones = self.indicaciones_text.get("1.0", tk.END)
            datos_prescriptor = self.datos_prescriptor_entry.get("1.0", tk.END)
            cie10 = self.cie_text.get("1.0", tk.END)
            advertencias = self.adver_text.get("1.0", tk.END)
            # Obtener datos de medicamentos y cantidades de la lista
            medicamentos = [(med, cant) for med, cant in self.medicamentos_list]
            if not medicamentos:
                messagebox.showerror("Error", "Por favor agregue al menos un medicamento para generar la receta.")
                return
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", size=10)
            # Título y detalles de la receta
            pdf.cell(200, 7, txt="_____________________________________________________________________________________________________________________________________", ln=True, align='C')
            pdf.ln()
            pdf.set_font("Arial", size=10, style='B')
            pdf.cell(200, -10, txt="Receta para Atención Ambulatoria", ln=True, align='C')
            pdf.set_x(110)
            pdf.set_font("Arial", size=12, style='B')
            pdf.cell(0, 10, txt=f"Nª Receta: {n_receta}", ln=True, align='R')
            pdf.set_font("Arial", size=10)
            pdf.cell(200, 10, txt=f"Servicio/Especialidad: {servicio_especialidad}" , ln=True, align='C')
            pdf.cell(200, 10, txt=f"Fecha: {fecha}", ln=True, align='C')
            pdf.cell(200, 10, txt="_____________________________________________________________________________________________________________________________________", ln=True, align='C')
            
            
            
            # Agregar logo aqui cambias la ruta
            #image_path =  "C:/Users/BU_UTEQ-42673/Documents/imagen/logo uteq.png"
            #print("Ruta completa de la imagen:", os.path.abspath(image_path))
            #pdf.image(image_path, x=10, y=18, w=27)
            # Datos del paciente





            pdf.set_font("Arial", size=10, style='B')
            pdf.cell(200, 10, txt="DATOS DEL PACIENTE", ln=True, align='C')
            pdf.ln()  # Ajustar posición para imprimir la cédula
            pdf.set_font("Arial", size=10)
            pdf.cell(100, -10, txt=f"Nombres: {nombres_paciente}", ln=True, align='L')
            pdf.set_x(110)  # Ajustar posición para imprimir la cédula
            pdf.cell(49, 10, txt=f"H. Clinica Nª: {historia_medica}", ln=False, align='R')
            pdf.cell(40, 10, txt=f"CIE 10: {cie10}", ln=True, align='R')
            pdf.ln()
            pdf.cell(50, -10, txt=f"Cédula: {cedula}", ln=True, align='L')
            pdf.set_x(110)
            pdf.cell(36, 10, txt=f"Edad: {edad}", ln=False, align='R')
            pdf.cell(54, 10, txt=f"Sexo: {sexo}", ln=True, align='R')
            pdf.cell(200, 10, txt=f"_______________________________________________________________________________________________________________________________________", ln=True, align='C')

            # Imprimir encabezados de la tabla de medicamentos agregados
            pdf.set_font("Arial", size=10, style='B')
            pdf.cell(200, 10, txt="DATOS DEL MEDICAMENTO", ln=True, align='C')        
            pdf.set_font("Arial", size=10)
            # Imprimir encabezados de la tabla de medicamentos agregados
            pdf.cell(135, 5, txt="Medicamento", border=1, align='C')  # Ajustar ancho de celda para la columna "Medicamento"
            pdf.cell(55, 5, txt="Cantidad", border=1, align='C')  # Ajustar ancho de celda para la columna "Cantidad"
            pdf.ln()

            # Imprimir datos de la tabla de medicamentos agregados
            for med, cant in medicamentos:  # Usamos medicamentos directamente
                pdf.cell(135, 5, txt=med, border=1, align='L')  # Ajustar ancho de celda para medicamento
                pdf.cell(55, 5, txt=cant, border=1, align='C')  # Ajustar ancho de celda para cantidad
                pdf.ln()

            # Datos del prescriptor
            pdf.cell(200, 10, txt="____________________________________________________________________________________________________________________________", ln=True, align='C')
            pdf.set_font("Arial", size=10, style='B')
            pdf.cell(200, 10, txt="DATOS DEL PRESCRIPTOR", ln=True, align='C')
            pdf.set_font("Arial", size=10)
            pdf.cell(200, 10, txt=f"Nombre: {datos_prescriptor}", ln=True, align='L')
            pdf.cell(200, 12, txt="____________________________________________________________________________________________________________________________", ln=True, align='C')
            # Indicaciones
            pdf.set_font("Arial", size=10, style='B')
            pdf.cell(200, -1, txt="INDICACIONES:", ln=True, align='L')
            pdf.set_x(110)
            pdf.set_font("Arial", size=12, style='B')
            pdf.cell(0, 4, txt=f"Nª Receta: {n_receta}", ln=True, align='R')
            pdf.set_font("Arial", size=10)
            pdf.cell(200, 10, txt=f"{indicaciones}", ln=True, align='L')
            pdf.cell(50, 10, txt=f"Nombre del paciente: {nombres_paciente}", ln=True, align='L')
            pdf.cell(50, 10, txt=f"Fecha: {fecha}", ln=True, align='L')
            pdf.cell(200, 5, txt="______________________________________________________________________________________________________________________________________", ln=True, align='C')


            pdf.set_font("Arial", size=10, style='B')
            pdf.cell(200, 10, txt="MEDICAMENTOS", ln=True, align='C')
            # Imprimir encabezados de la tabla de medicamentos 
            pdf.set_font("Arial", size=7)       
            encabezados_medicamentos = ["Vía de Administración", "Dosis", "Frecuencia", "Duración"]
        
        
            pdf.set_font("Arial", size=7)  # Ajustar tamaño de fuente
            # Imprimir encabezados como fila
            # Imprimir encabezados de la tabla de medicamentos
            pdf.cell(50, 10, txt="Medicamento", border=1, align='C')  # Agregar la columna de medicamentos al inicio
            for encabezado in encabezados_medicamentos:
                pdf.cell(35, 10, txt=encabezado, border=1, align='C')  # Ajustar ancho de celda
            pdf.ln()

            # Imprimir datos de la tabla de medicamentos
            pdf.set_font("Arial", size=7)  # Ajustar tamaño de fuente
            for i in range(len(self.filas_tabla)):
                fila = self.filas_tabla[i]
                max_length = max(len(entry.get("1.0", tk.END).strip().split(',')) for entry in fila)
                max_medicamentos = len(medicamentos)
                # Asegurarnos de que iteremos sobre la longitud máxima entre las filas de entrada y los medicamentos
                for k in range(max(max_length, max_medicamentos)):
                    pdf.cell(50, 7, txt=medicamentos[k][0] if k < max_medicamentos else "", border=1, align='C')  # Imprimir medicamento
                    for entry in fila:
                        medicamento_text = entry.get("1.0", tk.END).strip()  # Obtener texto del entry y eliminar espacios en blanco
                        partes_medicamento = medicamento_text.split(",")  # Dividir el texto en partes separadas por coma
                        if len(partes_medicamento) > k:
                            pdf.cell(35, 7, txt=partes_medicamento[k].strip(), border=1, align='C')  # Ajustar ancho de celda
                        else:
                            pdf.cell(35, 7, txt="", border=1, align='C')  # Ajustar ancho de celda con celda vacía
                    pdf.ln()   # Agregar salto de línea para imprimir la próxima fila
            
            #ADVERTENCIAS
            pdf.cell(200, 10, txt="_____________________________________________________________________________________________________________________________________________________________________", ln=True, align='C')
            pdf.set_font("Arial", size=10, style='B')
            pdf.cell(200, 10, txt="ADVERTENCIAS: ", ln=True, align='C')
            pdf.set_font("Arial", size=8)
            pdf.cell(200, 10, txt=f"{advertencias}", ln=True, align='L')



            pdf_file = "receta_medica_{}.pdf".format(datetime.now()).replace(" ","-").replace(":",".")
            pdf.output(pdf_file)

            # Abrir el archivo PDF automáticamente según el sistema operativo
            if sys.platform.startswith('linux'):
                subprocess.Popen(["xdg-open", pdf_file])
            elif sys.platform.startswith('win32'):
                subprocess.Popen(["start", pdf_file], shell=True)
            elif sys.platform.startswith('cygwin'):
                subprocess.Popen(["cygstart", pdf_file])
            elif sys.platform.startswith('darwin'):
                subprocess.Popen(["open", pdf_file])
            else:
                print("No se pudo abrir el archivo PDF automáticamente.")
            
    def guardarrecetadef(self):
        # Obtener los valores ingresados en los campos de entrada y cajas de texto
        fecha_receta = self.fecha_entry.get()
        servicio_especialidad = self.servicio_entry.get()
        prescriptor_nombre = self.datos_prescriptor_entry.get("1.0", tk.END).strip()

        # Obtener los datos de los medicamentos ingresados en la tabla
        vias_administracion = self.obtener_datos_columna(0)
        dosis = self.obtener_datos_columna(1)
        frecuencia = self.obtener_datos_columna(2)
        duracion = self.obtener_datos_columna(3)
 

        # Llamar a la función guardarReceta con los valores obtenidos
        guardarReceta(self.idHistoriaMedica, fecha_receta, servicio_especialidad, prescriptor_nombre, vias_administracion, dosis, frecuencia, duracion)
        
        # Llamar al método para mostrar las recetas actualizadas
        self.mostrarRecetas(self.idHistoriaMedica)
        self.habilitar()
        self.tablaPaciente()
        self.ventana_receta.destroy()
        self.topRecetas.destroy()
        self.topEditarHistoria.destroy()
        self.topHistoriaMedica.destroy()
        self.topRecetas.destroy()
        self.idPersona = None
       

    def obtener_datos_columna(self, indice_columna):
        datos_columna = []
        for fila in self.filas_tabla:
            entry_text = fila[indice_columna].get("1.0", tk.END).strip()
            datos = entry_text.split(",")
            datos_columna.extend(datos)
        return ",".join(datos_columna)
    
    def mostrarRecetasSeleccionada(self):
        try:
            # Obtener el ID de la historia médica seleccionada en la tabla
            self.idHistoriaMedica = self.tablaHistoria.item(self.tablaHistoria.selection())['text']
            # Mostrar la tabla de recetas correspondiente
            self.mostrarRecetas(self.idHistoriaMedica)
        except Exception as e:
            title = 'Mostrar Recetas'
            mensaje = 'Error al mostrar las recetas'
            messagebox.showerror(title, mensaje)


    def mostrarRecetas(self, idHistoriaMedica):
        self.topRecetas = Toplevel()
        self.topRecetas.title('RECETAS')
        self.topRecetas.resizable(0,0)
        self.topRecetas.config(bg='#CDD8FF')

        self.listaRecetas = listarReceta(idHistoriaMedica)
        self.tablaRecetas = ttk.Treeview(self.topRecetas, column=('Fecha Receta', 'Especialidad', 'Prescriptor', 'Vías de administración', 'Dosis', 'Frecuencia', 'Duración', 'Horarios'))
        self.tablaRecetas.grid(row=0, column=0, columnspan=11, sticky='nse')

        self.scrollRecetas = ttk.Scrollbar(self.topRecetas, orient='vertical', command=self.tablaRecetas.yview)
        self.scrollRecetas.grid(row=0, column=12, sticky='nse')

        self.tablaRecetas.configure(yscrollcommand=self.scrollRecetas.set)
        self.tablaRecetas.heading('#0', text='ID')
        self.tablaRecetas.heading('#1', text='Fecha Receta')
        self.tablaRecetas.heading('#2', text='Especialidad')
        self.tablaRecetas.heading('#3', text='Prescriptor')
        self.tablaRecetas.heading('#4', text='Vías de administración')
        self.tablaRecetas.heading('#5', text='Dosis')
        self.tablaRecetas.heading('#6', text='Frecuencia')
        self.tablaRecetas.heading('#7', text='Duración')

        self.tablaRecetas.column('#0', anchor=W, width=50)
        self.tablaRecetas.column('#1', anchor=W, width=100)
        self.tablaRecetas.column('#2', anchor=W, width=100)
        self.tablaRecetas.column('#3', anchor=W, width=100)
        self.tablaRecetas.column('#4', anchor=W, width=100)
        self.tablaRecetas.column('#5', anchor=W, width=100)
        self.tablaRecetas.column('#6', anchor=W, width=100)
        self.tablaRecetas.column('#7', anchor=W, width=100)
        self.tablaRecetas.column('#8', anchor=W, width=100)

        for p in self.listaRecetas:
            self.tablaRecetas.insert('',0, text=p[0], values=(p[1],p[2],p[3],p[4],p[5],p[6],p[7]))
        
        self.btnAgregarReceta = tk.Button(self.topRecetas, text='Agregar Receta', command=self.abrirVentanaReceta)
        self.btnAgregarReceta.config(width=20, font=('ARIAL', 12, 'bold'), fg='#DAD5D6', bg='#002771', cursor='hand2', activebackground='#7198E0')
        self.btnAgregarReceta.grid(row=2, column=0, padx=10, pady=5)

        self.btnSalir = tk.Button(self.topRecetas, text='Salir', command=self.topRecetas.destroy)
        self.btnSalir.config(width=20, font=('ARIAL', 12, 'bold'), fg='#DAD5D6', bg='#002771', cursor='hand2', activebackground='#7198E0')
        self.btnSalir.grid(row=2, column=1, padx=10, pady=5)

        
       
#hasta aca recetaaaaaaaaaaaaaaaaaaaaa

    
    def update_svExamenAuxiliar(self, event):
        self.svExamenAuxiliar.set(self.entryExamenAuxiliar.get("1.0", tk.END))

    def update_svDetalle(self, event):
        self.svDetalle.set(self.entryDetalle.get("1.0", tk.END))

    def agregaHistorialMedico(self):
        try:
            # Obtener el ID del paciente seleccionado en la tabla
            self.idPersona = self.tabla.item(self.tabla.selection())['text']

            # Validar el formato de PA (Presión Arterial)
            if not re.match(r'\d{1,3}/\d{1,3}', self.svPA.get()):
                messagebox.showerror("Error", "Formato incorrecto para la Presión Arterial (PA). Debe ser en formato 'número/número'.")
                return

            # Validar que FC (Frecuencia Cardíaca) sea un número entero
            if not self.svFC.get().strip().isdigit():
                messagebox.showerror("Error", "La Frecuencia Cardíaca (FC) debe ser un número entero.")
                return

            # Validar que Peso sea un número (entero o decimal)
            if not re.match(r'\d+(\.\d+)?', self.svPESO.get().strip()):
                messagebox.showerror("Error", "El Peso debe ser un número (entero o decimal).")
                return

            # Validar que Talla sea un número (entero o decimal)
            if not re.match(r'\d+(\.\d+)?', self.svTalla.get().strip()):
                messagebox.showerror("Error", "La Talla debe ser un número (entero o decimal).")
                return

            # Validar que IMC sea un número (entero o decimal)
            if not re.match(r'\d+(\.\d+)?', self.svICM.get().strip()):
                messagebox.showerror("Error", "El Índice de Masa Corporal (IMC) debe ser un número (entero o decimal).")
                return

            # Si los campos cumplen con los formatos requeridos, guardar la historia médica
            if self.idHistoriaMedica == None:
                self.update_svExamenAuxiliar(None)  # Llama a la función para actualizar el examen auxiliar
                self.update_svDetalle(None)
                guardarHistoria(self.idPersona, self.svFechaHistoria.get(), self.svPA.get(), self.svFC.get(),  self.svPESO.get(), self.svTalla.get(), self.svICM.get(), self.svMotivoConsulta.get(),  self.svExamenAuxiliar.get(), self.svDetalle.get())
            self.topAHistoria.destroy()
            self.topHistoriaMedica.destroy()
            self.idPersona = None
        except Exception as e:
            print("Error:", e)
            messagebox.showerror("Error", "Error al agregar historia médica")
            
    def topEditarHistorialMedico(self):
        try:
            self.idHistoriaMedica = self.tablaHistoria.item(self.tablaHistoria.selection())['text']         
            self.idHistoriaRec = self.idHistoriaMedica
            self.fechaHistoriaEditar = self.tablaHistoria.item(self.tablaHistoria.selection())['values'][1]
            self.PAEditar = self.tablaHistoria.item(self.tablaHistoria.selection())['values'][2]
            self.FCEditar = self.tablaHistoria.item(self.tablaHistoria.selection())['values'][3]
            self.PesoEditar = self.tablaHistoria.item(self.tablaHistoria.selection())['values'][4]
            self.TallaEditar = self.tablaHistoria.item(self.tablaHistoria.selection())['values'][5]
            self.IMCEditar = self.tablaHistoria.item(self.tablaHistoria.selection())['values'][6]
            self.MotivoEditar = self.tablaHistoria.item(self.tablaHistoria.selection())['values'][7]
            self.ExamenAuxiliarEditar = self.tablaHistoria.item(self.tablaHistoria.selection())['values'][8]
            self.DetalleEditar = self.tablaHistoria.item(self.tablaHistoria.selection())['values'][9]
            self.topEditarHistoria = Toplevel()
            self.topEditarHistoria.title('EDITAR HISTORIA MEDICA')
            self.topEditarHistoria.resizable(0,0)
            self.topEditarHistoria.config(bg='#CDD8FF')
            #FRAME 1 EDITAR DATOS HISTORIA
            self.frameEditarHistoria = tk.LabelFrame(self.topEditarHistoria)
            self.frameEditarHistoria.config(bg='#CDD8FF')
            self.frameEditarHistoria.pack(fill="both", expand="yes", padx=20,pady=10)          
            # Signos Vitales
            self.lblSignosVitalesEditar = tk.Label(self.frameEditarHistoria, text='SIGNOS VITALES', font=('ARIAL', 12, 'bold'), bg='#CDD8FF')
            self.lblSignosVitalesEditar.grid(row=0, column=0, columnspan=4, pady=5)

            #PA
            self.lblPAEditar = tk.Label(self.frameEditarHistoria, text='PA (sistolica/diastolica):', width=20, font=('ARIAL', 12, 'bold'), bg='#CDD8FF')
            self.lblPAEditar.grid(row=1, column=0, pady=3, padx=0, sticky='w', columnspan=2)

            self.svPAEditar = tk.StringVar()
            self.entryPAEditar = tk.Entry(self.frameEditarHistoria, width=30, textvariable=self.svPAEditar)
            self.entryPAEditar.config(width=20, font=('Nexa',8,'bold'))
            self.entryPAEditar.grid(row=1, column=0, pady=3,  sticky='e')

            #FC
            self.lblFCEditar = tk.Label(self.frameEditarHistoria, text='FC (lpm):', width=15, font=('ARIAL', 12, 'bold'), bg='#CDD8FF')
            self.lblFCEditar.grid(row=1, column=1, pady=3, sticky='w', columnspan=2)
            
            self.svFCEditar = tk.StringVar()
            self.entryFCEditar = tk.Entry(self.frameEditarHistoria, width=30, textvariable=self.svFCEditar)
            self.entryFCEditar.config(width=20, font=('Nexa',8,'bold'))
            self.entryFCEditar.grid(row=1, column=1, pady=3, sticky='e')

            #PESO
            self.lblPesoEditar = tk.Label(self.frameEditarHistoria, text='PESO (kg):', width=15, font=('ARIAL', 12, 'bold'), bg='#CDD8FF')
            self.lblPesoEditar.grid(row=2, column=0, pady=2, sticky='w', columnspan=2)
            
            self.svPESOEditar = tk.StringVar()
            self.entryPesoEditar = tk.Entry(self.frameEditarHistoria, width=30, textvariable=self.svPESOEditar)
            self.entryPesoEditar.config(width=20, font=('Nexa',8,'bold'))
            self.entryPesoEditar.grid(row=2, column=0, pady=3, sticky='e')

             #TALLA
            self.lblTallaEditar = tk.Label(self.frameEditarHistoria, text='TALLA (cm):', width=15, font=('ARIAL', 12, 'bold'), bg='#CDD8FF')
            self.lblTallaEditar.grid(row=2, column=1, pady=3, sticky='w', columnspan=2)
            self.svTallaEditar = tk.StringVar()
            self.entryTallaEditar = tk.Entry(self.frameEditarHistoria, width=30, textvariable=self.svTallaEditar)
            self.entryTallaEditar.config(width=20, font=('Nexa',8,'bold'))
            self.entryTallaEditar.grid(row=2, column=1, pady=3, sticky='e')    
            #IMC
            self.lblIMCEditar = tk.Label(self.frameEditarHistoria, text='IMC:', width=15, font=('ARIAL', 12, 'bold'), bg='#CDD8FF')
            self.lblIMCEditar.grid(row=3, column=0, pady=3, sticky='w', columnspan=2)
            self.svICMEditar = tk.StringVar()
            self.entryIMCEditar = tk.Entry(self.frameEditarHistoria, width=30, textvariable=self.svICMEditar)
            self.entryIMCEditar.config(width=20, font=('Nexa',8,'bold'))
            self.entryIMCEditar.grid(row=3, column=0, pady=3, sticky='e')
             # Motivo de Consulta
            self.lblMotivoConsultaEditar = tk.Label(self.frameEditarHistoria, text='MOTIVO DE CONSULTA:', font=('ARIAL', 12, 'bold'), bg='#CDD8FF')
            self.lblMotivoConsultaEditar.grid(row=6, column=0, columnspan=2, pady=5, sticky='nsew')
            self.svMotivoConsultaEditar = tk.StringVar()
            self.entryMotivoConsultaEditar = tk.Entry(self.frameEditarHistoria, width=30, textvariable=self.svMotivoConsultaEditar)
            self.entryMotivoConsultaEditar.config(width=30, font=('Nexa',8,'bold'))
            self.entryMotivoConsultaEditar.grid(row=7, column=0, columnspan=2, pady=5, sticky='nsew')
            # Notas de Evolución
            self.lblNotasEvolucionEditar = tk.Label(self.frameEditarHistoria, text='EXAMEN AUXILIAR:', font=('ARIAL', 12, 'bold'), bg='#CDD8FF')
            self.lblNotasEvolucionEditar.grid(row=8, column=0, pady=5, sticky='nsew')
            self.svExamenAuxiliarEditar = tk.StringVar()
            self.entryExamenAuxiliarEditar = tk.Text(self.frameEditarHistoria, width=40, height=5)
            self.entryExamenAuxiliarEditar.grid(row=9, column=0, pady=3, sticky='nsew')
           # y Prescripción Médica
            self.lblPrescripcionMedicaEditar = tk.Label(self.frameEditarHistoria, text='DETALLE:', font=('ARIAL', 12, 'bold'), bg='#CDD8FF')
            self.lblPrescripcionMedicaEditar.grid(row=8, column=1, pady=5, sticky='nsew')
            self.svDetalleEditar = tk.StringVar()
            self.entryDetalleEditar = tk.Text(self.frameEditarHistoria, width=40, height=5)
            self.entryDetalleEditar.grid(row=9, column=1, pady=3, sticky='nsew')

            
            # Tratamiento y Botón Generar Receta
            self.lblTratamiento = tk.Label(self.frameEditarHistoria, text='TRATAMIENTO', font=('ARIAL', 12, 'bold'), bg='#CDD8FF')
            self.lblTratamiento.grid(row=10, column=0, columnspan=2, pady=3, sticky='nsew')
    #revisa acaaaa       
            self.btnGenerarReceta = tk.Button(self.frameEditarHistoria, text='RECETA', command=self.mostrarRecetasSeleccionada)
            self.btnGenerarReceta.config(width=20, font=('ARIAL', 12, 'bold'), fg='#DAD5D6', bg='#000992', cursor='hand2', activebackground='#4E56C6')
            self.btnGenerarReceta.grid(row=11, column=0, columnspan=2, pady=5, sticky='nsew')
            #FRAME FECHA EDITAR
            self.frameFechaEditar = tk.LabelFrame(self.topEditarHistoria)
            self.frameFechaEditar.config(bg='#CDD8FF')
            self.frameFechaEditar.pack(fill="both", expand="yes", padx=20, pady=10)

            #LABEL FECHA EDITAR
            self.lblFechaHistoriaEditar = tk.Label(self.frameFechaEditar, text='Fecha y Hora', width=30, font=('ARIAL', 15, 'bold'), bg='#CDD8FF')
            self.lblFechaHistoriaEditar.grid(row=1, column=0, padx=5, pady=3)

            #  ENTRY FECHA EDITAR
            self.svFechaHistoriaEditar = tk.StringVar()
            self.entryFechaHistoriaEditar = tk.Entry(self.frameFechaEditar, textvariable=self.svFechaHistoriaEditar)
            self.entryFechaHistoriaEditar.config(width=20, font=('ARIAL', 15))
            self.entryFechaHistoriaEditar.grid(row = 1, column=1, pady=3, padx=5)
            
            # Insertar texto en Entry widgets para editar
            self.entryFechaHistoriaEditar.delete(0, tk.END)
            self.entryFechaHistoriaEditar.insert(0, self.fechaHistoriaEditar)

            self.entryPAEditar.delete(0, tk.END)
            self.entryPAEditar.insert(0, self.PAEditar)

            self.entryFCEditar.delete(0, tk.END)
            self.entryFCEditar.insert(0, self.FCEditar)

            self.entryPesoEditar.delete(0, tk.END)
            self.entryPesoEditar.insert(0, self.PesoEditar)

            self.entryTallaEditar.delete(0, tk.END)
            self.entryTallaEditar.insert(0, self.TallaEditar)

            self.entryIMCEditar.delete(0, tk.END)
            self.entryIMCEditar.insert(0, self.IMCEditar)

            self.entryExamenAuxiliarEditar.delete("1.0", tk.END)  # Limpiar todo el contenido antes de insertar
            self.entryExamenAuxiliarEditar.insert(tk.END, self.ExamenAuxiliarEditar)

            
            self.entryDetalleEditar.delete("1.0", tk.END)  # Limpiar todo el contenido antes de insertar
            self.entryDetalleEditar.insert(tk.END, self.DetalleEditar)


            self.entryMotivoConsultaEditar.delete(0, tk.END)
            self.entryMotivoConsultaEditar.insert(0, self.MotivoEditar)


            #BUTTON EDITAR HISTORIA
            self.btnEditarHistoriaMedica = tk.Button(self.frameFechaEditar, text='Editar Historia', command=self.historiaMedicaEditar)
            self.btnEditarHistoriaMedica.config(width=20, font=('ARIAL', 12, 'bold'), fg='#DAD5D6', bg='#030058', cursor='hand2', activebackground='#8986DA')
            self.btnEditarHistoriaMedica.grid(row=2, column=0, padx=10, pady=5)

            self.btnSalirEditarHistoriaMedica = tk.Button(self.frameFechaEditar, text='Salir', command=self.topEditarHistoria.destroy)
            self.btnSalirEditarHistoriaMedica.config(width=20, font=('ARIAL', 12, 'bold'), fg='#DAD5D6', bg='#000000', cursor='hand2', activebackground='#676767')
            self.btnSalirEditarHistoriaMedica.grid(row=2, column=1, padx=10, pady=5)
            
            if self.idHistoriaMedicaEditar == None:
                self.idHistoriaMedicaEditar = self.idHistoriaMedica
            self.idHistoriaMedica = None
            
        except:
            title = 'Editar Historia'
            mensaje = 'Error al editar historia'
            messagebox.showerror(title, mensaje)
    
    


    def historiaMedicaEditar(self):
        try:
            # Validar el formato de PA (Presión Arterial)
            if not re.match(r'\d{2,3}/\d{2,3}', self.svPAEditar.get()):
                messagebox.showerror("Error", "Formato incorrecto para la Presión Arterial (PA). Debe ser en formato 'número/número'.")
                return

            # Validar que FC (Frecuencia Cardíaca) sea un número entero o decimal
            if not re.match(r'^\d+(\,\d+)?$', self.svFCEditar.get().strip().replace('.', ',')):
                messagebox.showerror("Error", "La Frecuencia Cardíaca (FC) debe ser un número (entero o decimal).")
                return

            # Validar que Peso sea un número (entero o decimal)
            if not re.match(r'^\d+(\,\d+)?$', self.svPESOEditar.get().strip().replace('.', ',')):
                messagebox.showerror("Error", "El Peso debe ser un número (entero o decimal).")
                return

            # Validar que Talla sea un número (entero o decimal)
            if not re.match(r'^\d+(\,\d+)?$', self.svTallaEditar.get().strip().replace('.', ',')):
                messagebox.showerror("Error", "La Talla debe ser un número (entero o decimal).")
                return

            # Validar que IMC sea un número (entero o decimal)
            if not re.match(r'^\d+(\,\d+)?$', self.svICMEditar.get().strip().replace('.', ',')):
                messagebox.showerror("Error", "El Índice de Masa Corporal (IMC) debe ser un número (entero o decimal).")
                return

            # Si los campos cumplen con los formatos requeridos, proceder con la edición de la historia médica
            examen_auxiliar = self.entryExamenAuxiliarEditar.get("1.0", "end-1c").strip()
            detalle = self.entryDetalleEditar.get("1.0", "end-1c").strip()
            editarHistoria(self.svFechaHistoriaEditar.get(), self.svPAEditar.get(), self.svFCEditar.get(), self.svPESOEditar.get(), self.svTallaEditar.get(), self.svICMEditar.get(), self.svMotivoConsultaEditar.get(), examen_auxiliar, detalle, self.idHistoriaMedicaEditar)
            self.idHistoriaMedicaEditar = None
            self.idHistoriaMedica = None
            self.topEditarHistoria.destroy()
            self.topHistoriaMedica.destroy()
        except Exception as e:
            print("Error:", e)
            messagebox.showerror("Error", "Error al editar historia médica")
            self.topEditarHistoria.destroy()




    def eliminarHistorialMedico(self):
        try:
            self.idHistoriaMedica = self.tablaHistoria.item(self.tablaHistoria.selection())['text']
            eliminarHistoria(self.idHistoriaMedica)

            self.idHistoriaMedica = None
            self.topHistoriaMedica.destroy()
        except:
            title = 'Eliminar Historia'
            mensaje = 'Erro al eliminar'
            messagebox.showerror(title, mensaje)
    

    def editarPaciente(self):
        try:
            self.idPersona = self.tabla.item(self.tabla.selection())['text'] #Trae el ID
            self.svFecha.set('')
            self.fechaRegistroPaciente= self.tabla.item(self.tabla.selection())['values'][0]
            self.NombresPaciente = self.tabla.item(self.tabla.selection())['values'][1]
            self.ApellidosPaciente = self.tabla.item(self.tabla.selection())['values'][2]
            # Asegurarse de que la cédula se maneje como texto
            self.CedulaPaciente = str(self.tabla.item(self.tabla.selection())['values'][3])
            self.fechaNacimientoPaciente = self.tabla.item(self.tabla.selection())['values'][4]
            self.EdadPaciente = self.tabla.item(self.tabla.selection())['values'][5]
            self.EstadoCivilPaciente = self.tabla.item(self.tabla.selection())['values'][6]
            self.DomicilioPaciente = self.tabla.item(self.tabla.selection())['values'][7]
            self.TelefonoPaciente = self.tabla.item(self.tabla.selection())['values'][8]
            self.ApppPaciente = self.tabla.item(self.tabla.selection())['values'][9]
            self.ApfPaciente = self.tabla.item(self.tabla.selection())['values'][10]
            self.AgoPaciente = self.tabla.item(self.tabla.selection())['values'][11]
            self.AlergiasPaciente = self.tabla.item(self.tabla.selection())['values'][12]
            self.CorreoPaciente = self.tabla.item(self.tabla.selection())['values'][13]
            self.CarreraPaciente = self.tabla.item(self.tabla.selection())['values'][14]
            self.GeneroPaciente = self.tabla.item(self.tabla.selection())['values'][15]
            self.SemestrePaciente = self.tabla.item(self.tabla.selection())['values'][16]

            self.habilitar()

            self.entryFecha.insert(0, self.fechaRegistroPaciente)
            self.entryNombre.insert(0, self.NombresPaciente)
            self.entryApellidos.insert(0, self.ApellidosPaciente)
            self.entryCedula.insert(0, self.CedulaPaciente)  # Insertar la cédula como texto
            self.entryFechaNacimiento.insert(0, self.fechaNacimientoPaciente)
            self.entryEdad.insert(0, self.EdadPaciente)
            self.entryEstadoCivil.insert(0, self.EstadoCivilPaciente)
            self.entryDomicilio.insert(0, self.DomicilioPaciente)
            self.entryTelefono.insert(0, self.TelefonoPaciente)
            self.entryApp.insert(0, self.ApppPaciente)
            self.entryAPF.insert(0, self.ApfPaciente)
            self.entryAGO.insert(0, self.AgoPaciente)
            self.entryAlergia.insert(0, self.AlergiasPaciente)
            self.entryCorreo.insert(0, self.CorreoPaciente)
            self.entryCarrera.insert(0, self.CarreraPaciente)
            self.entryGenero.insert(0, self.GeneroPaciente)
            self.entrySemestre.insert(0, self.SemestrePaciente)

        except:
            title = 'Editar Paciente'
            mensaje = 'Error al editar paciente'
            messagebox.showerror(title, mensaje)
    
    def eliminarDatoPaciente(self):
        try:
            self.idPersona = self.tabla.item(self.tabla.selection())['text']
            eliminarPaciente(self.idPersona)
            
            self.tablaPaciente()
            self.idPersona = None
        except:
            title = 'Eliminar Paciente'
            mensaje = 'No se pudo eliminar paciente'
            messagebox.showinfo(title, mensaje)
    
    
    
    def show_calendar(self):
        
        self.cal_window = Toplevel(self)
        self.cal_window.title("Seleccionar fecha")
        self.cal = tc.Calendar(self.cal_window, selectmode='day', year=int(datetime.now().year), month=int(datetime.now().month), day=int(datetime.now().day))
        self.cal.pack(fill="both", expand=True)
        self.btn_set_date = tk.Button(self.cal_window, text="Seleccionar", command=self.set_selected_date)
        self.btn_set_date.pack()

    def set_selected_date(self, *args):
        selected_date = self.cal.selection_get()
        self.svFechaNacimiento.set(selected_date)
        
        self.calcularEdad()  # Llamar a la función para calcular la edad
        
        self.cal_window.destroy()

    def calcularEdad(self, *args):
        self.fechaActual = date.today()
        self.date1 = self.cal.get_date()
        self.conver = datetime.strptime(self.date1, "%m/%d/%y")  # Ajuste del formato
        
        self.resul = self.fechaActual.year - self.conver.year
        self.resul -= ((self.fechaActual.month, self.fechaActual.day) < (self.conver.month, self.conver.day))
        self.svEdad.set(self.resul)
