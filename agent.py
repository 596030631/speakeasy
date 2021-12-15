import requests, json, time
from IPython.display import Javascript

url = "https://speakeasy.ifi.uzh.ch"
username="bot_393"
password="9uiyFFWgF_"


def start_agent():
    print("start agent")
    r = requests.post(url=url + "/api/login", json={"username": username, "password": password}).json()
    print(r)
    sessionToken = r['sessionToken']

if __name__ == '__main__':
    start_agent()