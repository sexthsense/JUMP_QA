from django.contrib import admin
from .models import Question

class QuestionAdmin(admin.ModelAdmin): # 제목으로 검색하기 위해 추가
    search_fields = ['subject']


admin.site.register(Question, QuestionAdmin) # 사이트에 질문과 질문으로 검색하기 위해 등록

# Register your models here.
