class Producto:

    def __init__(
        self,
        codigo,
        nombre,
        categoria,
        precio,
        stock
    ):
        self.codigo = codigo
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
        self.stock = stock

    # ==============================
    # VALIDACIÓN DE TEXTO
    # ==============================

    @staticmethod
    def validar_texto(valor, campo):

        if not valor or not valor.strip():
            raise ValueError(
                f"El campo {campo} no puede estar vacío."
            )

        return valor.strip()

    # ==============================
    # CÓDIGO
    # ==============================

    @property
    def codigo(self):
        return self._codigo

    @codigo.setter
    def codigo(self, valor):
        self._codigo = self.validar_texto(
            valor,
            "código"
        )

    # ==============================
    # NOMBRE
    # ==============================

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        self._nombre = self.validar_texto(
            valor,
            "nombre"
        )

    # ==============================
    # CATEGORÍA
    # ==============================

    @property
    def categoria(self):
        return self._categoria

    @categoria.setter
    def categoria(self, valor):
        self._categoria = self.validar_texto(
            valor,
            "categoría"
        )

    # ==============================
    # PRECIO
    # ==============================

    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, valor):

        valor_float = float(valor)

        if valor_float < 0:
            raise ValueError(
                "El precio no puede ser negativo."
            )

        self._precio = valor_float

    # ==============================
    # STOCK
    # ==============================

    @property
    def stock(self):
        return self._stock

    @stock.setter
    def stock(self, valor):

        valor_int = int(valor)

        if valor_int < 0:
            raise ValueError(
                "El stock no puede ser negativo."
            )

        self._stock = valor_int

    # ==============================
    # REPRESENTACIÓN
    # ==============================

    def __str__(self):
        return (
            f"[{self.codigo}] "
            f"{self.nombre} - "
            f"${self.precio:.2f}"
        )

    # ==============================
    # CONVERTIR A DICCIONARIO
    # ==============================

    def to_dict(self):

        return {
            "codigo": self.codigo,
            "nombre": self.nombre,
            "categoria": self.categoria,
            "precio": self.precio,
            "stock": self.stock
        }

    # ==============================
    # CREAR DESDE DICCIONARIO
    # ==============================

    @staticmethod
    def from_dict(data):

        return Producto(
            data.get("codigo", ""),
            data.get("nombre", ""),
            data.get("categoria", "General"),
            float(data.get("precio", 0)),
            int(data.get("stock", 0))
        )