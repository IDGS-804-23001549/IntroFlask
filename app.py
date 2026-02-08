from flask import Flask, render_template, request
import math
import forms
import cinepolisForm
import pizzeriaForm
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

@app.route('/cinepolis', methods=['GET', 'POST'])
def cinepolis():
    form = cinepolisForm.CinepolisForm()
    res = 0
    error = None
    
    # Si el método es POST y el formulario pasa las validaciones de WTForms
    if request.method == 'POST' and form.validate():
        nombre = form.nombre.data
        cant_compradores = form.compradores.data
        cant_boletas = form.boletas.data
        tarjeta_cineco = form.cineco.data
        
        # Validación de límite de boletos
        max_boletas = cant_compradores * 7
        if cant_boletas > max_boletas:
            error = f"No puedes comprar más de {max_boletas} boletas por comprador."
        else:
            # --- SOLO LA LÓGICA DE CÁLCULO SI NO HAY ERROR ---
            precio_base = 12000 
            subtotal = cant_boletas * precio_base

            if cant_boletas > 5:
                subtotal *= 0.85  # 15% de descuento 
            elif 3 <= cant_boletas <= 5:
                subtotal *= 0.90  # 10% de descuento 
            
            if tarjeta_cineco == 'Si':
                subtotal *= 0.90  # 10% adicional 
            
            res = subtotal
                
    return render_template('cinepolis.html', form=form, res=res, error=error)

@app.route('/pizzeria', methods=['GET', 'POST'])
def pizzeria():
    form = pizzeriaForm.PizzeriaForm()
    res = 0
    nombre_cliente = ""
    tamanio_txt = ""
    ingredientes_txt = ""
    
    if request.method == 'POST' and form.validate():
        nombre_cliente = form.nombre.data
        precio_tamanio = int(form.tamanio.data)
        
        opciones_tamanio = dict(form.tamanio.choices)
        tamanio_txt = opciones_tamanio.get(form.tamanio.data)

        opciones_ing = dict(form.ingredientes.choices)
        seleccionados = [opciones_ing.get(i) for i in form.ingredientes.data]
        ingredientes_txt = ", ".join(seleccionados) if seleccionados else "Sin ingredientes extra"
        
        cant_ingredientes = len(form.ingredientes.data)
        num_pizzas = form.num_pizzas.data
        
        costo_por_pizza = precio_tamanio + (cant_ingredientes * 10)
        res = costo_por_pizza * num_pizzas
        
    return render_template('pizzeria.html', form=form, res=res, nombre=nombre_cliente, tamanio=tamanio_txt, ingredientes=ingredientes_txt)

if __name__ == '__main__':
    app.run(debug = True)
