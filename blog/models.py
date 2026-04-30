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

    conteudo = models.TextField()

    data_criacao = models.DateTimeField(
        auto_now_add=True
    )

    slug = models.SlugField(
        unique=True
    )

    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    likes = models.PositiveIntegerField(
        default=0
    )

    def __str__(self):

        return self.titulo


class Comment(models.Model):

    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments'
    )

    nome = models.CharField(
        max_length=100
    )

    texto = models.TextField()

    data_criacao = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):

        return self.nome