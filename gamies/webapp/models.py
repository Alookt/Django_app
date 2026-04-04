from django.db import models

# Create your models here.
class Book(models.Model):
    id = models.BigAutoField(primary_key=True)
    Book_title = models.CharField("Title of the book",max_length=30)
    summary = models.TextField(blank=True, help_text="A short story about the story")
    manuscript = models.FileField(upload_to="books/manuscripts/")
    cover = models.ImageField(upload_to="books/covers/", blank=True, null=True)
    pages = models.CharField(max_length=80,default=8)
    author = models.CharField(max_length=80,default="John")
    author_id = models.IntegerField(default=0) 
    published = models.DateField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.Book_title
    


