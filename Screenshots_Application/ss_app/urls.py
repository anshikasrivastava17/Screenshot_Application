from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',views.index1, name="home"),
    path('ss',views.index, name="ss"),
    path('signup',views.signup,name='Signup'),
] + static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
