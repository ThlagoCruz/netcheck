import os
import flask
from colorama import *
import sqlite3
import subprocess
import ipaddress
from tkinter import *
import pandas as pd
import numpy as np
import socket
import yaml
import random
import string
import requests
import string
import time
import hashlib

def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')

def colorama_print(text, color):
    colors = {
        'red': Fore.RED,
        'green': Fore.GREEN,
        'yellow': Fore.YELLOW,
        'blue': Fore.BLUE,
        'cyan': Fore.CYAN,
        'magenta': Fore.MAGENTA,
        'white': Fore.WHITE,
    }
    color_code = colors.get(color, Fore.WHITE)
    print(color_code + text + Style.RESET_ALL)

def read_stored_hash():
    with open('configs/cess.bin', 'rb') as file:
        return file.read().decode('utf-8')

# Função para criar um hash SHA-256 da chave
def hash_key(key):
    return hashlib.sha256(key.encode('utf-8')).hexdigest()

# Função para verificar se a chave fornecida é válida
def verify_key(provided_key):
    stored_hash = read_stored_hash()
    hashed_provided_key = hash_key(provided_key)
    return hashed_provided_key == stored_hash

# Função principal para verificação da chave
def verify():
    key = input("Insira a chave de acesso >_")
    if verify_key(key):
        print("ACESSO_PERMITIDO")
        home()
    else:
        print("ACESSO_NEGADO")
        time.sleep(2)
        exit()


def home():
    limpar()
    colorama_print("""
███╗░░██╗███████╗████████╗░█████╗░██╗░░██╗███████╗░█████╗░██╗░░██╗
████╗░██║██╔════╝╚══██╔══╝██╔══██╗██║░░██║██╔════╝██╔══██╗██║░██╔╝
██╔██╗██║█████╗░░░░░██║░░░██║░░╚═╝███████║█████╗░░██║░░╚═╝█████═╝░
██║╚████║██╔══╝░░░░░██║░░░██║░░██╗██╔══██║██╔══╝░░██║░░██╗██╔═██╗░
██║░╚███║███████╗░░░██║░░░╚█████╔╝██║░░██║███████╗╚█████╔╝██║░╚██╗
╚═╝░░╚══╝╚══════╝░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝╚══════╝░╚════╝░╚═╝░░╚═╝
=================================================================================
Selecione o tipo de teste(digite na forma 01, 02, 03...):
[01]sql injection          [02]ping

[03]tráfego de rede        [04]nmap

[05]bruteforce             [06]certificados SSL/TLS

[07]logs                   [00]sair         """, 'magenta')

opcao = input("Opção >_ ")

match opcao:
    case '01':
        sql_injection()
        break
    case '02':
        ping()
        break
    case '03':
        traffic_rede()
        break
    case '04':
        nmap()
        break
    case '05':
        bruteforce()
        break
    case '06':
        certificados_ssl_tls()
        break
    case '07':
        logs()
        break
    case '00':
        sair()
        break
    case _:
        print("Opção inválida!")
        time.sleep(2)
        home()

def ping():
    ip = input("Insira o IP para realizar o ping >_ ")
    subprocess.run(['ping', '-n', '1', ip], capture_output=True)
    home()

def sql_injection():
    param = input("Insira os parâmetros >_")
    subprocess.run(['sqlmap', param ])
    home()

def nmap():
    ip = input("Insira o IP para realizar o nmap >_ ")
    subprocess.run(['nmap', ip], capture_output=True)
    home()

def traffic_rede():
    ip = input("Insira o IP para realizar o tráfego de rede >_ ")
    subprocess.run(['netstat', '-n', '-o', '-i', ip], capture_output=True)
    home()

def bruteforce():
    ip = input("Insira o IP para realizar o bruteforce >_ ")
    username = input("Insira o nome de usuário >_ ")
    password_file = input("Insira o caminho para o arquivo de senhas >_ ")
    subprocess.run(['sources/thc-hydra-windows-v9.1/hydra.exe', '-l', username, '-P', password_file, 'http-get', ip], capture_output=True)
    home()

def certificados_ssl_tls():
    ip = input("Insira o IP para verificar os certificados SSL/TLS (inclua a porta, ex: example.com:443) >_ ")
    subprocess.run(['sources/OpenSSL-Win64/bin/openssl.exe', 's_client', '-connect', ip], capture_output=True)
    home()

def logs():
    ip = input("Insira o IP para visualizar os logs >_ ")
    subprocess.run(['tail', '-f', 'logs/' + ip + '.log'], capture_output=True)
    home()

def sair():
    colorama_print("Saindo do NetCheck...", 'red')
    time.sleep(1)
    exit()

verify()