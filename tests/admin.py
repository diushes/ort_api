from django.contrib import admin
from nested_inline.admin import NestedStackedInline, NestedModelAdmin
from .models import Option, Question, Test


class OptionInline(NestedStackedInline):
    model = Option
    extra = 4


class QuestionInline(NestedStackedInline):
    model = Question
    extra = 1
    inlines = [OptionInline]
    fk_name = 'test'


class TestAdmin(NestedModelAdmin):
    inlines = [QuestionInline]


admin.site.register(Test, TestAdmin)
