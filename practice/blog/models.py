from django.db import models
<<<<<<< HEAD
# from django.conf import settings

class Blog(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return self.title
=======

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()

    def __str__(self):
        return self.title
>>>>>>> 7b4a247334409ecc4f201fd6c81ff925389d25b6
