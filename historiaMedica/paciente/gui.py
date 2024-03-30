import tkinter as tk
from fpdf import FPDF
import sys
import subprocess

from tkinter import *
from tkinter import Button, ttk, scrolledtext, Toplevel, LabelFrame
from tkinter import messagebox
from modelo.pacienteDao import Persona, eliminarPaciente, guardarDatosPaciente, listar, listarCondicion, editarDatoPaciente
from modelo.historiaMedicaDao import guardarHistoria, listarHistoria, eliminarHistoria, editarHistoria
import tkcalendar as tc
from tkcalendar import *
from tkcalendar import Calendar
from datetime import datetime, date
from tkinter import ttk, Toplevel


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
        self.camposPaciente()
        self.create_encabezado()
        self.fill_current_date()
        self.deshabilitar()
        self.tablaPaciente()

    
    def create_encabezado(self):
        # Encabezado
        universidad_label = tk.Label(self, text='Unidad\n'
                                               'SERVICIO MÉDICO',
                                    font=('Nexa', 12, 'bold'), bg='#1B7505', fg='white')
        universidad_label.grid(row=0, column=1, columnspan=3,  sticky='n', padx=(10, 0))
        
        #img_path = 'C:/Users/MI Pc/OneDrive/Escritorio/proyecto-PPP-historial-medico/archivos/logo.png'
        #img = tk.PhotoImage(file=img_path)
        #lbl_img = tk.Label(self, image=img)
        #lbl_img.grid(row=0, column=0, columnspan=3, pady=(10, 0), sticky='n', padx=(10, 0))

    

    def fill_current_date(self):
        current_date = datetime.now().strftime("%Y-%m-%d")  # Obtiene la fecha actual en formato YYYY-MM-DD
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
    

    
    #antecedentes
        self.lblAntecedentes= tk.Label(self, text='ANTECEDENTES:')
        self.lblAntecedentes.config(font=('Nexa', 8, 'bold'), bg='#1B7505', fg='white')
        self.lblAntecedentes.grid(column=2, row=12, padx=90,sticky='e')  

    #APP
        self.lblFechaRegistro = tk.Label(self, text='APP: ')
        self.lblFechaRegistro.config(font=('Nexa', 8, 'bold'), bg='#1B7505', fg='white')
        self.lblFechaRegistro.grid(column=3, row=7,  sticky='w')
    
    #APF
        self.lblCarrera= tk.Label(self, text='APF: ')
        self.lblCarrera.config(font=('Nexa', 8, 'bold'), bg='#1B7505', fg='white')
        self.lblCarrera.grid(column=3, row=8, sticky='w')  
        

     #AGO7
        self.lblSemestre= tk.Label(self, text='AGO: ')
        self.lblSemestre.config(font=('Nexa', 8, 'bold'), bg='#1B7505', fg='white')
        self.lblSemestre.grid(column=3, row=9, sticky='w')
        
    
     #AGO7
        self.lblSemestre= tk.Label(self, text='ALERGIA: ')
        self.lblSemestre.config(font=('Nexa', 8, 'bold'), bg='#1B7505', fg='white')
        self.lblSemestre.grid(column=3, row=10, sticky='w')

       
    
    

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
        self.entryCarrera.grid(column=2, row=1, columnspan=1)  

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
        self.entryTelefono.grid(column=2, row=10, columnspan=2, sticky='w')

        #CORREO
        self.svCorreo = tk.StringVar()
        self.entryCorreo = tk.Entry(self, textvariable=self.svCorreo)
        self.entryCorreo.config(width=35, font=('Nexa',8,'bold'))
        self.entryCorreo.grid(column=2, row=11,  columnspan=2, sticky='w')

        
        #APP
        self.svApp = tk.StringVar()
        self.entryApp = tk.Entry(self, textvariable=self.svApp)
        self.entryApp.config(width=35, font=('Nexa',8,'bold'))
        self.entryApp.grid(column=3, row=7, padx=50, pady=5, columnspan=3)

        #APF
        self.svAPF = tk.StringVar()
        self.entryAPF = tk.Entry(self, textvariable=self.svAPF)
        self.entryAPF.config(width=35, font=('Nexa',8,'bold'))
        self.entryAPF.grid(column=3, row=8, padx=50, pady=5, columnspan=3)

        #AGO
        self.svAGO = tk.StringVar()
        self.entryAGO = tk.Entry(self, textvariable=self.svAGO)
        self.entryAGO.config(width=35, font=('Nexa',8,'bold'))
        self.entryAGO.grid(column=3, row=9, padx=50, pady=5, columnspan=3)

        #Alergia
        self.svAlergia = tk.StringVar()
        self.entryAlergia = tk.Entry(self, textvariable=self.svAlergia)
        self.entryAlergia.config(width=35, font=('Nexa',8,'bold'))
        self.entryAlergia.grid(column=3, row=10, padx=50, pady=5, columnspan=3)

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
        self.btnBuscarCondicion.config(width=17, font=('Nexa',8,'bold'), fg='#DAD5D6', 
                                bg='#00396F', cursor='hand2',activebackground='#5B8DBD')
        self.btnBuscarCondicion.grid(column=3, row=5,sticky='w')

        self.btnLimpiarBuscador = tk.Button(self, text='LIMPIAR', command= self.limpiarBuscador)
        self.btnLimpiarBuscador.config(width=18, font=('Nexa',8,'bold'), fg='#DAD5D6', 
                                bg='#00396F', cursor='hand2',activebackground='#5B8DBD')
        self.btnLimpiarBuscador.grid(column=3, row=5, padx=40, pady=4, columnspan=3)  

        # FECHA - CALENDARIO 
        self.btnCalendario = tk.Button(self, text='CALENDARIO', command=self.show_calendar)
        self.btnCalendario.config(width=17, font=('Nexa',8,'bold'), fg='#DAD5D6', 
                                bg='#120061', cursor='hand2',activebackground='#7C6DC1')
        self.btnCalendario.grid(column=3, row=6, sticky='w')

   #BUTTONS
        self.btnNuevo = tk.Button(self, text='Nuevo', command=self.habilitar)
        self.btnNuevo.config(width=20, font=('ARIAL',8,'bold'), fg='#DAD5D6', 
                                bg='#158645', cursor='hand2',activebackground='#35BD6F')
        self.btnNuevo.grid(column=1,row=17,  pady=5)

        self.btnGuardar = tk.Button(self, text='Guardar', command=self.guardarPaciente)
        self.btnGuardar.config(width=20, font=('ARIAL',8,'bold'), fg='#DAD5D6', 
                                bg='#000000', cursor='hand2',activebackground='#5F5F5F')
        self.btnGuardar.grid(column=2, row=17, pady=5)

        self.btnCancelar = tk.Button(self, text='Cancelar', command=self.deshabilitar)
        self.btnCancelar.config(width=20, font=('ARIAL',8,'bold'), fg='#DAD5D6', 
                                bg='#B00000', cursor='hand2',activebackground='#D27C7C')
        self.btnCancelar.grid(column=3,row=17, pady=5)
    
    def buscarCondicion(self):
        if len(self.svBuscarDni.get()) > 0 or len(self.svBuscarApellido.get()) > 0 or len(self.svBuscarCarrera.get()) > 0:
            where = "WHERE 1=1"
            if len(self.svBuscarDni.get()) > 0:
                # Agrega la condición para buscar por cédula
                where += f" AND cedula = {self.svBuscarDni.get()}"
            if len(self.svBuscarApellido.get()) > 0:
                # Agrega la condición para buscar por apellido
                where += f" AND apellidos LIKE '{self.svBuscarApellido.get()}%' AND activo = 1"
            if len(self.svBuscarCarrera.get()) > 0:
                # Agrega la condición para buscar por carrera
                where += f" AND carrera LIKE '{self.svBuscarCarrera.get()}%'"
            self.tablaPaciente(where)
        else:
            self.tablaPaciente()





    def limpiarBuscador(self):
        self.svBuscarApellido.set('')
        self.svBuscarDni.set('')
        self.svBuscarCarrera.set('')
        self.tablaPaciente()

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

    def habilitar(self):
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
        self.btnEditarPaciente.grid(row=20, column=1, padx=10, pady=5)
       
        self.btnEliminarPaciente = tk.Button(self, text='Eliminar Paciente', command= self.eliminarDatoPaciente )
        self.btnEliminarPaciente.config(width=20,font=('ARIAL',12,'bold'), fg='#DAD5D6', bg='#8A0000', activebackground='#D58A8A', cursor='hand2')
        self.btnEliminarPaciente.grid(row=20, column=2, padx=10, pady=5)

        self.btnHistorialPaciente = tk.Button(self, text='Historial Paciente', command=self.historiaMedica)
        self.btnHistorialPaciente.config(width=20,font=('ARIAL',12,'bold'), fg='#DAD5D6', bg='#007C79', activebackground='#99F2F0', cursor='hand2')
        self.btnHistorialPaciente.grid(row=20, column=3, padx=10, pady=5)

        self.btnSalir = tk.Button(self, text='Salir', command=self.root.destroy)
        self.btnSalir.config(width=20,font=('ARIAL',12,'bold'), fg='#DAD5D6', bg='#000000', activebackground='#5E5E5E', cursor='hand2')
        self.btnSalir.grid(row=20, column=4, padx=10, pady=5)

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
            self.tablaHistoria.heading('#3', text='Motivo')
            self.tablaHistoria.heading('#4', text='PA')
            self.tablaHistoria.heading('#5', text='FC')
            self.tablaHistoria.heading('#6', text='Peso')
            self.tablaHistoria.heading('#7', text='Talla')
            self.tablaHistoria.heading('#8', text='IMC')
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
        self.lblPA = tk.Label(self.frameDatosHistoria, text='PA:', width=15, font=('ARIAL', 12, 'bold'), bg='#CDD8FF')
        self.lblPA.grid(row=1, column=0, pady=3, padx=0, sticky='w', columnspan=2)
        
        self.svPA = tk.StringVar()
        self.entryPA = tk.Entry(self.frameDatosHistoria, width=30, textvariable=self.svPA)
        self.entryPA.config(width=30, font=('Nexa',8,'bold'))
        self.entryPA.grid(row=1, column=0, pady=3,  sticky='e')

        #FC
        self.lblFC = tk.Label(self.frameDatosHistoria, text='FC:', width=15, font=('ARIAL', 12, 'bold'), bg='#CDD8FF')
        self.lblFC.grid(row=1, column=1, pady=3, sticky='w', columnspan=2)
        
        self.svFC = tk.StringVar()
        self.entryFC = tk.Entry(self.frameDatosHistoria, width=30, textvariable=self.svFC)
        self.entryFC.config(width=30, font=('Nexa',8,'bold'))
        self.entryFC.grid(row=1, column=1, pady=3, sticky='e')

        #PESO
        self.lblPeso = tk.Label(self.frameDatosHistoria, text='PESO:', width=15, font=('ARIAL', 12, 'bold'), bg='#CDD8FF')
        self.lblPeso.grid(row=2, column=0, pady=2, sticky='w', columnspan=2)
        
        self.svPESO = tk.StringVar()
        self.entryPeso = tk.Entry(self.frameDatosHistoria, width=30, textvariable=self.svPESO)
        self.entryPeso.config(width=30, font=('Nexa',8,'bold'))
        self.entryPeso.grid(row=2, column=0, pady=3, sticky='e')

        #TALLA
        self.lblTalla = tk.Label(self.frameDatosHistoria, text='TALLA:', width=15, font=('ARIAL', 12, 'bold'), bg='#CDD8FF')
        self.lblTalla.grid(row=2, column=1, pady=3, sticky='w', columnspan=2)

        self.svTalla = tk.StringVar()
        self.entryTalla = tk.Entry(self.frameDatosHistoria, width=30, textvariable=self.svTalla)
        self.entryTalla.config(width=30, font=('Nexa',8,'bold'))
        self.entryTalla.grid(row=2, column=1, pady=3, sticky='e')

        #IMC
        self.lblIMC = tk.Label(self.frameDatosHistoria, text='IMC:', width=15, font=('ARIAL', 12, 'bold'), bg='#CDD8FF')
        self.lblIMC.grid(row=3, column=0, pady=3, sticky='w', columnspan=2)

        self.svICM = tk.StringVar()
        self.entryIMC = tk.Entry(self.frameDatosHistoria, width=30, textvariable=self.svICM)
        self.entryIMC.config(width=30, font=('Nexa',8,'bold'))
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
    # Tratamiento y Botón Generar Receta
        self.lblTratamiento = tk.Label(self.frameDatosHistoria, text='TRATAMIENTO', font=('ARIAL', 12, 'bold'), bg='#CDD8FF')
        self.lblTratamiento.grid(row=10, column=0, columnspan=2, pady=3, sticky='nsew')
 
 #revisa acaaaa       
        self.btnGenerarReceta = tk.Button(self.frameDatosHistoria, text='RECETA', command=self.abrirVentanaReceta)
        self.btnGenerarReceta.config(width=20, font=('ARIAL', 12, 'bold'), fg='#DAD5D6', bg='#000992', cursor='hand2', activebackground='#4E56C6')
        self.btnGenerarReceta.grid(row=11, column=0, columnspan=2, pady=5, sticky='nsew')

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
        self.svFechaHistoria.set(datetime.today().strftime('%d-%m-%Y %H:%M'))

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
        self.ventana_receta = Toplevel()
        self.ventana_receta.title("Receta Médica")
        self.ventana_receta.geometry("800x600")
        self.ventana_receta.config(bg='#CDD8FF')
      
        # Frame de receta
        frame_receta = tk.Frame(self.ventana_receta, bg='#CDD8FF')
        frame_receta.pack(fill="both", expand="yes", padx=20, pady=10)

        # Título
        titulo_label = tk.Label(frame_receta, text="RECETA PARA ATENCIÓN AMBULATORIA", font=('Arial', 16, 'bold'), bg='#CDD8FF')
        titulo_label.pack()

        # Datos del paciente (supongo que estos campos deberían llenarse)
        paciente_frame = tk.Frame(frame_receta, bg='#CDD8FF')
        paciente_frame.pack(pady=10, padx=10, fill='x')
        
        tk.Label(paciente_frame, text="DATOS DEL PACIENTE", font=('Arial', 14, 'bold'), bg='#CDD8FF').grid(row=0, column=0, columnspan=2, sticky='w')
        tk.Label(paciente_frame, text="NOMBRES PACIENTE", font=('Arial', 12), bg='#CDD8FF').grid(row=1, column=0, sticky='w')
        self.nombres_paciente_entry = tk.Entry(paciente_frame, width=30)
        self.nombres_paciente_entry.grid(row=1, column=1, sticky='w')
        tk.Label(paciente_frame, text="CEDULA", font=('Arial', 12), bg='#CDD8FF').grid(row=2, column=0, sticky='w')
        self.cedula_entry = tk.Entry(paciente_frame, width=30)
        self.cedula_entry.grid(row=2, column=1, sticky='w')
        tk.Label(paciente_frame, text="Nª HISTORIA", font=('Arial', 12), bg='#CDD8FF').grid(row=3, column=0, sticky='w')
        self.historia_medica_entry = tk.Entry(paciente_frame, width=30)
        self.historia_medica_entry.grid(row=3, column=1, sticky='w')
        tk.Label(paciente_frame, text="EDAD", font=('Arial', 12), bg='#CDD8FF').grid(row=4, column=0, sticky='w')
        self.edad_entry = tk.Entry(paciente_frame, width=10)
        self.edad_entry.grid(row=4, column=1, sticky='w')
        tk.Label(paciente_frame, text="MESES", font=('Arial', 12), bg='#CDD8FF').grid(row=4, column=2, sticky='w')
        self.meses_entry = tk.Entry(paciente_frame, width=10)
        self.meses_entry.grid(row=4, column=3, sticky='w')
        tk.Label(paciente_frame, text="SEXO", font=('Arial', 12), bg='#CDD8FF').grid(row=4, column=4, sticky='w')
        self.sexo_entry = tk.Entry(paciente_frame, width=10)
        self.sexo_entry.grid(row=4, column=5, sticky='w')

        # Formulario de medicamentos
        medicamento_frame = tk.Frame(frame_receta, bg='#CDD8FF')
        medicamento_frame.pack(pady=10, padx=10, fill='both', expand=True)
        tk.Label(medicamento_frame, text="MEDICAMENTOS", font=('Arial', 14, 'bold'), bg='#CDD8FF').grid(row=0, column=0, columnspan=2, sticky='w')
        tk.Label(medicamento_frame, text="Nombre:", font=('Arial', 12), bg='#CDD8FF').grid(row=1, column=0, sticky='w')
        self.medicamento_entry = tk.Entry(medicamento_frame, width=30)
        self.medicamento_entry.grid(row=1, column=1, sticky='w')
        tk.Label(medicamento_frame, text="Cantidad:", font=('Arial', 12), bg='#CDD8FF').grid(row=2, column=0, sticky='w')
        self.cantidad_entry = tk.Entry(medicamento_frame, width=10)
        self.cantidad_entry.grid(row=2, column=1, sticky='w')

        # Lista de medicamentos
        lista_med_frame = tk.Frame(medicamento_frame, bg='#CDD8FF')
        lista_med_frame.grid(row=3, column=0, columnspan=2, sticky='we')
        tk.Label(lista_med_frame, text="MEDICAMENTOS", font=('Arial', 12, 'bold'), bg='#CDD8FF').pack()
        scrollbar = tk.Scrollbar(lista_med_frame, orient='vertical')
        scrollbar.pack(side='right', fill='y')
        self.lista_med = tk.Listbox(lista_med_frame, yscrollcommand=scrollbar.set, width=50)
        self.lista_med.pack(side='left', fill='both', expand=True)
        scrollbar.config(command=self.lista_med.yview)

        # Botones
        btn_frame = tk.Frame(frame_receta, bg='#CDD8FF')
        btn_frame.pack(pady=20)
        tk.Button(btn_frame, text="Guardar", font=('Arial', 12)).grid(row=0, column=0, padx=10)
        tk.Button(btn_frame, text="Imprimir", font=('Arial', 12), command=self.generar_pdf).grid(row=0, column=1, padx=10)
        tk.Button(btn_frame, text="Cancelar", font=('Arial', 12)).grid(row=0, column=2, padx=10)

    def generar_pdf(self):
        # Obtener los datos de la ventana
        nombres_paciente = self.nombres_paciente_entry.get()
        cedula = self.cedula_entry.get()
        historia_medica = self.historia_medica_entry.get()
        edad = self.edad_entry.get()
        meses = self.meses_entry.get()
        sexo = self.sexo_entry.get()

        # Obtener los datos del medicamento
        nombre_medicamento = self.medicamento_entry.get()
        cantidad_medicamento = self.cantidad_entry.get()

        # Agregar el medicamento a la lista
        self.lista_med.insert(tk.END, f"{nombre_medicamento}: {cantidad_medicamento}")

        # Crear el PDF con los datos obtenidos
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)

        # Título
        pdf.cell(200, 10, txt="Receta Médica", ln=True, align='C')

        # Datos del paciente
        pdf.cell(200, 10, txt="DATOS DEL PACIENTE", ln=True, align='L')
        pdf.cell(200, 10, txt=f"Nombres: {nombres_paciente}", ln=True, align='L')
        pdf.cell(200, 10, txt=f"Cédula: {cedula}", ln=True, align='L')
        pdf.cell(200, 10, txt=f"Nª Historia Médica: {historia_medica}", ln=True, align='L')
        pdf.cell(200, 10, txt=f"Edad: {edad} años {meses} meses", ln=True, align='L')
        pdf.cell(200, 10, txt=f"Sexo: {sexo}", ln=True, align='L')

        # Datos de los medicamentos
        pdf.cell(200, 10, txt="DATOS DEL MEDICAMENTO", ln=True, align='L')
        for item in self.lista_med.get(0, tk.END):
            nombre, cantidad = item.split(":")
            pdf.cell(200, 10, txt=f"Medicamento: {nombre}", ln=True, align='L')
            pdf.cell(200, 10, txt=f"Cantidad: {cantidad}", ln=True, align='L')

        # Guardar el PDF
        pdf_file = "receta_medica.pdf"
        pdf.output(pdf_file)

        # Abrir el PDF
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

