from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    tittle = "IDGGS804 - Intro Flask"
    listado = ['Juan', 'Ana', 'Pedro']
    return render_template('index.html', tittle=tittle, listado=listado)

@app.route('/hola')
def func():
    return 'hola mundo - hola nuvs'

@app.route('/saludo1')
def saludo1():
    return render_template('saludo1.html')

@app.route('/saludo2')
def saludo2():
    return render_template('saludo2.html')

@app.route('/user/<string:user>')
def u(user):
    return f'hola, {user}!'

@app.route('/numero/<int:n>')
def num(n):
    return f'tu numero es: {n}'

@app.route('/user/<int:id>/<string:username>')
def username(id, username):
    return f'<h1>hola, {username}!, tu ID es: {id}</h1>'

@app.route('/suma/<float:n1>/<float:n2>')
def suma(n1, n2):
    return f'<h1>La suma es: {n1+n2}</h1>'

@app.route('/default')
@app.route('/default/<string:parm>')
def func2(param = "juan"):
    return f'<h1>hola {param}</h1>'

@app.route('/operas')
def operas():
    return """
    <form>
    <label for="name>Name</label>
    <input type="text" id="name" name="name" required>
    </br>
    <labelfor="name">apaterno:</label>
    <input type="text" id="name" name="name" required>
    </br>
    <input type="submit" value="Submit">
    </form>
    """

@app.route('/OperasBas')
def operasbas():
    return render_template('operasBas.html')

@app.route('/resultado', methods=['GET', 'POST'])
def resul1():
    n1 = request.form.get('num1')
    n2 = request.form.get('num2')
    return f'<h1>la suma es: {float(n1)+float(n2)}</h1>'

if __name__ == '__main__':
    app.run(debug = True)
