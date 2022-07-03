from flask import Flask,jsonify


app = Flask(__name__)

@app.route('/')
def raiz():
    return 'Ola mãe!'


@app.route('/rota2')
def rota2():
    return '<h1>Essa é a segunda rota da aplicação </H1>'

@app.route('/pessoas/<string:nome>/<string:cidade>')
def pessoa(nome,cidade):
    return jsonify({'nome':nome,'cidade':cidade})
        

app.run(debug=True)