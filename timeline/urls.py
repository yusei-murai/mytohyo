from django.urls import path
from . import views

app_name='timeline'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/',views.create,name='create'),
    path('delete/<uuid:pk>/',views.delete,name='delete'),
    path('q/<uuid:pk>/',views.q,name='q'),
    path('good1/<uuid:pk>/', views.good1, name='good1'),
    path('good2/<uuid:pk>/', views.good2, name='good2'),
    path('good3/<uuid:pk>/', views.good3, name='good3'),
    path('good4/<uuid:pk>/', views.good4, name='good4'),
    path('user/<uuid:auther>/', views.u, name='u'),
    path('post/',views.p,name='p'),
    path('category/<str:category>/', views.cate, name='cate'),
    path('privacy/', views.privacy, name='privacy'),
]