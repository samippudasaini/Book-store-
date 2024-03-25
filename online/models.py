from django.db import models

# Create your models here.
class Author(models.Model):
    name=models.CharField(max_length=225)
    email=models.EmailField(max_length=50)
    phone=models.IntegerField()
    image=models.ImageField(upload_to='authors')
    def __str__(self):
        return self.name



class Category(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name
    

class Book(models.Model):
    title=models.CharField(max_length=100)
    author_id=models.ForeignKey(Author, on_delete=models.PROTECT)
    category_id=models.ForeignKey(Category, on_delete=models.PROTECT)
    price=models.IntegerField
    image=models.ImageField(upload_to='books',blank=True ,null=True)
    description=models.CharField(max_length=500,blank=True)
    page=models.IntegerField(default=1)
    
