# -*- coding: utf-8 -*-
"""
Created on Mon Jan 23 16:47:12 2023

@author: Aldo
"""

class estanteria :
    def __init__(self,escritor,precio,creado,pasta,nombre):
        self.escritor = escritor
        self.precio = precio
        self.creado = creado
        self.pasta = pasta
        self.nombre = nombre
        
    def tipoLibro (self):
        print("<-CUALIDADES->")
        print("el creador =" + self.escritor)
        print("el precio =" + self.precio)
        print("creacion =" + self.creado)
        print("la pasta =" + self.pasta)
        print("el nombre =" + self.nombre)
        
        
        
Harry_el_mago_loco = estanteria(" J.K Rowling ", "1199.99" , "1997" ," pasta dura "," Harry potter & la piedra filosofal")

Harry_el_mago_loco.tipoLibro()


Grimms_brothers_stories = estanteria(" hermanos grimm ", "607.07" , "1785" ," pasta blanda "," grimm brother's stories")

Grimms_brothers_stories.tipoLibro()



