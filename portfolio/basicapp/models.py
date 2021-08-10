from django.db import models

# Create your models here.
class Project(models.Model):
    name=models.TextField(max_length=None)
    short_desc=models.TextField(max_length=None)
    long_desc=models.TextField(max_length=None)
    report_link=models.TextField(max_length=None)
    sem=models.TextField(max_length=None)
    image=models.ImageField(upload_to='media',blank=True)
    rank=models.PositiveIntegerField()
    google_drive_link=models.TextField(max_length=None)
    def __str__(self):
        return str(self.rank)+":"+self.name
