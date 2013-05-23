import web

db = web.database(dbn="mysql", db="pyinventory", user="root", passwd="Fritz")

def get_items():
    return db.select("item", order="id")

def new_item(webInput):
    new_id = db.insert("item",
                       name=webInput['name'],
                       description=webInput['description'],
                       quantity=webInput['quantity'],
                       purchase_price=webInput['purchase_price'],
                       sale_price=webInput['sale_price'],
                       vars=locals())
    return new_id

def update_item(webInput):
    name = webInput['name']
    description = webInput['description']
    quantity = webInput['quantity']
    purchase_price = webInput['purchase_price']
    sale_price = webInput['sale_price']
    db.update("item",where="item.id = $webInput['id']",vars=locals())

def delete_item(id):
    db.delete("item", where="id=$id", vars=locals())
