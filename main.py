import tkinter
import tkinter.messagebox   # modulo(es una biblioteca gráfica)
from PIL import Image, ImageTk # type: ignore
import json
from tkinter import messagebox
import random


window = tkinter.Tk() #esto es para mostrar la ventana
window.geometry("630x630+5+5") #esto es para dimensionar la ventana
window.title("Bodybuilder App")
window.resizable(False, False)

# Variables globales
button1 = None 

total_time = 0
activity = ""
rounds = 3 

#flag
is_paused = False

# Variable global textos
text_label = "verdana"

#CONSTANTES

COLOR_BUTTON = "orange"
CURSOR = "pirate"
RELIEF = "groove"

def createbutton(text, frame, command, width, height, pady):
    """
    crea un botón al que se le dan los argumentos de arriba
    """
    button = tkinter.Button(frame, text=text, command=command)
    button.config(bg = COLOR_BUTTON , width = width, height = height, relief = RELIEF, bd = 15, cursor = CURSOR, font = (text_label, 15))
    button.pack(pady = pady)


def clearwindow():
    """
    limpia la ventana
    """
    for widget in frame1.winfo_children(): #se usa el for porque winfo... da una lista de los elementos en la ventana
        widget.destroy()

    

def show_new_window(): # permite vaciar la ventana para llevarnos al menu principal
    """
    muestra una ventana limpia
    y muestra el mensaje de menú principal, ademas de que crea 2 botones
    """
    clearwindow()

    label1 = tkinter.Label(frame1, text = "Menú principal", font = (text_label, 30), bg = "black", fg = "white" )
    label1.pack(pady = 20)
    
    createbutton("Ingresar", frame1, ingress_user, 15, 2, 100)
    createbutton("crear user", frame1, create_user, 15, 2, 20)
    createbutton("admin funtion", frame1, crud,  15, 2, 10)


def crud():

    clearwindow()
    global user_actualizar

    bd = []
    with open("users.json", "r") as users:
        bd = json.load(users)

    # Crear una lista de nombres de users
    names_users = [user["name"] for user in bd]

    # Título del CRUD
    label1 = tkinter.Label(frame1, text="CRUD", font=(text_label, 30), bg="black", fg="white")
    label1.pack(pady=25)  

 
    label2 = tkinter.Label(frame1, text="Seleccione el usuario", font=(text_label, 30), bg="black", fg="white")
    label2.pack(padx=10, pady=40)  


    user_actualizar = tkinter.Spinbox(frame1, values=names_users, font=(text_label, 15))
    user_actualizar.pack(padx=20, pady=20)  

    botton1 = tkinter.Button(frame1, text="Actualizar", command=actualizar, width=20, height=2, bg = "orange", 
                                relief = "groove", bd = 15, cursor = "pirate", font = (text_label, 15))
    botton1.pack(padx=10, pady=40)

    botton2 = tkinter.Button(frame1, text="Eliminar", command=eliminar,  width=20, height=2, bg="orange",
                            relief ="groove", bd=15, cursor="pirate", font= (text_label,15) )
    botton2.pack(padx=10, pady=40)

def actualizar():
    global usuario
    usuario = user_actualizar.get().strip()

    bd = list()
    with open("users.json", "r") as users:
        bd = json.load(users)
    
    names = list()
    for i in range(len(bd)):
        names.append(bd[i]["name"])

    if not usuario or not(usuario in names): 
        messagebox.showinfo("Error", "ingrese una opcion valida")
    else:
        clearwindow()
        actualizar2()


def actualizar2():
    global entry1, entry2, entry3, entry4

    text_label = "Arial"  # Ejemplo de fuente
    edades = list(range(15, 100))  # Ejemplo de edades

    label1 = tkinter.Label(frame1, text="nombre y apellido", font=(text_label, 30), bg="black", fg="white")
    label1.grid(row=0, column=0, padx=10, pady=10)
    entry1 = tkinter.Entry(frame1, font=(text_label, 15))
    entry1.grid(row=0, column=1, padx=10, pady=10)

    label3 = tkinter.Label(frame1, text="edad", font=(text_label, 30), bg="black", fg="white")
    label3.grid(row=1, column=0, padx=10, pady=10)
    entry2 = tkinter.Spinbox(frame1, values=edades, font=(text_label, 15))
    entry2.grid(row=1, column=1, padx=10, pady=10)

    label4 = tkinter.Label(frame1, text="universidad", font=(text_label, 30), bg="black", fg="white")
    label4.grid(row=2, column=0, padx=10, pady=10)

    entry3 = tkinter.Entry(frame1, font=(text_label, 15))
    entry3.grid(row=2, column=1, padx=10, pady=10)

    label5 = tkinter.Label(frame1, text="carrera", font=(text_label, 30), bg="black", fg="white")
    label5.grid(row=3, column=0, padx=10, pady=10)

    entry4 = tkinter.Entry(frame1, font=(text_label, 15))
    entry4.grid(row=3, column=1, padx=10, pady=10)

    botton1 = tkinter.Button(frame1, text="registrar", command= save_actu_user, width=20, height=3, bg = "orange",
                              relief = "groove", bd = 15, cursor = "pirate", font = (text_label, 15))
    botton1.grid(row=4, column=0, columnspan=2, padx=10, pady=50)

    botton2 = tkinter.Button(frame1, text="regresar", command=save_actu_user, width=20, height=2, bg = "orange", 
                                relief = "groove", bd = 15, cursor = "pirate", font = (text_label, 15))
    botton2.grid(row=5, column=0, columnspan=2, padx=10, pady=50)

def save_actu_user():
    user = usuario
    entry5 = entry1.get().strip()  # Nombre
    entry6 = entry2.get().strip()  # Edad
    entry7 = entry3.get().strip()  # Universidad
    entry8 = entry4.get().strip()  # Carrera
    entry6 = int(entry6)

    # Validaciones
    if not entry5: 
        messagebox.showinfo("Error", "Por favor, ingrese su nombre y apellido.")
        clearwindow()
        actualizar2()
    elif entry6 <= 14:
        messagebox.showinfo("Error", "Edad incorrecta")
        clearwindow()
        actualizar2()
    elif not entry7:
        messagebox.showinfo("Error", "Por favor, ingrese su universidad.")
        clearwindow()
        actualizar2()
    elif not entry8:
        messagebox.showinfo("Error", "Por favor, ingrese su carrera.")
        clearwindow()
        actualizar2()
    else:
        # Cargar base de datos
        bd = []
        with open("users.json", "r") as archivo:
            bd = json.load(archivo)
        
        # Buscar el usuario en la lista
        encontrado = False
        for user in bd:
            if user["name"] == usuario:
                user["name"] = entry5
                user["age"] = entry6
                user["university"] = entry7
                user["career"] = entry8
                encontrado = True
                break
        
        if not encontrado:
            messagebox.showinfo("Error", "Usuario no encontrado.")
        else:
            # Guardar cambios
            with open("users.json", "w") as archivo:
                json.dump(bd, archivo, indent=4)
            messagebox.showinfo("Éxito", f"Se ha modificado el usuario {usuario}")
            clearwindow()
            show_new_window()

def eliminar():
    usuario = user_actualizar.get().strip()

    bd = []
    with open("users.json", "r") as users:
        bd = json.load(users)

    # Extraer los nombres de los users
    names = [user["name"] for user in bd]

    if not usuario or usuario not in names:
        messagebox.showinfo("Error", "Usuario no encontrado, rectifique la información.")
    else:
        # Eliminar el usuario
        bd = [user for user in bd if user["name"] != usuario]

        with open("users.json", "w") as archivo:
            json.dump(bd, archivo, indent=4)

        messagebox.showinfo("Éxito", f"Se ha eliminado a {usuario}.")
        clearwindow()
        show_new_window()

def ingress_user():
    global user, contra

    clearwindow()
    label1 = tkinter.Label(frame1, text = "Ingresar usuario", font = (text_label, 30), bg = "black", fg = "white" )
    label1.pack(pady = 20)
    user = tkinter.Entry(frame1, font = (text_label, 15))
    user.pack(padx = 10, pady = 20)
    label2 = tkinter.Label(frame1, text = "Ingrese su contraseña", font = (text_label, 15), bg = "black", fg = "white")
    label2.pack(pady = 20)
    contra = tkinter.Entry(frame1, font = (text_label, 15), show = "*")
    contra.pack(pady = 20)


    #boton para get user
    createbutton("Ingresar", frame1, check_user, 15, 2, 20)
    createbutton("volver al menú", frame1, show_new_window, 15, 2, 20)
    

