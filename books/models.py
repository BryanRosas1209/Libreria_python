from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=100)
    def __str__(self): return self.title

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    # Cambiamos CharField por ImageField para poder subir archivos
    image = models.ImageField(upload_to='books_covers/') 
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title