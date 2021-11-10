from django.contrib import admin
from .models import Product, ProductImage, News, NewsImage, Discount, DiscountImage, Topics, TopicsImage, Movie, MovieImage, Brand, BrandImage, Category
# Register your models here.


class ProductImageInline(admin.TabularInline):
    model = ProductImage


class NewsImageInline(admin.TabularInline):
    model = NewsImage


class DiscountImageInline(admin.TabularInline):
    model = DiscountImage


class TopicsImageInline(admin.TabularInline):
    model = TopicsImage


class MovieImageInline(admin.TabularInline):
    model = MovieImage


class BrandImageInline(admin.TabularInline):
    model = BrandImage

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'image', 'parent']
    list_filter = ['name', ]
    list_editable = ['image', ]
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'description', 'price',
                    'stock', 'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'stock', 'available']
    inlines = [ProductImageInline]
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Product, ProductAdmin)


class NewsAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'description',
                    'created', 'updated']
    list_filter = ['created', 'updated']
    inlines = [NewsImageInline]
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(News, NewsAdmin)


class DiscountAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'description',
                    'created', 'updated']
    list_filter = ['created', 'updated']
    inlines = [DiscountImageInline]
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Discount, DiscountAdmin)


class TopicsAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'description', 'description2',
                    'created', 'updated']
    list_filter = ['created', 'updated']
    inlines = [TopicsImageInline]
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Topics, TopicsAdmin)


class MovieAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug',
                    'created', 'updated']
    list_filter = ['created', 'updated']
    inlines = [MovieImageInline]
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Movie, MovieAdmin)


class BrandAdmin(admin.ModelAdmin):
    list_display = ['name', 'description3', 'slug', 'description', 'price',
                    'stock', 'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'stock', 'available']
    inlines = [BrandImageInline]
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Brand, BrandAdmin)
