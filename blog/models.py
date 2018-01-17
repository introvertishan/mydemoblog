from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Blogdata(models.Model):
    title=models.CharField(max_length=50)
    comment=models.TextField()
    Date_created=models.DateTimeField(auto_now=True,null=True)
    created_by=models.ForeignKey(User,null=True)
    pic=models.FileField(upload_to = 'pic',blank=True, null=True)
    def __str__(self):
        return self.title