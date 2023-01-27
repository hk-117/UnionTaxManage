from django.contrib import admin
from django.urls import path,include

admin.site.site_header = "ইউনিয়ন ট্যাক্স এডমিন"
admin.site.site_title = "ইউনিয়ন ট্যাক্স এডমিন পোর্টাল"
admin.site.index_title = "ইউনিয়ন ট্যাক্স এডমিন পোর্টালে স্বাগতম"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('maguraunion.urls')),
]
