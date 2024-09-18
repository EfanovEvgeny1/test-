from django.contrib import admin
from django.urls import path
from django.urls import re_path
from firstapp import views
from django.views.generic import TemplateView


urlpatterns = [
path('admin/', admin.site.urls),
path('', views.index),
path('create/', views.create),
path('edit/<int:id>/', views.edit),
path('delete/<int:id>/', views.delete),
path('details/', views.details),
path('about/', TemplateView.as_view(template_name="firstapp/about.html")),
path('contact/', TemplateView.as_view(template_name="firstapp/contact.html",
            extra_context={"work": "Разработка программных продуктов"})),
]