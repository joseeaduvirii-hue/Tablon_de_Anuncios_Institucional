from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import current_user  # <-- 1. Importa current_user aquí
from app.models import db, Anuncio, Categoria
from app.forms import AnuncioForm

post_bp = Blueprint('anuncios', __name__)

@post_bp.route('/', methods=['GET', 'POST'])
def listar():
    form = AnuncioForm()
    # Cargar las opciones de categorías en el selector desplegable
    form.categoria_id.choices = [(c.id, c.nombre) for c in Categoria.query.all()]
    
    if form.validate_on_submit():
        nuevo_anuncio = Anuncio(
            titulo=form.titulo.data,
            descripcion=form.descripcion.data,
            categoria_id=form.categoria_id.data,
            usuario_id=current_user.id  # <-- 2. Usa el ID del usuario autenticado actualmente
        )
        db.session.add(nuevo_anuncio)
        db.session.commit()
        flash('Anuncio publicado exitosamente.', 'success')
        return redirect(url_for('anuncios.listar'))
    
    anuncios = Anuncio.query.all()
    return render_template('anuncios/listar.html', anuncios=anuncios, form=form)

@post_bp.route('/eliminar/<int:id>')
def eliminar(id):
    anuncio = Anuncio.query.get_or_404(id)
    db.session.delete(anuncio)
    db.session.commit()
    flash('Anuncio eliminado correctamente.', 'info')
    return redirect(url_for('anuncios.listar'))