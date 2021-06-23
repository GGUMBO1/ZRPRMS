
from django.contrib import admin
from django.urls import path
from django.urls import path , include



admin.site.site_title = "ZRP RMS"
admin.site.site_header = "ZRP RMS"
urlpatterns = [
    path('', include('rmsapp.urls')),
    path('admin/', admin.site.urls),
    
]
