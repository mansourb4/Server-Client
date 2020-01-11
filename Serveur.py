import socket

def serveur() :
    
    principale = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Je construis le socket
    principale.bind(('', 12801)) #Je connecte le socket
    principale.listen(5) #Je fais écouter le socket
    connexion_avec_client, infos_connexion = principale.accept() #J'attend qu'un client se connecte ()
    print(infos_connexion)
    connexion_avec_client.send(b"Je viens d'accepter la connexion") #J'envoi un message au client
    
serveur()