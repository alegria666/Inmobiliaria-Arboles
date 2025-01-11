def __ver_nodo(sub_arbol, con_hijos=True):      
    print(f"[{sub_arbol.clave}]")     
    if con_hijos:          
        print(('O' if sub_arbol.izq else 'X') + ' : ' +            
              ('O' if sub_arbol.der else 'X'))      
#------------------------------------------------------------------------------------  
def preorden (arbol_binario):
    __preorden(arbol_binario.raiz)
def __preorden (sub_arbol):
    if sub_arbol:
        __ver_nodo(sub_arbol)
        __preorden(sub_arbol.izq)
        __preorden(sub_arbol.der)

def cad_preorden(arbol_bin, sep="^"):
    def __cad_preorden(sub_arbol):
        nonlocal cadena
        if sub_arbol :
            if sub_arbol == arbol_bin.raiz:
                cadena =cadena+ str(sub_arbol.clave)
            else:
                cadena =cadena+ sep+ str(sub_arbol.clave)
            __cad_preorden(sub_arbol.izq)    
            __cad_preorden(sub_arbol.der)
    cadena = ""
    __cad_preorden(arbol_bin.raiz)
    return cadena
#------------------------------------------------------------------------------------  
def inorden (arbol_binario):
    __inorden(arbol_binario.raiz)
def __inorden (sub_arbol):
    if sub_arbol:
        __inorden(sub_arbol.izq)
        __ver_nodo(sub_arbol, False)
        __inorden(sub_arbol.der) 

def cad_inorden(arbol_bin, sep="-"):
    def __cad_inorden(sub_arbol):
        nonlocal cadena
        if sub_arbol :
            __cad_inorden(sub_arbol.izq)
            if sub_arbol == arbol_bin.buscar_minimo():
                cadena = cadena+str(sub_arbol.clave)
            else:
                cadena = cadena+sep+ str(sub_arbol.clave)  
            __cad_inorden(sub_arbol.der)
    cadena = ""
    __cad_inorden(arbol_bin.raiz)
    return cadena
#------------------------------------------------------------------------------------  
def postorden (arbol_binario):
    __postorden(arbol_binario.raiz)
def __postorden (sub_arbol):
    if sub_arbol:
        __postorden(sub_arbol.izq)
        __postorden(sub_arbol.der)
        __ver_nodo(sub_arbol, True)

def cad_postorden(arbol_bin, sep="\\"):
    def __cad_postorden(sub_arbol):
        nonlocal cadena
        if sub_arbol :
            __cad_postorden(sub_arbol.izq)    
            __cad_postorden(sub_arbol.der)
            if sub_arbol == arbol_bin.raiz:
                cadena =cadena+ str(sub_arbol.clave)
            else:
                cadena =cadena+ str(sub_arbol.clave)+sep
    cadena= ""
    __cad_postorden(arbol_bin.raiz)
    return cadena

def inmo_postorden(arbol_bin):
    def __cad_postorden(sub_arbol):
        nonlocal cadena
        if sub_arbol :
            __cad_postorden(sub_arbol.izq)    
            __cad_postorden(sub_arbol.der)
            cadena =cadena+"-"+str(sub_arbol.clave)+"\n"
    cadena= ""
    __cad_postorden(arbol_bin.raiz)
    return cadena