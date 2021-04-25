from django.contrib import admin
from . import models
# Register your models here.
@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    fields = ('title','category','apodo','excerpt','content','slug','published','author','status',)
    list_display = ('title','id','status','author')
  

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    fields = ('name', )
    list_display = ('name',)
