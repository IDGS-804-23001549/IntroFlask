from wtforms import Form

from wtforms import StringField, PasswordField, EmailField, BooleanField, IntegerField, RadioField
from wtforms import validators

class UserForm(Form):
    matricula = IntegerField("Matricula", [
        validators.DataRequired(message = "El campo es requerido")
    ])
    nombre = StringField("Nombre", [
        validators.DataRequired(message = "El campo es requerido")
    ])
    apellido = StringField("Apellido", [
        validators.DataRequired(message = "El campo es requerido")
    ])
    correo = EmailField("correo", [
        validators.Email(message = "Ingrese correo valido")
    ])

class CinepolisForm(Form):
    nombre = StringField("Nombre", [
        validators.DataRequired(message="El nombre es requerido")
    ])
    compradores = IntegerField("Cantidad Compradores", [
        validators.DataRequired(message="Ingrese número de compradores")
    ])
    boletas = IntegerField("Cantidad de Boletas", [
        validators.DataRequired(message="Ingrese cantidad de boletas")
    ])
    # Usamos RadioField para que WTForms gestione la opción de la tarjeta
    cineco = RadioField('Tarjeta Cineco', choices=[('Si','Sí'),('No','No')], default='Si')