from django.db import models


class Records(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.IntegerField(null=False)
    category_type = models.CharField(max_length=255, null=False)
    category_content = models.CharField(max_length=255, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(default=None)

    class Meta:
        managed = False
        db_table = "records"
