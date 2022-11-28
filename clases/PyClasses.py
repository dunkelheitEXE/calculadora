# Este es un apunte rapido sobre las clases en python

# Lo primero es definir que una clase es una serie de
# funciones y atributos que describen y definen a un ente

# Para definir una clase:
class Humano:
    def __init__(self, name, edad): # Esta es la funcion o modulo inicial
        # Lo que hace este modulo es definir los atributos
        # iniciales de la clase. En este caso definira
        # las caracteristicas iniciales del obejto o clase
        # (puede ser una especie de equivalencia de metodo constructor)
        # Algo importante a destacar es que el atributo self
        # siempre va al PRINCIPIO de los atributos dentro de ()
        self.name = name;
        self.edad = edad;

    # De aqui en adelante iran los modulos para funciones u otras
    # caracteristicas del objeto

    def imprimirData(self):
        print("Este humano se llama: {}".format(self.name))
        print("Su edad es de: {} años".format(self.edad))


# Fuera de la clase:

alan = Humano("Alan Grajeda", 25)
alan.imprimirData()