def check_user():
    """
    verifica si el usuario existe
    """
    contraseña = contra.get()
    usuario = user.get()
    
    bd = list()

    # Comprobar si el archivo existe y cargar los datos

    with open("users.json", "r") as users:
            bd = json.load(users)
            print("Cargados exitosamente")
    
    print (bd)
    total_users = len(bd)


    users = []
    password = []
    for i in range(total_users):
        users.append(bd[i]["usuario"])
        password.append(bd[i]["password"])
    
    if contraseña in password and usuario in users:
        clearwindow()
        show_new_window2()

    else:
        messagebox.showinfo("error", f"usted no esta registrado, cree un usuario por favor")
        clearwindow()
        show_new_window()
    
def create_user():
    clearwindow()
    global entry1, entry2, entry3, entry4

    text_label = "Arial"  # Ejemplo de fuente
    edades = list(range(15, 100))  # Ejemplo de edades con list lambda

    label1 = tkinter.Label(frame1, text="nombre y apellido", font=(text_label, 30), bg="black", fg="white")
    label1.grid(row=0, column=0, padx=10, pady=10)
    entry1 = tkinter.Entry(frame1, font=(text_label, 15))
    entry1.grid(row=0, column=1, padx=10, pady=10)

    label3 = tkinter.Label(frame1, text="edad", font=(text_label, 30), bg="black", fg="white")
    label3.grid(row=1, column=0, padx=10, pady=10)
    entry2 = tkinter.Spinbox(frame1, values = edades, font=(text_label, 15))
    entry2.grid(row=1, column=1, padx=10, pady=10)

    label4 = tkinter.Label(frame1, text="universidad", font=(text_label, 30), bg="black", fg="white")
    label4.grid(row=2, column=0, padx=10, pady=10)

    entry3 = tkinter.Entry(frame1, font=(text_label, 15))
    entry3.grid(row=2, column=1, padx=10, pady=10)

    label5 = tkinter.Label(frame1, text="carrera", font=(text_label, 30), bg="black", fg="white")
    label5.grid(row=3, column=0, padx=10, pady=10)

    entry4 = tkinter.Entry(frame1, font=(text_label, 15))
    entry4.grid(row=3, column=1, padx=10, pady=10)


    botton1 = tkinter.Button(frame1, text="registrar", command= new_user, width=20, height=3, bg = "orange",
                              relief = "groove", bd = 15, cursor = "pirate", font = (text_label, 15))
    botton1.grid(row=4, column=0, columnspan=2, padx=10, pady=50)

    botton2 = tkinter.Button(frame1, text="regresar", command=show_new_window, width=20, height=2, bg = "orange", 
                                relief = "groove", bd = 15, cursor = "pirate", font = (text_label, 15))
    botton2.grid(row=5, column=0, columnspan=2, padx=10, pady=50)


def new_user():
    # Obtener los valores de los campos de entrada
    entry5 = entry1.get().strip()  # Llama a get() con paréntesis
    entry6 = entry2.get().strip()  # Llama a get() con paréntesis
    entry7 = entry3.get().strip()  # Llama a get() con paréntesis
    entry8 = entry4.get().strip()  # Llama a get() con paréntesis
    entry6 = int(entry6)

    # validamos 
    if not entry5: 
        messagebox.showinfo("Error", "Por favor, ingrese su nombre y apellido.")
        clearwindow()
        create_user()
    elif not entry6 or entry6 <= 14 or entry6 >= 116:
        messagebox.showinfo("Error", "Edad incorrecta")
        clearwindow()
        create_user()
    elif not entry7:
        messagebox.showinfo("Error", "Por favor, ingrese su universidad.")
        clearwindow()
        create_user()
    elif not entry8:
        messagebox.showinfo("Error", "Por favor, ingrese su carrera.")
        clearwindow()
        create_user()
    else:
        # Inicializar la lista de users
        bd = []

        # Crear una contraseña aleatoria de 4 dígitos
        c = random.randint(1000, 9999)

        # Comprobar si el archivo existe y cargar los datos
        try:
            with open("users.json", "r") as users:
                bd = json.load(users)
                print("Cargados exitosamente")
        except FileNotFoundError:
            print("El archivo 'users.json' no se encontró. Se creará uno nuevo.")
        except json.JSONDecodeError:
            print("Error al decodificar el archivo JSON. Se creará uno nuevo.")
        except Exception as e:
            print(f"Ocurrió un error: {e}")

        # Crear un nuevo usuario con un nombre basado en el número actual de users
        user_id = len(bd) + 1  # Calcula el número del próximo usuario
        
        user = {
            "usuario": f"usuario {user_id}",  # Nombre del usuario incrementado
            "name": entry5,
            "age": entry6,
            "university": entry7,
            "career": entry8,
            "password": str(c)  # Guardar la contraseña como string
        }

        bd.append(user)  # Agregar el nuevo usuario a la lista

        # Guardar los datos actualizados en el archivo JSON
        with open("users.json", "w") as users:
            json.dump(bd, users, indent=4)

        messagebox.showinfo("Contraseña", f" su user es: usuario {user_id}, \n Su contraseña es: {c}")

        clearwindow()  # Limpiar la ventana actual
        show_new_window()  # Mostrar la nueva ventana


def show_new_window2(): #muestra el menú con las opciones de tren sup e inf.=
    """
    limpia la ventana de nuevo y crea 3 botones
    """
    clearwindow()

    createbutton("Tren Superior", frame1, sup_routines_menu, 15, 2, 100)
    createbutton("Tren inferior", frame1, inf_routines_menu, 15, 2, 20)
    createbutton("Regresar", frame1, show_new_window, 15, 2, 10)


#flag
is_paused = False

def image(image_path):

    """
    abre una nueuva ventana que contiene la imagen
    abre la imagen, la expande por toda la nueva ventana y la redimensiona
    """
    window_image = tkinter.Toplevel() # es para abrir una nueva ventana
    window_image.title("Ejemplos")
    window_image.geometry("500x500+700+100")

    frame_image = tkinter.Frame(window_image, bg="black")
    frame_image.pack(expand=True, fill=tkinter.BOTH)
    
    img = Image.open(image_path).resize((500,500))  
    img_tk = ImageTk.PhotoImage(img)
        
    
    label = tkinter.Label(frame_image, image=img_tk)
    label.image = img_tk
    label.pack()


def chest_timer():
    """
    es el temporizador, crea los botones de iniciar, pausar, reaundar y regresar
    """

    def countdown():
        """se globalizan las 3 variables (para modificarlas dentro de la función)
        se revisa que el tiempo no esté en pausa y sea mayor que cero (0)
        le va quitando de a 1 a 1
        hace lo mismo con los rounds o series
        si llega al final imprimer un mensaje de felicidades
        """
        global total_time, is_paused, activity, rounds


        if total_time > 0 and not is_paused:
            mins, secs = divmod(total_time, 60)
            timer = f"{mins:02d}:{secs:02d}"
            label.config(text=f"{activity}: {timer}")
            total_time -= 1
            frame1.after(1000, countdown)  # Llama a countdown cada segundo
        elif total_time == 0:
            if activity == "Moviendote":
                activity = "Descanso"
                total_time = 30  # Tiempo de descanso
            else:
                rounds -= 1
                if rounds > 0:
                    activity = "Moviendote"
                    total_time = 25  # Tiempo de trabajo
                else:
                    label.config(text="Felicidades, lo has completado")
                    return
            countdown()  # Inicia el siguiente ciclo


    def start_timer():
        """inicializa el temporizador 
        establece la actividad a trabajo
          reinicia el temporizador a 25
        """
        global total_time, activity, rounds
        activity = "Trabajo"
        total_time = 25  # Tiempo de trabajo
        countdown()


    def pause_timer():
        """ pausa el temporizador
        """
        global is_paused
        is_paused = True


    def resume_timer():
        """
        reaunda el temporizador
        cambia el estado de pausa a False, haciendo que continue
        """
        global is_paused
        is_paused = False
        countdown()


    label = tkinter.Label(frame1, text="", font=("Helvetica", 24))
    label.pack(pady=20)

    button_frame_a = tkinter.Frame(frame1, bg = "black")
    button_frame_a.pack(anchor = "nw", padx = 20, pady = 40)

    start_button = tkinter.Button(button_frame_a, text="Iniciar", command=start_timer)
    start_button.config(bg = "orange", width = 16, height = 2, relief = "groove", bd = 15, cursor = "pirate", font = (text_label, 15))
    start_button.pack(side=tkinter.LEFT, padx=10, pady=40)

    pause_button = tkinter.Button(button_frame_a, text="Pausar", command=pause_timer)
    pause_button.config(bg = "orange", width = 16, height = 2, relief = "groove", bd = 15, cursor = "pirate", font = (text_label, 15))
    pause_button.pack(side=tkinter.LEFT, padx=10, pady=20)


    resume_button = tkinter.Button(frame1, text="Reanudar/iniciar", command=resume_timer)
    resume_button.config(bg = "orange", width = 16, height = 2, relief = "groove", bd = 15, cursor = "pirate", font = (text_label, 15))
    resume_button.pack(side=tkinter.LEFT, padx=20, pady=20)

    exit_button = tkinter.Button(frame1, text="Salir", command = chest_menu,)
    exit_button.config(bg = "orange", width = 16, height = 2, relief = "groove", bd = 15, cursor = "pirate", font = (text_label, 15))
    exit_button.pack(side=tkinter.LEFT, padx=20, pady=20)


