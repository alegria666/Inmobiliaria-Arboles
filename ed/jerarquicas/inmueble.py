class inmueble():
        def __init__ (self,operacion,direccion,habitacion=1,
        baños=1,garaje=True,valor=0):
                self.operacion=operacion
                self.direccion=direccion
                self.habitacion=habitacion
                self.baño=baños
                self.garaje=garaje
                self.valor=valor
        def __str__(self):
            if self.garaje:
                mensaje=f"La propiedad en la dirección {self.direccion} está en {self.operacion} tiene: {self.habitacion} habitacion(es), {self.baño} baño(s) y cuenta con garaje, tiene un valor de: {self.valor}."
            else:
                mensaje=f"La propiedad en la dirección {self.direccion} está en {self.operacion} tiene: {self.habitacion} habitacion(es), {self.baño} baños, tiene un valor de: {self.valor}."
            return mensaje
        def __gt__ (self,otro_inmueble):
            if self.direccion>otro_inmueble.direccion:
                return True
            elif self.direccion==otro_inmueble.direccion and self.operacion>otro_inmueble.operacion:
                return True
            return False
        
        def __eq__(self, otro_inmueble):
            if self.direccion==otro_inmueble.direccion and  self.operacion==otro_inmueble.operacion:
                return True
            return False