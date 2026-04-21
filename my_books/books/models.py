from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=250)

    def __str__(self):
        return self.title

class Book(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='books')
    title = models.CharField(max_length=250)
    author = models.CharField(max_length=250)
    image = models.CharField(max_length=2000)
    # Se utiliza DateTimeField para que los parámetros auto_now funcionen correctamente
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title