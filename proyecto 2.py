# CALCULADORA DE IMC
# JESUS ALESSANDRO RAMOS AJU
# VICTOR DANIEL DE LA CRUZ HERNANDEZ

import tkinter as tk
from tkinter import messagebox


# FUNCION CALCULAR IMC


def calcular():
    try:
        nombre = entrada_nombre.get()
        edad = int(entrada_edad.get())
        peso = float(entrada_peso.get())
        altura = float(entrada_altura.get())

        if nombre == "":
            messagebox.showerror("Error", "Ingrese su nombre")
            return

        if peso <= 0 or altura <= 0:
            messagebox.showerror("Error", "Peso y altura deben ser mayores que cero")
            return

        imc = peso / (altura ** 2)

        # Clasificación y recomendaciones
        if imc < 18.5:
            clasificacion = "BAJO PESO"
            recomendacion = "Procura una alimentacion equilibrada y consulta a un especialista."

        elif imc < 25:
            clasificacion = "PESO NORMAL"
            recomendacion = "Mantenga una alimentacion saludable y realice ejercicio regularmente."

        elif imc < 30:
            clasificacion = "SOBREPESO"
            recomendacion = "Aumente la actividad fisica y reduzca el consumo de comida chatarra."

        else:
            clasificacion = "OBESIDAD"
            recomendacion = "Se recomienda acudir con un profesional de la salud."

        resultado.config(
            text=f"Nombre: {nombre}\n"
                 f"Edad: {edad} años\n"
                 f"Peso: {peso} kg\n"
                 f"Altura: {altura} m\n"
                 f"{'-'*35}\n"
                 f"IMC: {imc:.2f}\n"
                 f"Clasificacion: {clasificacion}\n\n"
                 f"Recomendacion:\n{recomendacion}")
        

        messagebox.showinfo("Exito", "Calculo realizado correctamente")

    except ValueError:
        messagebox.showerror("Error", "Ingrese datos numericos validos")



# FUNCION LIMPIAR


def limpiar():
    entrada_nombre.delete(0, tk.END)
    entrada_edad.delete(0, tk.END)
    entrada_peso.delete(0, tk.END)
    entrada_altura.delete(0, tk.END)
    resultado.config(text="")



# FUNCION SALIR


def salir():
    respuesta = messagebox.askyesno(
        "Salir",
        "¿Desea salir del programa?")
    

    if respuesta:
        ventana.destroy()


# VENTANA PRINCIPAL

ventana = tk.Tk()
ventana.title("Calculadora de IMC")
ventana.geometry("600x650")
ventana.config(bg="#F5F7FA")

# TITULO

titulo = tk.Label(
    ventana,
    text="CALCULADORA DE IMC",
    font=("Segoe UI", 20, "bold"),
    bg="#F5F7FA",
    fg="#2563EB")

titulo.pack(pady=10)

subtitulo = tk.Label(
    ventana,
    text="Indice de Masa Corporal",
    font=("Segoe UI", 11),
    bg="#F5F7FA",
    fg="#6B7280")

subtitulo.pack()

# FRAME DATOS

frame = tk.Frame(
    ventana,
    bg="white",
    bd=2,
    relief="groove")


frame.pack(padx=20, pady=20)

# Nombre

tk.Label(
    frame,
    text="Nombre:",
    bg="white",
    font=("Segoe UI", 10, "bold"))
.grid(row=0, column=0, padx=10, pady=10)

entrada_nombre = tk.Entry(
    frame,
    width=30,
    font=("Segoe UI", 10)
)
entrada_nombre.grid(row=0, column=1)

# Edad

tk.Label(
    frame,
    text="Edad:",
    bg="white",
    font=("Segoe UI", 10, "bold")
).grid(row=1, column=0, padx=10, pady=10)

entrada_edad = tk.Entry(
    frame,
    width=30,
    font=("Segoe UI", 10)
)
entrada_edad.grid(row=1, column=1)

# Peso

tk.Label(
    frame,
    text="Peso (kg):",
    bg="white",
    font=("Segoe UI", 10, "bold")
).grid(row=2, column=0, padx=10, pady=10)

entrada_peso = tk.Entry(
    frame,
    width=30,
    font=("Segoe UI", 10)
)
entrada_peso.grid(row=2, column=1)

# Altura

tk.Label(
    frame,
    text="Altura (m):",
    bg="white",
    font=("Segoe UI", 10, "bold")
).grid(row=3, column=0, padx=10, pady=10)

entrada_altura = tk.Entry(
    frame,
    width=30,
    font=("Segoe UI", 10)
)
entrada_altura.grid(row=3, column=1)

# BOTONES

frame_botones = tk.Frame(
    ventana,
    bg="#F5F7FA"
)

frame_botones.pack(pady=10)

btn_calcular = tk.Button(
    frame_botones,
    text="CALCULAR",
    command=calcular,
    bg="#2563EB",
    fg="white",
    font=("Segoe UI", 10, "bold"),
    width=15
)

btn_calcular.pack(side="left", padx=10)

btn_limpiar = tk.Button(
    frame_botones,
    text="LIMPIAR",
    command=limpiar,
    bg="#DC2626",
    fg="white",
    font=("Segoe UI", 10, "bold"),
    width=15
)

btn_limpiar.pack(side="left", padx=10)

btn_salir = tk.Button(
    frame_botones,
    text="SALIR",
    command=salir,
    bg="#374151",
    fg="white",
    font=("Segoe UI", 10, "bold"),
    width=15
)

btn_salir.pack(side="left", padx=10)

# RESULTADOS


frame_resultado = tk.LabelFrame(
    ventana,
    text="RESULTADO DEL IMC",
    font=("Segoe UI", 11, "bold"),
    bg="#E2E8F0",
    padx=15,
    pady=15
)

frame_resultado.pack(
    padx=20,
    pady=20,
    fill="both"
)

resultado = tk.Label(
    frame_resultado,
    text="Ingrese sus datos y presione CALCULAR",
    bg="#E2E8F0",
    justify="left",
    font=("Consolas", 11)
)

resultado.pack()

# PIE DE PAGINA

pie = tk.Label(
    ventana,
    text="Proyecto de Programacion - Calculadora de IMC",
    bg="#F5F7FA",
    fg="#6B7280",
    font=("Segoe UI", 9)
)

pie.pack(side="bottom", pady=10)

ventana.mainloop()