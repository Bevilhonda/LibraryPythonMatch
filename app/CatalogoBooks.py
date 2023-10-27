class CatalogoBook:

    def __init__(self):
        self.catalogo = []

    def cadastrar_livro(self, livro):
        self.catalogo.append(livro)

    def pesquisar_livros_por_titulo(self, titulo):
        resultados = []
        for livro in self.catalogo:
            if titulo.lower() in livro.titulo.lower():
                resultados.append(livro)
        return resultados

    def pesquisar_livros_por_autor(self, autor):
        resultados = []
        for livro in self.catalogo:
            if autor.lower() in livro.autor.lower():
                resultados.append(livro)
        return resultados