from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Student
from django.contrib import messages

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            return render(request, "core/login.html", {"error": "Invalid credentials!"})

    return render(request, "core/login.html")


def register_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        if password != confirm_password:
            return render(request, "core/register.html", {"error": "Passwords do not match!"})

        if User.objects.filter(username=username).exists():
            return render(request, "core/register.html", {"error": "Username already exists!"})

        if User.objects.filter(email=email).exists():
            return render(request, "core/register.html", {"error": "Email already registered!"})

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        return redirect("login")

    return render(request, "core/register.html")


# Logout
def logout_view(request):
    logout(request)
    return redirect('login')


# Home page
def home_view(request):
    if not request.user.is_authenticated:
        return redirect('login')
    students = Student.objects.all()
    return render(request, 'core/home.html', {'students': students})


# Add student
def add_student(request):
    if not request.user.is_authenticated:
        return redirect('login')

    if request.method == 'POST':
        name = request.POST.get('studentName')
        contact = request.POST.get('contactNumber')
        birthdate = request.POST.get('birthdate')
        course = request.POST.get('course')
        totalfees = request.POST.get('totalfees')
        feesPaid = request.POST.get('feesPaid')

        Student.objects.create(
            studentName=name,
            contactNumber=contact,
            birthdate=birthdate,
            course=course,
            totalfees=totalfees,
            feesPaid=feesPaid
        )
        messages.success(request, "Student added successfully!")
        return redirect('home')

    return render(request, 'core/add_student.html')


# Edit student
def edit_student(request, id):
    if not request.user.is_authenticated:
        return redirect('login')
    student = get_object_or_404(Student, pk=id)

    if request.method == 'POST':
        student.studentName = request.POST.get('studentName')
        student.contactNumber = request.POST.get('contactNumber')
        student.birthdate = request.POST.get('birthdate')
        student.course = request.POST.get('course')
        student.totalfees = request.POST.get('totalfees')
        student.feesPaid = request.POST.get('feesPaid')
        student.save()
        messages.success(request, "Student updated successfully!")
        return redirect('home')

    return render(request, 'core/edit_student.html', {'student': student})


# Delete student
def delete_student(request, id):
    if not request.user.is_authenticated:
        return redirect('login')
    student = get_object_or_404(Student, pk=id)
    student.delete()
    messages.success(request, "Student deleted successfully!")

    return redirect('home')
