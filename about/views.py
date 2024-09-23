from django.shortcuts import render, redirect
from .forms import AchievementForm
from .models import *
from django.contrib import messages

import os
from django.http import Http404
from django.conf import settings
from django.http import FileResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.utils.text import slugify
import os





@csrf_exempt
# def upload_achievement(request):
#     if request.method == 'POST':
#         form = AchievementForm(request.POST, request.FILES)
#         print(form)
#         if form.is_valid():
#             files = form.cleaned_data['achievement_files']
#             for f in files:
#                 model = Achievement()
#                 model.achievement_files = f
#                 model.news_name_for = form.cleaned_data['news_name_for']
#                 model.save()
#             return redirect('index')
#     else:
#         form = AchievementForm()
#     return render(request, 'upload.html', {'form': form})

# Check if the user is an admin (superuser)
def admin_required(user):
    return user.is_superuser


def sanitize_filename(file):
    filename, ext = os.path.splitext(file.name)
    sanitized_name = slugify(filename) + ext
    file.name = sanitized_name
    return file


from django.shortcuts import render, redirect
from django.http import Http404
from .forms import AchievementForm  # Adjust based on your actual import
from .models import News, Achievement
import datetime

ALLOWED_IMAGE_EXTENSIONS = ['.jpg', '.jpeg', '.png']
ALLOWED_VIDEO_EXTENSIONS = ['.mp4']


def upload_achievement(request):
    if not request.user.is_superuser:
        raise Http404("Page not found")
    if request.method == 'POST':
        form = AchievementForm(request.POST, request.FILES)
        if form.is_valid():
            # Save the News instance first
            news = News.objects.create(
                news_name=form.cleaned_data['news_name'],
                news_description=form.cleaned_data['news_description'],
                news_date=form.cleaned_data['news_date'] or datetime.datetime.now()
            )

            # Save Achievement files associated with the News
            files = request.FILES.getlist('achievement_files')  # Get list of uploaded files
            for f in files:
                achievement = Achievement(
                    news_name_for_achv=news,
                    achievement_files=f
                )
                achievement.save()

            return redirect('index')
    else:
        form = AchievementForm()
    return render(request, 'upload.html', {'form': form})


@csrf_exempt
def serve_media(request, file_path):
    file_path = os.path.join(settings.MEDIA_ROOT, file_path)
    if os.path.exists(file_path):
        response = FileResponse(open(file_path, 'rb'))
        return response
    else:
        return HttpResponse("Media not found!")


from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags


def send_welcome_email(to_email, first_name):
    subject = "Muvaffaqiyatli ro'yxatdan o'tish"
    from_email = 'umidyor007@gmail.com'
    to = to_email

    # Render the HTML content using a template
    html_content = render_to_string('welcome_email_template.html', {'first_name': first_name})

    # Create plain text by stripping the HTML content
    text_content = strip_tags(html_content)

    # Create the email message object
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])

    # Attach the HTML content as an alternative
    msg.attach_alternative(html_content, "text/html")

    # Send the email
    msg.send()


def index(request):
    pictures = Homepage.objects.all()
    about_part_1 = About_part_1.objects.all()
    about_part_1_desc = About_part_1_desc.objects.all()
    carousel = Carousel_picture.objects.all()
    courses = Course.objects.all()
    our_group_photo = Our_group.objects.all()
    teachers = Teacher.objects.all()
    latest_post = News.objects.order_by('-news_date').first()
    print(latest_post)

    post_av = Achievement.objects.filter(news_name_for_achv=latest_post)

    files_with_types = []
    for achievement in post_av:
        file_url = achievement.achievement_files.url
        # Determine the file type
        if file_url.endswith('.mp4'):
            file_type = 'video'
        elif file_url.endswith(('.jpg', '.jpeg', '.png')):
            file_type = 'image'
        else:
            file_type = 'unknown'  # Fallback in case of unsupported file type

        files_with_types.append({
            'file': file_url,
            'type': file_type
        })

    return render(request, "index.html",
                  {"pictures": pictures, "about_part_1": about_part_1, "about_part_1_desc": about_part_1_desc,
                   "carousel": carousel, "courses": courses, "our_group_photo": our_group_photo, "teachers": teachers,
                   'latest_post': latest_post, "files_with_types": files_with_types,
        "length": len(files_with_types)})

