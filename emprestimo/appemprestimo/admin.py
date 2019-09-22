from django.contrib import admin
from .models import *

# Register your models here.
class AlunoAdmin(admin.ModelAdmin):
    list_display = ('name', 'registration', 'date_birth')

class EmprestimoAdmin(admin.ModelAdmin):
    list_display = ('date_devolution', 'date_withdrawn', 'student','returned')
    filter_horizontal = ['books']
class AutorAdmin(admin.ModelAdmin):
    list_display = ('name', 'last_name')


admin.site.register(Livro)
admin.site.register(Aluno,AlunoAdmin)
admin.site.register(Autor,AutorAdmin)
admin.site.register(Emprestimo,EmprestimoAdmin)
