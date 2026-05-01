from django.contrib import admin

from .models import (
    Post,
    Categoria,
    Comment
)


admin.site.register(Post)

admin.site.register(Categoria)

admin.site.register(Comment)