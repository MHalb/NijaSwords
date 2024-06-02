import json

class PasswordManager:
	def __init__(self):
		with open("tempdb.json", 'r') as r:
			self.tempdb = json.load(r)


	def PasswordValidation(self) -> bool:
		if not self.tempdb['MasterKey']:
			self.DefineNewPassword()

		MasterKey = input("Insira a senha mestre: ")
		if self.tempdb['MasterKey'] == MasterKey:
			print('igual')
			return True
		
		return False

	def DefineNewPassword(self):		
		while True:
			NewPassword = input("Insira sua nova senha mestre: ")
			if not NewPassword:
				print("insert a válid password", end='\n\n')

			else:
				self.tempdb['MasterKey'] = NewPassword
				break