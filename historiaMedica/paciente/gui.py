import tkinter as tk
from tkinter import messagebox
from modelo.pacienteDao import Persona, eliminarPaciente, guardarDatosPaciente, listar, listarCondicion, editarDatoPaciente
from tkinter import *
from tkinter import ttk, Toplevel
from datetime import datetime
import tkcalendar as tc
from tkcalendar import *
from datetime import datetime, date


class Frame(tk.Frame):
    def __init__(self, root):
        super().__init__(root, width=1300, height=750)
        self.root = root
        self.pack()
        self.config(bg='#1B7505')
        self.idPersona = None
        self.camposPaciente()
        self.create_encabezado()
        self.fill_current_date()
        self.deshabilitar()
        self.tablaPaciente()
    
    def create_encabezado(self):
        # Encabezado
        universidad_label = tk.Label(self, text='UNIVERSIDAD TÉCNICA ESTATAL DE QUEVEDO\n'
                                               'UNIDAD DE BIENESTAR UNIVERSITARIO SERVICIO MÉDICO',
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
    #CEDULA
        self.lblCedula = tk.Label(self, text='No. CÉDULA: ')
        self.lblCedula.config(font=('Nexa', 8, 'bold'), bg='#1B7505', fg='white')
        self.lblCedula.grid(column=1,row=6, padx=90, pady=5, sticky='w')

    #Fecha de nacimiento
        self.lblDni = tk.Label(self, text='FECHA NACIMIENTO: ')
        self.lblDni.config(font=('Nexa', 8, 'bold'), bg='#1B7505', fg='white')
        self.lblDni.grid(column=1,row=5, padx=90, pady=5, sticky='w')

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

        #FECHA de nacimiento
        self.svFechaNacimiento = tk.StringVar()
        self.entryFechaNacimiento = tk.Entry(self, textvariable=self.svFechaNacimiento)
        self.entryFechaNacimiento.config(width=35, font=('Nexa',8,'bold'))
        self.entryFechaNacimiento.grid(column=2, row=5, columnspan=3, sticky='w')
        
        #CEDULA 
        self.svCedula = tk.StringVar()
        self.entryCedula = tk.Entry(self, textvariable=self.svCedula)
        self.entryCedula.config(width=35, font=('Nexa',8,'bold'))
        self.entryCedula.grid(column=2, row=6,  columnspan=3, sticky='w')


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

        #ENTRYS BUSCADOR
        self.svBuscarDni = tk.StringVar()
        self.entryBuscarDni = tk.Entry(self, textvariable=self.svBuscarDni)
        self.entryBuscarDni.config(width=25, font=('Nexa',8,'bold'))
        self.entryBuscarDni.grid(column=3, row=2, padx=150, pady=5, columnspan=3, sticky='w')

        self.svBuscarApellido = tk.StringVar()
        self.entryBuscarApellido = tk.Entry(self, textvariable=self.svBuscarApellido)
        self.entryBuscarApellido.config(width=25, font=('Nexa',8,'bold'))
        self.entryBuscarApellido.grid(column=3, row=3, padx=150, pady=5, columnspan=3, sticky='w')
        
        # BUTTON BUSCADOR
        self.btnBuscarCondicion = tk.Button(self, text='BUSCAR', command=self.buscarCondicion)
        self.btnBuscarCondicion.config(width=17, font=('Nexa',8,'bold'), fg='#DAD5D6', 
                                bg='#00396F', cursor='hand2',activebackground='#5B8DBD')
        self.btnBuscarCondicion.grid(column=3, row=4,sticky='w')

        self.btnLimpiarBuscador = tk.Button(self, text='LIMPIAR', command= self.limpiarBuscador)
        self.btnLimpiarBuscador.config(width=18, font=('Nexa',8,'bold'), fg='#DAD5D6', 
                                bg='#00396F', cursor='hand2',activebackground='#5B8DBD')
        self.btnLimpiarBuscador.grid(column=3, row=4, padx=40, pady=4, columnspan=3)  

        # FECHA - CALENDARIO 
        self.btnCalendario = tk.Button(self, text='CALENDARIO', command=self.show_calendar)
        self.btnCalendario.config(width=17, font=('Nexa',8,'bold'), fg='#DAD5D6', 
                                bg='#120061', cursor='hand2',activebackground='#7C6DC1')
        self.btnCalendario.grid(column=3, row=5, sticky='w')

   
    
    
    



  


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
        if len(self.svBuscarDni.get()) > 0 or len(self.svBuscarApellido.get()) > 0:
            where = "WHERE 1=1"
            if (len(self.svBuscarDni.get())) > 0:
                where = "WHERE cedula = " + self.svBuscarDni.get() + "" 
   
    
            if (len(self.svBuscarApellido.get())) > 0:
                where = "WHERE apellidos LIKE '" + self.svBuscarApellido.get()+"%' AND activo = 1"
            
            self.tablaPaciente(where)
        else:
            self.tablaPaciente()
    
    def limpiarBuscador(self):
        self.svBuscarApellido.set('')
        self.svBuscarDni.set('')
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
        
        self.tabla = ttk.Treeview(self, column=('Fecha_registro','Nombres', 'Apellidos', 'Cédula', 'fecha_nacimiento',
                                                'edad','estado_civil','Domicilio','telefono','app', 'apf','ago','alergias',
                                                'correo','Carrera', 'Género', 'Semestre'))
        self.tabla.grid(column=1, row=18, columnspan=8, sticky='nsew')

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
            self.tabla.insert('', 0, text=p[0], values=(p[1],p[2], p[3], p[4],p[5],p[6],p[7],p[8],p[9],p[10],p[11],p[12],p[13], p[14],p[15], p[16], p[17]), tags=('evenrow',))

        # Configurar el tamaño de la fila para que la tabla ocupe la mitad del espacio disponible
        self.grid_rowconfigure(18, weight=1)

        # Agregar botones debajo de la tabla
        self.btnEditarPaciente = tk.Button(self, text='Editar Paciente', command=self.editarPaciente)
        self.btnEditarPaciente.config(width=20,font=('ARIAL',12,'bold'), fg='#DAD5D6', bg='#1E0075', activebackground='#9379E0', cursor='hand2')
        self.btnEditarPaciente.grid(row=20, column=1, padx=10, pady=5)

       
        self.btnEliminarPaciente = tk.Button(self, text='Eliminar Paciente', command= self.eliminarDatoPaciente )
        self.btnEliminarPaciente.config(width=20,font=('ARIAL',12,'bold'), fg='#DAD5D6', bg='#8A0000', activebackground='#D58A8A', cursor='hand2')
        self.btnEliminarPaciente.grid(row=20, column=2, padx=10, pady=5)

        self.btnHistorialPaciente = tk.Button(self, text='Historial Paciente')
        self.btnHistorialPaciente.config(width=20,font=('ARIAL',12,'bold'), fg='#DAD5D6', bg='#007C79', activebackground='#99F2F0', cursor='hand2')
        self.btnHistorialPaciente.grid(row=20, column=3, padx=10, pady=5)

        self.btnSalir = tk.Button(self, text='Salir', command=self.root.destroy)
        self.btnSalir.config(width=20,font=('ARIAL',12,'bold'), fg='#DAD5D6', bg='#000000', activebackground='#5E5E5E', cursor='hand2')
        self.btnSalir.grid(row=20, column=4, padx=10, pady=5)

    def editarPaciente(self):
        try:
            self.idPersona = self.tabla.item(self.tabla.selection())['text'] #Trae el ID
            self.svFecha.set('')
            self.fechaRegistroPaciente= self.tabla.item(self.tabla.selection())['values'][0]
            self.NombresPaciente = self.tabla.item(self.tabla.selection())['values'][1]
            self.ApellidosPaciente = self.tabla.item(self.tabla.selection())['values'][2]
            self.CedulaPaciente = self.tabla.item(self.tabla.selection())['values'][3]
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
