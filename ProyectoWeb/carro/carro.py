class Carro:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carro = self.session.get("carro")
        if not carro:
            carro = self.session["carro"] = {}
        self.carro = carro

    def agregar(self, producto):
        if str(producto.id) not in self.carro.keys():
            self.carro[producto.id] = {
                "producto_id": producto.id,
                "nombre": producto.nombre,
                "precio": producto.precio,
                "cantidad": 1,
                "imagen": producto.imagen.url,
            }
        else:
            self.carro[str(producto.id)]["cantidad"] += 1
        self.guardar_carro()

    def guardar_carro(self):
        self.session["carro"] = self.carro
        self.session.modified = True

    def eliminar_producto(self, producto):
        producto.id = str(producto.id)
        if producto.id in self.carro:
            del self.carro[producto.id]
            self.guardar_carro()

    def restar_producto(self, producto):
        if self.carro[str(producto.id)]["cantidad"] > 1:
            self.carro[str(producto.id)]["cantidad"] -= 1
        else:
            self.eliminar_producto(producto)
        self.guardar_carro()

    def limpiar_carro(self, producto):
        self.session["carro"] = {}
        self.session.modified = True
