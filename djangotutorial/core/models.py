from django.db import models

class AIAuthor(models.Model):
    name = models.CharField(max_length=200)
    definition = models.TextField()
    year = models.CharField(max_length=50)
    
    class Meta:
        verbose_name = "Autor de IA"
        verbose_name_plural = "Autores de IA"
    
    def __str__(self):
        return self.name


class NeuralNetworkType(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    use_case = models.TextField()
    icon = models.CharField(max_length=100, default='network')
    
    class Meta:
        verbose_name = "Tipo de Red Neuronal"
        verbose_name_plural = "Tipos de Redes Neuronales"
    
    def __str__(self):
        return self.name

