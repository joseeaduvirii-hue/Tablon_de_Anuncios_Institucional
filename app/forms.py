from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, SelectField
from wtforms.validators import DataRequired, Length, Email

class CategoriaForm(FlaskForm):
    nombre = StringField('Nombre de la Categoría', validators=[DataRequired(), Length(min=2, max=50)])
    submit = SubmitField('Guardar Categoría')

class AnuncioForm(FlaskForm):
    titulo = StringField('Título del Anuncio', validators=[DataRequired(), Length(min=3, max=100)])
    descripcion = TextAreaField('Descripción', validators=[DataRequired(), Length(min=5, max=500)])
    categoria_id = SelectField('Categoría', coerce=int, validators=[DataRequired()])
    submit = SubmitField('Publicar Anuncio')

class UsuarioForm(FlaskForm):
    nombre = StringField('Nombre', validators=[DataRequired(), Length(min=2, max=100)])
    email = StringField('Correo Electrónico', validators=[DataRequired(), Email()])
    password = PasswordField('Contraseña', validators=[DataRequired(), Length(min=4)])
    submit = SubmitField('Registrar Usuario')

class LoginForm(FlaskForm):
    email = StringField('Correo Electrónico', validators=[DataRequired(), Email()])
    password = PasswordField('Contraseña', validators=[DataRequired()])
    submit = SubmitField('Iniciar Sesión')