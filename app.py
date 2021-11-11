from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

URL = "https://5000-white-magpie-i9tjavc8.ws-us18.gitpod.io"

vendas = [
    {"id": 1, "name": "Lucas Alixame", "product": "Camiseta Azul - G", "price": 25.00 },
    {"id": 2, "name": "Ana Maria", "product": "Camiseta Rosa - M", "price": 25.00},
]

@app.route('/')
def index():
     """
        Renderizando Tela: INDEX
        Passando variavel: lista(tipo lista de dados)
    """
    return render_template('index.html', lista=vendas)

@app.route('/create')
def create():
    """
        Renderizando Tela: CREATE
    """
    return render_template('create.html')

@app.route('/save', methods=['POST'])  # <form action="/save" method="POST">
def save():
    """
        Pegando Dados do Formulario
    """
    name = request.form['name']          # <input name="name"/>
    product = request.form['product']    # <input name="product"/>
    price = request.form['price']        # <input name="price"/>

    """
        Aplicando REPLACE no preço (trocando , por .)
    """
    price = price.replace(",", ".")

    """
        Identificando ultimo elemento dentro da lista
    """
    ultimo = vendas[-1]

    """
        Moldando Lista e definindo dados
        OBS: Ao definir o 'id' do registro, utilizamos o ultimo elemento da lista somando o valor de seu id + 1
    """
    venda = {"id": ultimo["id"] + 1,"name": name, "product": product, "price": float(price)}

    """
        Adicionando elemento a lista
    """
    vendas.append(venda)

    """
        Redirecionando para a pagina principal
    """
    return redirect(URL + '/')

@app.route('/delete/<id>')
def delete(id):
    index = int(id)

    del vendas[index - 1]

    return redirect(URL + '/')


app.run(debug=True)



# Implementar o DELETE!! (2,0 pontos)
# Implementar uma pesquisa (3,0 pontos)
