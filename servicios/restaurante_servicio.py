from modelos.producto import Producto
from modelos.usuario import Usuario
from modelos.venta import Venta

from servicios.archivo_servicio import (
    cargar_productos,
    cargar_usuarios,
    cargar_ventas,
    guardar_productos,
    guardar_usuarios,
    guardar_ventas
)


class RestauranteServicio:

    def __init__(self):
        self.productos: list[Producto] = cargar_productos()
        self.usuarios: list[Usuario] = cargar_usuarios()
        self.ventas: list[Venta] = cargar_ventas()

    # ==========================================
    # ACCESO
    # ==========================================

    def buscar_usuario(
        self,
        usuario_ingresado: str
    ) -> Usuario | None:

        for usuario in self.usuarios:
            if usuario.usuario == usuario_ingresado.strip():
                return usuario

        return None

    def validar_acceso(
        self,
        usuario_ingresado: str,
        contrasena: str
    ) -> Usuario | None:

        usuario = self.buscar_usuario(usuario_ingresado)

        if usuario is None:
            return None

        if usuario.contrasena == contrasena.strip():
            return usuario

        return None

    # ==========================================
    # USUARIOS
    # ==========================================

    def listar_usuarios(self) -> list[Usuario]:
        return self.usuarios

    # ==========================================
    # PRODUCTOS
    # ==========================================

    def listar_productos(self) -> list[Producto]:
        return self.productos

    def buscar_producto(
        self,
        codigo: str
    ) -> Producto | None:

        codigo = codigo.strip()

        if not codigo:
            return None

        for producto in self.productos:
            if producto.codigo == codigo:
                return producto

        return None

    def registrar_producto(
        self,
        codigo: str,
        nombre: str,
        categoria: str,
        precio: float,
        stock: int
    ) -> bool:

        if self.buscar_producto(codigo) is not None:
            return False

        producto = Producto(
            codigo,
            nombre,
            categoria,
            precio,
            stock
        )

        self.productos.append(producto)

        return guardar_productos(self.productos)

    def actualizar_producto(
        self,
        codigo: str,
        nombre: str,
        categoria: str,
        precio: float,
        stock: int
    ) -> bool:

        producto = self.buscar_producto(codigo)

        if producto is None:
            return False

        producto.nombre = nombre.strip()
        producto.categoria = categoria.strip()
        producto.precio = precio
        producto.stock = stock

        return guardar_productos(self.productos)

    def eliminar_producto(
        self,
        codigo: str
    ) -> bool:

        producto = self.buscar_producto(codigo)

        if producto is None:
            return False

        self.productos.remove(producto)

        return guardar_productos(self.productos)

    def consultar_cantidades(
        self
    ) -> list[tuple[str, int]]:

        cantidades = []

        for producto in self.productos:
            cantidades.append(
                (producto.nombre, producto.stock)
            )

        return cantidades

    # ==========================================
    # VENTAS
    # ==========================================

    def listar_ventas(self) -> list[Venta]:
        return self.ventas

    def registrar_venta(
        self,
        usuario: str,
        codigo_producto: str
    ) -> tuple[bool, str]:

        # ------------------------------
        # Validar usuario
        # ------------------------------

        usuario_encontrado = self.buscar_usuario(usuario)

        if usuario_encontrado is None:
            return False, "El usuario seleccionado no existe."

        # ------------------------------
        # Validar producto
        # ------------------------------

        producto = self.buscar_producto(codigo_producto)

        if producto is None:
            return False, "El producto seleccionado no existe."

        # ------------------------------
        # Crear venta
        # ------------------------------

        try:
            venta = Venta(
                usuario_encontrado.usuario,
                producto.codigo
            )

            self.ventas.append(venta)

        except (TypeError, ValueError) as e:
            return False, str(e)

        # ------------------------------
        # Guardar venta
        # ------------------------------

        if not guardar_ventas(self.ventas):
            self.ventas.pop()
            return False, "No se pudo guardar la venta."

        return True, "Venta registrada correctamente."