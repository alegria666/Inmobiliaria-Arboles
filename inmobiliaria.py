import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from ed.jerarquicas.arbol_binario_busqueda import *
from ed.jerarquicas.inmueble import *
from ed.jerarquicas.recorridos import *
from ed.jerarquicas.excepciones import *

class Inmobiliaria(QWidget):

        def __init__(self):
                super().__init__()
                self.setGeometry(200,200,750,450)
                self.setWindowTitle("INMOBILIARIA")
                self.setWindowIcon(QIcon("imagenes/casa.png"))
                self.generar_formulario()
                self.show()
                self.prop=ArbolBinarioBusqueda()
        

        def generar_formulario(self): 
        
#-------fuentes-------------------------------------------------         
        
                font = QFont('Helvetica [Cronyx]',30,5,True)
                font.setBold(True)
                
                fonts = QFont('Helvetica [Cronyx]',9,5,True)
                
                fontl = QFont('Helvetica [Cronyx]',9,5,True)
                fontl.setBold(True)
                
                font_labels = QFont("Calibri", 10,5)
                font_labels.setItalic(True)
                
                font_checks = QFont("Calibri", 10,5)
                font_checks.setBold(True)
                
                font_lista = QFont("Calibri", 10,5,True)
                font_lista.setBold(True)
                
                font_boton = QFont("Times New Roman",13)
                font_boton.setBold(True)
                

        #-------labels------------------------------------------
                
                label = QLabel(self)
                fondo = QPixmap("imagenes/fondo.png").scaled(750, 450)
                label.setGeometry(0,0,750,450)
                label.setPixmap(fondo)
        
                
                
                labeltitle = QLabel(self)
                labeltitle.move(480,20)
                labeltitle.setText("SUITE HOME")
                labeltitle.setFont(font)
                labeltitle.setStyleSheet("color: #D4AF37")
                
                
                labelsubtitle = QLabel(self)
                labelsubtitle.setText("INMOBILIARIA")
                labelsubtitle.move(645,59)
                labelsubtitle.setFont(fonts)
                labelsubtitle.setStyleSheet("color: #D4AF37") 
                
                
                labelline = QLabel(self)
                labelline.setText("_____________________________________")   
                labelline.setFont(fontl)
                labelline.move(480,65)
                labelline.setStyleSheet("color: #D4AF37")  
                
                
                
                operacion_label=QLabel(self)
                operacion_label.setText("Operación: ")
                operacion_label.move(300,100)
                operacion_label.setFont(font_labels)
                
                direccion_label=QLabel(self)
                direccion_label.setText("Dirección:")
                direccion_label.move(510,100)
                direccion_label.setFont(font_labels)
                
                baño_label=QLabel(self)
                baño_label.setText("Num. Baños:")
                baño_label.move(300,138)
                baño_label.setFont(font_labels)
                
                habitacion_label = QLabel(self)
                habitacion_label.setText("Num. Habitaciones:")
                habitacion_label.move(450,138)
                habitacion_label.setFont(font_labels)
                
                garage_label = QLabel(self)
                garage_label.setText("Garage:")
                garage_label.move(625,138)
                garage_label.setFont(font_labels)
                
                check1_label = QLabel(self)
                check1_label.setText("SI")
                check1_label.move(695,137)
                check1_label.setFont(font_checks)
                
                valor_label = QLabel(self)
                valor_label.setText("Valor:")
                valor_label.move(439,177)
                valor_label.setFont(font_labels)
                
                separador_imagen = QPixmap("imagenes/separador.png")#.scaled(750,30)
                separador_label = QLabel(self)
                separador_label.setGeometry(150,245,750,10)
                separador_label.setPixmap(separador_imagen)
                
                consulta_label = QLabel(self)
                consulta_label.setText("Dirección:")
                consulta_label.move(233,270)
                consulta_label.setFont(font_labels)
                
                operacion2_label = QLabel(self)
                operacion2_label.setText("Operación:")
                operacion2_label.move(233,297)
                operacion2_label.setFont(font_labels)
                
                borrar_label = QLabel(self)
                borrar_label.setText(" Borrar\nMayor:")
                borrar_label.move(380,297)
                borrar_label.setFont(font_labels)
                
                o_label = QLabel(self)
                o_label.setText("Ó")
                o_label.move(586,286)
                o_label.setFont(font_checks)
                
                
                separador2_label = QLabel(self)
                separador2_label.setGeometry(260,335,750,10)
                separador2_label.setPixmap(separador_imagen)
                
                
                opciones_label = QLabel(self)
                opciones_label.setText("Otras opciones:")
                opciones_label.setFont(font_labels)
                opciones_label.move(420,358)
                
                casa_imagen = QPixmap("imagenes/casa.png").scaled(50,50)
                casa_label = QLabel(self)
                casa_label.move(700,400)
                casa_label.setPixmap(casa_imagen)
                
                
                
        #-------ingreso datos----------------------------------------------------        
                
                self.direccion_input=QLineEdit(self)
                self.direccion_input.resize(150,24)
                self.direccion_input.move(570,94)
                self.direccion_input.setStyleSheet("background:QLinearGradient(x1:0,y1:0,x2:1,y2:0,stop: 0 #FFFFFF,stop: 1  #C0C0C0 )")
                
                self.valor_input=QLineEdit(self)
                self.valor_input.resize(100,20)
                self.valor_input.move(475,175)
                self.valor_input.setStyleSheet("background:QLinearGradient(x1:0,y1:0,x2:1,y2:0,stop: 0 #FFFFFF,stop: 1  #C0C0C0 )")
                
                self.consulta_input=QLineEdit(self)
                self.consulta_input.resize(150,24)
                self.consulta_input.move(290,265)
                self.consulta_input.setStyleSheet("background:QLinearGradient(x1:0,y1:0,x2:1,y2:0,stop: 0 #FFFFFF,stop: 1   #C0C0C0)")
                
                
                
        #-------botones----------------------------------------------------

                registrar_boton = QPushButton(self)
                imagen_registrar = QPixmap("imagenes/registrar.png")
                icon = QIcon(imagen_registrar)
                registrar_boton.setIcon(icon)
                registrar_boton.setStyleSheet("QPushButton { text-align: left; }")
                registrar_boton.setText("REGISTRAR")
                registrar_boton.move(586,207)
                registrar_boton.setFont(font_boton)
                registrar_boton.clicked.connect(self.registrar)
                
                
                venta_boton = QPushButton(self)
                venta_imagen = QPixmap("imagenes/venta.png")
                icono = QIcon(venta_imagen)
                venta_boton.setIcon(icono)
                venta_boton.setStyleSheet("QPushButton { text-align: left; }")
                venta_boton.setText("OPERAR")
                venta_boton.move(470,281)
                venta_boton.setFont(font_boton)
                venta_boton.clicked.connect(self.venta)
                
                
                consultar_boton = QPushButton(self)
                consultar_imagen = QPixmap("imagenes/consulta.png")
                icono = QIcon(consultar_imagen)
                consultar_boton.setIcon(icono)
                consultar_boton.setStyleSheet("QPushButton { text-align: left; }")
                consultar_boton.setText("CONSULTAR")
                consultar_boton.move(610,281)
                consultar_boton.setFont(font_boton)
                consultar_boton.clicked.connect(self.consulta)
                
                
                mostrar_boton = QPushButton(self)
                mostrar_imagen = QPixmap("imagenes/mostrar.png")
                icono = QIcon(mostrar_imagen)
                mostrar_boton.setIcon(icono)
                mostrar_boton.setStyleSheet("QPushButton { text-align: left; }")
                mostrar_boton.setText(" LISTAR")
                mostrar_boton.move(510,375)
                mostrar_boton.setFont(font_boton)
                mostrar_boton.clicked.connect(self.mostrar)
                
                
                cantidad_boton = QPushButton(self)
                cantidad_imagen = QPixmap("imagenes/cantidad.png")
                icono = QIcon(cantidad_imagen)
                cantidad_boton.setIcon(icono)
                cantidad_boton.setStyleSheet("QPushButton { text-align: left; }")
                cantidad_boton.setText("CANTIDAD")
                cantidad_boton.move(510,405)
                cantidad_boton.setFont(font_boton)
                cantidad_boton.clicked.connect(self.cantidad)
                
                
        #-------combobox----------------------------------------------------

                self.operacion_combo = QComboBox(self)
                self.operacion_combo.addItem("Venta")
                self.operacion_combo.addItem("Arriendo")
                self.operacion_combo.move(363,98)
                self.operacion_combo.setFont(font_lista)
                
                self.consulta_combo = QComboBox(self)
                self.consulta_combo.addItem("Venta")
                self.consulta_combo.addItem("Arriendo")
                self.consulta_combo.move(295,295)
                self.consulta_combo.setFont(font_lista)
                
                
        #-------checkbox----------------------------------------------------
                
                self.garage_check1 = QCheckBox(self)
                self.garage_check1.move(675,138)
                self.garage_check1.setChecked(True) 
             
                
                self.borrar_check = QCheckBox(self)
                self.borrar_check.move(425,310)
                self.borrar_check.setChecked(True)
                
                
        #-------spinbox----------------------------------------------------
                
                self.baños_barra = QSpinBox(self)
                self.baños_barra.setValue(1)
                self.baños_barra.move(373,134)
                self.baños_barra.setFont(font_lista)
                
                self.habitaciones_barra = QSpinBox(self)
                self.habitaciones_barra.setValue(1)
                self.habitaciones_barra.move(548,134)
                self.habitaciones_barra.setFont(font_lista)

