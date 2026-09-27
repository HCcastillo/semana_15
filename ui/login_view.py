import tkinter as tk
from pathlib import Path
from tkinter import ttk


class LoginView(tk.Frame):

    def __init__(self, master, restaurante_servicio, al_iniciar_sesion):
        super().__init__(master, bg="#eef3f8")

        self.restaurante_servicio = restaurante_servicio
        self.al_iniciar_sesion = al_iniciar_sesion

        self.usuario_entry = None
        self.contrasena_entry = None
        self.mensaje_error = None
        self.logo = None

        self.definir_estilos()
        self.construir_interfaz()

    # ==============================
    # ESTILOS
    # ==============================

    def definir_estilos(self):
        estilo = ttk.Style()

        estilo.theme_use("clam")

        estilo.configure(
            "Login.TButton",
            background="#2563eb",
            foreground="#ffffff",
            font=("Arial", 11, "bold"),
            padding=(14, 8),
            borderwidth=0
        )

        estilo.map(
            "Login.TButton",
            background=[
                ("active", "#1d4ed8")
            ]
        )

    # ==============================
    # CARGAR LOGO
    # ==============================

    def cargar_logo(self):

        ruta_base = Path(__file__).resolve().parent.parent

        ruta_logo = (
            ruta_base
            / "assets"
            / "icons"
            / "logo.png"
        )

        if not ruta_logo.exists():
            return None

        try:
            logo_original = tk.PhotoImage(
                file=str(ruta_logo)
            )

            self.logo = logo_original.subsample(
                7,
                7
            )

            return self.logo

        except Exception:
            return None

    # ==============================
    # CONSTRUIR INTERFAZ
    # ==============================

    def construir_interfaz(self):

        contenedor = tk.Frame(
            self,
            bg="#ffffff",
            padx=32,
            pady=28
        )

        contenedor.place(
            relx=0.5,
            rely=0.5,
            anchor="center"
        )

        # ==============================
        # LOGO
        # ==============================

        logo = self.cargar_logo()

        if logo is not None:

            tk.Label(
                contenedor,
                image=logo,
                bg="#ffffff"
            ).pack(
                pady=(0, 12)
            )

        # ==============================
        # TÍTULO
        # ==============================

        titulo = tk.Label(
            contenedor,
            text="Restaurante",
            bg="#ffffff",
            fg="#1f2a44",
            font=("Arial", 22, "bold")
        )

        titulo.pack(
            pady=(0, 6)
        )

        subtitulo = tk.Label(
            contenedor,
            text="Inicio de sesión",
            bg="#ffffff",
            fg="#516173",
            font=("Arial", 11)
        )

        subtitulo.pack(
            pady=(0, 22)
        )

        # ==============================
        # USUARIO
        # ==============================

        tk.Label(
            contenedor,
            text="Usuario",
            bg="#ffffff",
            fg="#243447",
            font=("Arial", 10, "bold")
        ).pack(
            anchor="w"
        )

        self.usuario_entry = tk.Entry(
            contenedor,
            width=30,
            font=("Arial", 11)
        )

        self.usuario_entry.pack(
            pady=(4, 14),
            ipady=4
        )

        self.usuario_entry.focus()

        # ==============================
        # CONTRASEÑA
        # ==============================

        tk.Label(
            contenedor,
            text="Contraseña",
            bg="#ffffff",
            fg="#243447",
            font=("Arial", 10, "bold")
        ).pack(
            anchor="w"
        )

        self.contrasena_entry = tk.Entry(
            contenedor,
            width=30,
            font=("Arial", 11),
            show="*"
        )

        self.contrasena_entry.pack(
            pady=(4, 14),
            ipady=4
        )

        # ==============================
        # MENSAJE DE ERROR
        # ==============================

        self.mensaje_error = tk.Label(
            contenedor,
            text="",
            bg="#ffffff",
            fg="#b42318",
            font=("Arial", 10)
        )

        self.mensaje_error.pack(
            pady=(0, 14)
        )

        # ==============================
        # BOTÓN
        # ==============================

        boton = ttk.Button(
            contenedor,
            text="Iniciar sesión",
            command=self.iniciar_sesion,
            style="Login.TButton"
        )

        boton.pack(
            fill="x"
        )

        # ==============================
        # ENTER PARA INICIAR SESIÓN
        # ==============================

        self.usuario_entry.bind(
            "<Return>",
            lambda event: self.iniciar_sesion()
        )

        self.contrasena_entry.bind(
            "<Return>",
            lambda event: self.iniciar_sesion()
        )

    # ==============================
    # INICIAR SESIÓN
    # ==============================

    def iniciar_sesion(self):

        if (
            self.usuario_entry is None
            or self.contrasena_entry is None
            or self.mensaje_error is None
        ):
            return

        usuario = self.usuario_entry.get().strip()

        contrasena = (
            self.contrasena_entry
            .get()
            .strip()
        )

        # ==============================
        # VALIDAR CAMPOS VACÍOS
        # ==============================

        if not usuario or not contrasena:

            self.mensaje_error.config(
                text="Ingrese usuario y contraseña."
            )

            return

        # ==============================
        # VALIDAR CON EL SERVICIO
        # ==============================

        usuario_validado = (
            self.restaurante_servicio.validar_acceso(
                usuario,
                contrasena
            )
        )

        # ==============================
        # CREDENCIALES INCORRECTAS
        # ==============================

        if usuario_validado is None:

            self.mensaje_error.config(
                text="Credenciales incorrectas."
            )

            self.contrasena_entry.delete(
                0,
                tk.END
            )

            return

        # ==============================
        # ACCESO CORRECTO
        # ==============================

        self.mensaje_error.config(
            text=""
        )

        self.al_iniciar_sesion(
            usuario_validado
        )