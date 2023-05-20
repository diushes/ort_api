from django.db import models


class Test(models.Model):
    title = models.CharField(max_length=150, blank=False)

    def __str__(self) -> str:
        return self.title


class Question(models.Model):
    question_text = models.TextField(blank=False)
    test = models.ForeignKey("Test", on_delete=models.CASCADE, related_name="questions")

    def __str__(self) -> str:
        return self.question


class Option(models.Model):
    option_text = models.CharField(max_length=50)
    is_correct = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.option_text