#------funciones
        def consulta(self):#hecha
                busdir=self.consulta_input.text()
                busope=self.consulta_combo.currentText()
                buscpro=inmueble(busope, busdir)
                if busdir!="":
                        if self.prop.buscar(buscpro)is None:
                                QMessageBox.information(self,"Informacion" ,"No hay propiedades con esas caracteristicas",
                                QMessageBox.StandardButton.Ok,
                                QMessageBox.StandardButton.Ok)
                        else:
                                QMessageBox.information(self,"Informacion" ,str(self.prop.buscar(buscpro)),
                                QMessageBox.StandardButton.Ok,
                                QMessageBox.StandardButton.Ok)
                else:
                        QMessageBox.warning(self,"Advertencia" ,"Por favor llene la direccion de la propiedad a "+ busope,
                                QMessageBox.StandardButton.Close,
                                QMessageBox.StandardButton.Close)
                self.consulta_input.setText("")
                        
        def mostrar(self):
                if len(self.prop)==0:
                        QMessageBox.information(self,"Propiedades" ,"No hay inmuebles disponibles",
                        QMessageBox.StandardButton.Ok,
                        QMessageBox.StandardButton.Ok)
                else:       
                        QMessageBox.information(self,"Propiedades" ,"Hay los siguientes inmuebles disponibles:\n"+str(inmo_postorden(self.prop)),
                        QMessageBox.StandardButton.Ok,
                        QMessageBox.StandardButton.Ok)
                        
        def cantidad(self):#hecha
                QMessageBox.information(self,"Cantidad" ,"Hay "+str(len(self.prop))+" inmuebles",
                QMessageBox.StandardButton.Ok,
                QMessageBox.StandardButton.Ok)
                
        def registrar(self):#Hecha
                dire =self.direccion_input.text()
                valor=self.valor_input.text()
                hab=self.baños_barra.text()
                baño=self.habitaciones_barra.text()
                opera=self.operacion_combo.currentText()
                garaje=self.garage_check1.isChecked()
                if dire!="" and valor!="":
                        prop=inmueble(opera,dire,hab,baño,garaje,valor)
                        try :
                                self.prop.adicionar(prop)
                                QMessageBox.information(self,"Exito" ,"El inmueble  ha sido registrado exitosamente",
                                QMessageBox.StandardButton.Ok,
                                QMessageBox.StandardButton.Ok)
                        except DuplicatedKeyError as e:
                                QMessageBox.warning(self,"Advertencia" ,str(e),
                                QMessageBox.StandardButton.Close,
                                QMessageBox.StandardButton.Close)
                                
                        self.direccion_input.setText("")
                        self.valor_input.setText("")
                        self.habitaciones_barra.setValue(1)
                        self.baños_barra.setValue(1)
                else:
                        QMessageBox.warning(self,"Advertencia" ,"Llene todos los campos",
                                QMessageBox.StandardButton.Close,
                                QMessageBox.StandardButton.Close)
                
        def venta(self):
                operdir=self.consulta_input.text()
                opera=self.consulta_combo.currentText()
                buscpro=inmueble(opera, operdir)
                check=self.borrar_check.isChecked()
                if operdir!="":
                        inmu=self.prop.buscar(buscpro)
                        if inmu is not None:
                                self.prop.borrar(buscpro,check)
                                QMessageBox.information(self,"Operacion" ,"La vivienda en la dirección: " + operdir+" ha efectuado la operación: "+opera+" exitosamente",
                                QMessageBox.StandardButton.Ok,
                                QMessageBox.StandardButton.Ok)
                        else:
                                QMessageBox.warning(self,"Advertencia" ,"La propiedad en "+opera+" no ha sido encontrada",
                                QMessageBox.StandardButton.Close,
                                QMessageBox.StandardButton.Close)
                else:
                        QMessageBox.warning(self,"Advertencia" ,"Por favor llene la direccion de la propiedad a "+opera,
                                QMessageBox.StandardButton.Close,
                                QMessageBox.StandardButton.Close)
                self.consulta_input.setText("")
                

           
           
        
if __name__=="__main__":
    app = QApplication(sys.argv)
    w = Inmobiliaria()
    w.show()
    sys.exit(app.exec())
