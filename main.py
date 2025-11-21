from fastapi import FastAPI
from services.sync_master import sync_reparaciones
from services.trello_service import TrelloService

app = FastAPI()

@app.get("/")
def root():
    return {"status":"ok"}

@app.post("/sync/odoo-to-trello")
def sync_odoo():
    return sync_reparaciones()

@app.post("/trello/create-card")
def create_card(payload: dict):
    title = payload.get("title")
    desc = payload.get("description")
    list_id = payload.get("list_id")

    if not all([title, desc, list_id]):
        return {"error": "Faltan campos: title, description, list_id"}

    service = TrelloService()
    return service.create_card(title, desc, list_id)


@app.get("/trello/lists/{board_id}")
def get_lists(board_id: str):
    service = TrelloService()
    return service.get_lists(board_id)
