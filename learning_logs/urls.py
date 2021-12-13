"""Defines URL patterns for learning_logs."""

from django.urls import path
from . import views

app_name = 'learning_logs'
urlpatterns = [
    # Home Page
    path('', views.index, name='index'),
    path('topics/', views.topics, name='topics'),
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    path('topics/add/', views.add_topic, name='add_topic'),
    path('entries/', views.entries, name='entries'),
    path('entries/add', views.add_entry, name='add_entry'),
    path('entries/edit/<int:entry_id>', views.edit_entry, name='edit_entry'),

]