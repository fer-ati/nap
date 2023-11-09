#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pspy import D                           #@
from random import choice                    #@
from kivymd.app import MDApp                 #@
from kivy.lang import Builder                #@ 
from kivy.core.window import Window          #@
from kivy.uix.boxlayout import BoxLayout     #@
from kivy.properties import ObjectProperty   #@

class MainApp(MDApp):
	
	def build(self):
		self.title = "My Pass Create"
		self.icon = "py.png"
		Window.top = 20
		Window.size =set([450,850])
		Window.left = 1300
		self.theme_cls.primary_palette = "Orange"
		self.theme_cls.theme_style = "Dark"
		
		return MainWindow() 


class MainWindow(BoxLayout):
	''' Oggeti di properita   '''
	teip = ObjectProperty(None)
	risultato = ObjectProperty(None) 
	
	def slak(self):
		stringa = self.teip.text
		nuova_stringa = ""
		
		for lettera in stringa:
		
			if lettera in D.par:
				nuova_stringa += D.par[lettera]
		
			else:
				nuova_stringa += lettera
		
		self.risultato.text = nuova_stringa
	
	def random_pass(self):
		final = ""
	
		for i in range(12):
			final += choice(D.lista_completa)
		
		self.risultato.text = final


if __name__ == "__main__":
	MainApp().run()

	
''' '''











