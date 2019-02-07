#!/usr/bin/env python
from passlib.hash import md5_crypt
import sys

def convertFileToList(filePath):
	passList = []
	with open(filePath, 'r', encoding="Latin-1") as f:
		for line in f:
			passList.append(line)

	return passList

def decrypt_md5(enc_pwd, pwdlist):
	##fill this

	split_enc = enc_pwd.split('$')
	#print(enc_pwd)
	for word in pwdlist:
		#print(md5_crypt.hash(word, salt=split_enc[2]))
		if md5_crypt.hash(word.rstrip(), salt=split_enc[2]).strip() == enc_pwd.strip():
			return word
	return ""

def crackPasswords(passwordFilePath, commonPasswordsFilePath):

	passList = convertFileToList(passwordFilePath)
	commonPassList = convertFileToList(commonPasswordsFilePath)

	for rawPass in passList:

		splitPass = rawPass.split(':')
		username = splitPass[0]
		saltedHash= splitPass[1]

		decryptedPassword = decrypt_md5(saltedHash, commonPassList)
		print(username + ": " + decryptedPassword)
	#for each password in pass list, run decrypt md5 after separating the hash



def main():

	passFilePath = sys.argv[1]
	commonPassFilePath = sys.argv[2]
	crackPasswords(passFilePath, commonPassFilePath)


if __name__ == '__main__':
	main()