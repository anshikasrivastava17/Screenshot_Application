from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.home, name="home"),
    path('ss',views.index, name="ss"),
    path('edit/',views.edit,name='edit'),
    path('signup',views.signup,name='Signup'),
    path('signin',views.signin,name='Signin'),
    path('logoutuser',views.logoutuser,name='logout'),
    path('upgrade',views.upgrade,name='upgrade'),
    
] + static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)

