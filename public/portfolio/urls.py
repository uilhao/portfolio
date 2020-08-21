from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

# views
from root import views as rout_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', rout_views.home, name='home'),
    path('about', rout_views.about, name='about'),
    path('contact', rout_views.contact, name='contact'),
    path('skills', rout_views.skills, name='skills'),
    path('portfolio', rout_views.portfolio, name='portfolio'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
