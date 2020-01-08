from django.db import models

class entry(models.Model):
    text=models.TextField()
    date_posted=models.DateTimeField(auto_now_add=True)


    