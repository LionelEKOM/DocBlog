from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=40)
    slug = models.SlugField()
    
    class Meta:
        verbose_name = "Categorie"
        
    def __str__(self):
        return self.name

class BlogPost(models.Model):
    # The User model that the BlogPost is associated with
    # Avec la metho CASCADE si le user qui a creer cet article est supprimer ses articles le seront egalement
    # author = models.ForeignKey(User, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    category = models.ManyToManyField(Category)

    # The title of the BlogPost
    title = models.CharField(max_length=150)

    # The slug of the BlogPost, used for creating a unique URL for the post
    slug = models.SlugField()

    # A boolean indicating whether the BlogPost has been published or not
    published = models.BooleanField(default=False)

    # The date that the BlogPost was published
    date = models.DateField(blank=True, null=True)

    # The content of the BlogPost
    content = models.TextField()

    # A brief description of the BlogPost
    description = models.TextField()
    
    class Meta:
        verbose_name = "Article"
        ordering = ['-date']
        
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
    def publish_string(self):
        if self.published:
            return "l'article est publie"
        return "l'article n'est pas publie"
    

# Exercice sur les models et relation
class Author(models.Model):
    firstname = models.CharField(max_length=150)
    lastname = models.CharField(max_length=150)
    wikipedia = models.URLField(blank=True)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"
    
class Book(models.Model):
    ADVENTURE = "AV"
    THRILLER = "TR"
    FANTASY = "FS"
    ROMANCE = "RM"
    HORROR = "HR"
    SCIENCE_FICTION = "SF"

    GENRES = [
        (ADVENTURE, "Aventure"),
        (THRILLER, "Thriller"),
        (FANTASY, "Fantastique"),
        (ROMANCE, "Romance"),
        (HORROR, "Horreur"),
        (SCIENCE_FICTION, "Science-fiction"),
    ]

    title = models.CharField(max_length=300)
    price = models.FloatField(blank=True, null=True)
    summary = models.TextField(blank=True)
    #Many to one
    author = models.ForeignKey(Author, on_delete=models.CASCADE, blank=True, null=True)
    category = models.CharField(max_length=25, blank=True, choices=GENRES)
    stock = models.IntegerField(default=0)

    def __str__(self):
        return self.title
