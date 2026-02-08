from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, RadioField, SubmitField
from wtforms.validators import DataRequired, NumberRange, InputRequired, ValidationError

class CinepolisForm(FlaskForm):
    nombre = StringField(
        'Nombre',
        validators=[InputRequired(message="El nombre es obligatorio")]
    )

    compradores = IntegerField(
        'Cantidad de compradores',
        validators=[
            InputRequired(message="La cantidad de compradores es obligatoria"),
            NumberRange(min=1, message="Debe haber al menos 1 comprador")
        ]
    )

    boletas = IntegerField(  
        'Cantidad de boletas',
        validators=[
            InputRequired(message="La cantidad de boletas es obligatoria"),
            NumberRange(min=1, message="Debe comprar al menos 1 boleto")
        ]
    )

    cineco = RadioField(  
        'Tarjeta CINECO',
        choices=[('Si', 'Sí'), ('No', 'No')],  
        default='No'
    )
    

    submit = SubmitField('Procesar')