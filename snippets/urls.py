from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views

urlpatterns = [
    path('', views.api_root),

    path('snippets/', views.snippet_list, name='snippet-list'),
    path('snippets/<int:pk>/', views.snippet_detail, name='snippet-detail'),
    path('snippets/<int:pk>/highlight/', views.snippet_highlight, name='snippet-highlight'),

    path('users/', views.user_list, name='user-list'),
    path('users/<int:pk>/', views.user_detail, name='user-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)