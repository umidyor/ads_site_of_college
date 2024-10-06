from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
urlpatterns = [
    path('upload/', upload_achievement, name='upload_achievement'),
    path('media/<path:file_path>',serve_media,name='serve_media'),
    path('about',about,name='about'),
    path('',index,name='index'),
    path('api/submit-form/', SubmitFormView.as_view(), name='submit_form'),
    path('courses',courses,name='courses'),
    path('courses/<str:course_name>',every_course,name="every_course"),
    path('news',news,name="news"),
    path('news/<int:news_id>/edit/', edit_news, name='edit_news'),
    # path('login',login_view,name='login'),
    path('logout',logout_view,name='logout'),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)