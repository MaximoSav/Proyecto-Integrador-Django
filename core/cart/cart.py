from mercado.models import *


class Cart:

    def __init__(self, request):
        self.request = request
        self.session = request.session
        cart = self.session.get("cart")
        if not cart:
            cart = self.session["cart"] = {}
        self.cart = cart

    def add(self, Producto):
        if str(Producto.id) not in self.cart.keys():
            self.cart[Producto.id] = {
                "product_id": Producto.id,
                "nombre": Producto.nombre,
                "stock": 1,
                "precio": Producto.precio,
                "foto": Producto.foto.url
            }
        else:
            for key, value in self.cart.items():
                if key == str(Producto.id):
                    value["stock"] = value["stock"] + 1
                    break

        self.save()

    def save(self):
        self.session["cart"] = self.cart
        self.session.modified = True

    def remove(self, Producto):
        producto_id = str(Producto.id)
        if producto_id in self.cart:
            del self.cart[producto_id]
            self.save()

    def decrement(self, Producto):
        for key, value in self.cart.items():
            if key == str(Producto.id):
                value["stock"] = value["stock"] - 1
                if value["stock"] < 1:
                    self.remove(Producto)
                else:
                    self.save()
                break
            else:
                print("El producto no esta en el carrito...")

    def clear(self):
        self.session["cart"] = {}
        self.session.modified = True
