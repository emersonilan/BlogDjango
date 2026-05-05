from django.contrib import admin
from django.utils.html import format_html

from .models import (
    Post,
    Categoria,
    Comment
)


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'nome'
    )

    search_fields = (
        'nome',
    )


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'usuario',
        'post',
        'data_criacao'
    )

    search_fields = (
        'usuario__username',
        'texto',
        'post__titulo'
    )

    list_filter = (
        'data_criacao',
    )

    readonly_fields = (
        'data_criacao',
    )


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'titulo',
        'categoria',
        'total_likes_admin',
        'preview_imagem',
        'data_criacao'
    )

    search_fields = (
        'titulo',
        'conteudo',
        'slug'
    )

    list_filter = (
        'categoria',
        'data_criacao'
    )

    prepopulated_fields = {
        'slug': ('titulo',)
    }

    readonly_fields = (
        'preview_imagem_grande',
        'data_criacao'
    )

    fieldsets = (

        (
            'Informações do Post',
            {
                'fields': (
                    'titulo',
                    'slug',
                    'categoria'
                )
            }
        ),

        (
            'Conteúdo',
            {
                'fields': (
                    'conteudo',
                )
            }
        ),

        (
            'Imagem',
            {
                'fields': (
                    'imagem',
                    'preview_imagem_grande'
                )
            }
        ),

        (
            'Engajamento',
            {
                'fields': (
                    'likes',
                    'data_criacao'
                )
            }
        ),

    )

    filter_horizontal = (
        'likes',
    )

    def total_likes_admin(self, obj):

        return obj.total_likes()

    total_likes_admin.short_description = 'Likes'

    def preview_imagem(self, obj):

        if obj.imagem:

            return format_html(
                '<img src="{}" width="70" style="border-radius:10px;" />',
                obj.imagem.url
            )

        return 'Sem imagem'

    preview_imagem.short_description = 'Preview'

    def preview_imagem_grande(self, obj):

        if obj.imagem:

            return format_html(
                '<img src="{}" width="300" style="border-radius:15px;" />',
                obj.imagem.url
            )

        return 'Sem imagem'

    preview_imagem_grande.short_description = 'Imagem Atual'