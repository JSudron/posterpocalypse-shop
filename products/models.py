from django.db import models


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250)
    description = models.TextField()
    artist = models.CharField(max_length=250, default='')
    price = models.DecimalField(max_digits=6, decimal_places=2, default=1.00)
    image = models.ImageField(upload_to="images", default='')
    quantity = models.IntegerField(default=1.00)
    category = models.ForeignKey(
        "products.ProductCategory",
        blank=True,
        null=True,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name
        


class ProductCategory(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250)
    image = models.ImageField(upload_to="images")

    def __str__(self):
        return self.name

