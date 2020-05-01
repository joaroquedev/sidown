try:
	import os
	import io
	import sys
	import time
	import urllib
	import requests
except ImportError:
	exit("Verifica os módulos e tente denovo ...")


#-------------COLOR/STYLE-------------#
class Color:
	END = '\033[0m'
	BOLD = '\33[1m'
	RED = '\033[91m'
	PISCA = '\33[5m'
	BGRED = '\33[41m'
	BLUE = '\033[94m'
	GREEN = '\033[92m'
	BGBLUE = '\33[44m'
	WARNING = '\033[93m'
	UNDERLINE = '\033[4m'
	IMPORTANT = '\33[35m'

#atalhos-cores
r = '\033[91m'
g = '\033[92m'
e = '\033[0m'
b = '\33[1m'
abrir = r+"["+e
fechar = r+"]"+e
banner = """
  .::::::. ::::::::::-.      ...    .::    .   .::::::.    :::.
 ;;;`    ` ;;; ;;,   `';, .;;;;;;;. ';;,  ;;  ;;;' `;;;;,  `;;;
 '[==/[[[[,[[[ `[[     [[,[[     \[[,'[[, [[, [['    [[[[[. '[[
   '''    $$$$  $$,    $$$$$,     $$$  Y$c$$$c$P     $$$ "Y$c$$
  88b    dP888  888_,o8P'"888,_ _,88P   "88"888      888    Y88
   "YMmMY" MMM  MMMMP"`    "YMMMMMP"     "M "M"      MMM     YM
╔═════════════════════════════════════════════════════════════╝
╚[04-2020]═════════════════[HaguacomH]═════════════════[V.1.0]$
"""


#-------------FUNÇÕES-------------#

#-------------LIMPATELA-------------#
def clearScr():
	os.system('clear')
	

#-------------SAI-DO-PROGRAMA-------------#
def exit():
	os.system('exit')
	


#-------------BANNER&MENU-------------#

def menu():
	
	ops=[g+"1", g+"2", g+"3", g+"4", g+"5", g+"6", g+"7", g+"8", g+"9", g+"0"+e]
	print("\t"+abrir+ops[0]+fechar+" start full scan    "+abrir+ops[4]+fechar+" find passwds.txt")
	print("\t"+abrir+ops[1]+fechar+" find css files     "+abrir+ops[5]+fechar+" find htaccess")
	print("\t"+abrir+ops[2]+fechar+" find js files      "+abrir+ops[6]+fechar+" find admin")
	print("\t"+abrir+ops[3]+fechar+" find fonts         "+abrir+ops[7]+fechar+" about & exit")
	

#-------------BAIXA-ARQUIVO-------------#
def down(m, nome=None):
	#m="http://unitel.ao/hi.html"

	if nome is None:
		nome = os.path.basename(m.split("?")[0])
	
	file_res = requests.get(m, stream=True)
	if file_res.status_code == requests.codes.OK:
		with open(nome, 'wb') as novo_arquivo:
			for parte in file_res.iter_content(chunk_size=256):
				novo_arquivo.write(parte)
	
		print("\r    Downlod {}".format(nome))
	else:
		file_res.raise_for_status()
	

#-------------ACHA OS DIRECTÓRIOS E ARQUIVOS DENTRO-------------#
def find(url,dirs_txt,files_txt):

	#---LISTA DIR
	dirs = io.open(dirs_txt , "r", encoding="utf8")
	dirs_list = dirs.readlines()
	dirs.close()

	#print("Number of dirs: "+str(len(dirs_list)))
	#---ACHA DIR
	for i in range(len(dirs_list)):
		search = dirs_list[i].strip()
		target = (url + "/" + search + "/")
		response = requests.get(target)

		if response.status_code == 403:
			print("\nDIR FOUND: {}".format(target))

			#---LISTA ARQUIVO
			files = io.open(files_txt , "r", encoding="utf8")
			files_list = files.readlines()
			files.close()
			
			#---ACHA ARQUIVO
			for x in range(len(files_list)):			
				sub_search = files_list[x].strip()
				sub_target = (target + sub_search)
				sub_response = requests.get(sub_target)

				if sub_response.status_code == 200:
					print("    File Found ══> {}".format(files_list[x]))

					down(sub_target)

					#---BAIXA ARQUVIO
	
				else:
					#print("Bad file")
					pass
				pass
			pass
		else:
			#print("Bad dirs")
			pass
		pass
	
	back2menu = str(input("\nBack to menu(Y/N): "))
	if back2menu.upper() == "Y":
		main()
	
	else:
		exit()
		pass
	pass
