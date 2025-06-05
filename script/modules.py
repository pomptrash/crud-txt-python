import os
import datetime

# Nesse código, há as funções que irão manipular o diretório onde os arquivos txt estão.
# Foram definidas as funções para atualizar o diretório, mostrar os arquivos criados, criar um novo arquivo, deletar ou selecionar um arquivo.

# get the current date
date = datetime.datetime.now().strftime("%x %X")
print(date)

databases = []

def refreshDir():
	# access the current directory 
	currentDir = os.getcwd()
	# populate the databases list with the txt files from the current directory 
	for root, dirs, files in os.walk(currentDir):
			for file in files:
				if file.endswith(".txt") and file not in databases:
					databases.append(os.path.join(file))


# checks for the presence of txt files, accepts 1 as parameter to display the interface table	
def showDatabase(display=0):
	
	if len(databases) > 0: 	
		if display == 1:
			print(f"+{'-'*34}+")
			print(f"|{'DATABASES':^34}|")
			print(f"+{'-'*34}+")
			for key, DB in enumerate(databases):
				print(f"| {key:^4} | {DB:<25} | ")
			print(f"+{'-'*34}+")
		return True
	else:
		if display == 1:
			print(f"+{'-'*34}+")
			print(f"|{'DATABASES':^34}|")
			print(f"+{'-'*34}+")
			print(f"| {'THERE IS NO DATABASE':^32} | ")
			print(f"+{'-'*34}+")
		return False

# create a new database whenever its called or when theres any databases created on the list
def createDatabase():
	while True:
		
		DBName = str(input("new database name (-1 to cancel):  "))
		if DBName == '-1':
			os.system("cls||clear")
			print("operation canceled.")
			break
		if DBName.isalpha() == False or len(DBName) not in range(3,16):
			os.system("cls||clear")
			print("database name must be alphabetic only and 3-15 characters. try again")
			continue
		else:
			DBName+= ".txt"
			if DBName not in databases:
				with open(DBName, 'w') as DBFile:
					DBFile.writelines(f"created in {date}\n")
				print(f"{DBName} created")
				break
			else:
				os.system("cls||clear")
				print(f"{DBName} already exists.")
				continue

# prompt the user for which database he wants to delete from the list				
def dropDatabase():
	show = showDatabase(1)
	if show == False:
		return None
		
	while True:
		try:
			choice = str(input("which database do you want to delete? -1 to cancel: "))
			if int(choice) != -1 and int(choice) not in range(len(databases)):
				os.system("cls||clear")
				showDatabase(1)
				print("invalid index. try again.")
				continue
		except:
			os.system("cls||clear")
			showDatabase(1)
			print("error. try again. make sure to enter a valid index")
			continue
		else:
			if int(choice) == -1:
				os.system("cls||clear")
				print("operation canceled.")
				return None
			else:
				try:
					os.remove(databases[int(choice)])
				except:
					print("")
				else:
					os.system("cls||clear")
					print(f"{databases[int(choice)]} deleted")
					databases.pop(int(choice))
					break	

def selectDatabase():
	show = showDatabase(1)
	if show == False:
		return None
		
	while True:
		try:
			selectedDB = str(input("select a database (-1 to cancel): "))
			if selectedDB == '-1':
				os.system("cls||clear")
				print("operation canceled")
				return None
			databases[int(selectedDB)]
		except:
			os.system("cls||clear")
			showDatabase(1)
			print("error. try again. make sure to enter a valid index")
			continue
		else:
			if int(selectedDB) not in range(len(databases)):
				print("invalid index. try again")
				continue
			else:
				os.system("cls||clear")
				print(databases[int(selectedDB)])
				return databases[int(selectedDB)]
