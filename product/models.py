from django.db import models


class Category(models.Model):
    parent = models.ForeignKey(
        'self', on_delete=models.CASCADE,
        related_name='sub', null=True, blank=True
    )
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.title


class Size(models.Model):
    title = models.CharField(max_length=10)

    def __str__(self):
        return self.title


class Color(models.Model):
    title = models.CharField(max_length=10)

    def __str__(self):
        return self.title


class Product(models.Model):
    categories = models.ManyToManyField(Category, blank=True, related_name="products")
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    discount = models.IntegerField(blank=True, null=True)
    image = models.ImageField(upload_to='products')
    size = models.ManyToManyField(Size, blank=True, related_name='products')
    color = models.ManyToManyField(Color, blank=True, related_name='products')

    def __str__(self):
        return self.title


class Information(models.Model):
    product = models.ForeignKey(
        Product, null=True, on_delete=models.CASCADE, related_name='information'
    )
    text = models.TextField(max_length=200)

    def __str__(self):
        return self.text[:30]
