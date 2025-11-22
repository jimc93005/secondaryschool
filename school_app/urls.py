from django.urls import path
from . import views

app_name = 'school_app'

urlpatterns = [
    # index and collins urls
    path('', views.index, name='index'),


    # department urls
    path('departments/', views.departments, name='departments'),
    path('new_department/', views.new_department, name='new_department'),

    # subject urls
    path('departments/<int:department_id>/', views.subjects, name='subjects'),
    path('new_subject/<int:department_id>/', views.new_subject, name='new_subject'),
    path('edit_subject/<int:subject_id>/', views.edit_subject, name='edit_subject'),


    # topics urls
    path('subjects/<int:subject_id>/topics/', views.topics, name='topics'),
    path('new_topics/<int:subject_id>/', views.new_topics, name='new_topics'),
    path('edit_topic/<int:topic_id>', views.edit_topic, name='edit_topic'),


    # subject teachers name:
    path('subject/<int:subject_id>/', views.subject_teacher, name='subject_teacher'),
    path('new_teacher/<int:subject_id>/', views.new_teacher, name='new_teacher'),
]

