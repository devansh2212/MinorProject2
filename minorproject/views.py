from django.shortcuts import render,redirect
from django.http import HttpResponse
from doctor.models import *
from patient.models import *


def home(request):
    key = request.session.get('key')
    context = {
        'key': key
    }
    return render(request,'minorproject/home.html',context)


def profile(request, user):
	key = request.session.get('key')
	print(request.user)
	userid = User.objects.get(username=request.user)
	print(userid)
	# if request.user:
	# 	status = request.user
	if request.method == "POST":
		print(request.POST['name'])
		if key == "P":
			update = Patient.objects.get(username=userid)
			update.name = request.POST['name']
			update.phone = request.POST['phone']
			update.email = request.POST['email']
			update.gender = request.POST['gender']
			update.age = request.POST['age']
			update.blood = request.POST['blood']
			update.address = request.POST['address']
			userid.username=request.POST['name']
			userid.save()
			update.save()
			return redirect('minor-home')
		else:
			update = Doctor.objects.get(username=userid)
			update.name = request.POST['name']
			update.phone = request.POST['phone']
			update.email = request.POST['email']
			update.gender = request.POST['gender']
			update.age = request.POST['age']
			update.department=request.POST['department']     
			update.address = request.POST['address']
			update.Specializations=request.POST['specializations']
			userid.username=request.POST['name']
			userid.save()
			update.save()
			return redirect('minor-home')


	if key == "P":
		userdata = Patient.objects.get(username=userid)
		return render(request  , 'patient/profile.html',{'userdata' : userdata , 'user':user})

	else:
		userdata  = Doctor.objects.get(username=userid)
		return render(request  , 'doctor/profile.html',{'userdata' : userdata , 'user':user})


	return redirect('minor-home')

def dashboard(request,user):
    key = request.session.get('key')
    if request.method=="GET":
        if key=="D":
            return render(request,"doctor/dashboard.html")
        else:
            return render(request,"patient/dashboard.html")
    else:
        return HttpResponse("Error 404!")
    
def logins(request):
    return render(request,'minorproject/logins.html')

def search(request):
    return render(request,'minorproject/search.html')