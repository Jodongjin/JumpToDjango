from django.contrib import admin

# 추가
from .models import Question

# Register your models here.
class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['subject']

admin.site.register(Question, QuestionAdmin)
