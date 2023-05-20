from django.db import models
from django.templatetags.static import static


class Category(models.Model):
    title = models.CharField(max_length=100, blank=False)
    image = models.ImageField(
        blank=False, upload_to="categories/", default=static("images/placeholder.png")
    )

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self) -> str:
        return self.title


class Topic(models.Model):
    title = models.CharField(max_length=100, blank=False)
    content = models.TextField(blank=False)
    category = models.ForeignKey(
        "Category", on_delete=models.CASCADE, related_name="topics"
    )

    def __str__(self) -> str:
        return self.title
