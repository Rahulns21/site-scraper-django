from django.db import models

class Link(models.Model):

    def __str__(self) -> str:
        return str(self.name) if self.name is not None else 'No Name Provided'

    address = models.CharField(max_length=1000, null=True, blank=True)
    name = models.CharField(max_length=1000, null=True, blank=True)
