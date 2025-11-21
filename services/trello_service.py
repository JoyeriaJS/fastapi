import os
import requests

class TrelloService:
    def __init__(self):
        self.key = os.getenv("TRELLO_KEY")
        self.token = os.getenv("TRELLO_TOKEN")
        self.base_url = "https://api.trello.com/1"

    def create_card(self, title, description, list_id):
        url = f"{self.base_url}/cards"
        params = {
            "name": title,
            "desc": description,
            "idList": list_id,
            "key": self.key,
            "token": self.token
        }
        response = requests.post(url, params=params)
        return response.json()

    def get_lists(self, board_id):
        url = f"{self.base_url}/boards/{board_id}/lists"
        params = {
            "key": self.key,
            "token": self.token
        }
        response = requests.get(url, params=params)
        return response.json()
