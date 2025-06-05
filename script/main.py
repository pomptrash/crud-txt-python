from modules import *
from FilesManipulate import *
import os

# Nesse código, há o menu interativo para navegar entre todos os arquivos txt criados no diretório atual.
# Ao selecionar um arquivo (opção 3), será chamado o código FilesManipulate.py, que dará início à manipulação dos dados no arquivo selecionado. 

# display a interactive menu
DBopts =[
	"show",
	"create",
	"drop",
	"select",
	"exit"
]

while True:
	refreshDir() # refresh the directory for new created files
	
	print(f"+{'-'*34}+")
	print(f"|{'MENU':^34}|")
	print(f"+{'-'*34}+")
	for key, options in enumerate(DBopts):
			print(f"| {key:^4} | {options:<25} | ")
	print(f"+{'-'*34}+")
	
	try:
		choice = int(input("select an option: "))
		os.system("cls||clear")
	except:
		os.system("cls||clear")
		
		print("error. try again. make sure to enter a valid index")
		continue
	else:
		
		if choice == 0:
			showDatabase(1)
		elif choice == 1:
			createDatabase()
		elif choice == 2:
			dropDatabase()
		elif choice == 3:
			try:
				menu(selectDatabase())
			except:
				None
			else:
				continue
			
		elif choice == 4:
			print(f"+{'-'*34}+")
			print(f"|{'PROGRAM FINISHED':^34}|")
			print(f"+{'-'*34}+")
			break
		else:
			print("error. try again. make sure to enter a valid index")
			continue
		