def about(request):
    courses = Course.objects.all()
    datas = About_page_1.objects.all()
    teachers = Teacher.objects.all()
    goals = About_page_2.objects.all()
    return render(request, "about.html", {"courses": courses, "datas": datas, "teachers": teachers, 'goals': goals})


def navbar_only(request):
    courses = Course.objects.all()
    footer = Footer.objects.get()
    return render(request, "navbar_only.html", {"courses": courses, "footer": footer})


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class SubmitFormView(APIView):
    def post(self, request, *args, **kwargs):
        first_name = request.data.get('first_name')
        last_name = request.data.get('last_name')
        phone_number = request.data.get('phone_number')
        email = request.data.get('email')

        if Register.objects.filter(gmail=email).exists():
            message = "Bu google akkauntdan allaqachon ro'yxatdan o'tilgan yoki siz allaqachon ro'yxatdan o'tkansiz!"
        else:
            user = Register(first_name=first_name, last_name=last_name, phone_number=phone_number, gmail=email)
            user.save()
            send_welcome_email(email, first_name)
            # Prepare and send a Telegram notification
            notification_message = (
                f"*Yangi foydalanuvchi ro'yxatdan o'tdi👀*\n\n"
                f"*Ism🕵️: {first_name}\n"
                f"*Familiya💁‍♂️: {last_name}\n"
                f"*Telefon raqam📲: {phone_number}\n"
                f"*Gmail📧: {email}\n"
            )
            send_telegram_message(notification_message)
            message = f"Muvaffaqiyatli ro'yxatdan o'tildi! Iltimos {email} nomli pochtangizni tekshiring biz unga xabar yubordik🧑‍💻"

        return Response({"message": message}, status=status.HTTP_200_OK)

    def get(self, request, *args, **kwargs):
        return Response({"message": "Invalid request method."}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


import requests

TELEGRAM_BOT_TOKEN = '7370565735:AAFPVROFACFRYmrfdHPtzJUREgb_1ufZbRE'
CHAT_ID = '5149506457'


def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        'chat_id': CHAT_ID,
        'text': message
    }
    requests.post(url, data=payload)


def courses(request):
    courses = Course.objects.all()
    return render(request, "courses.html", {"courses": courses})


def every_course(request, course_name):
    courses = Course.objects.all()
    course_name = get_object_or_404(Course, course_name=course_name)
    onecourse = EveryCourse.objects.filter(course_name=course_name)
    skills = EveryCourseSkills.objects.filter(course_name_for_skill=course_name)
    teachers = Teacher.objects.filter(teacher_major=course_name)
    carousel = Carousel_picture.objects.all()
    return render(request, "every_course.html",
                  {"courses": courses, "onecourse": onecourse, "skills": skills, "teachers": teachers,
                   "carousel": carousel})



def news(request):
    news_posts = News.objects.order_by('-news_date')
    courses=Course.objects.all()
    # For each news post, get all related achievements and determine the file type
    news_with_achievements = []
    for news_item in news_posts:
        achievements_with_type = []
        for achievement in news_item.achievements.all():
            file_url = achievement.achievement_files.url
            # Determine if the file is an image or a video
            if file_url.endswith('.mp4'):
                file_type = 'video'
            elif file_url.endswith(('.jpg', '.jpeg', '.png')):
                file_type = 'image'
            else:
                file_type = 'unknown'  # Fallback for unsupported file types

            achievements_with_type.append({
                'achievement': achievement,
                'file_type': file_type,
                'file_url': file_url,
            })

        news_with_achievements.append({
            'news_item': news_item,
            'achievements': achievements_with_type,
        })

    context = {
        'news_with_achievements': news_with_achievements,
        'courses':courses,
    }

    return render(request, "news.html", context)


def edit_news(request, news_id):
    if not request.user.is_superuser:
        raise Http404("Page not found")
    news_instance = get_object_or_404(News, id=news_id)

    # Check if the POST request contains updated data
    if request.method == 'POST':
        form = AchievementForm(request.POST, request.FILES, instance=news_instance)

        if form.is_valid():
            # Save changes to the News object and associated achievements
            form.save()
            return redirect('index')  # Redirect to the news detail page after saving

    else:
        # Pre-fill the form with the existing news data
        form = AchievementForm(instance=news_instance)

    return render(request, 'edit_news.html', {'form': form, 'news': news_instance})


# from django import template
#
# register = template.Library()
#
# @register.filter
# def jsonify(value):
#   import json
#   return json.dumps(value)
