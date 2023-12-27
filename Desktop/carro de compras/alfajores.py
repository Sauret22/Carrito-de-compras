import tkinter as tk
from PIL import Image, ImageTk

def on_entry_click(event, entry, placeholder):
    if entry.get() == placeholder:
        entry.delete(0, "end")
        entry.config(fg='white')  # Cambiar color del texto cuando se empieza a escribir

def validar_nombre(cadena):
    return len(cadena) >= 7

def validar_direccion(cadena):
    return len(cadena) >= 10

def validar_numero(cadena):
    return 10 <= len(cadena) <= 10

def iniciar():
    nombre_valor = nombre.get()
    direccion_valor = direccion.get()
    numero_valor = numero.get()

    if not (validar_nombre(nombre_valor) and validar_direccion(direccion_valor) and validar_numero(numero_valor)):
        etiqueta_obligatorio.config(text="¡Campos inválidos!", fg="red")
        return
    else:
        etiqueta_obligatorio.config(text="", fg="red")

    productos_seleccionados = []

    def agregar_al_carrito(producto, precio):
        productos_seleccionados.append((producto, precio))

    nueva_ventana = tk.Toplevel(ventana)
    nueva_ventana.title("Nueva Ventana")
    nueva_ventana.geometry(f"{ancho_pantalla}x{alto_pantalla}+0+0")
    nueva_ventana.configure(bg='#800020')

    mensaje_nueva_ventana = "Christmas '23 con El Coso"
    etiqueta_nueva_ventana = tk.Label(nueva_ventana, text=mensaje_nueva_ventana, font=("Cursive", 36, "italic"), bg='#800020', fg='white')
    etiqueta_nueva_ventana.pack(pady=20)

    producto_1 = tk.Label(nueva_ventana, text="Caja de 10", font=("Cursive", 24, "italic"), bg='#800020', fg='white')
    producto_1.pack(pady=20)

    boton_producto_1 = tk.Button(nueva_ventana, text="Caja de 10 ------------$210", command=lambda: agregar_al_carrito("Caja de 10", 210), font=("Helvetica", 16), bd=0, highlightthickness=0, fg='white')
    boton_producto_1.pack(pady=5)
    boton_producto_1.configure(bg=ventana.cget('bg'), activebackground=ventana.cget('bg'))

    # Producto 2
    producto_2 = tk.Label(nueva_ventana, text="Caja de 20", font=("Cursive", 24, "italic"), bg='#800020', fg='white')
    producto_2.pack(pady=20)

    boton_producto_2 = tk.Button(nueva_ventana, text="Caja de 20 ------------$390", command=lambda: agregar_al_carrito("Caja de 20", 390), font=("Helvetica", 16), bd=0, highlightthickness=0, fg='white')
    boton_producto_2.pack(pady=5)
    boton_producto_2.configure(bg=ventana.cget('bg'), activebackground=ventana.cget('bg'))

    # Producto 3
    producto_3 = tk.Label(nueva_ventana, text="Caja de 16", font=("Cursive", 24, "italic"), bg='#800020', fg='white')
    producto_3.pack(pady=20)

    boton_producto_3 = tk.Button(nueva_ventana, text="Caja de 16 ------------$318", command=lambda: agregar_al_carrito("Caja de 16", 318), font=("Helvetica", 16), bd=0, highlightthickness=0, fg='white')
    boton_producto_3.pack(pady=5)
    boton_producto_3.configure(bg=ventana.cget('bg'), activebackground=ventana.cget('bg'))

    # Producto 4
    producto_4 = tk.Label(nueva_ventana, text="Caja de 24", font=("Cursive", 24, "italic"), bg='#800020', fg='white')
    producto_4.pack(pady=20)

    boton_producto_4 = tk.Button(nueva_ventana, text="Caja de 24 ------------$460", command=lambda: agregar_al_carrito("Caja de 24", 460), font=("Helvetica", 16), bd=0, highlightthickness=0, fg='white')
    boton_producto_4.pack(pady=5)
    boton_producto_4.configure(bg=ventana.cget('bg'), activebackground=ventana.cget('bg'))

    # Producto 5
    producto_5 = tk.Label(nueva_ventana, text="Caja de 18 (plástico)", font=("Cursive", 24, "italic"), bg='#800020', fg='white')
    producto_5.pack(pady=20)

    boton_producto_5 = tk.Button(nueva_ventana, text="Caja de 18 ------------$335", command=lambda: agregar_al_carrito("Caja de 18 (plástico)", 335), font=("Helvetica", 16), bd=0, highlightthickness=0, fg='white')
    boton_producto_5.pack(pady=5)
    boton_producto_5.configure(bg=ventana.cget('bg'), activebackground=ventana.cget('bg'))
    

    numero_telefono1 = tk.Label(nueva_ventana, text="449-111-4281", font=("cursive", 24, "italic"), bg='#800020', fg='white')
    numero_telefono1.pack(pady=40)

    pagina_insta = tk.Label(nueva_ventana, text="@alfajores_elcoso", font=("cursive", 24, "italic"), bg='#800020', fg='white')
    pagina_insta.pack(pady=20)

    ruta_imagen = r'C:\Users\Sango\Desktop\carrito de compras\.vscode\carrito.png'
    original_image = Image.open(ruta_imagen)
    resized_image = original_image.resize((80, 80))  # Corrected attribute name
    carrito_image = ImageTk.PhotoImage(resized_image)

    # Carrito button with resized image
    boton_carrito = tk.Button(nueva_ventana, image=carrito_image,
                              command=lambda: mostrar_carrito(productos_seleccionados), bd=0, highlightthickness=0, bg='#800020')
    boton_carrito.image = carrito_image
    boton_carrito.place(relx=1, rely=0, x=-8, y=10, anchor="ne")



