from flask import render_template, Flask
app = Flask('')


'''
Escreva os Controllers neste arquivo
'''
@app.route('/')
def pagina_principal():
    return render_template('pagina_principal.html')

@app.route('/sobre')
def sobre():
    return render_template('sobre.html')

@app.route('/contato')
def contato():
    return render_template('contato.html')

@app.route('/1905370')
def samuel():
    return render_template('samuel.html')

@app.route('/1802042')
def adalto():
    return render_template('adalto.html')

@app.route('/1905136')
def pedro():
    return render_template('pedro.html')
