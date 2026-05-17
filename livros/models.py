from django.db import models

class Autor(models.Model):
    nome = models.CharField(max_length=100)
    nacionalidade = models.CharField(max_length=50)

    def __str__(self):
        return self.nome


class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Livro(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    ano_publicacao = models.IntegerField()
    quantidade = models.IntegerField()

    autor = models.ForeignKey(
        Autor,
        on_delete=models.CASCADE
    )

    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.titulo
    
capa = models.ImageField(
    upload_to='capas/',
    blank=True,
    null=True
)