def mostrar_carrito(productos_seleccionados):
    carrito_ventana = tk.Toplevel(ventana)
    carrito_ventana.title("Carrito de Compras")
    carrito_ventana.geometry(f"{ancho_pantalla}x{alto_pantalla}+0+0")
    carrito_ventana.configure(bg='#800020')

    total_pagar = sum(precio for _, precio in productos_seleccionados)

    for producto, precio in productos_seleccionados:
        etiqueta_producto = tk.Label(carrito_ventana, text=f"{producto} - ${precio}", font=("Helvetica", 30), bg='#800020', fg='white')
        etiqueta_producto.pack(pady=5)

    etiqueta_total = tk.Label(carrito_ventana, text=f"Total a pagar: ${total_pagar}", font=("Helvetica", 30), bg='#800020', fg='white')
    etiqueta_total.pack(pady=20)


ventana = tk.Tk()
ventana.title("El Coso")
ventana.configure(bg='#800020')

ancho_pantalla = ventana.winfo_screenwidth()
alto_pantalla = ventana.winfo_screenheight()
ventana.geometry(f"{ancho_pantalla}x{alto_pantalla}+0+0")

# Título en la parte superior
alfajores =tk.Label(ventana, text="Alfajores", font=("Cursive", 50, "italic"), bg='#800020', fg='white')
alfajores.pack(side=tk.TOP, pady=40)

coso = tk.Label(ventana, text="EL COSO", font=("Cursive", 70, "italic"), bg='#800020', fg='white')
coso.pack(side=tk.TOP, pady=50)



# Contenedor principal centrado
contenedor_central = tk.Frame(ventana, bg='#800020')
contenedor_central.pack(expand=True)

# Etiqueta "obligatorio*"
etiqueta_obligatorio = tk.Label(contenedor_central, text="", font=("Helvetica", 12), fg="red", bg='#800020')
etiqueta_obligatorio.pack(pady=5)

# Entry para el nombre con tamaño personalizado
nombre = tk.Entry(contenedor_central, font=("Helvetica", 16), bd=1, relief="solid", fg='white', bg='#800020')
nombre.insert(0, "Nombre y Apellido")
nombre.bind('<FocusIn>', lambda event: on_entry_click(event, nombre, "Nombre y Apellido"))
nombre.pack(pady=5, padx=20, fill=tk.X)

# Entry para la dirección con tamaño personalizado
direccion = tk.Entry(contenedor_central, font=("Helvetica", 16), bd=1, relief="solid", fg='white', bg='#800020')
direccion.insert(0, "Dirección")  # Texto predeterminado
direccion.bind('<FocusIn>', lambda event: on_entry_click(event, direccion, "Dirección"))
direccion.pack(pady=5, padx=20, fill=tk.X)

# Entry para el número con tamaño personalizado
numero = tk.Entry(contenedor_central, font=("Helvetica", 16), bd=1, relief="solid", fg='white', bg='#800020')
numero.insert(0, "Número")  # Texto predeterminado
numero.bind('<FocusIn>', lambda event: on_entry_click(event, numero, "Número"))
numero.pack(pady=5, padx=20, fill=tk.X)

# Botón en la parte inferior
boton_iniciar = tk.Button(ventana, text="Iniciar", command=iniciar, font=("Helvetica", 18), bd=0, highlightthickness=0, fg='white')
boton_iniciar.pack(side=tk.BOTTOM, pady=70)
boton_iniciar.configure(bg=ventana.cget('bg'))

ventana.mainloop()