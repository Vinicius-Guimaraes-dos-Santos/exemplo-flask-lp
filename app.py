from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

URL = "https://scarlet-vicuna-q5ne8wug.ws-us18.gitpod.io"

vendas = [
    {"name": "Lucas Alixame", "product": "Camiseta Azul - G", "price": 25.00 },
    {"name": "Ana Maria", "product": "Camiseta Rosa - M", "price": 25.00},

]

@app.route('/')
def index():
    return render_template('index.html', lista=vendas)

@app.route('/create')
def create():
    return render_template('create.html')

@app.route('/save', methods=['POST'])  # <form action="/save" method="POST">
def save():
    name = str(request.form['name'])    # <input name="name"/>
    product = str(request.form['product'])    # <input name="product"/>
    price = float(request.form['price'])    # <input name="price"/>

    venda = { "name": name, "product": product, "price": price}
    vendas.append(venda)

    return redirect(URL + '/')

app.run(debug=True)


# Implementar o DELETE!! (2,0 pontos)
# Implementar uma pesquisa (3,0 pontos)