from django.contrib import admin
from .models import AIAuthor, NeuralNetworkType

@admin.register(AIAuthor)
class AIAuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'year')
    search_fields = ('name',)

@admin.register(NeuralNetworkType)
class NeuralNetworkTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