def bench_press():

    clearwindow()
    chest_timer()


    def image_window():

        image("pressbanca.gif")

    image_window()


def inclined_press():

    clearwindow()
    chest_timer()


    def image_window():

        image("image2.jpg")

    image_window()


def push_ups():
    
    clearwindow()
    chest_timer()


    def image_window():

        image("flexiones.jpg")


    image_window()


def openins():
    
    clearwindow()    
    chest_timer()


    def image_window():

        image("aperturas.jpg")


    image_window()


def chest_menu(): #presionando el boton de pecho nos lleva a otro menú y muestra las opciones de ejercicios
    clearwindow()


    button_frame_a = tkinter.Frame(frame1, bg = "black")
    button_frame_a.pack(anchor = "nw", padx = 20, pady = 10)

    button1_chest = tkinter.Button(button_frame_a, text = "Press banca", command = bench_press     )
    button1_chest.config(bg = "orange", width = 15, height = 2, relief = "groove", bd = 15, cursor = "pirate", font = (text_label, 15))
    button1_chest.pack(side = tkinter.LEFT , padx = 10, pady = 30)

    button2_chest = tkinter.Button(button_frame_a, text = "Press Inclinado", command = inclined_press      )
    button2_chest.config(bg = "orange", width = 15, height = 2, relief = "groove", bd = 15, cursor = "pirate", font = (text_label, 15))
    button2_chest.pack(side = tkinter.LEFT, padx= 10, pady = 30 )

    button_frame_b = tkinter.Frame(frame1, bg = "black")
    button_frame_b.pack(anchor = "nw", padx = 20, pady = (10,0))    

    button3_chest = tkinter.Button(button_frame_b, text = "Flexiones", font = 15, relief = "groove", command = push_ups    )
    button3_chest.config(bg = "orange", width = 15, height = 2, relief = "groove", bd = 15, cursor = "pirate", font = (text_label, 15))
    button3_chest.pack(side = tkinter.LEFT, padx = 10, pady = 30)

    button4_chest = tkinter.Button(button_frame_b, text = "Aperturas", font = 15, relief = "groove", command = openins    )
    button4_chest.config(bg = "orange", width = 15, height = 2, relief = "groove", bd = 15, cursor = "pirate", font = (text_label, 15))
    button4_chest.pack(side = tkinter.LEFT, padx = 10, pady = 30)

    back_button = tkinter.Button(frame1, text = "Regresar", command = sup_routines_menu)
    back_button.config(bg = "orange" , width=15, height=2, relief = "groove", bd = 15, cursor = "pirate", font = (text_label, 15))
    back_button.pack(pady = 2)

    
def biceps_timer():

    
    def countdown():
        global total_time, is_paused, activity, rounds

        if total_time > 0 and not is_paused:
            mins, secs = divmod(total_time, 60)
            timer = f"{mins:02d}:{secs:02d}"
            label.config(text=f"{activity}: {timer}")
            total_time -= 1
            frame1.after(1000, countdown)  # Llama a countdown cada segundo
        elif total_time == 0:
            if activity == "Moviendote":
                activity = "Descanso"
                total_time = 30  # Tiempo de descanso
            else:
                rounds -= 1
                if rounds > 0:
                    activity = "Moviendote"
                    total_time = 25  # Tiempo de trabajo
                else:
                    label.config(text="Felicidades, lo has completado")
                    return
            countdown()  # Inicia el siguiente ciclo


    def start_timer():
        global total_time, activity, rounds
        activity = "Trabajo"
        total_time = 25  # Tiempo de trabajo
        countdown()


    def pause_timer():
        global is_paused
        is_paused = True


    def resume_timer():
        global is_paused
        is_paused = False
        countdown()
        

    label = tkinter.Label(frame1, text="", font=("Helvetica", 24))
    label.pack(pady=20)

    button_frame_a = tkinter.Frame(frame1, bg = "black")
    button_frame_a.pack(anchor = "nw", padx = 20, pady = 40)

    start_button = tkinter.Button(button_frame_a, text="Iniciar", command=start_timer)
    start_button.config(bg = "orange", width = 16, height = 2, relief = "groove", bd = 15, cursor = "pirate", font = (text_label, 15))
    start_button.pack(side=tkinter.LEFT, padx=10, pady=40)

    pause_button = tkinter.Button(button_frame_a, text="Pausar", command=pause_timer)
    pause_button.config(bg = "orange", width = 16, height = 2, relief = "groove", bd = 15, cursor = "pirate", font = (text_label, 15))
    pause_button.pack(side=tkinter.LEFT, padx=10, pady=20)


    resume_button = tkinter.Button(frame1, text="Reanudar/iniciar", command=resume_timer)
    resume_button.config(bg = "orange", width = 16, height = 2, relief = "groove", bd = 15, cursor = "pirate", font = (text_label, 15))
    resume_button.pack(side=tkinter.LEFT, padx=20, pady=20)

    exit_button = tkinter.Button(frame1, text="Salir", command = biceps_menu)
    exit_button.config(bg = "orange", width = 16, height = 2, relief = "groove", bd = 15, cursor = "pirate", font = (text_label, 15))
    exit_button.pack(side=tkinter.LEFT, padx=20, pady=20)
    

def curl_bar():
    
    clearwindow()
    biceps_timer()


    def image_window():

        image("curlbarra.jpg")


    image_window()


def curl_manc():
    
    clearwindow()
    biceps_timer()


    def image_window():

        image("curlmancuerna.jpg")
        

    image_window()


def focused_curl():
    clearwindow()
    
    biceps_timer()


    def image_window():

        image("focusedcurl.jpg")


    image_window()


def hammer_curl():

    clearwindow()
    biceps_timer()


    def image_window():

        image("hammercurl.jpg")

    image_window()


def biceps_menu():
    
    clearwindow()

    button_frame_a = tkinter.Frame(frame1, bg = "black")
    button_frame_a.pack(anchor = "nw", padx = 20, pady = 10)

    button1_biceps = tkinter.Button(button_frame_a, text = "Curl con barra", command = curl_bar      )
    button1_biceps.config(bg = "orange", width = 15, height = 2, relief = "groove", bd = 15, cursor = "pirate", font = (text_label, 15))
    button1_biceps.pack(side = tkinter.LEFT , padx = 10, pady = 30)

    button2_biceps = tkinter.Button(button_frame_a, text = "Curl mancuernas", command = curl_manc      )
    button2_biceps.config(bg = "orange", width = 15, height = 2, relief = "groove", bd = 15, cursor = "pirate", font = (text_label, 15))
    button2_biceps.pack(side = tkinter.LEFT, padx= 10, pady = 30 )

    button_frame_b = tkinter.Frame(frame1, bg = "black")
    button_frame_b.pack(anchor = "nw", padx = 20, pady = (10,0))    

    button3_biceps = tkinter.Button(button_frame_b, text = "Curl concentrado", font = 15, relief = "groove", command = focused_curl     )
    button3_biceps.config(bg = "orange", width = 15, height = 2, relief = "groove", bd = 15, cursor = "pirate", font = (text_label, 15))
    button3_biceps.pack(side = tkinter.LEFT, padx = 10, pady = 30)

    button4_biceps = tkinter.Button(button_frame_b, text = "Curl de martillo", font = 15, relief = "groove", command = hammer_curl    )
    button4_biceps.config(bg = "orange", width = 15, height = 2, relief = "groove", bd = 15, cursor = "pirate", font = (text_label, 15))
    button4_biceps.pack(side = tkinter.LEFT, padx = 10, pady = 30)

    back_button = tkinter.Button(frame1, text = "Regresar", command = sup_routines_menu)
    back_button.config(bg = "orange" , width=15, height=2, relief = "groove", bd = 15, cursor = "pirate", font = (text_label, 15))
    back_button.pack(pady = 2)


