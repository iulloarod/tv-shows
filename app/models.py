from django.db import models

class Show(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=99)
    network = models.CharField(max_length=44)
    rel_date = models.DateField()
    desc = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)