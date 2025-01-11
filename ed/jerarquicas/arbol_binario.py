from random import random 
from ed.jerarquicas.nodo_ab import NodoArbolBinario

class ArbolBinario:
    def __init__(self):
        self.raiz=None
#------------------------------------------------------------------------------    
    def adicionar (self,nueva_clave):
        self.raiz=self.__adicionar(self.raiz,nueva_clave)
    def __adicionar(self,sub_arbol,nueva_clave):
        if sub_arbol is None:
            sub_arbol=NodoArbolBinario(nueva_clave)   
        elif random()<=0.5:#voy por izquierda
            nodo_izq=self.__adicionar(sub_arbol.izq, nueva_clave)
            sub_arbol.izq=nodo_izq    
        else:#voy por derecha
            sub_arbol.der=self.__adicionar(sub_arbol.der, nueva_clave)
        return sub_arbol 
#---------------------------------------------------------------------------   
    def buscar(self,clave_busar):
        return self.__buscar(self.raiz,clave_busar)
    def __buscar (self, sub_arbol,clave_buscar):
        if sub_arbol is not None:
            if sub_arbol.clave == clave_buscar:
                return sub_arbol.clave
            else:
                busc_izq=self.__buscar(sub_arbol.izq, clave_buscar)
                if busc_izq is not None:
                    return busc_izq
                busc_der=self.__buscar(sub_arbol.der, clave_buscar)
                if busc_der is not None:
                    return busc_der
        return None
#-----------------------------------------------------------------------  
    def __len__(self):
        return self.__tamaño(self.raiz)
    def __tamaño(self,sub_arbol):
        if sub_arbol is not None:
            return (1
                    +self.__tamaño(sub_arbol.izq)
                    +self.__tamaño(sub_arbol.der))
        return 0
#--------------------------------------------------------------------   
    def hojas (self):
        return self.__hojas(self.raiz)
    def __hojas(self,sub_arbol):
        if sub_arbol is None:
            return 0
        elif sub_arbol.tiene_hijos() is False:
            return 1
        return self.__hojas(sub_arbol.izq)+self.__hojas(sub_arbol.der)
        #Retorna el numero de hojas
#--------------------------------------------------------------------   
    def internos(self):
        return self.__internos(self.raiz)
    def __internos(self,sub_arbol):
        if sub_arbol.tiene_hijos():
            return (1
                    +self.__internos(sub_arbol.izq)
                    +self.__internos(sub_arbol.der))
         #Retorna el numero de nodos
#-----------------------------------------------------------------        
    def altura(self):
        return self.__altura(self.raiz)
    def __altura(self,sub_arbol):
        if sub_arbol.izq == None and sub_arbol.der == None:
            return 0
        else:
            x=1
            y=1
            if sub_arbol.izq!=None:
                x=self.__altura(sub_arbol.izq)
            if sub_arbol.der!=None:
                y=self.__altura(sub_arbol.der)
            return 1+max(x,y)
    



 

        

    

