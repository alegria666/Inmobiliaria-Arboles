from PyQt6.QtWidgets import *
class DuplicatedKeyError(Exception):
    def __init__(self,nueva_clave):
        super().__init__(f"La propiedad ya esta registrada")
 
#------------------------------------------------------------------------------------  
class DateError(Exception):
    def __init__(self,nueva_clave):
        super().__init__(f"La clave {nueva_clave} no es del nuevo tipo") 