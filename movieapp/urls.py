from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.index, name='home'),
    path('series', views.series, name='series'),
    path('clips', views.clips, name='clips'),
    path(r'<slug>/', views.movie_detail, name='detail'),
    path('register', views.register, name='register'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('editprofile', views.user_edit_view, name='editprofile'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

#path(r'^(?P<slug>[\w-]+)/$', views.movie_detail, name='detail'),

#i changed the slug here