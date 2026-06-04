# CALCULADORA DE IMC
# JESUS ALESSANDRO RAMOS AJU
# VICTOR DANIEL DE LA CRUZ HERNANDEZ

import tkinter as tk
from tkinter import messagebox

# FUNCION CALCULAR

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

        if imc < 18.5:
            clasificacion = "BAJO PESO"
            recomendacion = "Procura una alimentación equilibrada y consulta a un especialista."

        elif imc < 25:
            clasificacion = "PESO NORMAL"
            recomendacion = "Mantenga una alimentación saludable y realice ejercicio regularmente."

        elif imc < 30:
            clasificacion = "SOBREPESO"
            recomendacion = "Aumente la actividad física y reduzca el consumo de comida chatarra."

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
                 f"Clasificación: {clasificacion}\n\n"
                 f"Recomendación:\n{recomendacion}"
        )

        messagebox.showinfo("Éxito", "Cálculo realizado correctamente")

    except ValueError:
        messagebox.showerror("Error", "Ingrese datos numéricos válidos")


# FUNCION LIMPIAR

def limpiar():
    entrada_nombre.delete(0, tk.END)
    entrada_edad.delete(0, tk.END)
    entrada_peso.delete(0, tk.END)
    entrada_altura.delete(0, tk.END)

    resultado.config(
        text="Ingrese sus datos y presione CALCULAR"
    )


# FUNCION SALIR

def salir():
    respuesta = messagebox.askyesno(
        "Salir",
        "¿Desea salir del programa?"
    )

    if respuesta:
        ventana.destroy()


# VENTANA PRINCIPAL

ventana = tk.Tk()
ventana.title("Calculadora de IMC")
ventana.geometry("500x600")
ventana.config(bg="#0F172A")


# TITULO

titulo = tk.Label(
    ventana,
    text="💪 CALCULADORA DE IMC",
    font=("Segoe UI", 22, "bold"),
    bg="#0F172A",
    fg="#38BDF8"
)
titulo.pack(pady=15)

subtitulo = tk.Label(
    ventana,
    text="Conoce tu Índice de Masa Corporal",
    font=("Segoe UI", 11),
    bg="#0F172A",
    fg="#CBD5E1"
)
subtitulo.pack()

# FRAME PRINCIPAL

frame = tk.Frame(
    ventana,
    bg="white",
    bd=3,
    relief="ridge"
)

frame.pack(
    padx=20,
    pady=20,
    ipadx=30,
    ipady=20
)

# TITULO DEL FORMULARIO

tk.Label(
    frame,
    text="DATOS DEL USUARIO",
    bg="white",
    fg="#2563EB",
    font=("Segoe UI", 15, "bold")
).grid(
    row=0,
    column=0,
    columnspan=2,
    pady=(0, 20)
)

# NOMBRE

tk.Label(
    frame,
    text="👤 Nombre:",
    bg="white",
    fg="#1F2937",
    font=("Segoe UI", 11, "bold")
).grid(
    row=1,
    column=0,
    padx=15,
    pady=12,
    sticky="w"
)

entrada_nombre = tk.Entry(
    frame,
    width=35,
    font=("Segoe UI", 11),
    bd=2,
    relief="solid"
)
entrada_nombre.grid(row=1, column=1, padx=10)

# EDAD

tk.Label(
    frame,
    text="🎂 Edad:",
    bg="white",
    fg="#1F2937",
    font=("Segoe UI", 11, "bold")
).grid(
    row=2,
    column=0,
    padx=15,
    pady=12,
    sticky="w"
)

entrada_edad = tk.Entry(
    frame,
    width=35,
    font=("Segoe UI", 11),
    bd=2,
    relief="solid"
)
entrada_edad.grid(row=2, column=1, padx=10)

# PESO

tk.Label(
    frame,
    text="⚖ Peso (kg):",
    bg="white",
    fg="#1F2937",
    font=("Segoe UI", 11, "bold")
).grid(
    row=3,
    column=0,
    padx=15,
    pady=12,
    sticky="w"
)

entrada_peso = tk.Entry(
    frame,
    width=35,
    font=("Segoe UI", 11),
    bd=2,
    relief="solid"
)
entrada_peso.grid(row=3, column=1, padx=10)

# ALTURA

tk.Label(
    frame,
    text="📏 Altura (m):",
    bg="white",
    fg="#1F2937",
    font=("Segoe UI", 11, "bold")
).grid(
    row=4,
    column=0,
    padx=15,
    pady=12,
    sticky="w"
)

entrada_altura = tk.Entry(
    frame,
    width=35,
    font=("Segoe UI", 11),
    bd=2,
    relief="solid"
)
entrada_altura.grid(row=4, column=1, padx=10)

# BOTONES

frame_botones = tk.Frame(
    ventana,
    bg="#0F172A"
)

frame_botones.pack(pady=15)

btn_calcular = tk.Button(
    frame_botones,
    text="CALCULAR",
    command=calcular,
    bg="#22C55E",
    fg="white",
    activebackground="#16A34A",
    font=("Segoe UI", 11, "bold"),
    width=15,
    cursor="hand2"
)
btn_calcular.pack(side="left", padx=10)

btn_limpiar = tk.Button(
    frame_botones,
    text="LIMPIAR",
    command=limpiar,
    bg="#F59E0B",
    fg="white",
    activebackground="#D97706",
    font=("Segoe UI", 11, "bold"),
    width=15,
    cursor="hand2"
)
btn_limpiar.pack(side="left", padx=10)

btn_salir = tk.Button(
    frame_botones,
    text="SALIR",
    command=salir,
    bg="#EF4444",
    fg="white",
    activebackground="#DC2626",
    font=("Segoe UI", 11, "bold"),
    width=15,
    cursor="hand2"
)
btn_salir.pack(side="left", padx=10)

# RESULTADO

frame_resultado = tk.LabelFrame(
    ventana,
    text="📊 RESULTADO DEL IMC",
    font=("Segoe UI", 12, "bold"),
    bg="#DBEAFE",
    fg="#1E40AF",
    padx=20,
    pady=20
)

frame_resultado.pack(
    padx=20,
    pady=20,
    fill="both"
)

resultado = tk.Label(
    frame_resultado,
    text="Ingrese sus datos y presione CALCULAR",
    bg="#DBEAFE",
    fg="#111827",
    justify="left",
    font=("Consolas", 11, "bold")
)

resultado.pack()

# PIE DE PAGINA

pie = tk.Label(
    ventana,
    text="Proyecto de Programación • Calculadora de IMC",
    bg="#0F172A",
    fg="#94A3B8",
    font=("Segoe UI", 9)
)

pie.pack(side="bottom", pady=10)

ventana.mainloop()