from django.urls import path

from . import views

app_name = 'board'

urlpatterns = [
    path('',views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('answer/create/<int:question_id>/', views.answer_create, name='answer_create'),
]

#새로 생성한 파일 url을 별도로 커피그에서 추출해서 개별 관리를 하기 위해서