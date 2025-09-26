
from django.contrib import admin
from django.urls import path
from appname import views
from django.contrib.auth import views as auth_views
from appname.views import TaskDeleteView, TaskListView, TaskCreateView, TaskUpdateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', views.simple_logout, name='logout'),
    path('register/', views.register, name='register'),

    path('', TaskListView.as_view(), name='task-list'),
    path('create/', TaskCreateView.as_view(), name='task-create'),
    path('update/<int:pk>/', TaskUpdateView.as_view(), name='task-update'),
    path('delete/<int:pk>/', TaskDeleteView.as_view(), name='task-delete'),
    path('comment/<int:pk>/', views.CommentCreateView.as_view(), name='comment-create'),
]
