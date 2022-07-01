from flask import Flask


app = Flask(__name__)

@app.route('/')
def raiz():
    return 'Ola mãe!'


@app.route('/rota2')
def rota2():
    return '<h1>Essa é a segunda rota da aplicação </H1>'
app.run()