
import requests
import os

ODOO_URL=os.getenv("ODOO_URL")
ODOO_DB=os.getenv("ODOO_DB")
ODOO_USER=os.getenv("ODOO_USER")
ODOO_PASS=os.getenv("ODOO_PASS")
TRELLO_KEY=os.getenv("TRELLO_KEY")
TRELLO_TOKEN=os.getenv("TRELLO_TOKEN")
TRELLO_LIST_ID=os.getenv("TRELLO_LIST_ID")

import xmlrpc.client

def odoo_connect():
    common=xmlrpc.client.ServerProxy(f"{ODOO_URL}/xmlrpc/2/common")
    uid=common.authenticate(ODOO_DB, ODOO_USER, ODOO_PASS,{})
    models=xmlrpc.client.ServerProxy(f"{ODOO_URL}/xmlrpc/2/object")
    return uid,models

def sync_reparaciones():
    uid,models=odoo_connect()
    recs=models.execute_kw(ODOO_DB,uid,ODOO_PASS,"joyeria.reparacion","search_read",[[]],{"fields":["id","name","descripcion"]})
    created=[]
    for r in recs:
        name=r.get("name","")
        desc=r.get("descripcion","")
        requests.post(f"https://api.trello.com/1/cards",
            params={
                "idList":TRELLO_LIST_ID,
                "key":TRELLO_KEY,
                "token":TRELLO_TOKEN,
                "name":name,
                "desc":desc
            })
        created.append(name)
    return {"synced":created}
