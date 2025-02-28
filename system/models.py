from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_lecturer = models.BooleanField(default=False)
    is_researcher = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    full_name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)  # Email as unique identifier
    faculty = models.ForeignKey('Faculty', on_delete=models.SET_NULL, null=True, blank=True)
    department = models.ForeignKey('Department', on_delete=models.SET_NULL, null=True, blank=True)
    course = models.ForeignKey('Course', on_delete=models.SET_NULL, null=True, blank=True)
    profile_picture = models.ImageField(upload_to='profiles/', null=True, blank=True)
    phone = models.CharField(max_length=12 , null=True , blank=True)
    bio = models.TextField(null=True, blank=True)

    USERNAME_FIELD = 'username'  # Default username field is preserved
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.username  # Use username (index_num) for display


# Faculty Model
class Faculty(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

# Department Model
class Department(models.Model):
    name = models.CharField(max_length=100)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE, related_name='departments')

    class Meta:
        unique_together = ('name', 'faculty')

    def __str__(self):
        return f"{self.name} ({self.faculty.name})"

# Course Model
class Course(models.Model):
    name = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='courses')

    class Meta:
        unique_together = ('name', 'department')

    def __str__(self):
        return f"{self.name} ({self.department.name})"

# Project Model
class Project(models.Model):
    title = models.CharField(max_length=255 , null=True , blank= True)
    category = models.CharField(max_length=50 , null=True , blank= True)
    technologies = models.TextField(null=True , blank= True)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE , null=True , blank= True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE , null=True , blank= True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'is_student': True} , null=True , blank= True)
    supervisor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='supervised_projects', limit_choices_to={'is_lecturer': True})
    status = models.CharField(max_length=20 , null=True , blank= True)
    description = models.TextField(null=True , blank= True)
    document = models.FileField(upload_to='projects/documents', null=True , blank= True)
    image = models.ImageField(null=True , blank=True , upload_to='projects/images')
    submission_date = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.title

# Comment Model
class Comment(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies')
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user.username} on {self.project.title}"

# Activity Log Model
class ActivityLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    action = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.action} at {self.timestamp}"
    


class Message(models.Model):
    name = models.CharField(max_length=200 , null=True , blank= False)
    email = models.EmailField(null=True , blank=True)
    subject = models.CharField(max_length=500 , null= True , blank= True)
    message = models.TextField(null=True , blank=True)


    def __str__(self):
        return self.subject