def back_timer():


    def countdown():
        global total_time, is_paused, activity, rounds

        if total_time > 0 and not is_paused:
            mins, secs = divmod(total_time, 60)
            timer = f"{mins:02d}:{secs:02d}"
            label.config(text=f"{activity}: {timer}")
            total_time -= 1
            frame1.after(1000, countdown)  # Llama a countdown cada segundo
        elif total_time == 0:
            if activity == "Moviendote":
                activity = "Descanso"
                total_time = 30  # Tiempo de descanso
            else:
                rounds -= 1
                if rounds > 0:
                    activity = "Moviendote"
                    total_time = 25  # Tiempo de trabajo
                else:
                    label.config(text="Felicidades, lo has completado")
                    return
            countdown()  # Inicia el siguiente ciclo

    def start_timer():
        global total_time, activity, rounds
        activity = "Trabajo"
        total_time = 25  # Tiempo de trabajo
        countdown()


    def pause_timer():
        global is_paused
        is_paused = True


    def resume_timer():
        global is_paused
        is_paused = False
        countdown()
        

    label = tkinter.Label(frame1, text="", font=("Helvetica", 24))
    label.pack(pady=20)

    button_frame_a = tkinter.Frame(frame1, bg = "black")
    button_frame_a.pack(anchor = "nw", padx = 20, pady = 40)

    start_button = tkinter.Button(button_frame_a, text="Iniciar", command=start_timer)
    start_button.config(bg = "orange", width = 16, height = 2, relief = "groove", bd = 15, cursor = "pirate", font = (text_label, 15))
    start_button.pack(side=tkinter.LEFT, padx=10, pady=40)

    pause_button = tkinter.Button(button_frame_a, text="Pausar", command=pause_timer)
    pause_button.config(bg = "orange", width = 16, height = 2, relief = "groove", bd = 15, cursor = "pirate", font = (text_label, 15))
    pause_button.pack(side=tkinter.LEFT, padx=10, pady=20)

    resume_button = tkinter.Button(frame1, text="Reanudar/iniciar", command=resume_timer)
    resume_button.config(bg = "orange", width = 16, height = 2, relief = "groove", bd = 15, cursor = "pirate", font = (text_label, 15))
    resume_button.pack(side=tkinter.LEFT, padx=20, pady=20)

    exit_button = tkinter.Button(frame1, text="Salir", command = back_menu)
    exit_button.config(bg = "orange", width = 16, height = 2, relief = "groove", bd = 15, cursor = "pirate", font = (text_label, 15))
    exit_button.pack(side=tkinter.LEFT, padx=20, pady=20)


def bar_rem():

    clearwindow()
    back_timer()


    def image_window():

        image("remobarra.jpg")


    image_window()


def pulldown():

    clearwindow()
    back_timer()


    def image_window():

        image("pulldown.jpg")


    image_window()


def deadlift():

    clearwindow()
    back_timer()


    def image_window():

        image("deadlift.jpg")

    image_window()


def rem_manc():

    clearwindow()
    back_timer()


    def image_window():

        image("remomancuerna.jpg")


    image_window()


def back_menu():

    clearwindow()

    button_frame_a = tkinter.Frame(frame1, bg = "black")
    button_frame_a.pack(anchor = "nw", padx = 20, pady = 10)

    button1_back = tkinter.Button(button_frame_a, text = "Remo con barra", command = bar_rem     )
    button1_back.config(bg = "orange", width = 15, height = 2, relief = "groove", bd = 15, cursor = "pirate", font = (text_label, 15))
    button1_back.pack(side = tkinter.LEFT , padx = 10, pady = 30)

    button2_back = tkinter.Button(button_frame_a, text = "Pulldown", command = pulldown      )
    button2_back.config(bg = "orange", width = 15, height = 2, relief = "groove", bd = 15, cursor = "pirate", font = (text_label, 15))
    button2_back.pack(side = tkinter.LEFT, padx= 10, pady = 30 )

    button_frame_b = tkinter.Frame(frame1, bg = "black")
    button_frame_b.pack(anchor = "nw", padx = 20, pady = (10,0))    

    button3_back = tkinter.Button(button_frame_b, text = "Peso muerto", font = 15, relief = "groove", command = deadlift     )
    button3_back.config(bg = "orange", width = 15, height = 2, relief = "groove", bd = 15, cursor = "pirate", font = (text_label, 15))
    button3_back.pack(side = tkinter.LEFT, padx = 10, pady = 30)

    button4_back = tkinter.Button(button_frame_b, text = "remo con mancuerna", font = 15, relief = "groove", command = rem_manc    )
    button4_back.config(bg = "orange", width = 16, height = 2, relief = "groove", bd = 15, cursor = "pirate", font = (text_label, 15))
    button4_back.pack(side = tkinter.LEFT, padx = 10, pady = 30)

    createbutton("Regresar", frame1, sup_routines_menu, 15, 2, 2)

def triceps_timer():


    def countdown():

        global total_time, is_paused, activity, rounds

        if total_time > 0 and not is_paused:
            mins, secs = divmod(total_time, 60)
            timer = f"{mins:02d}:{secs:02d}"
            label.config(text=f"{activity}: {timer}")
            total_time -= 1
            frame1.after(1000, countdown)  # Llama a countdown cada segundo
        elif total_time == 0:
            if activity == "Moviendote":
                activity = "Descanso"
                total_time = 30  # Tiempo de descanso
            else:
                rounds -= 1
                if rounds > 0:
                    activity = "Moviendote"
                    total_time = 25  # Tiempo de trabajo
                else:
                    label.config(text="Felicidades, lo has completado")
                    return
            countdown()  # Inicia el siguiente ciclo


    def start_timer():
        global total_time, activity, rounds
        activity = "Trabajo"
        total_time = 25  # Tiempo de trabajo
        countdown()


    def pause_timer():
        global is_paused
        is_paused = True


    def resume_timer():
        global is_paused
        is_paused = False
        countdown()
        

    label = tkinter.Label(frame1, text="", font=("Helvetica", 24))
    label.pack(pady=20)

    button_frame_a = tkinter.Frame(frame1, bg = "black")
    button_frame_a.pack(anchor = "nw", padx = 20, pady = 40)

    start_button = tkinter.Button(button_frame_a, text="Iniciar", command=start_timer)
    start_button.config(bg = "orange", width = 16, height = 2, relief = "groove", bd = 15, cursor = "pirate", font = (text_label, 15))
    start_button.pack(side=tkinter.LEFT, padx=10, pady=40)

    pause_button = tkinter.Button(button_frame_a, text="Pausar", command=pause_timer)
    pause_button.config(bg = "orange", width = 16, height = 2, relief = "groove", bd = 15, cursor = "pirate", font = (text_label, 15))
    pause_button.pack(side=tkinter.LEFT, padx=10, pady=20)

    resume_button = tkinter.Button(frame1, text="Reanudar/iniciar", command=resume_timer)
    resume_button.config(bg = "orange", width = 16, height = 2, relief = "groove", bd = 15, cursor = "pirate", font = (text_label, 15))
    resume_button.pack(side=tkinter.LEFT, padx=20, pady=20)

    exit_button = tkinter.Button(frame1, text="Salir", command = triceps_menu)
    exit_button.config(bg = "orange", width = 16, height = 2, relief = "groove", bd = 15, cursor = "pirate", font = (text_label, 15))
    exit_button.pack(side=tkinter.LEFT, padx=20, pady=20)


def manc_extensions():

    clearwindow()
    triceps_timer()


    def image_window():

        image("image3.jpg")


    image_window()


