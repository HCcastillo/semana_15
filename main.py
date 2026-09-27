import tkinter as tk

from servicios.restaurante_servicio import RestauranteServicio
from ui.login_view import LoginView
from ui.main_view import MainView


def iniciar_aplicacion():

    print("1. Iniciando aplicación...")

    root = tk.Tk()

    print("2. Ventana creada")

    root.title("Restaurante App")
    root.geometry("1000x650")

    servicio = RestauranteServicio()

    print("3. Servicio creado")

    def mostrar_login():

        print("4. Mostrando login")

        for widget in root.winfo_children():
            widget.destroy()

        login = LoginView(
            root,
            servicio,
            mostrar_menu
        )

        login.pack(
            fill="both",
            expand=True
        )

        print("5. Login creado")

    def mostrar_menu(usuario):

        print("6. Mostrando menú principal")

        for widget in root.winfo_children():
            widget.destroy()

        vista_principal = MainView(
            root,
            servicio,
            mostrar_login
        )

        vista_principal.frame.pack(
            fill="both",
            expand=True
        )

    mostrar_login()

    print("7. Antes de mainloop")

    root.mainloop()

    print("8. Mainloop terminó")


if __name__ == "__main__":
    iniciar_aplicacion()