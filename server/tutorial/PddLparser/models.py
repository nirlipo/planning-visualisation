from django.db import models

# Create your models here.
class PDDL(models.Model):
    name = models.TextField()
    filetype = models.TextField()
    file = models.FileField(default="")

    class Meta:
        db_table = "PDDL"