def french_press():

    clearwindow()
    back_timer()


    def image_window():

        image("french.jpg")


    image_window()


def tricep_kick():

    clearwindow()
    back_timer()


    def image_window():

        image("tricep_kick.jpg")


    image_window()


def paralels():

    clearwindow()
    
    back_timer()


    def image_window():

        image("paralels.jpg")


    image_window()


def triceps_menu():

    clearwindow()

    button_frame_a = tkinter.Frame(frame1, bg = "black")
    button_frame_a.pack(anchor = "nw", padx = 20, pady = 10)

    button1_tricep = tkinter.Button(button_frame_a, text = "Extensiones con mancuerna", command = manc_extensions     )
    button1_tricep.config(bg = "orange", width = 16, height = 2, relief = "groove", bd = 15, cursor = "pirate", font = (text_label, 15))
    button1_tricep.pack(side = tkinter.LEFT , padx = 10, pady = 30)

    button2_tricep = tkinter.Button(button_frame_a, text = "Press frances", command = french_press      )
    button2_tricep.config(bg = "orange", width = 15, height = 2, relief = "groove", bd = 15, cursor = "pirate", font = (text_label, 15))
    button2_tricep.pack(side = tkinter.LEFT, padx= 10, pady = 30 )

    button_frame_b = tkinter.Frame(frame1, bg = "black")
    button_frame_b.pack(anchor = "nw", padx = 20, pady = (10,0))    

    button3_tricep = tkinter.Button(button_frame_b, text = "Patada de triceps", font = 15, relief = "groove", command = tricep_kick    )
    button3_tricep.config(bg = "orange", width = 16, height = 2, relief = "groove", bd = 15, cursor = "pirate", font = (text_label, 15))
    button3_tricep.pack(side = tkinter.LEFT, padx = 10, pady = 30)

    button4_tricep = tkinter.Button(button_frame_b, text = "Fondos en paralelas", font = 15, relief = "groove", command = paralels    )
    button4_tricep.config(bg = "orange", width = 16, height = 2, relief = "groove", bd = 15, cursor = "pirate", font = (text_label, 15))
    button4_tricep.pack(side = tkinter.LEFT, padx = 10, pady = 30)

    back_button = tkinter.Button(frame1, text = "Regresar", command = sup_routines_menu)
    back_button.config(bg = "orange" , width=15, height=2, relief = "groove", bd = 15, cursor = "pirate", font = (text_label, 15))
    back_button.pack(pady = 2)
    

def shoulder_timer():


    def countdown():

        global total_time, is_paused, activity, rounds

        if total_time > 0 and not is_paused:
            mins, secs = divmod(total_time, 60)
            timer = f"{mins:02d}:{secs:02d}"
            label.config(text=f"{activity}: {timer}")
            total_time -= 1
            frame1.after(1000, countdown)  # Llama a countdown cada segundo
        elif total_time == 0:
            if activity == "Moviendote":
                activity = "Descanso"
                total_time = 30  # Tiempo de descanso
            else:
                rounds -= 1
                if rounds > 0:
                    activity = "Moviendote"
                    total_time = 25  # Tiempo de trabajo
                else:
                    label.config(text="Felicidades, lo has completado")
                    return
            countdown()  # Inicia el siguiente ciclo


    def start_timer():
        global total_time, activity, rounds
        activity = "Trabajo"
        total_time = 25  # Tiempo de trabajo
        countdown()


    def pause_timer():
        global is_paused
        is_paused = True


    def resume_timer():
        global is_paused
        is_paused = False
        countdown()
        

    label = tkinter.Label(frame1, text="", font=("Helvetica", 24))
    label.pack(pady=20)

    button_frame_a = tkinter.Frame(frame1, bg = "black")
    button_frame_a.pack(anchor = "nw", padx = 20, pady = 40)

    start_button = tkinter.Button(button_frame_a, text="Iniciar", command=start_timer)
    start_button.config(bg = "orange", width = 16, height = 2, relief = "groove", bd = 15, cursor = "pirate", font = (text_label, 15))
    start_button.pack(side=tkinter.LEFT, padx=10, pady=40)

    pause_button = tkinter.Button(button_frame_a, text="Pausar", command=pause_timer)
    pause_button.config(bg = "orange", width = 16, height = 2, relief = "groove", bd = 15, cursor = "pirate", font = (text_label, 15))
    pause_button.pack(side=tkinter.LEFT, padx=10, pady=20)

    resume_button = tkinter.Button(frame1, text="Reanudar/iniciar", command=resume_timer)
    resume_button.config(bg = "orange", width = 16, height = 2, relief = "groove", bd = 15, cursor = "pirate", font = (text_label, 15))
    resume_button.pack(side=tkinter.LEFT, padx=20, pady=20)

    exit_button = tkinter.Button(frame1, text="Salir", command = shoulder_menu)
    exit_button.config(bg = "orange", width = 16, height = 2, relief = "groove", bd = 15, cursor = "pirate", font = (text_label, 15))
    exit_button.pack(side=tkinter.LEFT, padx=20, pady=20)


def militar_press():

    clearwindow()
    shoulder_timer()


    def image_window():

        image("pressmil.jpg")


    image_window()


def lateral_elevations():

    clearwindow()
    shoulder_timer()


    def image_window():

        image("image4.jpg")


    image_window()


def frontal_elev():
    clearwindow()
    
    shoulder_timer()


    def image_window():

        image("frontales.jpg")


    image_window()


def shrughs():
    clearwindow()
    
    shoulder_timer()


    def image_window():

        image("shrugs.jpg")


    image_window()


def shoulder_menu():
    
    clearwindow()
        

    button_frame_a = tkinter.Frame(frame1, bg = "black")
    button_frame_a.pack(anchor = "nw", padx = 20, pady = 10)

    button1_shoulder = tkinter.Button(button_frame_a, text = "Press militar", command = militar_press     )
    button1_shoulder.config(bg = "orange", width = 16, height = 2, relief = "groove", bd = 15, cursor = "pirate", font = (text_label, 15))
    button1_shoulder.pack(side = tkinter.LEFT , padx = 10, pady = 30)

    button2_shoulder = tkinter.Button(button_frame_a, text = "Elevaciones laterales", command = lateral_elevations      )
    button2_shoulder.config(bg = "orange", width = 16, height = 2, relief = "groove", bd = 15, cursor = "pirate", font = (text_label, 15))
    button2_shoulder.pack(side = tkinter.LEFT, padx= 10, pady = 30 )

    button_frame_b = tkinter.Frame(frame1, bg = "black")
    button_frame_b.pack(anchor = "nw", padx = 20, pady = (10,0))    

    button3_shoulder = tkinter.Button(button_frame_b, text = "Elevaciones frontales", font = 15, relief = "groove", command = frontal_elev    )
    button3_shoulder.config(bg = "orange", width = 16, height = 2, relief = "groove", bd = 15, cursor = "pirate", font = (text_label, 15))
    button3_shoulder.pack(side = tkinter.LEFT, padx = 10, pady = 30)

    button4_shoulder = tkinter.Button(button_frame_b, text = "Shrugs", font = 15, relief = "groove", command = shrughs    )
    button4_shoulder.config(bg = "orange", width = 16, height = 2, relief = "groove", bd = 15, cursor = "pirate", font = (text_label, 15))
    button4_shoulder.pack(side = tkinter.LEFT, padx = 10, pady = 30)

    back_button = tkinter.Button(frame1, text = "Regresar", command = sup_routines_menu)
    back_button.config(bg = "orange" , width=15, height=2, relief = "groove", bd = 15, cursor = "pirate", font = (text_label, 15))
    back_button.pack(pady = 2)