#hasta aca recetaaaaaaaaaaaaaaaaaaaaa

    
    def update_svExamenAuxiliar(self, event):
        self.svExamenAuxiliar.set(self.entryExamenAuxiliar.get("1.0", tk.END))

    def update_svDetalle(self, event):
        self.svDetalle.set(self.entryDetalle.get("1.0", tk.END))

    def agregaHistorialMedico(self):
        try:
            # Obtener el ID del paciente seleccionado en la tabla
            self.idPersona = self.tabla.item(self.tabla.selection())['text']

            if self.idHistoriaMedica == None:
                self.update_svExamenAuxiliar(None)  # Llama a la función para actualizar el examen auxiliar
                self.update_svDetalle(None)
                guardarHistoria(self.idPersona, self.svFechaHistoria.get(), self.svMotivoConsulta.get(), self.svPA.get(), self.svFC.get(), self.svPESO.get(), self.svTalla.get(), self.svICM.get(), self.svExamenAuxiliar.get(), self.svDetalle.get())
            self.topAHistoria.destroy()
            self.topHistoriaMedica.destroy()
            self.idPersona = None
        except Exception as e:
            print("Error:", e)
            messagebox.showerror("Error", "Error al agregar historia médica")

    
    def topEditarHistorialMedico(self):
        try:
            self.idHistoriaMedica = self.tablaHistoria.item(self.tablaHistoria.selection())['text']
            self.fechaHistoriaEditar = self.tablaHistoria.item(self.tablaHistoria.selection())['values'][1]
            self.PAEditar = self.tablaHistoria.item(self.tablaHistoria.selection())['values'][3]
            self.FCEditar = self.tablaHistoria.item(self.tablaHistoria.selection())['values'][4]
            self.PesoEditar = self.tablaHistoria.item(self.tablaHistoria.selection())['values'][5]
            self.TallaEditar = self.tablaHistoria.item(self.tablaHistoria.selection())['values'][6]
            self.IMCEditar = self.tablaHistoria.item(self.tablaHistoria.selection())['values'][7]
            self.MotivoEditar = self.tablaHistoria.item(self.tablaHistoria.selection())['values'][2]
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


            #labels ______________
            
            # Signos Vitales
            self.lblSignosVitalesEditar = tk.Label(self.frameEditarHistoria, text='SIGNOS VITALES', font=('ARIAL', 12, 'bold'), bg='#CDD8FF')
            self.lblSignosVitalesEditar.grid(row=0, column=0, columnspan=4, pady=5)

            #PA
            self.lblPAEditar = tk.Label(self.frameEditarHistoria, text='PA:', width=15, font=('ARIAL', 12, 'bold'), bg='#CDD8FF')
            self.lblPAEditar.grid(row=1, column=0, pady=3, padx=0, sticky='w', columnspan=2)

            self.svPAEditar = tk.StringVar()
            self.entryPAEditar = tk.Entry(self.frameEditarHistoria, width=30, textvariable=self.svPAEditar)
            self.entryPAEditar.config(width=30, font=('Nexa',8,'bold'))
            self.entryPAEditar.grid(row=1, column=0, pady=3,  sticky='e')

            #FC
            self.lblFCEditar = tk.Label(self.frameEditarHistoria, text='FC:', width=15, font=('ARIAL', 12, 'bold'), bg='#CDD8FF')
            self.lblFCEditar.grid(row=1, column=1, pady=3, sticky='w', columnspan=2)
            
            self.svFCEditar = tk.StringVar()
            self.entryFCEditar = tk.Entry(self.frameEditarHistoria, width=30, textvariable=self.svFCEditar)
            self.entryFCEditar.config(width=30, font=('Nexa',8,'bold'))
            self.entryFCEditar.grid(row=1, column=1, pady=3, sticky='e')

            #PESO
            self.lblPesoEditar = tk.Label(self.frameEditarHistoria, text='PESO:', width=15, font=('ARIAL', 12, 'bold'), bg='#CDD8FF')
            self.lblPesoEditar.grid(row=2, column=0, pady=2, sticky='w', columnspan=2)
            
            self.svPESOEditar = tk.StringVar()
            self.entryPesoEditar = tk.Entry(self.frameEditarHistoria, width=30, textvariable=self.svPESOEditar)
            self.entryPesoEditar.config(width=30, font=('Nexa',8,'bold'))
            self.entryPesoEditar.grid(row=2, column=0, pady=3, sticky='e')

             #TALLA
            self.lblTallaEditar = tk.Label(self.frameEditarHistoria, text='TALLA:', width=15, font=('ARIAL', 12, 'bold'), bg='#CDD8FF')
            self.lblTallaEditar.grid(row=2, column=1, pady=3, sticky='w', columnspan=2)

            self.svTallaEditar = tk.StringVar()
            self.entryTallaEditar = tk.Entry(self.frameEditarHistoria, width=30, textvariable=self.svTallaEditar)
            self.entryTallaEditar.config(width=30, font=('Nexa',8,'bold'))
            self.entryTallaEditar.grid(row=2, column=1, pady=3, sticky='e')
        
            #IMC
            self.lblIMCEditar = tk.Label(self.frameEditarHistoria, text='IMC:', width=15, font=('ARIAL', 12, 'bold'), bg='#CDD8FF')
            self.lblIMCEditar.grid(row=3, column=0, pady=3, sticky='w', columnspan=2)

            self.svICMEditar = tk.StringVar()
            self.entryIMCEditar = tk.Entry(self.frameEditarHistoria, width=30, textvariable=self.svICMEditar)
            self.entryIMCEditar.config(width=30, font=('Nexa',8,'bold'))
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

            self.entryFechaHistoriaEditar.delete(0, tk.END)
            self.entryFechaHistoriaEditar.insert(0, self.fechaHistoriaEditar)

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
            editarHistoria(self.svFechaHistoriaEditar.get(), self.svPAEditar.get(), self.svFCEditar.get(), self.svPESOEditar.get(), self.svTallaEditar.get(), self.svICMEditar.get(), self.svMotivoConsultaEditar.get(), self.svExamenAuxiliarEditar.get(), self.svDetalleEditar.get(), self.idHistoriaMedicaEditar)
            self.idHistoriaMedicaEditar = None
            self.idHistoriaMedica = None
            self.topEditarHistoria.destroy()
            self.topHistoriaMedica.destroy()
        except:
            title = 'Editar Historia'
            mensaje = 'Error al editar historia'
            messagebox.showerror(title, mensaje)
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
            self.CedulaPaciente = self.tabla.item(self.tabla.selection())['values'][4]
            self.fechaNacimientoPaciente = self.tabla.item(self.tabla.selection())['values'][3]
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
            self.entryCedula.insert(0, self.CedulaPaciente)
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
