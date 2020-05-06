from django.contrib import admin
from django.contrib.gis import forms
from django.utils.safestring import mark_safe


from .models import Category,GrapeSort,Wine,Food,Rating,RatingStar,Reviews

from ckeditor_uploader.widgets import CKEditorUploadingWidget


class WineAdminForm(forms.ModelForm):
    description = forms.CharField(label="Описание", widget=CKEditorUploadingWidget())

    class Meta:
        model = Wine
        fields = '__all__'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "url")
    list_display_links = ("name",)


class ReviewInLine(admin.TabularInline):
    model = Reviews
    extra = 1
    readonly_fields = ("name", "email")


@admin.register(Wine)
class WineAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "url", "get_image")
    readonly_fields = ("get_image",)
    list_filter = ("category", "country", "year")
    search_fields = ("name", "category__name", "country")
    inlines = [ReviewInLine]
    save_on_top = True
    save_as = True
    form = WineAdminForm

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width = "50" height = "60" ')

    get_image.short_description = "Изображение"


@admin.register(Reviews)
class ReviewsAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "parent", "wine", "id")
    readonly_fields = ("name", "email")


@admin.register(GrapeSort)
class GrapeAdmin(admin.ModelAdmin):
    list_display = ("name", "country", "get_image")
    readonly_fields = ("get_image", )

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width = "50" height = "60" ')

    get_image.short_description = "Изображение"


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ("star", "ip")


@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = ("name", "get_image")
    readonly_fields = ("get_image", )

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width = "50" height = "60" ')

    get_image.short_description = "Изображение"


admin.site.register(RatingStar)

admin.site.site_tittle = "Django Wines"
admin.site.site_header = "Django Wines"

