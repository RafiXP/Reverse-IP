#!/usr/bin/python

import os,sys,random,requests
from termcolor import cprint

def menu():
 print
os.system('clear')
os.system('date')
print ('')
cprint ('     R E V E R S E  I P  L O O K U P','blue')
cprint ('          [ Coded By : RafiXP ]','red')
print ('')
url = input ('[+] Masukan URL Target : ')
print ('')

dm = url
api = "https://api.hackertarget.com/reverseiplookup/?q="

def request_info(url):
 print
request = requests.get(api+dm)
response = request.text
print (response)
print ('')

menu()