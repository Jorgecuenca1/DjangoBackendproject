from django.contrib import admin
from . import models
# Register your models here.
@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    fields = ('name','category','apodo','adress','nit','phone','published','author','status',)
    list_display = ('name','id','status','author')
  

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    fields = ('name', )
    list_display = ('name',)
