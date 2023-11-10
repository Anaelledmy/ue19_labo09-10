import requests

def get_pun():
    url = "https://api.punapi.com/random"
    response = requests.get(url)
    
    if response.status_code == 200:
        pun_data = response.json()
        return pun_data.get('content')
    else:
        return "Failed to fetch pun."

if __name__ == "__main__":
    pun = get_pun()
    print("Pun of the day:", pun)

    
