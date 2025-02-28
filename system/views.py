from django.shortcuts import render , redirect
from .models import *
from django.contrib.auth import get_user_model , authenticate , login as user_login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

User = get_user_model()

# Create your views here.

@login_required
def home(request):
    return render(request , 'home.html')

@login_required
def add_project(request):
    # Fetch lecturers sorted by full name
    lecturer = User.objects.filter(is_lecturer=True).order_by('full_name')


    # Initialize context to ensure it’s always available
    context = {'lecturer': lecturer}
    print(lecturer)

    if request.method == 'POST':
        name = request.POST.get('title')
        cat = request.POST.get('category')
        tech = request.POST.get('tech')
        supervisor_id = request.POST.get('supervisor')
        status = request.POST.get('status')
        description = request.POST.get('description')
        image = request.FILES.get('image_file')
        document = request.FILES.get('file')

        # Get logged-in user details
        author = request.user
        faculty = author.faculty
        department = author.department
        course = author.course # Safe access to course if it exists

        # Try to fetch supervisor
        try:
            supervisor = User.objects.get(id=supervisor_id)
        except User.DoesNotExist:
            supervisor = None

        # Create the project
        project = Project.objects.create(
            title=name,
            category=cat,
            technologies=tech,
            faculty=faculty,
            department=department,
            course=course,
            author=author,
            supervisor=supervisor,
            status=status,
            description=description,
            document=document,
            image=image,
        )

        project.save()
        

        
        context['project'] = project
        messages.success(request , 'Project uploaded successfully')
        return redirect('projects')
    return render(request, 'add-project.html', context)

@login_required
def edit_project(request):
    return render(request , 'edit_project.html')


@login_required
def project_listing(request):
    projects = Project.objects.all()  # Fetch all projects
    return render(request, 'projects.html', {'projects': projects})

@login_required
def project_details(request,id):
    pro = Project.objects.get(author=request.user,pk=id)
    context ={'pro':pro}
    return render(request , 'project_details.html',context)

import re  # Import for regular expressions

def register(request):
    if request.method == 'POST':
        user_type = request.POST.get('userType')

        full_name = request.POST.get('name')
        email = request.POST.get('email').strip()
        password = request.POST.get('password').strip()
        confirm_password = request.POST.get('confirmpassword').strip()

        # For student, index number is required, otherwise it can be left empty.
        index_number = request.POST.get('indexNumber', '').strip()
        faculty_name = request.POST.get('faculty')
        department_name = request.POST.get('department')
        course_name = request.POST.get('course')

        # Check if full name contains numbers
        if re.search(r'\d', full_name):  # Regular expression to check for any digits
            messages.error(request, "Full name cannot contain numbers.")
            return redirect('register')

        if len(password) < 8:
            messages.error(request, 'Password cannot be less than 8 characters')
            return redirect('register')

        # Check if passwords match
        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return redirect('register')

        # Check if user is a student and if index number is provided
        if user_type == 'student' and index_number:
            if User.objects.filter(username=index_number).exists():
                messages.info(request, "Index number already exists.")
                return redirect('register')

        # Check if email already exists
        if User.objects.filter(email=email).exists():
            messages.info(request, "Email already exists.")
            return redirect('register')

        # Create user with index number as username
        user = User(
            username=index_number if user_type == 'student' else email,  # Use index number as username for student or email for others
            full_name=full_name,
            email=email
        )
        user.set_password(password)

        if user_type == 'student':
            user.is_student = True
            user.index_num = index_number
            faculty, created = Faculty.objects.get_or_create(name=faculty_name)
            department, created = Department.objects.get_or_create(name=department_name, faculty=faculty)
            course, created = Course.objects.get_or_create(name=course_name, department=department)
            user.faculty = faculty
            user.department = department
            user.course = course
        elif user_type == 'lecturer':
            user.is_lecturer = True
        elif user_type == 'researcher':
            user.is_researcher = True

        # Save the user to the database
        user.save()
        messages.success(request, f"Registration successful for {user.full_name}")
        return redirect('login')

    return render(request, 'register.html')



def about(request):
    return render(request , 'about-us.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        msg = Message(
            name = name,
            email = email,
            subject = subject,
            message  = message
        )

        msg.save()
        return redirect('thanks')


    return render(request , 'contact-us.html')


def login(request):
    if request.user.is_authenticated:
        return redirect('home')  # Redirect already logged-in users to home

    if request.method == 'POST':
        username = request.POST.get('username').strip()
        password = request.POST.get('password').strip()

        user = authenticate(request, username=username, password=password)

        if user is not None:
            user_login(request, user)
            messages.success(request, f"Successfully logged in as {user.full_name}")
            return redirect('home')
        else:
            messages.error(request, 'Invalid credentials. Please try again.')
            return redirect('login')

    return render(request, 'login.html')



def ThankYou(request):
    return render(request , 'thankyou.html')


def user_logout(request):
    logout(request)  
    return redirect('home') 


def dashboard(request):
    return render(request , 'user-dashboard.html')


