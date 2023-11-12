import requests

def obtenir_jeu_de_mot():
    url = "https://api.punapi.com/random"
    reponse = requests.get(url)
    if reponse.status_code == 200:
        jeu_de_mot = reponse.json()["content"]
        return jeu_de_mot
    else:
        return "Échec de récupération du jeu de mot"

if __name__ == "__main__":
    jeu_de_mot = obtenir_jeu_de_mot()
    print("Jeu de mot du jour :", jeu_de_mot)
