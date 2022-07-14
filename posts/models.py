from django.db import models


class Post(models.Model):
    id = models.PositiveBigIntegerField(primary_key=True)
    title = models.CharField(max_length=200, null=False)
    body = models.CharField(max_length=1000, null=True)
    userid = models.PositiveIntegerField(null=False)


