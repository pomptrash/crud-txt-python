import os
from modules import *


# Nesse código, há as funções que manipulam O arquivo txt.
# funções para escrever, ler, atualizar ou remover uma linha de dentro do arquivo. Definindo as quatro funções essenciais do CRUD.
# possui também o menu interativo onde o usuário poderá escolher a função desejada.

# clear console
def clear():
	return os.system("cls||clear")

# to write on the selected file
def write(fileName):
	while True:
		# it tries to open the file 
		try:
			with open(fileName, "r") as file:
				rows = file.readlines()
			id = len(rows)
			# prompt the message that will be written 
			message = str(input("write (-1 to cancel): "))
	
		except:
			print("error. try again")
			continue
		else:
			# if -1, the operation is canceled 
			if message == "-1":
				clear()
				print("operation canceled")
				return None
			else: 
				with open(fileName, "a") as file:
					file.write(f"{id:>3} {message}\n")
				clear()
				print("done")
				break

# it shows all the content from the selected file
def read(fileName):
	while True:
		try:
			with open(fileName, "r") as file:
				rows = file.readlines()
			print(f"+{'-'*34}+")
			print(f"|{fileName +' content':^34}|")
			print(f"+{'-'*34}+")
			if len(rows) == 0:
				print(f"| {'NO REGISTERS':^32} | ")
			for row in rows:
				print(f"| {row.strip():<32} | ")
			print(f"+{'-'*34}+")
		except:
			print("error. wait. trying again.")
		else:
			return len(rows) # it returns the file lines quantity
			
# update a selected line from the file
def update(fileName):
	lengthList = read(fileName)
	if lengthList > 1:
		while True:
			try:
				# prompt the line that will be updated
				rowSelect = int(input("which line do you want to update? (-1 to cancel ) "))
			except:
				clear()
				read(fileName)
				print("error. try again.")
				continue
			else:
				if rowSelect == -1:
					clear()
					print("operation canceled")
					return None
				else:
					# verifies if the file has the selected line
					if rowSelect in range(lengthList) and rowSelect != 0:		
						while True:
							message = str(input("write the new value: "))
							if len(message) in range(3,16):
								break
							else:
								clear()
								read(fileName)
								print("the new value size must be between 3 and 15 characters. try again")
								continue
						
						with open(fileName, "r") as file:
							rows = file.readlines()
						rows[rowSelect] = f"{rowSelect:>3} {message}\n"
						with open(fileName, "w") as file:
							file.writelines(rows)
						clear()
						print("updated")
						break
							
					else: 
						clear()
						read(fileName)
						print("index out of range. try again.")
						continue
	else:
		print("No registers to update")
		return None


# remove a selected line from the file
def remove(fileName):
	lengthList= read(fileName)

	if lengthList > 1:
		while True:
			try:
				# prompt the line that will be removed
				rowSelect = int(input("which line do you want to remove? (-1 to cancel) "))
			except:
				clear()
				read(fileName)
				print("error. try again.")
				continue
			else:
				if rowSelect == -1:
					clear()
					print("operation canceled")
					break
				if rowSelect in range(lengthList) and rowSelect != 0:			
					with open(fileName, "r") as file:
						rows = file.readlines()
					
					rows.pop(rowSelect)
					with open(fileName, "w") as file:
						file.writelines(rows)
					clear()
					print("removed")
					break
						
				else: 
					clear()
					read(fileName)
					print("index out of range. try again.")
					continue
	else:
		print("No registers to remove")
		return None

# display a interactive menu of the file manipulators options
def menu(fileName):
	opts = [
		"write",
		"read",
		"update",
		"remove",
		f"quit {fileName}"
	]
	while True:
		print(f"+{'-'*34}+")
		print(f"|{fileName:^34}|")
		print(f"+{'-'*34}+")
		for opt in opts:
			print(f"| {opts.index(opt)} {opt.strip():<30} | ")
		print(f"+{'-'*34}+")
		
		try:
			choice = int(input("select the option: "))
			clear()
		except:
			clear()
			print("invalid option. try again")
		else: 
			if choice == 0:
				write(fileName)
			elif choice == 1:
				read(fileName)
			elif choice == 2:
				update(fileName)
			elif choice == 3:
				remove(fileName)
			elif choice == 4:
				print(f"{fileName} closed.")
				return None
			else:
				print("option out of index. try again.")
				continue
