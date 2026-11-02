from flask import Blueprint, render_template, redirect, url_for, flash, request
from app.models import db, Usuario
from app.forms import UsuarioForm
from werkzeug.security import generate_password_hash

user_bp = Blueprint('usuarios', __name__)

@user_bp.route('/', methods=['GET', 'POST'])
def listar():
    form = UsuarioForm()
    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data)
        nuevo_usuario = Usuario(
            nombre=form.nombre.data,
            email=form.email.data,
            password=hashed_password
        )
        db.session.add(nuevo_usuario)
        db.session.commit()
        flash('Usuario registrado exitosamente.', 'success')
        return redirect(url_for('usuarios.listar'))
    
    usuarios = Usuario.query.all()
    return render_template('usuarios/listar.html', usuarios=usuarios, form=form)

@user_bp.route('/eliminar/<int:id>')
def eliminar(id):
    usuario = Usuario.query.get_or_404(id)
    db.session.delete(usuario)
    db.session.commit()
    flash('Usuario eliminado correctamente.', 'info')
    return redirect(url_for('usuarios.listar'))