def abs_timer():


    def countdown():
        global total_time, is_paused, activity, rounds

        if total_time > 0 and not is_paused:
            mins, secs = divmod(total_time, 60)
            timer = f"{mins:02d}:{secs:02d}"
            label.config(text=f"{activity}: {timer}")
            total_time -= 1
            frame1.after(1000, countdown)  # Llama a countdown cada segundo
        elif total_time == 0:
            if activity == "Moviendote":
                activity = "Descanso"
                total_time = 30  # Tiempo de descanso
            else:
                rounds -= 1
                if rounds > 0:
                    activity = "Moviendote"
                    total_time = 25  # Tiempo de trabajo
                else:
                    label.config(text="Felicidades, lo has completado")
                    return
            countdown()  # Inicia el siguiente ciclo


    def start_timer():
        global total_time, activity, rounds
        activity = "Trabajo"
        total_time = 25  # Tiempo de trabajo
        countdown()


    def pause_timer():
        global is_paused
        is_paused = True


    def resume_timer():
        global is_paused
        is_paused = False
        countdown()
        

    label = tkinter.Label(frame1, text="", font=("Helvetica", 24))
    label.pack(pady=20)

    button_frame_a = tkinter.Frame(frame1, bg = "black")
    button_frame_a.pack(anchor = "nw", padx = 20, pady = 40)

    start_button = tkinter.Button(button_frame_a, text="Iniciar", command=start_timer)
    start_button.config(bg = "orange", width = 16, height = 2, relief = "groove", bd = 15, cursor = "pirate", font = (text_label, 15))
    start_button.pack(side=tkinter.LEFT, padx=10, pady=40)

    pause_button = tkinter.Button(button_frame_a, text="Pausar", command=pause_timer)
    pause_button.config(bg = "orange", width = 16, height = 2, relief = "groove", bd = 15, cursor = "pirate", font = (text_label, 15))
    pause_button.pack(side=tkinter.LEFT, padx=10, pady=20)

    resume_button = tkinter.Button(frame1, text="Reanudar/iniciar", command=resume_timer)
    resume_button.config(bg = "orange", width = 16, height = 2, relief = "groove", bd = 15, cursor = "pirate", font = (text_label, 15))
    resume_button.pack(side=tkinter.LEFT, padx=20, pady=20)

    exit_button = tkinter.Button(frame1, text="Salir", command = abs_menu)
    exit_button.config(bg = "orange", width = 16, height = 2, relief = "groove", bd = 15, cursor = "pirate", font = (text_label, 15))
    exit_button.pack(side=tkinter.LEFT, padx=20, pady=20)


def crunches():

    clearwindow()
    
    abs_timer()


    def image_window():

        image("crunches.jpg")


    image_window()


def leg_raisin():
    clearwindow()
    
    abs_timer()


    def image_window():

        image("image5.jpg")


    image_window()


def plank():
    clearwindow()
    
    abs_timer()


    def image_window():

        image("plank.jpg")


    image_window()


def russian_twist():
    clearwindow()
    
    abs_timer()


    def image_window():

        image("russian.jpg")


    image_window()


def abs_menu():

    clearwindow()

    button_frame_a = tkinter.Frame(frame1, bg = "black")
    button_frame_a.pack(anchor = "nw", padx = 20, pady = 10)

    button1_abs = tkinter.Button(button_frame_a, text = "Crunches", command = crunches     )
    button1_abs.config(bg = "orange", width = 16, height = 2, relief = "groove", bd = 15, cursor = "pirate", font = (text_label, 15))
    button1_abs.pack(side = tkinter.LEFT , padx = 10, pady = 30)

    button2_abs = tkinter.Button(button_frame_a, text = "Elevaciones de piernas", command = leg_raisin       )
    button2_abs.config(bg = "orange", width = 17, height = 2, relief = "groove", bd = 15, cursor = "pirate", font = (text_label, 15))
    button2_abs.pack(side = tkinter.LEFT, padx= 10, pady = 30 )

    button_frame_b = tkinter.Frame(frame1, bg = "black")
    button_frame_b.pack(anchor = "nw", padx = 20, pady = (10,0))    

    button3_abs = tkinter.Button(button_frame_b, text = "Plancha", font = 15, relief = "groove", command = plank    )
    button3_abs.config(bg = "orange", width = 16, height = 2, relief = "groove", bd = 15, cursor = "pirate", font = (text_label, 15))
    button3_abs.pack(side = tkinter.LEFT, padx = 10, pady = 30)

    button4_abs = tkinter.Button(button_frame_b, text = "Russian twists", font = 15, relief = "groove", command = russian_twist    )
    button4_abs.config(bg = "orange", width = 16, height = 2, relief = "groove", bd = 15, cursor = "pirate", font = (text_label, 15))
    button4_abs.pack(side = tkinter.LEFT, padx = 10, pady = 30)

    back_button = tkinter.Button(frame1, text = "Regresar", command = sup_routines_menu)
    back_button.config(bg = "orange" , width=15, height=2, relief = "groove", bd = 15, cursor = "pirate", font = (text_label, 15))
    back_button.pack(pady = 2)


def sup_routines_menu(): #va a mostrar el nuevo menú, luego de presionar el boton de rutinas preestablecidas

    clearwindow()


    label2 = tkinter.Label(frame1, text = "Tren superior", font = 15,relief = "groove")
    label2.config(padx = 10)
    label2.pack(anchor = "nw", padx = 220, pady = 20) #anchor es para ubicarlo con puntos cardinales

    button_frame = tkinter.Frame(frame1, bg = "black")
    button_frame.pack(anchor = "nw", padx = 20, pady = 10)

    button4 = tkinter.Button(button_frame, text = "Pecho", command = chest_menu   )
    button4.config(bg = "orange", width = 15, height = 2, relief = "groove", bd = 15, cursor = "pirate", font = (text_label, 15))
    button4.pack(side = tkinter.LEFT , padx = 10, pady = 30)

    button7 = tkinter.Button(button_frame, text = "Biceps", command = biceps_menu   )
    button7.config(bg = "orange", width = 15, height = 2, relief = "groove", bd = 15, cursor = "pirate", font = (text_label, 15))
    button7.pack(side = tkinter.LEFT, padx= 10, pady = 30 )

    button_frame2 = tkinter.Frame(frame1, bg = "black")
    button_frame2.pack(anchor = "nw", padx = 20, pady = (10,0))    

    button5 = tkinter.Button(button_frame2, text = "Espalda", font = 15, relief = "groove", command = back_menu)
    button5.config(bg = "orange", width = 15, height = 2, relief = "groove", bd = 15, cursor = "pirate", font = (text_label, 15))
    button5.pack(side = tkinter.LEFT, padx = 10, pady = 30)

    button8 = tkinter.Button(button_frame2, text = "Triceps", font = 15, relief = "groove", command = triceps_menu)
    button8.config(bg = "orange", width = 15, height = 2, relief = "groove", bd = 15, cursor = "pirate", font = (text_label, 15))
    button8.pack(side = tkinter.LEFT, padx = 10, pady = 30)

    button_frame3 = tkinter.Frame(frame1, bg = "black")
    button_frame3.pack(anchor = "sw", padx = 20, pady = (10,0))

    button6 = tkinter.Button(button_frame3, text = "Hombros", command = shoulder_menu    )
    button6.config(bg = "orange", width = 15, height = 2, relief = "groove", bd = 15, cursor = "pirate", font = (text_label, 15))
    button6.pack(side = tkinter.LEFT, padx = 10, pady = 30)

    button9 = tkinter.Button(button_frame3, text = "Abdominales", command = abs_menu    )
    button9.config(bg = "orange", width = 15, height = 2, relief = "groove", bd = 15, cursor = "pirate", font = (text_label, 15))
    button9.pack(side = tkinter.LEFT, padx = 10, pady = 30)

    back_button = tkinter.Button(frame1, text = "Regresar", command = show_new_window2)
    back_button.config(bg = "orange" , width=15, height=2, relief = "groove", bd = 15, cursor = "pirate", font = (text_label, 15))
    back_button.pack(pady = 2)


