from django.urls import path
from .views import (ClientListCreateView, ClientDetailView,
                    TaskListCreateView, TaskDetailView,
                    InteractionListCreateView, InteractionDetailView)


urlpatterns = [
    path('clients/', ClientListCreateView.as_view(), name='clients'),
    path('clients/<int:pk>/', ClientDetailView.as_view(), name='clients'),
    path('tasks/', TaskListCreateView.as_view(), name='tasks'),
    path('tasks/<int:pk>/', TaskDetailView.as_view(), name='tasks'),
    path('interactions/', InteractionListCreateView.as_view(), name='interactions'),
    path('interactions/<int:pk>/', InteractionDetailView.as_view(), name='interactions'),
]