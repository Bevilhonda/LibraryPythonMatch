from flask import Flask, render_template, request, redirect, url_for

from Library.app.Book import Book
from Library.app.CatalogoBooks import CatalogoBook
from Library.app.validation import validar_numero_inteiro_maior_que_zero

app = Flask(__name__)
catalogo = CatalogoBook()


@app.route('/')
def index():
    return render_template('index.html', catalogo=catalogo.catalogo)


@app.route('/cadastrar_livro', methods=['GET', 'POST'])
def cadastrar_livro():
    if request.method == 'POST':
        titulo = request.form['titulo']
        autor = request.form['autor']
        exemplares_disponiveis = request.form['exemplares_disponiveis']

        exemplares_disponiveis = validar_numero_inteiro_maior_que_zero(exemplares_disponiveis)

        if exemplares_disponiveis is not None:
            livro = Book(titulo, autor, exemplares_disponiveis)
            catalogo.cadastrar_livro(livro)
    return redirect(url_for('index'))


@app.route('/pesquisar_por_titulo', methods=['POST'])
def pesquisar_por_titulo():
    titulo = request.form['titulo']
    resultados = catalogo.pesquisar_livros_por_titulo(titulo)
    return render_template('resultados.html', resultados=resultados)


@app.route('/pesquisar_por_autor', methods=['POST'])
def pesquisar_por_autor():
    autor = request.form['autor']
    resultados = catalogo.pesquisar_livros_por_autor(autor)
    return render_template('resultados.html', resultados=resultados)


if __name__ == '__main__':
    app.run()
