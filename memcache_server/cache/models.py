from django.db import models


# Create your models here.
class Cache(models.Model):
    """
    Cache (key-value)
    """
    key = models.CharField(max_length=250, unique=True, null=False, blank=False, primary_key=True)
    value = models.CharField(max_length=250, null=False, blank=True)
    exptime = models.BigIntegerField(verbose_name="Expiration time", null=False, blank=False)
    bytes_length = models.BigIntegerField(verbose_name="number of bytes", db_column='bytes', null=False, blank=False)

    def __str__(self):
        return f"{self.key}: {self.value}"

    class Meta:
        db_table = "cache"
