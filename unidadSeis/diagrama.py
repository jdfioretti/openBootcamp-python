
class Categorias:
    idCategoria = 0
    nombreCategoria = None


class Proveedores:
    Direccion = None
    telefono = 0
    codPostal = 0
    NombreProveedor = None


class Productos:
    idProducto = 0
    categoriaProducto = Categorias()
    Precio = 0
    Tamaño = 0
    Peso = 0
    tipoProducto = None
    CIFproveedor = Proveedores()

#como accedo a todos esos campos: instancio clase e invoco el dato que quiero

p = Productos()
p.CIFproveedor.NombreProveedor
p.categoriaProducto.idCategoria


#Cuando tenemos una clase que hace referencia a otras clases hablamos de composicion.