def timer_legs():


    def countdown():
        global total_time, is_paused, activity, rounds

        if total_time > 0 and not is_paused:
            mins, secs = divmod(total_time, 60)
            timer = f"{mins:02d}:{secs:02d}"
            label.config(text=f"{activity}: {timer}")
            total_time -= 1
            frame1.after(1000, countdown)  # Llama a countdown cada segundo
        elif total_time == 0:
            if activity == "Moviendote":
                activity = "Descanso"
                total_time = 30  # Tiempo de descanso
            else:
                rounds -= 1
                if rounds > 0:
                    activity = "Moviendote"
                    total_time = 25  # Tiempo de trabajo
                else:
                    label.config(text="Felicidades, lo has completado")
                    return
            countdown()  # Inicia el siguiente ciclo


    def start_timer():
        global total_time, activity, rounds
        activity = "Trabajo"
        total_time = 25  # Tiempo de trabajo
        countdown()


    def pause_timer():
        global is_paused
        is_paused = True


    def resume_timer():
        global is_paused
        is_paused = False
        countdown()

        
    label = tkinter.Label(frame1, text="", font=("Helvetica", 24))
    label.pack(pady=20)

    button_frame_a = tkinter.Frame(frame1, bg = "black")
    button_frame_a.pack(anchor = "nw", padx = 20, pady = 40)

    start_button = tkinter.Button(button_frame_a, text="Iniciar", command=start_timer)
    start_button.config(bg = "orange", width = 16, height = 2, relief = "groove", bd = 15, cursor = "pirate", font = (text_label, 15))
    start_button.pack(side=tkinter.LEFT, padx=10, pady=40)

    pause_button = tkinter.Button(button_frame_a, text="Pausar/reaunudar", command=pause_timer)
    pause_button.config(bg = "orange", width = 16, height = 2, relief = "groove", bd = 15, cursor = "pirate", font = (text_label, 15))
    pause_button.pack(side=tkinter.LEFT, padx=10, pady=20)

    resume_button = tkinter.Button(frame1, text="Reanudar/iniciar", command=resume_timer)
    resume_button.config(bg = "orange", width = 16, height = 2, relief = "groove", bd = 15, cursor = "pirate", font = (text_label, 15))
    resume_button.pack(side=tkinter.LEFT, padx=20, pady=20)

    exit_button = tkinter.Button(frame1, text="Salir", command = leg_menu,)
    exit_button.config(bg = "orange", width = 16, height = 2, relief = "groove", bd = 15, cursor = "pirate", font = (text_label, 15))
    exit_button.pack(side=tkinter.LEFT, padx=20, pady=20)


def deadlift_ruman():
    clearwindow()
    timer_legs()


    def image_window():

        image("image1.jpg")


    image_window()


def squats():
    clearwindow()

    timer_legs()


    def image_window():

        image("sentadillas.jpg")


    image_window()


def Press():
    clearwindow()

    timer_legs()


    def image_window():

        image("presspierna.jpg")


    image_window()


def strides():
    clearwindow()

    timer_legs()


    def image_window():

        image("zancadas.jpg")


    image_window()
    

def leg_menu():
    clearwindow()


    button_frame_a = tkinter.Frame(frame1, bg = "black")
    button_frame_a.pack(anchor = "nw", padx = 20, pady = 10)

    button1_legs = tkinter.Button(button_frame_a, text = "Sentadillas", command = squats     )
    button1_legs.config(bg = "orange", width = 16, height = 2, relief = "groove", bd = 15, cursor = "pirate", font = (text_label, 15))
    button1_legs.pack(side = tkinter.LEFT , padx = 10, pady = 30)

    button2_legs = tkinter.Button(button_frame_a, text = "Prensa", command = Press      )
    button2_legs.config(bg = "orange", width = 17, height = 2, relief = "groove", bd = 15, cursor = "pirate", font = (text_label, 15))
    button2_legs.pack(side = tkinter.LEFT, padx= 10, pady = 30 )

    button_frame_b = tkinter.Frame(frame1, bg = "black")
    button_frame_b.pack(anchor = "nw", padx = 20, pady = (10,0))    

    button3_legs = tkinter.Button(button_frame_b, text = "Peso muerto rumano", font = 15, relief = "groove", command = deadlift_ruman    )
    button3_legs.config(bg = "orange", width = 16, height = 2, relief = "groove", bd = 15, cursor = "pirate", font = (text_label, 15))
    button3_legs.pack(side = tkinter.LEFT, padx = 10, pady = 30)

    button4_legs = tkinter.Button(button_frame_b, text = "Zancadas", font = 15, relief = "groove", command = strides    )
    button4_legs.config(bg = "orange", width = 16, height = 2, relief = "groove", bd = 15, cursor = "pirate", font = (text_label, 15))
    button4_legs.pack(side = tkinter.LEFT, padx = 10, pady = 30)

    back_button = tkinter.Button(frame1, text = "Regresar", command = inf_routines_menu)
    back_button.config(bg = "orange" , width=15, height=2, relief = "groove", bd = 15, cursor = "pirate", font = (text_label, 15))
    back_button.pack(pady = 2)
 

def calves_timer():
 

    def countdown():

        global total_time, is_paused, activity, rounds

        if total_time > 0 and not is_paused:
            mins, secs = divmod(total_time, 60)
            timer = f"{mins:02d}:{secs:02d}"
            label.config(text=f"{activity}: {timer}")
            total_time -= 1
            frame1.after(1000, countdown)  
        elif total_time == 0:
            if activity == "Moviendote":
                activity = "Descanso"
                total_time = 30  
            else:
                rounds -= 1
                if rounds > 0:
                    activity = "Moviendote"
                    total_time = 25  
                else:
                    label.config(text="Felicidades, lo has completado")
                    return
            countdown()  


    def start_timer():
        global total_time, activity, rounds
        activity = "Trabajo"
        total_time = 25  
        countdown()


    def pause_timer():
        global is_paused
        is_paused = True


    def resume_timer():
        global is_paused
        is_paused = False
        countdown()


    label = tkinter.Label(frame1, text="", font=("Helvetica", 24))
    label.pack(pady=20)

    button_frame_a = tkinter.Frame(frame1, bg = "black")
    button_frame_a.pack(anchor = "nw", padx = 20, pady = 40)

    start_button = tkinter.Button(button_frame_a, text="Iniciar", command=start_timer)
    start_button.config(bg = "orange", width = 16, height = 2, relief = "groove", bd = 15, cursor = "pirate", font = (text_label, 15))
    start_button.pack(side=tkinter.LEFT, padx=10, pady=40)

    pause_button = tkinter.Button(button_frame_a, text="Pausar", command=pause_timer)
    pause_button.config(bg = "orange", width = 16, height = 2, relief = "groove", bd = 15, cursor = "pirate", font = (text_label, 15))
    pause_button.pack(side=tkinter.LEFT, padx=10, pady=20)

    resume_button = tkinter.Button(frame1, text="Reanudar/iniciar", command=resume_timer)
    resume_button.config(bg = "orange", width = 16, height = 2, relief = "groove", bd = 15, cursor = "pirate", font = (text_label, 15))
    resume_button.pack(side=tkinter.LEFT, padx=20, pady=20)

    exit_button = tkinter.Button(frame1, text="Salir", command = calves_menu)
    exit_button.config(bg = "orange", width = 16, height = 2, relief = "groove", bd = 15, cursor = "pirate", font = (text_label, 15))
    exit_button.pack(side=tkinter.LEFT, padx=20, pady=20)
    

def calves_raising():

    clearwindow()

    calves_timer()


    def image_window():

        image("elevacionesdepie.jpg")


    image_window()


def sit_raising():

    clearwindow()
    calves_timer()


    def image_window():

        image("pantorrillassentado.jpg")


    image_window()


def calves_press():

    clearwindow()
    calves_timer()


    def image_window():

        image("calvespress.jpg")


    image_window()


def calves_jumpin():

    clearwindow()
    calves_timer()


    def image_window():

        image("calvesjumpin.jpg")


    image_window()
    

def calves_menu():

    clearwindow()

    button_frame_a = tkinter.Frame(frame1, bg = "black")
    button_frame_a.pack(anchor = "nw", padx = 20, pady = 10)

    button1_calves = tkinter.Button(button_frame_a, text = "E. de talones de pie",  command= calves_raising    )
    button1_calves.config(bg = "orange", width = 16, height = 2, relief = "groove", bd = 15, cursor = "pirate", font = (text_label, 15))
    button1_calves.pack(side = tkinter.LEFT , padx = 10, pady = 30)

    button2_calves = tkinter.Button(button_frame_a, text = "E. de talones sentado", command = sit_raising      )
    button2_calves.config(bg = "orange", width = 17, height = 2, relief = "groove", bd = 15, cursor = "pirate", font = (text_label, 15))
    button2_calves.pack(side = tkinter.LEFT, padx= 10, pady = 30 )

    button_frame_b = tkinter.Frame(frame1, bg = "black")
    button_frame_b.pack(anchor = "nw", padx = 20, pady = (10,0))    

    button3_calves = tkinter.Button(button_frame_b, text = "Elevación en prensa", font = 15, relief = "groove", command= calves_press     )
    button3_calves.config(bg = "orange", width = 16, height = 2, relief = "groove", bd = 15, cursor = "pirate", font = (text_label, 15))
    button3_calves.pack(side = tkinter.LEFT, padx = 10, pady = 30)

    button4_calves = tkinter.Button(button_frame_b, text = "Saltos de pantorrilla", font = 15, relief = "groove", command = calves_jumpin    )
    button4_calves.config(bg = "orange", width = 16, height = 2, relief = "groove", bd = 15, cursor = "pirate", font = (text_label, 15))
    button4_calves.pack(side = tkinter.LEFT, padx = 10, pady = 30)

    back_button = tkinter.Button(frame1, text = "Regresar", command = inf_routines_menu)
    back_button.config(bg = "orange" , width=15, height=2, relief = "groove", bd = 15, cursor = "pirate", font = (text_label, 15))
    back_button.pack(pady = 2)


