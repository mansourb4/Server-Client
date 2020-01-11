import socket

def client() :
    
    connexion_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Je créer le client
    connexion_client.connect(('localhost', 12900)) #Je connecte le client

client()