
from fastapi import FastAPI
from services.sync_master import sync_reparaciones

app = FastAPI()

@app.get("/")
def root():
    return {"status":"ok"}

@app.post("/sync/odoo-to-trello")
def sync_odoo():
    return sync_reparaciones()
