from django.shortcuts import render
from listings.models import Applicant, Employer, Employer_Size
from django.contrib.auth.models import User, Group
from datetime import datetime

# Create your views here.
def loginPageView(request):
    return render(request, 'login/index.html')
def signupPageView(request,sup_type):
    context = {
        "message": sup_type
    }
    return render(request, 'login/signup.html',context)
def enterPageView(request):
    msg = "Success"    

    f_name = request.POST.get('first')
    l_name = request.POST.get('last')
    pwd = request.POST.get('password')
    cpwd = request.POST.get('confirmpassword')
    email = request.POST.get('email')
    sup_type = request.POST.get('sup_type')

    if f_name == '' or l_name == '' or pwd == '' or cpwd == '' or email == '':
        msg = "Please make sure the information is correct."
    else:
        # create user
        groups = []

        if sup_type == 'Applicant':
            groups = Group.objects.get(name='applicant')
        elif sup_type == 'Employer':
            groups = Group.objects.get(name='employer')


        User.objects.create(username=email, 
                            password=pwd,
                            date_joined=datetime.now()
                            )

        user =  User.objects.get(username=email)
        groups.user_set.add(user)

        size = Employer_Size.objects.all()[0]

        if sup_type == 'Applicant':
            Applicant.objects.create(username=email,
                                    first_name=f_name,
                                    last_name=l_name,
                                    email_address = email,
                                    user=user)
        elif sup_type == 'Employer':
            Employer.objects.create(employer_name=f_name,
                                    employer_email=email,
                                    size = size,
                                    user=user) 
            


    context = {
        "message": msg
    }
    return render(request, 'login/signup.html', context)