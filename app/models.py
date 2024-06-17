from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

class News(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='news/')
    category = models.ForeignKey(Category,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = 'New'
        verbose_name_plural = 'News'

class Blog(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='blog/')
    description = models.TextField()

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'

class Teacher(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    degree = models.CharField(max_length=255)
    image = models.ImageField(upload_to='teacher')

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = 'Teacher'
        verbose_name_plural = 'Teachers'


class Course(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='course')
    description = models.TextField()
    name = models.CharField(max_length=255)
    teacher = models.ForeignKey(Teacher,on_delete=models.DO_NOTHING)
    price = models.IntegerField(default=0)
    discount = models.IntegerField(default=0)

    
    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = 'Course'
        verbose_name_plural = 'Course'


class Student(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    adress = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = 'Student'
        verbose_name_plural = 'Students'


