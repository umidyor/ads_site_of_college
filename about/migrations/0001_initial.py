# Generated by Django 5.0.6 on 2024-09-21 17:33

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About_page_1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('long_desc', models.TextField()),
                ('about_pic1', models.ImageField(upload_to='images')),
                ('about_pic2', models.ImageField(upload_to='images')),
                ('about_pic3', models.ImageField(upload_to='images')),
                ('about_pic4', models.ImageField(upload_to='images')),
                ('about_pic5', models.ImageField(upload_to='images')),
                ('title_for_about_khm', models.CharField(max_length=300)),
                ('about_khm', models.TextField()),
                ('khm_picture', models.ImageField(upload_to='images')),
            ],
            options={
                'verbose_name': 'Biz haqimizda 1-qism',
                'verbose_name_plural': 'Biz haqimizda 1-qism',
            },
        ),
        migrations.CreateModel(
            name='About_page_2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_goal', models.CharField(max_length=300)),
                ('goal_desc', models.TextField()),
                ('group_picture', models.ImageField(upload_to='images')),
            ],
            options={
                'verbose_name': 'Biz haqimizda 2-qism(maqsad)',
                'verbose_name_plural': 'Biz haqimizda 2-qism(maqsad)',
            },
        ),
        migrations.CreateModel(
            name='About_part_1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('part1_title', models.CharField(max_length=5000)),
                ('part1_desc', models.TextField()),
                ('part1_pic1', models.ImageField(upload_to='images')),
                ('part1_pic2', models.ImageField(upload_to='images')),
            ],
            options={
                'verbose_name': 'Bosh sahifa 1-qism',
                'verbose_name_plural': 'Bosh sahifa 1-qism',
            },
        ),
        migrations.CreateModel(
            name='About_part_1_desc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about_part_1_desc', models.TextField()),
            ],
            options={
                'verbose_name': 'Bosh sahifa 1-qism description',
                'verbose_name_plural': 'Bosh sahifa 1-qism description',
            },
        ),
        migrations.CreateModel(
            name='Carousel_picture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('carousel', models.ImageField(upload_to='images')),
            ],
            options={
                'verbose_name': 'Carusel joy rasmlari',
                'verbose_name_plural': 'Carusel joy rasmlari',
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_picture', models.ImageField(upload_to='images')),
                ('course_name', models.CharField(max_length=200, unique=True)),
                ('course_description', models.TextField()),
            ],
            options={
                'verbose_name': 'Kurslar',
                'verbose_name_plural': 'Kurslar',
            },
        ),
        migrations.CreateModel(
            name='Footer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('footer', models.ImageField(upload_to='static/img/')),
            ],
        ),
        migrations.CreateModel(
            name='Homepage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('home_picture', models.ImageField(upload_to='images')),
                ('home_picture_2', models.ImageField(upload_to='images')),
            ],
            options={
                'verbose_name': 'Bosh sahifa',
                'verbose_name_plural': 'Bosh sahifa',
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('news_name', models.CharField(max_length=300)),
                ('news_description', models.TextField()),
                ('news_date', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='Our_group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_picture', models.ImageField(upload_to='images')),
            ],
            options={
                'verbose_name': 'Bizning guruh rasmi',
                'verbose_name_plural': 'Bizning guruh rasmi',
            },
        ),
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=300)),
                ('last_name', models.CharField(max_length=300)),
                ('phone_number', models.CharField(max_length=300)),
                ('gmail', models.CharField(max_length=300)),
                ('verification_code', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': "Ro'yxatdan o'tkanlar",
                'verbose_name_plural': "Ro'yxatdan o'tkanlar",
            },
        ),
        migrations.CreateModel(
            name='EveryCourse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_details', models.TextField()),
                ('course_theme', models.CharField(max_length=300)),
                ('course_description', models.TextField()),
                ('course_video', models.FileField(upload_to='')),
                ('course_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='about.course')),
            ],
        ),
        migrations.CreateModel(
            name='EveryCourseSkills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_skill_name', models.CharField(max_length=200)),
                ('course_skill_desc', models.TextField()),
                ('course_name_for_skill', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='about.course')),
            ],
        ),
        migrations.CreateModel(
            name='Achievement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('achievement_files', models.FileField(blank=True, null=True, upload_to='achievements/')),
                ('news_name_for_achv', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='about.news')),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teacher_fullname', models.CharField(max_length=300)),
                ('teacher_picture', models.ImageField(upload_to='images')),
                ('teacher_motto', models.TextField()),
                ('teacher_major', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='about.course')),
            ],
            options={
                'verbose_name': "O'qituvchilar",
                'verbose_name_plural': "O'qituvchilar",
            },
        ),
    ]
