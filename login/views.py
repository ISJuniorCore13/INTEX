from django.shortcuts import render, redirect
from listings.models import Applicant, Employer, Employer_Size, Education
from django.contrib.auth.models import User, Group
from datetime import datetime

# Create your views here.
def loginPageView(request):
    return render(request, 'login/index.html')
def signupPageView(request,sup_type):
    context = {
        "message": sup_type
        ,"msg2": ''
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
                            date_joined=datetime.now(),
                            first_name=f_name,
                            password="pbkdf2_sha256$216000$JgO4ONWgtSCj$iHd8ZCM6zysg0jn9cTbu/6Y1VvMkjMuOB2s1TtidO6w="
                            )


        user =  User.objects.get(username=email)
        user.set_password(pwd)
        user.save()
        groups.user_set.add(user)

        

        if sup_type == 'Applicant':
            edu = Education.objects.all()[0]
            Applicant.objects.create(first_name=f_name,
                                    last_name=l_name,
                                    email_address = email,
                                    user=user,
                                    education_lvl=edu)
        elif sup_type == 'Employer':
            size = Employer_Size.objects.all()[0]
            Employer.objects.create(employer_name=f_name,
                                    employer_email=email,
                                    size = size,
                                    user=user) 
            


    context = {
        "message": sup_type
        ,"msg2": msg
    }

    rtrn_object = render(request, 'login/signup.html', context)
    if msg == 'Success':
        rtrn_object = redirect('https://bcr13.herokuapp.com/accounts/login/')
    return rtrn_object
        