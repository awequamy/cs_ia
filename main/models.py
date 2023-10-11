from django.db import models
from ckeditor.fields import RichTextField
from django.urls import reverse


class Category(models.Model):
    slug = models.SlugField(primary_key=True, max_length=50)
    title = models.CharField(max_length=50,)
    parent = models.ForeignKey('self', related_name='children', null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        if self.parent:
            return f'{self.parent} -> {self.title}'
        return self.title

    @property
    def get_children(self):
        if self.children:
            return self.children.all()
        return False


class Product(models.Model):
    STATUS_CHOICES = (
        ('in stock', 'in stock'),
        ('out of stock', 'out of stock')
    )

    title = models.CharField(max_length=50,)
    category = models.ManyToManyField(Category, related_name='products',)
    description = RichTextField(null=True, blank=True)
    image = models.ImageField(upload_to='images/')
    price = models.DecimalField(max_digits=12, decimal_places=2)
    stock = models.CharField(choices=STATUS_CHOICES, max_length=50)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    @property
    def get_absolute_url(self):
        return reverse('product_detail', args=[str(self.id)])

    def get_category_name(self):
        return self.category

    class Meta:
        ordering = ['-created']



