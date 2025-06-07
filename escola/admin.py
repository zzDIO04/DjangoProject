from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario, Disciplina, Nota

class UsuarioAdmin(UserAdmin):
    list_display = ('username', 'email', 'tipo', 'matricula', 'is_staff')
    list_filter = ('tipo', 'is_staff', 'is_superuser')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Informações Pessoais', {'fields': ('first_name', 'last_name', 'email')}),
        ('Permissões', {'fields': ('tipo', 'matricula', 'is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'tipo', 'matricula', 'password1', 'password2'),
        }),
    )
    search_fields = ('username', 'email', 'matricula')
    ordering = ('username',)

class DisciplinaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'codigo', 'professor')
    search_fields = ('nome', 'codigo')
    list_filter = ('professor',)
    filter_horizontal = ('alunos',)

class NotaAdmin(admin.ModelAdmin):
    list_display = ('aluno', 'disciplina', 'valor', 'data')
    list_filter = ('disciplina', 'data')
    search_fields = ('aluno__username', 'disciplina__nome')
    date_hierarchy = 'data'

admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Disciplina, DisciplinaAdmin)
admin.site.register(Nota, NotaAdmin) 