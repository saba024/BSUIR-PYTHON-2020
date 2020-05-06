from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField("Категория", max_length=150)
    description = models.TextField("Описание")
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class GrapeSort(models.Model):
    name = models.CharField("Имя", max_length=150)
    description = models.TextField("Описание")
    country = models.CharField("Страна", max_length=150)
    image = models.ImageField("Изображение", upload_to="media/", null=True)
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Cорт Винограда"
        verbose_name_plural = "Сорта Винограда"


class Wine(models.Model):
    name = models.CharField("Название", max_length=150)
    description = models.TextField("Описание")
    country = models.CharField("Страна", max_length=150)
    image = models.ImageField("Изображение", upload_to="media/", null=True)
    grape_sort = models.ManyToManyField(GrapeSort, verbose_name="Сорт", related_name="grape")
    year = models.PositiveIntegerField("Год разлива", default=0)
    category = models.ForeignKey(
        Category, verbose_name="Категория", on_delete=models.SET_NULL, null=True
    )
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("wine_detail", kwargs={"slug": self.url})

    def get_review(self):
        return self.reviews_set.filter(parent__isnull=True)

    class Meta:
        verbose_name = "Вино"
        verbose_name_plural = "Вина"


class Food(models.Model):
    name = models.CharField("Блюдо", max_length=150)
    image = models.ImageField("Изображение", upload_to="food/", null=True)
    wine = models.ManyToManyField(Wine, verbose_name="Вино")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Еда"


class RatingStar(models.Model):
    value = models.PositiveSmallIntegerField("Значение", default=0)

    def __str__(self):
        return f'{self.value}'

    class Meta:
        verbose_name = "Звезда рейтинга"
        verbose_name_plural = "Звезды рейтинга"


class Rating(models.Model):
    ip = models.CharField("IP адрес", max_length=15)
    star = models.ForeignKey(RatingStar, on_delete=models.CASCADE, verbose_name="Звезда")
    wine = models.ForeignKey(Wine, on_delete=models.CASCADE, verbose_name="Вино")

    def __str__(self):
        return f"{self.star} - {self.wine}"

    class Meta:
        verbose_name = "Рейтинг"
        verbose_name_plural = "Рейтинги"
#        ordering = ["-value"]


class Reviews(models.Model):
    email = models.EmailField()
    name = models.CharField("Имя", max_length=100)
    text = models.TextField("Текст", max_length=5000)
    parent = models.ForeignKey(
        'self', verbose_name="Родитель", on_delete=models.SET_NULL, blank=True, null=True
    )
    wine = models.ForeignKey(Wine, verbose_name="Вино", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.wine}"

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
