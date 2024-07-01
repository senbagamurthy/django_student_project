from django.urls import path
from . import views
from students import urls


urlpatterns = [
    path('student/<int:id>/', views.student_detail, name='student_detail'),
]
