import datetime

from django.db import models



class Homepage(models.Model):
    home_picture=models.ImageField(upload_to="images")
    home_picture_2=models.ImageField(upload_to="images")

    class Meta:
        verbose_name="Bosh sahifa"
        verbose_name_plural ="Bosh sahifa"


    def __str__(self):
        return "Homepage_pictures"
class About_part_1(models.Model):
    part1_title=models.CharField(max_length=5000)
    part1_desc=models.TextField()
    part1_pic1=models.ImageField(upload_to="images")
    part1_pic2=models.ImageField(upload_to="images")

    def __str__(self):
        return "Title & Description & Pictures"

    class Meta:
        verbose_name="Bosh sahifa 1-qism"
        verbose_name_plural ="Bosh sahifa 1-qism"

class About_part_1_desc(models.Model):
    about_part_1_desc=models.TextField()

    def __str__(self):
        return "About Part 1 description"
    class Meta:
        verbose_name="Bosh sahifa 1-qism description"
        verbose_name_plural ="Bosh sahifa 1-qism description"

class Carousel_picture(models.Model):
    carousel=models.ImageField(upload_to="images")

    class Meta:
        verbose_name="Carusel joy rasmlari"
        verbose_name_plural ="Carusel joy rasmlari"


class Course(models.Model):
    course_picture=models.ImageField(upload_to="images")
    course_name=models.CharField(max_length=200, unique=True)
    course_description=models.TextField()

    def __str__(self):
        return self.course_name
    class Meta:
        verbose_name="Kurslar"
        verbose_name_plural ="Kurslar"



class Our_group(models.Model):
    group_picture=models.ImageField(upload_to="images")

    def __str__(self):
        return "Our group picture"

    class Meta:
        verbose_name="Bizning guruh rasmi"
        verbose_name_plural ="Bizning guruh rasmi"


class Teacher(models.Model):
    teacher_fullname=models.CharField(max_length=300)
    teacher_major=models.ForeignKey(Course,on_delete=models.SET_NULL,null=True)
    teacher_picture=models.ImageField(upload_to="images")
    teacher_motto=models.TextField()

    def __str__(self):
        return self.teacher_fullname



    class Meta:
        verbose_name="O'qituvchilar"
        verbose_name_plural ="O'qituvchilar"
import datetime
class News(models.Model):
    news_name=models.CharField(max_length=300)
    news_description=models.TextField()
    news_date=models.DateTimeField(default=datetime.datetime.now)

    def __str__(self):
        return self.news_name
class Achievement(models.Model):
    news_name_for_achv=models.ForeignKey(News,on_delete=models.SET_NULL,null=True,related_name='achievements')
    achievement_files = models.FileField(upload_to='achievements/', blank=True, null=True)




class About_page_1(models.Model):
    long_desc=models.TextField()
    about_pic1=models.ImageField(upload_to="images")
    about_pic2 = models.ImageField(upload_to="images")
    about_pic3 = models.ImageField(upload_to="images")
    about_pic4 = models.ImageField(upload_to="images")
    about_pic5 = models.ImageField(upload_to="images")

    title_for_about_khm=models.CharField(max_length=300)
    about_khm=models.TextField()
    khm_picture=models.ImageField(upload_to="images")

    class Meta:
        verbose_name="Biz haqimizda 1-qism"
        verbose_name_plural ="Biz haqimizda 1-qism"

    def __str__(self):
        return "About_page_1"

class About_page_2(models.Model):
    title_goal=models.CharField(max_length=300)
    goal_desc=models.TextField()
    group_picture=models.ImageField(upload_to="images")

    class Meta:
        verbose_name="Biz haqimizda 2-qism(maqsad)"
        verbose_name_plural ="Biz haqimizda 2-qism(maqsad)"

    def __str__(self):
        return "KHM Maqsadi!"






class Register(models.Model):
    first_name=models.CharField(max_length=300)
    last_name=models.CharField(max_length=300)
    phone_number=models.CharField(max_length=300)
    gmail=models.CharField(max_length=300)
    verification_code=models.CharField(max_length=200)

    class Meta:
        verbose_name="Ro'yxatdan o'tkanlar"
        verbose_name_plural ="Ro'yxatdan o'tkanlar"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"




class EveryCourse(models.Model):
    course_name=models.ForeignKey(Course,on_delete=models.SET_NULL,null=True)
    course_details=models.TextField()
    course_theme=models.CharField(max_length=300)
    course_description=models.TextField()
    course_video=models.FileField()

    def __str__(self):
        return self.course_theme


class EveryCourseSkills(models.Model):
    course_name_for_skill=models.ForeignKey(Course,on_delete=models.SET_NULL,null=True)
    course_skill_name=models.CharField(max_length=200)
    course_skill_desc=models.TextField()

    def __str__(self):
        return self.course_skill_name


class Footer(models.Model):
    footer=models.ImageField(upload_to='static/img/')

    def __str__(self):
        return "footer picture"

