import tkinter as tk


def iniciar():
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

    boton_carrito = tk.Button(nueva_ventana, text="Carrito", command=lambda: mostrar_carrito(productos_seleccionados), font=("Helvetica", 14), bd=0, highlightthickness=0, fg='white')
    boton_carrito.pack(side=tk.RIGHT, padx=20, pady=10)
    boton_carrito.configure(bg=ventana.cget('bg'), activebackground=ventana.cget('bg'))


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

titulo = tk.Label(ventana, text="EL COSO", font=("Cursive", 48, "italic"), bg='#800020', fg='white')
titulo.place(relx=0.5, rely=0.5, anchor="center")

boton_iniciar = tk.Button(ventana, text="Iniciar", command=iniciar, font=("Helvetica", 18), bd=0, highlightthickness=0, fg='white')
boton_iniciar.place(relx=0.5, rely=0.9, anchor="center")
boton_iniciar.configure(bg=ventana.cget('bg'))

ventana.mainloop()