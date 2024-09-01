from flask import Flask, render_template
import random
import string
import os
import hashlib

# Configura o aplicativo Flask
app = Flask(__name__)

# Função para gerar uma chave aleatória
def generate_key():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=30))

# Função para criar um hash SHA-256 da chave
def hash_key(key):
    return hashlib.sha256(key.encode('utf-8')).hexdigest()

# Função para salvar o hash da chave em um arquivo binário
def save_key_to_bin(hashed_key):
    with open('configs/cess.bin', 'wb') as f:
        f.write(hashed_key.encode('utf-8'))

# Rota para a página principal
@app.route('/')
def home():
    key = generate_key()
    hashed_key = hash_key(key)
    save_key_to_bin(hashed_key)
    return render_template('index.html', key=key)

# Executa o servidor Flask
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
