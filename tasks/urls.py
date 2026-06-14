from django.urls import path
from tasks.views import *

urlpatterns = [
    path('', home_page, name="home_page"),
    path('task-list/', task_list, name="task_list"),
    path('view-task/<str:t_id>/', view_task, name="view_task"),
    path('add-task/', task_add, name="task_add"),
    path('edit-task/<str:t_id>/', edit_task, name="edit_task"),
    path('delete-task/<str:t_id>/', delete_task, name="delete_task"),
]
