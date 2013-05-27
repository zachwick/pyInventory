import web

db = web.database(dbn="mysql", db="pyinventory", user="root", passwd="Fritz")

def get_items():
    return db.select("item", order="id")

def new_item(data):
    name = data['name']
    description = data['description']
    quantity = data['quantity']
    purchase_price = data['purchase_price']
    sale_price = data['sale_price']
    location = data['location']
    new_id = db.insert("item",
                       name=name,
                       description=description,
                       quantity=quantity,
                       purchase_price=purchase_price,
                       sale_price=sale_price,
                       location=location)
    return new_id

def update_item(data):
    name = data['name']
    description = data['description']
    quantity = data['quantity']
    purchase_price = data['purchase_price']
    sale_price = data['sale_price'],
    location = data['location'],
    db.update("item",where="item.id = $webInput['id']",vars=locals())

def delete_item(id):
    db.delete("item", where="id=$id", vars=locals())
