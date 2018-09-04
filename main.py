# coding: utf-8

from tkinter import *
import tkinter.messagebox as tkMsgBox

if __name__ == '__main__':
	
	def message():
		txt = "Bonjour " + str(valeurZoneSaisie.get())
		tkMsgBox.showwarning(" Info", txt, default = 'ok', icon = 'info', parent = root)
	# Création de la fenêtre principale
	root = Tk()
	root.title("Hello")
	
	# Ajout d'une zone de saisie et de son label
	
	labeZoneSaisie = Label(root, text = "Saisissez votre prénom")
	
	valeurZoneSaisie = StringVar()
	valeurZoneSaisie.set("")
	zoneSaisie = Entry(root, textvariable = valeurZoneSaisie)
	
	btnOk = Button(root, text = "Ok", command = message)
	btnQuitter = Button(root, text = "Quitter", command = root.destroy)
	
	labeZoneSaisie.grid(row = 0, column = 0)
	zoneSaisie.grid(row = 0, column = 1)
	
	btnOk.grid(row = 1, column = 0)
	btnQuitter.grid(row = 1, column = 1)
	
	
	root.mainloop()
