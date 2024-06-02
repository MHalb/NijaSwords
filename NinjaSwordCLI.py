import hashlib, platform, argparse
import CoreManagers, os, time, sys



def Login():

	while True:

		KeepLoginBlock = Password_Manager.PasswordValidation()
		
		if KeepLoginBlock == True:	
			if input("Deseja Manter a sessão? [S/n]").lower() in ['s', 'sim']:
				KeepThisSession = True

			else:
				KeepThisSession = False

			print("logado com sucesso")
			time.sleep(1)
			os.system("cls")
			return True

		else:
			print("Senha incorreta, tente novamente.")


def argsCliActions():
	pass

def ConsoleCliInterface():
		while True:
			system_call = input("insira o seu comando [Help para listar todos]: ")


			match system_call:
				case "clear" | "cls":
					os.system(systemBasedCommands['clearConsole'].get(OPsys))
							
				case s if s.startswith("help"):

					if not s.split()[1:]:
						print(InternalCommandsParser['help'].get("title"))
						
						for commands in InternalCommandsParser['help']['options'].values():
							print(commands)

					else:
						print(InternalCommandsParser['help']['options'][s.split()[0]])

				case s if s.startswith("save"):
					if not s.split()[1:]:
						print(InternalCommandsParser['help']['options'][s.split()[0]])
					else:
						pass

				case s if s.startswith("list"):
					if not s.split()[1:]:
						print(InternalCommandsParser['help']['options'][s.split()[0]])
					else:
						pass

				case s if s.startswith("remove"):
					if not s.split()[1:]:
						print(InternalCommandsParser['help']['options'][s.split()[0]])
					else:
						pass

				case s if s.startswith("masterkey"):
					if not s.split()[1:]:
						print(InternalCommandsParser['help']['options'][s.split()[0]])
					else:
						pass

				case s if s.startswith("sync"):
					if not s.split()[1:]:
						print(InternalCommandsParser['help']['options'][s.split()[0]])
					else:
						pass
				
				case "exit":
					exit()

				case _:
					print("insira um comando válido!")
					time.sleep(1)
					os.system(systemBasedCommands['clearConsole'].get(OPsys))
					continue



if __name__ == "__main__":
	Password_Manager = CoreManagers.PasswordManager()
	CriptografyType = "sha256"
	CloudBasedSave = False
	CloudBasedComputing = False
	CloudLocator = "NijaAnywhere.pythonanywhere.com"
	KeepThisSession = False
	OPsys = platform.system()

	systemBasedCommands = {
		"clearConsole": {
			"Windows": "cls",
			"Linux": "clear"
		}
	}

	InternalCommandsParser = {
		"help": {
			"title": "Veja todos so comandos disponíveis:\n",
			"options": {
				"help": "help <option> - Mostra o uso de todos os comandos disponíveis no software;",
				"clear": "clear - Limpa as informações do Console;",
				"save": "save <content> < save|encript > - criptografa sua chave, mostra ou salva eles;",
				"list": "list <saved items> - mostra os items criptografados salvos;",
				"remove": "remove <item> - remove algum item ou chave salva;",
				"masterkey": "masterkey < reset|recall > - muda a chave mestra ou chama ela novamente",
				"sync": "sync <NijaWebserver> <masterkey NijaServer> - transfere seus dados para os servidores Nuvem da Nija",
				"settings": "settings <settings option> <setting value> - define variáveis de configuração da aplicação.;",
				"exit": "exit - fecha a aplicação"
			}
		}
	}

	if not sys.argv[1:]:
		is_logged = Login()

		if is_logged == True:
			print("Seja bem vindo ao sistem de senhas seguras do NijaSwords. Insira \"help\" para ver os comandos.")
			ConsoleCliInterface()

	else:
		argsCliActions()
		