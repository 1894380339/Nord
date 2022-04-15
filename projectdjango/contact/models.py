from django.db import models

# Create your models here.
from django.utils import timezone
# Create your models here.
class md_contact(models.Model):
    name = models.CharField(max_length=20, blank=False, null=False)
    mail = models.EmailField(max_length=254,blank=False, null=False)
    content = models.CharField(max_length=1000, blank=False, null=False)
    time = models.DateTimeField(default=timezone.datetime.now())
    def __str__(self):
        return self.mail