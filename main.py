from fastapi import FastAPI
from services.sync_master import sync_reparaciones
from services.trello_service import TrelloService

app = FastAPI()

# ------------ ROOT ------------
@app.get("/")
def root():
    return {"status": "ok", "service": "Trello Sync API"}


# ------------ EXISTENTE: ODOO → TRELLO ------------
@app.post("/sync/odoo-to-trello")
def sync_odoo():
    return sync_reparaciones()


# ------------ NUEVO: CREAR TARJETA EN TRELLO ------------
@app.post("/trello/create-card")
def create_card(payload: dict):
    title = payload.get("title")
    desc = payload.get("description")
    list_id = payload.get("list_id")

    if not all([title, desc, list_id]):
        return {"error": "title, description y list_id son obligatorios"}

    trello = TrelloService()
    result = trello.create_card(
        title=title,
        description=desc,
        list_id=list_id
    )
    return result


# ------------ NUEVO: LISTAR LISTAS DE UN TABLERO ------------
@app.get("/trello/lists/{board_id}")
def get_lists(board_id: str):
    trello = TrelloService()
    return trello.get_board_lists(board_id)
