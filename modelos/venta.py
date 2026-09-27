from datetime import datetime


class Venta:

    def __init__(
        self,
        usuario: str,
        codigo_producto: str,
        fecha: str | None = None
    ):
        if not usuario.strip():
            raise ValueError(
                "El usuario no puede estar vacío."
            )

        if not codigo_producto.strip():
            raise ValueError(
                "El código del producto no puede estar vacío."
            )

        self.usuario = usuario.strip()
        self.codigo_producto = codigo_producto.strip()

        if fecha is None or not fecha.strip():
            self.fecha = datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            )
        else:
            self.fecha = fecha.strip()

    def to_dict(self) -> dict:
        return {
            "usuario": self.usuario,
            "codigo_producto": self.codigo_producto,
            "fecha": self.fecha
        }

    @classmethod
    def from_dict(cls, datos: dict) -> "Venta":
        try:
            return cls(
                str(datos["usuario"]),
                str(datos["codigo_producto"]),
                str(datos["fecha"])
            )

        except KeyError as e:
            raise KeyError(
                f"Falta la clave requerida: {e}"
            )

        except (TypeError, ValueError) as e:
            raise ValueError(
                f"Datos de venta inválidos: {e}"
            )