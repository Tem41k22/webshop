from django.db import models
from django.urls import reverse


# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True,)
    image = models.ImageField(upload_to='category', blank=True)
    parent = models.ForeignKey(
        'self', blank=True, null=True, related_name='children', on_delete=models.CASCADE)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категории'
        verbose_name_plural = 'Категории'
        index_together = (('id', 'slug'),)

    def get_absolute_url(self):
        return reverse("main:catalog_by_category", args=[self.slug])


class Product(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True,)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=0)
    stock = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(
        Category, related_name='products', on_delete=models.CASCADE, blank=True, null=True, default=None)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Товар'
        verbose_name_plural = 'Товар'
        index_together = (('id', 'slug'),)

    def get_title_image(self):
        if ProductImage.objects.filter(product=self).count() > 0:
            return ProductImage.objects.filter(product=self)[0]


class ProductImage(models.Model):
    product = models.ForeignKey(
        Product, default=None, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)


class News(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True,)
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Новости'
        verbose_name_plural = 'Новости'
        index_together = (('id', 'slug'),)

    def get_title_image(self):
        if NewsImage.objects.filter(news=self).count() > 0:
            return NewsImage.objects.filter(news=self)[0]


class NewsImage(models.Model):
    news = models.ForeignKey(
        News, default=None, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='news/%Y/%m/%d', blank=True)


class Discount(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True,)
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Новости | Акции'
        verbose_name_plural = 'Новости | Акции'
        index_together = (('id', 'slug'),)

    def get_title_image(self):
        if DiscountImage.objects.filter(discount=self).count() > 0:
            return DiscountImage.objects.filter(discount=self)[0]


class DiscountImage(models.Model):
    discount = models.ForeignKey(
        Discount, default=None, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='discount/%Y/%m/%d', blank=True)


class Topics(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True,)
    description = models.TextField(blank=True)
    description2 = models.DateField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Статьи'
        verbose_name_plural = 'Статьи'
        index_together = (('id', 'slug'),)

    def get_title_image(self):
        if TopicsImage.objects.filter(topics=self).count() > 0:
            return TopicsImage.objects.filter(topics=self)[0]


class TopicsImage(models.Model):
    topics = models.ForeignKey(
        Topics, default=None, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='topics/%Y/%m/%d', blank=True)


class Movie(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True,)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Видео'
        verbose_name_plural = 'Видео'
        index_together = (('id', 'slug'),)

    def get_title_image(self):
        if MovieImage.objects.filter(movie=self).count() > 0:
            return MovieImage.objects.filter(movie=self)[0]


class MovieImage(models.Model):
    movie = models.ForeignKey(
        Movie, default=None, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='movie/%Y/%m/%d', blank=True)


class Brand(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True,)
    description = models.TextField(blank=True)
    description3 = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=0)
    stock = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Бренды'
        verbose_name_plural = 'Бренды'
        index_together = (('id', 'slug'),)

    def get_title_image(self):
        if BrandImage.objects.filter(brand=self).count() > 0:
            return BrandImage.objects.filter(brand=self)[0]


class BrandImage(models.Model):
    brand = models.ForeignKey(
        Brand, default=None, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='brand/%Y/%m/%d', blank=True)
