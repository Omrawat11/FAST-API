from fastapi import FastAPI 

            # GET -> work in url

app = FastAPI()
@app.get("/") # ('/') -> for redirect home page
def home():
    return{"status":"Hello world"}

@app.get("/display")
def display():
    return{"This is another page..."}

@app.get("/name") # routes
def name():
    return{"Hi i am om "}

            # create a function that loads the json file in read mode.
import json
@app.get('/show')
def show_products():
    with open('products.json','r') as file:
        products = json.load(file) #this is a list where dictionary is stored 
    return products


@app.get('/show/{id}')
def getby_id(id:int):
    with open('products.json','r') as file:
        product = json.load(file)
        for i in product:
             if i['id'] == id:
                 return i 


                # POST -> work in docs
                
with open('products.json','r') as file:
    products = json.load(file)
new_d = {
    'id':9,
    'name':'iphone',
    'category':'mobile',
    'price': 100000,
    'in_stock': True
}
products.append(new_d)
with open('products.json','w') as file:
    json.dump(products,file,indent=4)

            # creating a post route which will add new data in json 
@app.post('/add')
def add_products(Userproduct:dict):
    try:
        with open('products.json') as file:
            Oldproducts = json.load(file)
        Oldproducts.append(Userproduct)

        with open('products.json','w') as file:
            json.dump(Oldproducts, file)
    except Exception as e:
        return{"status":"error","message":str(e)}

            # PUT -> used for replace or update values
@app.put('/update/{id}') 
def update_product(id:int,updateProduct:dict):
        with open('products.json','r') as file:
            products = json.load(file)

        for i in products:
            if i['id'] == id:
                i.update(updateProduct)
        with open('products.json','w') as file:
            json.dump(products, file)


# in dictinoary->  keys is called field , and field have values

        #DELETE 
@app.delete('/delete/{id}')
def delete_item(id:int):
    with open('products.json','r') as file:
        products = json.load(file)
    for i in products:
        if i['id'] == id:
            products.remove(i)
            with open('products.json','w') as file:
                json.dump(products,file) 
            return{'Item deleted'}
    else:
        return{'Item not found'}
    
            # PAGINATION start = (page-1)*limit   ,  end = start + limit 
