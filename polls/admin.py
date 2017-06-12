from django.contrib import admin
from .models import Question, Choice, Name
class NameAdmin(admin.ModelAdmin):
	list_display = ('Your_name','Age', 'Email') 
admin.site.register(Question)
admin.site.register(Name)
# Register your models here.
