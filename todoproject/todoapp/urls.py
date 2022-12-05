from django.urls import path
from .import views


urlpatterns = [
    path('',views.index,name='index'),
    path('base',views.base,name='base'),
    path('delete/<int:taskid>/',views.delete,name='delete'),
    path('update/<int:id>/',views.update,name='update'),
    path('classpage/',views.Tasklistview.as_view(),name='classpage'),
    path('details/<int:id>/',views.TaskDetailview.as_view(),name='details'),
    path('update/<int:id/',views.Taskupdateview.as_view(),name='update'),
]