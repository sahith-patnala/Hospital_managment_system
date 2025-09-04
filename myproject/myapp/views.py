

from django.shortcuts import render,redirect
from django.http import HttpResponse
import joblib
import numpy as np
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.models import User, auth
from .models import Appointment
from .models import data

# Load the model and scaler
model = joblib.load(settings.MODEL_PATH)
scaler = joblib.load(settings.SCALER_PATH)

def index(request):
    return render(request,'index.html')

def index1(request):
    return render(request,'index1.html')
# def register(request):
#     return render(request,'register.html')
# def login(request):
#     return render(request,'login.html')

def home(request):
    return render(request, 'home.html')

def predict(request):
    if request.method == 'GET':
        # Extract data from request
        try:
            n1 = float(request.GET.get('n1'))
            n2 = float(request.GET.get('n2'))
            n3 = float(request.GET.get('n3'))
            n4 = float(request.GET.get('n4'))
            n5 = float(request.GET.get('n5'))
            n6 = float(request.GET.get('n6'))
            n7 = float(request.GET.get('n7'))
            n8 = float(request.GET.get('n8'))

            # Convert to numpy array and reshape
            data = np.array([n1, n2, n3, n4, n5, n6, n7, n8]).reshape(1, -1)
            
            # Standardize the data
            data = scaler.transform(data)
            
            # Make prediction
            prediction = model.predict(data)
            result = "Positive" if prediction[0] == 1 else "Negative"
            
            return render(request, 'result.html', {'result': result})
        except Exception as e:
            return HttpResponse(f"Error: {e}")

    return render(request, 'home.html')
# def appionment(request):
#     if request.method=='POST':
#         name=request.POST.get('name')
#         email= request.POST.get('email')
#         phone=request.POST.get('phone')
#         department=request.POST.get('department')
#         date = request.POST.get('date')
#         time = request.POST.get('time')
#         Appionment=appionment(name=name,email=email,phone=phone,department=department,date=date,time=time)
#         Appionment.save()
#         messages.SUCCESS(request,'Your appionment was updated successfully!')

#     return render(request,'appionment.html')


# def appionement(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         phone = request.POST.get('phone')
#         department = request.POST.get('department')
#         date = request.POST.get('date')
#         time = request.POST.get('time')

#         # Create and save the appointment
#         appointment = Appointment(
#             name=name,
#             email=email,
#             phone=phone,
#             department=department,
#             date=date,
#             time=time
#         )
#         appointment.save()

#         messages.success(request, 'Your appionment was updated successfully!')
#         # return redirect('home')
    
#     return render(request, 'appionement.html')

def appointment(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        department = request.POST.get('department')
        date = request.POST.get('date')
        time = request.POST.get('time')

        # Create and save the appointment
        new_appointment = Appointment(
            name=name,
            email=email,
            phone=phone,
            department=department,
            date=date,
            time=time
        )
        new_appointment.save()

        messages.success(request, 'Your appointment was updated successfully!')
        # Optionally, redirect to another page
        # return redirect('home')

    return render(request, 'appointment.html')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email already exists')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username already exists')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password1)
                user.save()
                return redirect('login')
        else:
            messages.info(request, 'Passwords do not match')
            return redirect('register')
    return render(request,'register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return render(request, 'index1.html')
        else:
            messages.info(request, 'Invalid credentials')
            return redirect('login')
    else:
        return render(request, 'login.html')
    



def logout(request):
    auth.logout(request)
    return render(request,'index.html')

def relief(request):
    return render(request,'relief_source.html')

def articles(request):
    return render(request,'articles.html')

def youtube(request):
    return render(request,'youtube.html')

def self(request):
    return render(request,'self.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def help(request):
    return render(request,'help.html')