import os
from dotenv import load_dotenv

load_dotenv()

usuario = os.getenv("DB_USER")
senha = os.getenv("DB_PASSWORD")

if senha == "senha_super_secreta_123":
    print("Login bem-sucedido! Conectado usando credenciais protegidas pelo .env.")
else:
    print("Falha na autenticação.")