from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

URL = "https://5000-white-magpie-i9tjavc8.ws-us18.gitpod.io"

vendas = [
    {"id": 1, "name": "Lucas Alixame", "product": "Camiseta Azul - G", "price": 25.00 },
    {"id": 2, "name": "Ana Maria", "product": "Camiseta Rosa - M", "price": 25.00},
]

@app.route('/')
def index():
    return render_template('index.html', lista=vendas)

@app.route('/create')
def create():
    return render_template('create.html')

@app.route('/save', methods=['POST'])  # <form action="/save" method="POST">
def save():
    name = request.form['name']          # <input name="name"/>
    product = request.form['product']    # <input name="product"/>
    price = request.form['price']        # <input name="price"/>

    price = price.replace(",", ".")

    ultimo = vendas[-1]

    venda = {"id": ultimo["id"] + 1,"name": name, "product": product, "price": float(price)}
    vendas.append(venda)

    return redirect(URL + '/')

@app.route('/delete/<id>')
def delete(id):
    del(vendas[id - 1])

    return redirect(URL + '/')


app.run(debug=True)



# Implementar o DELETE!! (2,0 pontos)
# Implementar uma pesquisa (3,0 pontos)
