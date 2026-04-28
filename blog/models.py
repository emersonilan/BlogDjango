from django.db import models


class Categoria(models.Model):

    nome = models.CharField(
        max_length=100
    )

    def __str__(self):
        return self.nome


class Post(models.Model):

    titulo = models.CharField(
        max_length=200
    )

    slug = models.SlugField(
        blank=True
    )

    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.CASCADE,
        related_name='posts'
    )

    conteudo = models.TextField()

    data_criacao = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.titulo