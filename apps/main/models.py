from django.db import models


class SiteCategory(models.Model):
    name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Site Categories'


class Site(models.Model):
    category = models.ForeignKey(SiteCategory, on_delete=models.CASCADE)
    date = models.DateField()
    a = models.DecimalField(max_digits=9, decimal_places=2)
    b = models.DecimalField(max_digits=9, decimal_places=2)

    def __str__(self):
        return '%s - %d' % (self.category.name, self.id)