def gluteus_timer():


    def countdown():

        global total_time, is_paused, activity, rounds

        if total_time > 0 and not is_paused:
            mins, secs = divmod(total_time, 60)
            timer = f"{mins:02d}:{secs:02d}"
            label.config(text=f"{activity}: {timer}")
            total_time -= 1
            frame1.after(1000, countdown)  
        elif total_time == 0:
            if activity == "Moviendote":
                activity = "Descanso"
                total_time = 30  
            else:
                rounds -= 1
                if rounds > 0:
                    activity = "Moviendote"
                    total_time = 25  
                else:
                    label.config(text="Felicidades, lo has completado")
                    return
            countdown()  

    def start_timer():
        global total_time, activity, rounds
        activity = "Trabajo"
        total_time = 25  
        countdown()


    def pause_timer():
        global is_paused
        is_paused = True


    def resume_timer():
        global is_paused
        is_paused = False
        countdown()


    label = tkinter.Label(frame1, text="", font=("Helvetica", 24))
    label.pack(pady=20)

    button_frame_a = tkinter.Frame(frame1, bg = "black")
    button_frame_a.pack(anchor = "nw", padx = 20, pady = 40)

    start_button = tkinter.Button(button_frame_a, text="Iniciar", command=start_timer)
    start_button.config(bg = "orange", width = 16, height = 2, relief = "groove", bd = 15, cursor = "pirate", font = (text_label, 15))
    start_button.pack(side=tkinter.LEFT, padx=10, pady=40)

    pause_button = tkinter.Button(button_frame_a, text="Pausar", command=pause_timer)
    pause_button.config(bg = "orange", width = 16, height = 2, relief = "groove", bd = 15, cursor = "pirate", font = (text_label, 15))
    pause_button.pack(side=tkinter.LEFT, padx=10, pady=20)

    resume_button = tkinter.Button(frame1, text="Reanudar/iniciar", command=resume_timer)
    resume_button.config(bg = "orange", width = 16, height = 2, relief = "groove", bd = 15, cursor = "pirate", font = (text_label, 15))
    resume_button.pack(side=tkinter.LEFT, padx=20, pady=20)

    exit_button = tkinter.Button(frame1, text="Salir", command = gluteus_menu)
    exit_button.config(bg = "orange", width = 16, height = 2, relief = "groove", bd = 15, cursor = "pirate", font = (text_label, 15))
    exit_button.pack(side=tkinter.LEFT, padx=20, pady=20)
    

def bridges():

    clearwindow()
    gluteus_timer()


    def image_window():

        image("bridges.jpg")


    image_window()


def sumo():

    clearwindow()
    gluteus_timer()


    def image_window():

        image("sumo.jpg")


    image_window()


def waist_raisin():

    clearwindow()
    gluteus_timer()


    def image_window():

        image("waistraisin.jpg")


    image_window()


def lateral():

    clearwindow()
    gluteus_timer()


    def image_window():

        image("lateral.jpg")


    image_window()


def gluteus_menu():

    clearwindow()
    button_frame_a = tkinter.Frame(frame1, bg = "black")
    button_frame_a.pack(anchor = "nw", padx = 20, pady = 10)

    button1_calves = tkinter.Button(button_frame_a, text = "Puente", command = bridges     )
    button1_calves.config(bg = "orange", width = 16, height = 2, relief = "groove", bd = 15, cursor = "pirate", font = (text_label, 15))
    button1_calves.pack(side = tkinter.LEFT , padx = 10, pady = 30)

    button2_calves = tkinter.Button(button_frame_a, text = "Sentadillas sumo", command = sumo      )
    button2_calves.config(bg = "orange", width = 17, height = 2, relief = "groove", bd = 15, cursor = "pirate", font = (text_label, 15))
    button2_calves.pack(side = tkinter.LEFT, padx= 10, pady = 30 )

    button_frame_b = tkinter.Frame(frame1, bg = "black")
    button_frame_b.pack(anchor = "nw", padx = 20, pady = (10,0))    

    button3_calves = tkinter.Button(button_frame_b, text = "Elevaciones de cadera", font = 15, relief = "groove", command = waist_raisin    )
    button3_calves.config(bg = "orange", width = 16, height = 2, relief = "groove", bd = 15, cursor = "pirate", font = (text_label, 15))
    button3_calves.pack(side = tkinter.LEFT, padx = 10, pady = 30)

    button4_calves = tkinter.Button(button_frame_b, text = "Zancadas laterales", font = 15, relief = "groove", command = lateral    )
    button4_calves.config(bg = "orange", width = 16, height = 2, relief = "groove", bd = 15, cursor = "pirate", font = (text_label, 15))
    button4_calves.pack(side = tkinter.LEFT, padx = 10, pady = 30)

    back_button = tkinter.Button(frame1, text = "Regresar", command = inf_routines_menu)
    back_button.config(bg = "orange" , width=15, height=2, relief = "groove", bd = 15, cursor = "pirate", font = (text_label, 15))
    back_button.pack(pady = 2)

    
def inf_routines_menu():

    clearwindow()
    
    label3 = tkinter.Label(frame1, text = "tren inferior", font = 15,relief = "groove",     )
    label3.config(padx = 10)
    label3.pack(anchor = "nw", padx = 220, pady = 20)

    button_frame4 = tkinter.Frame(frame1, bg = "black")
    button_frame4.pack(anchor = "nw", padx = 20, pady = (10,0))

    button10 = tkinter.Button(button_frame4, text = "Pierna", command = leg_menu     )
    button10.config(bg = "orange", width = 15, height = 2, relief = "groove", bd = 15, cursor = "pirate", font = (text_label, 15))
    button10.pack(side = tkinter.LEFT, padx = 10, pady = 30)

    button11 = tkinter.Button(button_frame4, text = "Pantorrilla", command = calves_menu     )
    button11.config(bg = "orange", width = 15, height = 2, relief = "groove", bd = 15, cursor = "pirate", font = (text_label, 15))
    button11.pack(side = tkinter.LEFT, padx = 10, pady = 30)

    button_frame5 = tkinter.Frame(frame1, bg = "black")
    button_frame5.pack(anchor = "nw", padx = 20, pady = (10,0))

    button12 = tkinter.Button(button_frame5, text = "Glúteo",  command = gluteus_menu    )
    button12.config(bg = "orange", width = 15, height = 2, relief = "groove", bd = 15, cursor = "pirate", font = (text_label, 15))
    button12.pack(side = tkinter.LEFT, padx = 10, pady = 30)

    back_button = tkinter.Button(frame1, text = "Regresar", command = show_new_window2)
    back_button.config(bg = "orange" , width=15, height=2, relief = "groove", bd = 15, cursor = "pirate", font = (text_label, 15))
    back_button.pack(side = tkinter.BOTTOM )


def go_back(): #permite regresar al boton de ingresar
    clearwindow()
    button1.pack(pady = 200)


frame1 = tkinter.Frame(window, bg = "black")
frame1.config(width = 1000, height = 1000)
frame1.pack(expand = True, fill = tkinter.BOTH)

#etiquette = tkinter.Label(window, text = "Bienvenido a Workout app") #es una etiqueta
#etiquette.pack()  # mostrar en pantalla

button1 = tkinter.Button(frame1, text = "ingresar", font = text_label, command = show_new_window)
button1.config(bg = "gold" , width=10, height=2, relief = "groove", bd = 15, cursor = "pirate")
button1.pack(pady = 200)

window.mainloop() #lleva el registro de todo lo que pasa en la ventana
