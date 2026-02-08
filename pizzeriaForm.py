from flask_wtf import FlaskForm
from wtforms import StringField, RadioField, IntegerField, SelectMultipleField, SubmitField, widgets
from wtforms.validators import DataRequired, InputRequired

class PizzeriaForm(FlaskForm): 
    nombre = StringField("Nombre completo", validators=[InputRequired(message="El nombre es requerido")])
    direccion = StringField("Dirección", validators=[InputRequired(message="La dirección es requerida")])
    telefono = StringField("Teléfono", validators=[InputRequired(message="El teléfono es requerido")])
    
    tamanio = RadioField("Tamaño", choices=[
        ('40', 'Chica ($40)'), 
        ('80', 'Mediana ($80)'), 
        ('120', 'Grande ($120)')
    ], validators=[DataRequired()])

    ingredientes = SelectMultipleField("Ingredientes ($10 c/u)", 
        choices=[('jamon', 'Jamón'), ('pina', 'Piña'), ('champinones', 'Champiñones')],
        option_widget=widgets.CheckboxInput(),
        widget=widgets.ListWidget(prefix_label=False)
    )
    
    num_pizzas = IntegerField("Número de pizzas", validators=[InputRequired(message="Campo requerido")])
    agregar = SubmitField("Agregar")