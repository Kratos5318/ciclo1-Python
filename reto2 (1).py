# -*- coding: utf-8 -*-
"""Reto2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Mi4QYiTviaB8QBx1Clx19yq5dAYdqJew
"""

Vampiric= input("")
Frenzy = input ("")
listaReloj = input ("")

vam= 0
fre=0


for temp in listaReloj:
    if temp in Vampiric:
         vam+=1
    if temp in Frenzy:
        fre+= 1
    if vam==fre:
         print("≈",end ='')

    elif vam > fre:
       print("V",end ='')
    elif vam<fre:
      
      print("F",end ='')