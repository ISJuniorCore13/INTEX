from django.shortcuts import render

# Create your views here.
def loginPageView(request):
    return render(request, 'login/index.html')
def signupPageView(request):
    context = {
        "message": ''
    }
    return render(request, 'login/signup.html',context)
def enterPageView(request):
    msg = "Success"    

    f_name = request.POST.get('first')
    l_name = request.POST.get('last')
    pwd = request.POST.get('password')
    cpwd = request.POST.get('confirmpassword')
    email = request.POST.get('email')


    if f_name == '' or l_name == '' or pwd == '' or cpwd == '' or email == '':
        msg = "Please make sure the information is correct."


    context = {
        "message": msg
    }
    return render(request, 'login/signup.html', context)