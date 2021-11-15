
# Create your models here.
from django.db import models
from django.db.models.fields import NullBooleanField

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    desc = models.TextField()
    date = models.DateField()

    def _str_(self):
        return self.name


class Post(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=225)
    header_imgage = models.ImageField(null=True, blank=True, upload_to="images/")
    content = models.TextField()
    author = models.CharField(max_length=13)
    slug = models.CharField(max_length=130)
    timeStamp = models.DateTimeField(blank=True)

    def _str_(self):
        return self.title + 'by' + self.author