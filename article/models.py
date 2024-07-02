from django.db import models



class Article(models.Model):
    author = models.ForeignKey("auth.user", on_delete=models.CASCADE,verbose_name="Author")
    title = models.CharField(max_length=50, verbose_name="Title")
    content = models.TextField(verbose_name="Content")
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="Tarih") 
    def __str__(self):
        return self.title
    

# Create your models here.
