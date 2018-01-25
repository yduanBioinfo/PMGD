from django.urls import path

from . import views

app_name = 'database'
urlpatterns = [
    path('',views.Home.as_view(),name="home"),
    path('Abrowse',views.Genome_browser.as_view(),name="genome_browser"),
    path('Tools',views.Tools.as_view(),name="tools"),
    path('Tutorial',views.Tutorial.as_view(),name="tutorial"),
    path('Upload',views.Upload.as_view(),name="upload"),
]