#--------------ACHA ARQUIVOS ÚNICOS-----------#
def find_single(url,wordlists):
	#---LISTA WORDLIST
	word = io.open(wordlists, "r", encoding="utf-8")
	word_list = word.readlines()
	word.close()

	#---ACHA ARQUIVO
	for i in range(len(word_list)):
		search = word_list[i].strip()
		target = (url + "/" + search)
		response = requests.get(target)

		if respnse.status_code == 200:
			print("\nFILE FOUND: {}".format(target))
	
		else:
			pass
		pass
		
		back2menu = str(input("\nBack to menu(Y/N): "))
		if back2menu.upper() == "Y":
			main()
	
		else:
			exit()
			pass
	pass

#-------------ACHA O PAINEL ADMIN-------------#
def find_admin(url, wordlists):
	#---LISTA WORDLIST
	word = io.open(wordlists, "r", encoding="utf-8")
	word_list = word.readlines()
	word.close()

	for i in range(len(word_list)):
		search = word_list[i].strip()
		target = (url + "/" + search + "/")
		response = requests.get(target)
		if response.status_code == 200:
			print("ADMIN FOUND: {}".format(target))
	
		else:
			pass
		pass

	back2menu = str(input("\nBack to menu(Y/N): "))
	if back2menu.upper() == "Y":
		main()
	
	else:
		exit()
		pass
	pass
#-------------FUNÇÃO-PRINCIPAL-------------#
def main():
	clearScr()
	#---banner
	b = (Color.BOLD+banner+Color.END)
	print(b)
	#---inserir url
	url = str(input("\n[Ex: http://viado.com]\nInsere uma URL: http://"))
	url = "http://"+url
	#---função menu
	clearScr()
	print(b)
	menu()

	#---PROMPT
	abrir = g+"["+e
	fechar = g+"]"+e
	op = int(input("\n"+r+"╔═══"+abrir+"SiDown"+fechar+r+"══"+abrir+url[7:]+fechar+r+"═"+abrir+"menu"+fechar+r+":\n╚═════> "+e))

	if op == 1:
		#full_scan()
		print("Full scan")
	elif op == 2:
		p1 = "wordlists/css_dirs.txt"
		p2 = "wordlists/css_files.txt"
		find(url,p1,p2)
	elif op == 3:
		p1 = "wordlists/js_dirs.txt"
		p2 = "wordlists/js_files.txt"
		find(url,p1,p2)
	elif op == 4:
		p1 = "wordlists/fonts_dirs.txt"
		p2 = "wordlists/fonts_files.txt"
		find(url,p1,p2)
	elif op == 5:
		p1 = "wordlists/psswrd_dirs.txt"
		find_single(url,p1)
	elif op == 6:
		p1 = "wordlists/htaccess.txt"
		find_single(url,p1)
	elif op == 7:
		#about()
		p1 = "wordlists/admin.txt"
		find_admin(url,p1)
	elif op == 8:
		#find_psswd_txt()
		clearScr()
		print(b)
		print("""
   SiDown is a tool for download public files in websites.
             Sipmle, minimalist and nobbie kkk
                      By: Joa_Roque
                        Good Luky
			""")
		time.sleep(10)
		main()
	else:
		main()
	pass

if __name__ == '__main__':
	try:
		main()
	
	except KeyboardInterrupt:
		print("\n\nFIM DA EXECUÇÃO...\n")
		pass
	pass


