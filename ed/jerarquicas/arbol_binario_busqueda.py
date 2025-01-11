#Daniel Esteban Alegría Zamora


from ed.jerarquicas.arbol_binario import ArbolBinario
from ed.jerarquicas.nodo_ab import NodoArbolBinario
from ed.jerarquicas.excepciones import *

class ArbolBinarioBusqueda(ArbolBinario):
    
    def adicionar(self,nueva_clave):
        self.raiz=self.__adicionar(self.raiz,nueva_clave)
    def __adicionar(self,sub_arbol,nueva_clave):
        if sub_arbol is None:
            sub_arbol=NodoArbolBinario(nueva_clave)
        elif isinstance(nueva_clave,type(sub_arbol.clave)):
            if sub_arbol.clave>nueva_clave: #voy por izquierda
                sub_arbol.izq=self.__adicionar(sub_arbol.izq, nueva_clave) 
            elif sub_arbol.clave<nueva_clave:#voy por derecha
                sub_arbol.der=self.__adicionar(sub_arbol.der, nueva_clave)
            else: #nueva_clave duplicada
                raise DuplicatedKeyError (nueva_clave)
        else:#
            raise DateError (nueva_clave)
        return sub_arbol
#------------------------------------------------------------------------------------       
    def buscar (self,clave_buscar):
        return self.__buscar(self.raiz,clave_buscar)
    def __buscar(self,sub_arbol,clave_buscar):
        if sub_arbol is not None:
            if sub_arbol.clave==clave_buscar:
                return sub_arbol.clave
            elif sub_arbol.clave>clave_buscar:#voy por izquierda
                return self.__buscar(sub_arbol.izq, clave_buscar)
            return self.__buscar(sub_arbol.der, clave_buscar)#voy por derecha
        return None
    
    def buscar_minimo(self):
        return self.__buscar_minimo(self.raiz)
    def __buscar_minimo(self,sub_arbol):
        if sub_arbol.izq :
            return self.__buscar_minimo(sub_arbol.izq)
        return sub_arbol

    def buscar_maximo(self):
        return self.__buscar_maximo(self.raiz)
    def __buscar_maximo(self,sub_arbol):
        if sub_arbol.der :
            return self.__buscar_maximo(sub_arbol.der)
        return sub_arbol
    
    def borrar(self, clave_elimin, mayor=True):
        self.raiz = self.__borrar(self.raiz, clave_elimin, mayor)

    def __borrar(self, sub_arbol, clave_e, mayor):
        if sub_arbol:
            if sub_arbol.clave > clave_e:
                sub_arbol.izq = self.__borrar(sub_arbol.izq, clave_e, mayor)
            elif sub_arbol.clave < clave_e:
                sub_arbol.der = self.__borrar(sub_arbol.der, clave_e, mayor)
            elif sub_arbol.izq and sub_arbol.der:
                if mayor:
                    cambio = self.__buscar_maximo(sub_arbol.izq)
                    sub_arbol.clave = cambio.clave
                    sub_arbol.izq = self.__borrar(sub_arbol.izq, cambio.clave, mayor)
                else:
                    cambio = self.__buscar_minimo(sub_arbol.der)
                    sub_arbol.clave = cambio.clave
                    sub_arbol.der = self.__borrar(sub_arbol.der, cambio.clave, mayor)
            else:
                if sub_arbol.izq:
                    return sub_arbol.izq
                elif sub_arbol.der:
                    return sub_arbol.der
                return None
            return sub_arbol
        return None
                               
