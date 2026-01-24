from flask import Flask, render_template, request
import math
import forms
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
app.secret_key = 'clave_secreta'
csrf = CSRFProtect()

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
@app.route('/default/<string:param>')
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

@app.route('/OperasBas', methods=['GET', 'POST'])
def operasbas():
    res = None
    if request.method =='POST':
        n1 = request.form.get('num1')
        n2 = request.form.get('num2')

        if request.form.get('operacion')=='suma':
            res = float(n1)+float(n2)
        elif request.form.get('operacion') == 'resta':
            res = float(n1)-float(n2)
        elif request.form.get('operacion') == 'multiplicacion':
            res = float(n1)*float(n2)
        elif request.form.get('operacion') == 'division':
            res = float(n1)/float(n2)

    return render_template('operasBas.html', res=res)


@app.route('/resultado', methods=['GET', 'POST'])
def resul1():
    n1 = request.form.get('num1')
    n2 = request.form.get('num2')
    return f'<h1>la suma es: {float(n1)+float(n2)}</h1>'

@app.route('/distancia', methods=['GET', 'POST'])
def distancia():
    res = None
    if request.method == 'POST':
        x1_str = request.form.get('x1')
        y1_str = request.form.get('y1')
        x2_str = request.form.get('x2')
        y2_str = request.form.get('y2')

        x1 = float(x1_str)
        y1 = float(y1_str)
        x2 = float(x2_str)
        y2 = float(y2_str)

        distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
        res = distancia
        
    return render_template('distancia.html', res=res)

@app.route('/alumnos', methods=['GET', 'POST'])
def alumnos():
    mat = 0
    nom = ''
    ape = ''
    email = ''
    alumno_clas = forms.UserForm(request.form)
    if request.method == 'POST' and alumno_clas.validate():
        mat = alumno_clas.matricula.data
        nom = alumno_clas.nombre.data
        ape = alumno_clas.apellido.data
        email = alumno_clas.correo.data
    return render_template('alumnos.html', form=alumno_clas, mat=mat, nom=nom, ape=ape, email=email)

if __name__ == '__main__':
    csrf.init_app(app)
    app.run(debug = True)
