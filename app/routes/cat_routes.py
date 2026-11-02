from flask import Blueprint, render_template, redirect, url_for, flash, request
from app.models import db, Categoria
from app.forms import CategoriaForm

cat_bp = Blueprint('categorias', __name__)

@cat_bp.route('/', methods=['GET', 'POST'])
def listar():
    form = CategoriaForm()
    if form.validate_on_submit():
        nueva_cat = Categoria(nombre=form.nombre.data)
        db.session.add(nueva_cat)
        db.session.commit()
        flash('Categoría creada exitosamente.', 'success')
        return redirect(url_for('categorias.listar'))
    
    categorias = Categoria.query.all()
    return render_template('categorias/listar.html', categorias=categorias, form=form)

@cat_bp.route('/eliminar/<int:id>')
def eliminar(id):
    categoria = Categoria.query.get_or_404(id)
    db.session.delete(categoria)
    db.session.commit()
    flash('Categoría eliminada correctamente.', 'info')
    return redirect(url_for('categorias.listar'))