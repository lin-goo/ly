from django.db import models


class Students(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, null=False)
    gender = models.IntegerField(default=1)
    birthday = models.DateField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(default=None)

    class Meta:
        managed = False
        db_table = "students"
