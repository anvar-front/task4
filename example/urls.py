from django.urls import path
from example.views import *

urlpatterns = [
    path('', Courses.as_view()),
    path('<int:pk>/', CoursesId.as_view()),
]
