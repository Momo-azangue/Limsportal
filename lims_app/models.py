from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class reader(models.Model):

    reference_id = models.CharField(max_length=200, unique=True)
    reader_name = models.CharField(max_length=200)
    reader_contact = models.CharField(max_length=200)
    reader_address = models.TextField()
    active = models.BooleanField(default=True)
    mybag = models.ManyToManyField('book', related_name='readers', blank=True)
    def __str__(self):
        return self.reader_name


# Creation du modèle livre

class book(models.Model):
    titre = models.CharField(max_length=255)
    auteur = models.CharField(max_length=100)
    annee_publication = models.IntegerField()
    isbn = models.CharField(max_length=13, unique=True)
    categorie = models.CharField(max_length=100)
    disponibilite = models.BooleanField(default=True)
    nombre_exemplaires = models.PositiveIntegerField(default=1)  # Ajout de l'attribut

    def __str__(self):
        return self.titre


# class MyBag(models.Model):
#     reader = models.ForeignKey(User, on_delete=models.CASCADE, related_name="carts")
#     books = models.ForeignKey(book, on_delete=models.CASCADE)
#     quantity = models.PositiveIntegerField(default=1)






# class MyBagItem(models.Model):
#     book = models.ForeignKey(book, on_delete=models.SET_NULL, null=True, blank= True)
#     mybag = models.ForeignKey(MyBag, on_delete=models.CASCADE, related_name="mybagitem")







# class mybag(models.Model):
#     reader =models.CharField(max_length=200)
#     reference_id = models.CharField(max_length=200, unique=True)
#     name = models.CharField(max_length=200)
#     contact = models.CharField(max_length=200)
#     start_date_time= models.TextField()
#     return_date_time = models.TextField()
#
#     def __str__(self):
#         return self.start_date_time



class returns(models.Model):
        titre = models.CharField(max_length=255)
        auteur = models.CharField(max_length=100)
        annee_publication = models.IntegerField()
        isbn = models.CharField(max_length=13, unique=True)
        reference_id = models.CharField(max_length=200, unique=True)
        name = models.CharField(max_length=200)
        contact = models.CharField(max_length=200)
        start_date_time = models.TextField()
        return_date_time = models.TextField()

        def __str__(self):
            return self. return_date_time



