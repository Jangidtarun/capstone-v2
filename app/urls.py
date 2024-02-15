from django.urls import path
from app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('register', views.register, name='register'),
    path('academics', views.academics_view, name='academics'),
    path('all_courses', views.all_course_view, name='all_courses'),
    path('create_course', views.create_course, name='create_course'),
    path('add_course', views.add_course_view, name='add_course'),
    path('faculty_register', views.fac_register, name='fac_register'),
    path('course_register', views.course_register, name='course_register'),
    path('course_unregister', views.course_unregister, name='course_unregister')
]