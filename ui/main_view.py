import tkinter as tk
from tkinter import ttk, messagebox


class MainView:

    def __init__(self, root, servicio, cerrar_sesion):
        self.root = root
        self.servicio = servicio
        self.cerrar_sesion = cerrar_sesion

        self.frame = tk.Frame(root, padx=15, pady=15)
        self.frame.pack(fill="both", expand=True)

        titulo = tk.Label(
            self.frame,
            text="RESTAURANTE APP",
            font=("Arial", 20, "bold")
        )
        titulo.pack(pady=(0, 15))

        cuerpo = tk.Frame(self.frame)
        cuerpo.pack(fill="both", expand=True)

        # ==============================
        # MENÚ LATERAL
        # ==============================

        self.menu = tk.LabelFrame(
            cuerpo,
            text="Navegación",
            padx=10,
            pady=10
        )
        self.menu.pack(
            side="left",
            fill="y",
            padx=(0, 15)
        )

        tk.Button(
            self.menu,
            text="Inicio",
            width=18,
            command=self.mostrar_inicio
        ).pack(pady=5)

        tk.Button(
            self.menu,
            text="Usuarios",
            width=18,
            command=self.mostrar_usuarios
        ).pack(pady=5)

        tk.Button(
            self.menu,
            text="Productos",
            width=18,
            command=self.mostrar_productos
        ).pack(pady=5)

        tk.Button(
            self.menu,
            text="Ventas",
            width=18,
            command=self.mostrar_ventas
        ).pack(pady=5)

        tk.Button(
            self.menu,
            text="Cerrar sesión",
            width=18,
            command=self.salir
        ).pack(pady=(25, 5))

        # ==============================
        # ÁREA DE CONTENIDO
        # ==============================

        self.contenido = tk.Frame(cuerpo)
        self.contenido.pack(
            side="left",
            fill="both",
            expand=True
        )

        self.mostrar_inicio()

    # ==============================
    # LIMPIAR CONTENIDO
    # ==============================

    def limpiar_contenido(self):
        for widget in self.contenido.winfo_children():
            widget.destroy()

    # ==============================
    # INICIO
    # ==============================

    def mostrar_inicio(self):
        self.limpiar_contenido()

        titulo = tk.Label(
            self.contenido,
            text="Menú principal",
            font=("Arial", 16, "bold")
        )
        titulo.pack(pady=20)

        texto = tk.Label(
            self.contenido,
            text=(
                "Bienvenido a Restaurante App.\n\n"
                "Seleccione una opción del menú\n"
                "para consultar o administrar la información."
            ),
            font=("Arial", 12)
        )
        texto.pack(pady=20)

    # ==============================
    # USUARIOS
    # ==============================

    def mostrar_usuarios(self):
        self.limpiar_contenido()

        titulo = tk.Label(
            self.contenido,
            text="Consulta de usuarios",
            font=("Arial", 16, "bold")
        )
        titulo.pack(pady=(0, 10))

        tabla_frame = tk.Frame(self.contenido)
        tabla_frame.pack(
            fill="both",
            expand=True
        )

        columnas = (
            "identificador",
            "nombre",
            "usuario"
        )

        tabla = ttk.Treeview(
            tabla_frame,
            columns=columnas,
            show="headings"
        )

        tabla.heading(
            "identificador",
            text="Identificador"
        )

        tabla.heading(
            "nombre",
            text="Nombre"
        )

        tabla.heading(
            "usuario",
            text="Usuario"
        )

        tabla.column(
            "identificador",
            width=100
        )

        tabla.column(
            "nombre",
            width=180
        )

        tabla.column(
            "usuario",
            width=150
        )

        scrollbar = ttk.Scrollbar(
            tabla_frame,
            orient="vertical",
            command=tabla.yview
        )

        tabla.configure(
            yscrollcommand=scrollbar.set
        )

        tabla.pack(
            side="left",
            fill="both",
            expand=True
        )

        scrollbar.pack(
            side="right",
            fill="y"
        )

        usuarios = self.servicio.listar_usuarios()

        for usuario in usuarios:
            tabla.insert(
                "",
                tk.END,
                values=(
                    usuario.identificador,
                    usuario.nombre,
                    usuario.usuario
                )
            )

    # ==============================
    # PRODUCTOS
    # ==============================

    def mostrar_productos(self):
        self.limpiar_contenido()

        titulo = tk.Label(
            self.contenido,
            text="Gestión de productos",
            font=("Arial", 16, "bold")
        )
        titulo.pack(pady=(0, 10))

        formulario = tk.LabelFrame(
            self.contenido,
            text="Datos del producto",
            padx=10,
            pady=10
        )
        formulario.pack(
            fill="x",
            pady=(0, 10)
        )

        # Código
        tk.Label(
            formulario,
            text="Código:"
        ).grid(
            row=0,
            column=0,
            padx=5,
            pady=5
        )

        self.entrada_codigo = tk.Entry(
            formulario,
            width=20
        )
        self.entrada_codigo.grid(
            row=0,
            column=1,
            padx=5,
            pady=5
        )

        # Nombre
        tk.Label(
            formulario,
            text="Nombre:"
        ).grid(
            row=0,
            column=2,
            padx=5,
            pady=5
        )

        self.entrada_nombre = tk.Entry(
            formulario,
            width=20
        )
        self.entrada_nombre.grid(
            row=0,
            column=3,
            padx=5,
            pady=5
        )

        # Categoría
        tk.Label(
            formulario,
            text="Categoría:"
        ).grid(
            row=1,
            column=0,
            padx=5,
            pady=5
        )

        self.entrada_categoria = tk.Entry(
            formulario,
            width=20
        )
        self.entrada_categoria.grid(
            row=1,
            column=1,
            padx=5,
            pady=5
        )

        # Precio
        tk.Label(
            formulario,
            text="Precio:"
        ).grid(
            row=1,
            column=2,
            padx=5,
            pady=5
        )

        self.entrada_precio = tk.Entry(
            formulario,
            width=20
        )
        self.entrada_precio.grid(
            row=1,
            column=3,
            padx=5,
            pady=5
        )

        # Stock
        tk.Label(
            formulario,
            text="Stock:"
        ).grid(
            row=2,
            column=0,
            padx=5,
            pady=5
        )

        self.entrada_stock = tk.Entry(
            formulario,
            width=20
        )
        self.entrada_stock.grid(
            row=2,
            column=1,
            padx=5,
            pady=5
        )

        # ==============================
        # BOTONES
        # ==============================

        botones = tk.Frame(self.contenido)
        botones.pack(pady=5)

        tk.Button(
            botones,
            text="Registrar",
            width=12,
            command=self.registrar_producto
        ).grid(
            row=0,
            column=0,
            padx=3
        )

        tk.Button(
            botones,
            text="Cargar",
            width=12,
            command=self.cargar_producto
        ).grid(
            row=0,
            column=1,
            padx=3
        )

        tk.Button(
            botones,
            text="Actualizar",
            width=12,
            command=self.actualizar_producto
        ).grid(
            row=0,
            column=2,
            padx=3
        )

        tk.Button(
            botones,
            text="Eliminar",
            width=12,
            command=self.eliminar_producto
        ).grid(
            row=0,
            column=3,
            padx=3
        )

        tk.Button(
            botones,
            text="Limpiar",
            width=12,
            command=self.limpiar_formulario
        ).grid(
            row=0,
            column=4,
            padx=3
        )

        # ==============================
        # TABLA DE PRODUCTOS
        # ==============================

        tabla_frame = tk.LabelFrame(
            self.contenido,
            text="Productos registrados",
            padx=5,
            pady=5
        )
        tabla_frame.pack(
            fill="both",
            expand=True,
            pady=(10, 0)
        )

        columnas = (
            "codigo",
            "nombre",
            "categoria",
            "precio",
            "stock"
        )

        self.tabla_productos = ttk.Treeview(
            tabla_frame,
            columns=columnas,
            show="headings"
        )

        for columna, texto in [
            ("codigo", "Código"),
            ("nombre", "Nombre"),
            ("categoria", "Categoría"),
            ("precio", "Precio"),
            ("stock", "Stock")
        ]:
            self.tabla_productos.heading(
                columna,
                text=texto
            )

        self.tabla_productos.column(
            "codigo",
            width=80
        )

        self.tabla_productos.column(
            "nombre",
            width=150
        )

        self.tabla_productos.column(
            "categoria",
            width=120
        )

        self.tabla_productos.column(
            "precio",
            width=80
        )

        self.tabla_productos.column(
            "stock",
            width=80
        )

        scrollbar = ttk.Scrollbar(
            tabla_frame,
            orient="vertical",
            command=self.tabla_productos.yview
        )

        self.tabla_productos.configure(
            yscrollcommand=scrollbar.set
        )

        self.tabla_productos.pack(
            side="left",
            fill="both",
            expand=True
        )

        scrollbar.pack(
            side="right",
            fill="y"
        )

        self.actualizar_tabla_productos()

    # ==============================
    # ACTUALIZAR TABLA PRODUCTOS
    # ==============================

    def actualizar_tabla_productos(self):
        for item in self.tabla_productos.get_children():
            self.tabla_productos.delete(item)

        productos = self.servicio.listar_productos()

        for producto in productos:
            self.tabla_productos.insert(
                "",
                tk.END,
                values=(
                    producto.codigo,
                    producto.nombre,
                    producto.categoria,
                    f"{producto.precio:.2f}",
                    producto.stock
                )
            )

    # ==============================
    # REGISTRAR PRODUCTO
    # ==============================

    def registrar_producto(self):
        try:
            codigo = self.entrada_codigo.get().strip()
            nombre = self.entrada_nombre.get().strip()
            categoria = self.entrada_categoria.get().strip()
            precio = float(self.entrada_precio.get())
            stock = int(self.entrada_stock.get())

            if not codigo or not nombre or not categoria:
                messagebox.showwarning(
                    "Datos incompletos",
                    "Complete todos los campos."
                )
                return

            if self.servicio.registrar_producto(
                codigo,
                nombre,
                categoria,
                precio,
                stock
            ):
                messagebox.showinfo(
                    "Registro",
                    "Producto registrado correctamente."
                )

                self.limpiar_formulario()
                self.actualizar_tabla_productos()

            else:
                messagebox.showwarning(
                    "Producto existente",
                    "Ya existe un producto con ese código."
                )

        except ValueError:
            messagebox.showerror(
                "Error",
                "Precio y stock deben contener valores válidos."
            )

    # ==============================
    # CARGAR PRODUCTO
    # ==============================

    def cargar_producto(self):
        codigo = self.entrada_codigo.get().strip()

        if not codigo:
            messagebox.showwarning(
                "Código requerido",
                "Ingrese el código del producto."
            )
            return

        producto = self.servicio.buscar_producto(codigo)

        if producto is None:
            messagebox.showwarning(
                "No encontrado",
                "No existe un producto con ese código."
            )
            return

        self.entrada_nombre.delete(0, tk.END)
        self.entrada_nombre.insert(
            0,
            producto.nombre
        )

        self.entrada_categoria.delete(0, tk.END)
        self.entrada_categoria.insert(
            0,
            producto.categoria
        )

        self.entrada_precio.delete(0, tk.END)
        self.entrada_precio.insert(
            0,
            producto.precio
        )

        self.entrada_stock.delete(0, tk.END)
        self.entrada_stock.insert(
            0,
            producto.stock
        )

    # ==============================
    # ACTUALIZAR PRODUCTO
    # ==============================

    def actualizar_producto(self):
        try:
            codigo = self.entrada_codigo.get().strip()
            nombre = self.entrada_nombre.get().strip()
            categoria = self.entrada_categoria.get().strip()
            precio = float(self.entrada_precio.get())
            stock = int(self.entrada_stock.get())

            if self.servicio.actualizar_producto(
                codigo,
                nombre,
                categoria,
                precio,
                stock
            ):
                messagebox.showinfo(
                    "Actualización",
                    "Producto actualizado correctamente."
                )

                self.limpiar_formulario()
                self.actualizar_tabla_productos()

            else:
                messagebox.showwarning(
                    "No encontrado",
                    "No existe un producto con ese código."
                )

        except ValueError:
            messagebox.showerror(
                "Error",
                "Precio y stock deben contener valores válidos."
            )

    # ==============================
    # ELIMINAR PRODUCTO
    # ==============================

    def eliminar_producto(self):
        codigo = self.entrada_codigo.get().strip()

        if not codigo:
            messagebox.showwarning(
                "Código requerido",
                "Ingrese el código del producto."
            )
            return

        producto = self.servicio.buscar_producto(codigo)

        if producto is None:
            messagebox.showwarning(
                "No encontrado",
                "No existe un producto con ese código."
            )
            return

        confirmar = messagebox.askyesno(
            "Confirmar eliminación",
            f"¿Desea eliminar el producto {producto.nombre}?"
        )

        if not confirmar:
            return

        if self.servicio.eliminar_producto(codigo):
            messagebox.showinfo(
                "Eliminación",
                "Producto eliminado correctamente."
            )

            self.limpiar_formulario()
            self.actualizar_tabla_productos()

    # ==============================
    # LIMPIAR FORMULARIO
    # ==============================

    def limpiar_formulario(self):
        self.entrada_codigo.delete(0, tk.END)
        self.entrada_nombre.delete(0, tk.END)
        self.entrada_categoria.delete(0, tk.END)
        self.entrada_precio.delete(0, tk.END)
        self.entrada_stock.delete(0, tk.END)

    # ==============================
    # VENTAS - SEMANA 15
    # ==============================

    def mostrar_ventas(self):
        self.limpiar_contenido()

        titulo = tk.Label(
            self.contenido,
            text="Gestión de ventas",
            font=("Arial", 16, "bold")
        )
        titulo.pack(pady=(0, 10))

        formulario = tk.LabelFrame(
            self.contenido,
            text="Registrar nueva venta",
            padx=10,
            pady=10
        )
        formulario.pack(
            fill="x",
            pady=(0, 10)
        )

        # ==============================
        # USUARIO
        # ==============================

        tk.Label(
            formulario,
            text="Usuario:"
        ).grid(
            row=0,
            column=0,
            padx=5,
            pady=5
        )

        usuarios = [
            f"{usuario.usuario} - {usuario.nombre}"
            for usuario in self.servicio.listar_usuarios()
        ]

        self.combo_usuarios_venta = ttk.Combobox(
            formulario,
            values=usuarios,
            state="readonly",
            width=30
        )

        self.combo_usuarios_venta.grid(
            row=0,
            column=1,
            padx=5,
            pady=5
        )

        # ==============================
        # PRODUCTO
        # ==============================

        tk.Label(
            formulario,
            text="Producto:"
        ).grid(
            row=1,
            column=0,
            padx=5,
            pady=5
        )

        productos = [
            f"{producto.codigo} - {producto.nombre}"
            for producto in self.servicio.listar_productos()
        ]

        self.combo_productos_venta = ttk.Combobox(
            formulario,
            values=productos,
            state="readonly",
            width=30
        )

        self.combo_productos_venta.grid(
            row=1,
            column=1,
            padx=5,
            pady=5
        )

        # ==============================
        # BOTÓN REGISTRAR VENTA
        # ==============================

        tk.Button(
            formulario,
            text="Registrar venta",
            width=20,
            command=self.registrar_venta
        ).grid(
            row=2,
            column=0,
            columnspan=2,
            pady=10
        )

        # ==============================
        # HISTORIAL DE VENTAS
        # ==============================

        tabla_frame = tk.LabelFrame(
            self.contenido,
            text="Historial de ventas",
            padx=5,
            pady=5
        )

        tabla_frame.pack(
            fill="both",
            expand=True
        )

        columnas = (
            "usuario",
            "producto",
            "fecha"
        )

        self.tabla_ventas = ttk.Treeview(
            tabla_frame,
            columns=columnas,
            show="headings"
        )

        self.tabla_ventas.heading(
            "usuario",
            text="Usuario"
        )

        self.tabla_ventas.heading(
            "producto",
            text="Producto"
        )

        self.tabla_ventas.heading(
            "fecha",
            text="Fecha / Hora"
        )

        self.tabla_ventas.column(
            "usuario",
            width=150
        )

        self.tabla_ventas.column(
            "producto",
            width=180
        )

        self.tabla_ventas.column(
            "fecha",
            width=180
        )

        scrollbar = ttk.Scrollbar(
            tabla_frame,
            orient="vertical",
            command=self.tabla_ventas.yview
        )

        self.tabla_ventas.configure(
            yscrollcommand=scrollbar.set
        )

        self.tabla_ventas.pack(
            side="left",
            fill="both",
            expand=True
        )

        scrollbar.pack(
            side="right",
            fill="y"
        )

        self.refrescar_ventas()

    # ==============================
    # REGISTRAR VENTA
    # ==============================

    def registrar_venta(self):

        usuario_seleccionado = (
            self.combo_usuarios_venta.get().strip()
        )

        producto_seleccionado = (
            self.combo_productos_venta.get().strip()
        )

        if not usuario_seleccionado:
            messagebox.showwarning(
                "Ventas",
                "Seleccione un usuario."
            )
            return

        if not producto_seleccionado:
            messagebox.showwarning(
                "Ventas",
                "Seleccione un producto."
            )
            return

        usuario = (
            usuario_seleccionado
            .split(" - ")[0]
            .strip()
        )

        codigo_producto = (
            producto_seleccionado
            .split(" - ")[0]
            .strip()
        )

        exito, mensaje = self.servicio.registrar_venta(
            usuario,
            codigo_producto
        )

        if not exito:
            messagebox.showerror(
                "Ventas",
                mensaje
            )
            return

        messagebox.showinfo(
            "Ventas",
            mensaje
        )

        self.combo_usuarios_venta.set("")
        self.combo_productos_venta.set("")

        self.refrescar_ventas()

    # ==============================
    # ACTUALIZAR TABLA DE VENTAS
    # ==============================

    def refrescar_ventas(self):

        for item in self.tabla_ventas.get_children():
            self.tabla_ventas.delete(item)

        ventas = self.servicio.listar_ventas()

        for venta in ventas:
            self.tabla_ventas.insert(
                "",
                tk.END,
                values=(
                    venta.usuario,
                    venta.codigo_producto,
                    venta.fecha
                )
            )

    # ==============================
    # CERRAR SESIÓN
    # ==============================

    def salir(self):
        confirmar = messagebox.askyesno(
            "Cerrar sesión",
            "¿Desea cerrar la sesión?"
        )

        if confirmar:
            self.frame.destroy()
            self.cerrar_sesion()