from fileinput import close
from guizero import *


class Aplicacion:

    def __init__(self, bg="#594974"):
        self.app= App(title="Proyecto Final de POO II", width= 1000, height=1000 , bg=bg,layout="grid")
        self.titulo=Text(self.app, text="LIBRERIAS GRAFICAS DE PYTHON", width="fill", height="fill", align="top",grid=[0,0,3,1], size=18, font="Elephant", color="#FFA03D")
        #self.estudiante= Text(self.app, text="Proyecto final Programacion Orientada a Objetos II    Omar Rivilla      3AN", align="top", width="fill")
        self.librerias()
        self.app.display()

    def librerias(self):
    
        #Libreria1
        libreria1_box=Box(self.app, border=True,width=500,height=330, grid=[1,1], align="top")
        libreria1_titulo=Text(libreria1_box, text="LIBRERIA PLOTY",  align="top",size=14, font="Times New Roman" ,color="#52FFEA")
        libreria1_imagen= Picture(libreria1_box, image="D:\Python\Librerias\plotlyt.png", align="top", width=250, height=250)
        libreria1_boton= PushButton(libreria1_box, text="Abrir documentacion", align="top", command=self.Libreria1)
        #Libreria2

        libreria2_box=Box(self.app, border=True, width=500, height=330, grid=[2,1], align="top")
        libreria2_titulo=Text(libreria2_box, text="LIBRERIA MATPLOTLIB",size=14, font="Times New Roman" ,color="#52FFEA", align="top")
        libreria2_imagen= Picture(libreria2_box, image="D:\Python\Librerias\matplotlib.png",align="top", width=250, height=250 )
        libreria2_boton= PushButton(libreria2_box, text="Abrir documentacion", align="top", command=self.Libreria2)
        #Libreria3       
        libreria3_box=Box(self.app, border=True, width=500,height=330, grid=[1,2], align="bottom")
        libreria3_titulo=Text(libreria3_box, text="LIBRERIA SEABORN",size=14, font="Times New Roman" ,color="#52FFEA", align="top")
        libreria3_imagen= Picture(libreria3_box, image="D:\Python\Librerias\seaborn.png",align="top", width=250, height=250)
        libreria3_boton= PushButton(libreria3_box, text="Abrir documentacion", align="top", command=self.Libreria3)
        #Libreria4
        libreria4_box=Box(self.app, border=True, width=500,height=330, grid=[2,2], align="bottom")
        ibreria4_titulo=Text(libreria4_box, text="LIBRERIA NUMPY", size=14, font="Times New Roman" ,color="#52FFEA", align="top")
        libreria4_imagen= Picture(libreria4_box, image="D:\Python\Librerias\img_numpy.png",align="top", width=250, height=250)
        libreria4_boton= PushButton(libreria4_box, text="Abrir documentacion", align="top", command=self.Libreria4)
        
        #libreria 5
        #libreria5_box=Box(self.app, width=500,height=150, grid=[1,3,3,1],align="top" )
        #ibreria4_titulo=Text(libreria5_box, text="CODIGO QR", size=14, font="Times New Roman" ,color="#52FFEA", align="top")

    def Libreria1(self):
        ventana1= Window(self.app, title="Ventana Ploty",bg="#594974",width=600,height=450)
        ventana1_titulo=Text(ventana1, text="¿Para que sirve la Libreria Ploty?", size=14, font="Times New Roman" ,color="#52FFEA", align="top")
        ventana1_subtitulo1=Text(ventana1, text="")
        ventana1_imagen= Picture(ventana1, image="D:\Python\Librerias\img_ploty.png",align="top", width=250, height=250 )
        ventana1_subtitulo=Text(ventana1, text="La librería Plotly es una biblioteca de gráficos interactivos en línea de código abierto")            
        ventana1_subtitulo2=Text(ventana1, text="que se utiliza para visualizar datos. Permite crear gráficos en 2D y 3D, así como ")
        ventana1_subtitulo3=Text(ventana1, text="visualizaciones interactivas con controles deslizantes, botones y menús desplegables.")
        ventana1_subtitulo1=Text(ventana1, text="")
        ventana1_boton=PushButton(ventana1, text="Mostrar Grafico",align="left",command=self.LibPlo, width=25) 
        ventana1_boton=PushButton(ventana1, text="Salir",align="right", command=ventana1._close_window, width=25) 
    
    def Libreria2(self):
        ventana2= Window(self.app, title="Ventana Matplotlib",bg="#594974",width=660,height=450)
        ventana2_titulo=Text(ventana2, text="¿Para que sirve la Libreria Ploty?", size=14, font="Times New Roman" ,color="#52FFEA", align="top")
        ventana2_subtitulo1=Text(ventana2, text="")
        ventana2_imagen= Picture(ventana2, image="D:\Python\Librerias\matplotlib_ejemplo.png",align="top", width=250, height=250 )
        ventana2_subtitulo=Text(ventana2, text="La librería Matplotlib es una biblioteca de gráficos 2D en Python que permite crear ")            
        ventana2_subtitulo2=Text(ventana2, text="visualizaciones de datos estáticas, animadas e interactivas en diferentes formatos. Es muy útil")
        ventana2_subtitulo3=Text(ventana2, text="para el análisis y la exploración de datos, y para la comunicación de resultados.")
        ventana2_subtitulo1=Text(ventana2, text="")
        ventana2_boton=PushButton(ventana2, text="Mostrar Grafico",align="left",command=self.LibMat, width=25) 
        ventana2_boton=PushButton(ventana2, text="Salir",align="right", command=ventana2._close_window, width=25) 
    
    def Libreria3(self):
        ventana3= Window(self.app, title="Ventana Seaborn",bg="#594974",width=605,height=450)
        ventana3_titulo=Text(ventana3, text="¿Para que sirve la Libreria Seaborn?", size=14, font="Times New Roman" ,color="#52FFEA", align="top")
        ventana3_subtitulo1=Text(ventana3, text="")
        ventana3_imagen= Picture(ventana3, image="D:\Python\Librerias\seabornFinal.png",align="top", width=250, height=250 )
        ventana3_subtitulo=Text(ventana3, text="Seaborn es una herramienta muy útil para el análisis y visualización de datos en Python,")            
        ventana3_subtitulo2=Text(ventana3, text="especialmente para aquellos que buscan crear visualizaciones estadísticas elegantes ")
        ventana3_subtitulo3=Text(ventana3, text="y personalizables.")
        ventana3_subtitulo1=Text(ventana3, text="")
        ventana3_boton=PushButton(ventana3, text="Mostrar Grafico",align="left",command=self.LibSea, width=25) 
        ventana3_boton=PushButton(ventana3, text="Salir",align="right", command=ventana3._close_window, width=25)

    def Libreria4(self):
        ventana4= Window(self.app, title="Ventana Numpy",bg="#594974",width=675,height=450)
        ventana4_titulo=Text(ventana4, text="¿Para que sirve la Libreria Numpy?", size=14, font="Times New Roman" ,color="#52FFEA", align="top")
        ventana4_subtitulo1=Text(ventana4, text="")
        ventana4_imagen= Picture(ventana4, image="D:\Python\Librerias\seaborejemplo.png",align="top", width=250, height=250 )
        ventana4_subtitulo=Text(ventana4, text="Es una de las librerías más importantes de Python para la computación científicay el análisis ")            
        ventana4_subtitulo2=Text(ventana4, text="de datos. Proporciona una estructura de datos de matriz multidimensional eficiente y fácil de usar,")
        ventana4_subtitulo3=Text(ventana4, text="así como funciones matemáticas para realizar operaciones numéricas en matrices y arreglos.")
        ventana4_subtitulo1=Text(ventana4, text="")
        ventana4_boton=PushButton(ventana4, text="Mostrar Grafico",align="left",command=self.LibMat1, width=25) 
        ventana4_boton=PushButton(ventana4, text="Salir",align="right", command=ventana4._close_window, width=25)

    def LibPlo(self):
        from Lib_Plo import grafico  
        
    def LibMat(self):
        from Matplotlib import plt
    
    def LibSea(self):
        from Seaborn import plt

    def LibMat1(self):
        from Matplotlib1 import plt
        


blog = Aplicacion()