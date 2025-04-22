from django.contrib import admin
from django.urls import path, include
#from auth_test.main import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include ('main.urls')),
]
