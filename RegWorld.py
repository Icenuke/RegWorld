#!/usr/bin/python3
#-*- coding:utf-8 -*-

from re import findall 
from sys import argv
from os import getcwd


def Helper():
	print("""
		Usage: RegWorld [-h] [-i] [-u] [-b] [-x] [-m] [-a] [-p] <file>
			Description:
				RegWorld is a simple to parse files with regex style.
				The ip, url, base64, hexa, mails, mac address and phone number (FR)
				Can be parse by this script.
			Options:
				-h 		Show this message
				-i 		Use regex to find IPv4 addresses
				-u 		Use regex to find url
				-b 		Use regex to find base64
				-x 		Use regex to find hexa
				-m 		Use regex to find emails
				-a 		Use regex to find mac addresses
				-p 		Use regex to find phones numbers (FR)

	""")

def Export(name, datas):
	with open('%s\\%s' %(getcwd(), name), 'a') as ef:
		for case in datas:
			for d in case:
				ef.writelines('%s\n' %(str(d)))

	print('\t\t[>] Files created in:')
	print('\t\t\t|> %s\\%s' %(getcwd(), name))

class Line:
	def __init__(self, li):
		self.li = li

	def RegIP(self):
		return findall(r'\b(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b', self.li)
		
	def RegURL(self):
		return findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', self.li)
	
	def RegB64(self):
		return findall(r'(?:[A-Za-z0-9+/]{4})*(?:[A-Za-z0-9+/]{2}==|[A-Za-z0-9+/]{3}=)', self.li)
	
	def RegHexa(self):
		return findall(r'\b[0-9A-F]{2}\b', self.li)

	def RegMails(self):
		return findall(r'(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)', self.li)

	def RegMac(self):
		return findall(r'([a-fA-F0-9]{2}(:[a-fA-F0-9]{2}){5})', self.li)

	def RegPhone(self):
		return findall(r'(?:(?:\+|00)33[\s.-]{0,3}(?:\(0\)[\s.-]{0,3})?|0)[1-9](?:(?:[\s.-]?\d{2}){4}|\d{2}(?:[\s.-]?\d{3}){2})', self.li)


if __name__ == '__main__':
	print("""

		 ___            _ _ _            _    _  
		| . \ ___  ___ | | | | ___  _ _ | | _| | 
		|   // ._>/ . || | | |/ . \| '_>| |/ . | 
		|_\_\\___.\_. ||__/_/ \___/|_|  |_|\___| 
		          <___' 	Developed by Icenuke.


	""")

	if len(argv) >= 2:
		print('\t[+] Start Parsing by Regex!!')

		try:
			lsIP = [['[ IP Parsed ]']]
			lsUrl = [['[ URL Parsed ]']]
			lsb64 = [['[ Base64 Parsed ]']]
			lsHex = [['[ Hexa Parsed ]']]
			lsMail = [['[ Mail Parsed ]']]
			lsMac = [['[ MAC Parsed ]']]
			lsPhone = [['[ Phone Parsed ]']]

			with open(argv[-1], 'r') as fl:
				for l in fl.readlines():
					line = Line(l)

					if '-i' in argv:
						rip = line.RegIP()
						if len(rip) > 0:
							lsIP.append(rip)

					if '-u' in argv:
						ru = line.RegURL()
						if len(ru) > 0:
							lsUrl.append(ru)

					if '-b' in argv:
						rb = line.RegB64()
						if len(rb) > 0:
							lsb64.append(rb)

					if '-x' in argv:
						rh = line.RegHexa()
						if len(rh) > 0:
							lsHex.append(rh)

					if '-m' in argv:
						rm = line.RegMails()
						if len(rm) > 0:
							lsMail.append(rm)

					if '-a' in argv:
						ra = line.RegMac()
						if len(ra) > 0:
							lsMac.append(ra)

					if '-p' in argv:
						rp = line.RegPhone()
						if len(rp) > 0:
							lsPhone.append(rp)


			if len(lsIP) > 1:
				print('\t\t[>] Adding IPs in output file!!')
				Export('IPExport_%s.txt'%(argv[-1]), lsIP)

			if len(lsUrl) > 1:
				print('\t\t[>] Adding URLs in output file!!')
				Export('URLExport_%s.txt'%(argv[-1]), lsUrl)

			if len(lsb64) > 1:
				print('\t\t[>] Adding Base64 in output file!!')
				Export('B64Export_%s.txt'%(argv[-1]), lsb64)

			if len(lsHex) > 1:
				print('\t\t[>] Adding Hexa in output file!!')
				Export('HEXExport_%s.txt'%(argv[-1]), lsHex)

			if len(lsMail) > 1:
				print('\t\t[>] Adding MAILs in output file!!')
				Export('MailExport_%s.txt'%(argv[-1]), lsMail)

			if len(lsMac) > 1:
				print('\t\t[>] Adding MAC in output file!!')
				Export('MACExport_%s.txt'%(argv[-1]), lsMac)

			if len(lsPhone) > 1:
				print('\t\t[>] Adding PHONEs numbers in output file!!')
				Export('PHONEExport_%s.txt'%(argv[-1]), lsPhone)


		except Exception as e:
			print('\t[!] %s' %(e))

	else:
		Helper()


