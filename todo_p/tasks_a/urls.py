from django.urls import path
from . import views

urlpatterns = [
    path('', view=views.home, name='home'),
    path('login/', view=views.LoginInterfaceView.as_view(), name= 'login'),
    path('signup/', view=views.SignUpView.as_view(), name='signup'),
    path('logout/', view=views.logout_view, name='logout'),
    path('task/<int:pk>/delete/', view=views.TaskDeleteView.as_view(), name='task-delete'),
    path('task/<int:pk>/update/', view=views.TaskUpdateView.as_view(), name='task-update'),
    path('task/create/', view=views.TaskCreateView.as_view(), name='task-create')
]