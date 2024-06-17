from django.contrib import admin
from .models import *


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','created_at','updated_at']
    list_per_page = 10
    search_fields = ['name']
admin.site.register(Category,CategoryAdmin)


class NewsAdmin(admin.ModelAdmin):
    list_display = ['title','date','category']
    list_editable = ['category']
    list_per_page = 10
    search_fields = ['title','description']
admin.site.register(News,NewsAdmin)


class BlogAdmin(admin.ModelAdmin):
    list_display = ['title','description']
    list_per_page = 10
    search_fields = ['title','description']
admin.site.register(Blog,BlogAdmin)


class TeacherAdmin(admin.ModelAdmin):
    list_display = ['name','surname','degree']
    list_per_page = 10
    search_fields = ['name','surname']
admin.site.register(Teacher,TeacherAdmin)


class CourseAdmin(admin.ModelAdmin):
    list_display = ['title','teacher','price','discount']
    list_editable = ['teacher','price','discount']
    list_per_page = 10
    search_fields = ['title','description']
admin.site.register(Course,CourseAdmin)


class StudentAdmin(admin.ModelAdmin):
    list_display = ['name','surname','course','adress','phone']
    list_editable = ['course','adress','phone']
    list_per_page = 10
    search_fields = ['name','surname','adress']
admin.site.register(Student,StudentAdmin)