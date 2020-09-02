from django.db import models
from KeenEar import settings


class Library(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField("Name", max_length=50, null=True, blank=True)
    description = models.CharField("Description", max_length=300, null=True, blank=True)
    date = models.DateField("Date", auto_now_add=True, null=True)

    def __str__(self):
        return self.name


class Recording(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    library = models.ForeignKey(Library, on_delete=models.CASCADE, related_name='recordings', related_query_name='recording')
    name = models.CharField("Name", max_length=50, null=True, blank=True)
    description = models.CharField("Description", max_length=300, null=True, blank=True)
    date = models.DateField("Date", auto_now_add=True, null=True)
    file = models.FileField("File", upload_to='recordings/')

    def __str__(self):
        return self.name
