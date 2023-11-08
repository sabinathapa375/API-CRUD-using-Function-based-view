from django.urls import path
from crudapiapp import views
urlpatterns = [
    path('studentapi/', views.student_api, name = 'studentapi'),
    path('create_student/', views.create_student, name = "create_student"),
    path('update_student/<int:pk>', views.update_student, name='update_student'),
    path('delete_student/<int:pk>', views.delete_student, name='update_student')

]
