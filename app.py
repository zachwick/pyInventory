"""
" pyInventory API
"
" Copyright 2013 ZachWick <zach@zachwick.com>
"
" Licensed under the terms of the AGPLv3
"
"""
import web
import model
import json

### URL mapping/routing
urls = (
    '/',            'Index',
    '/items/(\d+)', 'Items',
    '/items/',      'Items'
)

### Templates
render = web.template.render("templates",base="base")

class Index:
    def GET(self):
        """ Show the base index.html page """
        return render.index();

class Items:
    def GET(self):
        """ GET all items """
        self.items = model.get_items()
        data = []
        for item in self.items:
            data.append({
                "name": item.name,
                "description": item.description,
                "id": item.id,
                "quantity": item.quantity,
                "purchase_price": item.purchase_price,
                "sale_price": item.sale_price
            })

        web.header("Content-Type","application/json")
        web.header("Cache-Control","no-cache")
        return json.dumps(data)

    def POST(self):
        """ Recieved a POST request, so adding a new item """
        new_id = model.new_item(web.input());
        data = [{
            "name": web.input()['name'],
            "description": web.input()['description'],
            "quantity": web.input()['quantity'],
            "purchase_price": web.input()['purchase_price'],
            "sale_price": web.input()['sale_price'],
            "id": new_id
        }]
        web.header("Content-Type","application/json")
        web.header("Cache-Control","no-cache")
        return json.dumps(data)

    def PUT(self):
        """ Recieved a PUT request, so updating an existing item """
        model.update_item(web.input())
        data = [{
            "name": web.input()['name'],
            "description": web.input()['description'],
            "quantity": web.input()['quantity'],
            "purchase_price": web.input()['purchase_price'],
            "sale_price": web.input()['sale_price'],
            "id": web.input()['id']
        }]
    
    def DELETE(self,id):
        """ Recieved an OPTIONS request, so delete an exising item with id """
        model.delete_item(id)

app = web.application(urls, globals())

if __name__ == '__main__':
    app.run()
