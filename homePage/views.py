from django.shortcuts import render, redirect
from listings.models import Job_Listing, Employer, Job_Type
from datetime import datetime, date

def indexPageView(request):
    aJobListing = ["Web Developer", "Software Engineer", "Data Analyst"]

    context = {
        "JobListings" : aJobListing
    }
    return render(request, 'homePage/index.html', context)

def addListingPageView(request):
    return render(request, 'homePage/addlisting.html')

def submitAddListingPageView(request):
    listing_description = request.POST.get('listing_description')
    job_title = request.POST.get('job_title')
    job_description = request.POST.get('job_description')
    
    job_city = request.POST.get('job_city')
    job_state = request.POST.get('job_state')
    job_zip = request.POST.get('job_zip')
    link_to_application = request.POST.get('link_to_application')
    wage_range = request.POST.get('wage_range')
    relocation_assistance = request.POST.get('relocation_assistance')
    extra_documents = request.POST.get('extra_documents')
    deadline_date = request.POST.get('deadline_date')
    user_id = request.POST.get('user_id')


    deadline_date = request.POST.get('deadline_date')
    print(deadline_date)

    deadline_date = datetime.strptime(deadline_date, "%Y-%m-%d")
    print(deadline_date)

    job_type = request.POST.get('job_type')
    print(job_type)

    job_type = Job_Type.objects.get(job_type_description = job_type)

    job_type = job_type.id

    user_id = int(user_id)
    employer_id = Employer.objects.get(user = user_id)

    employer_id = employer_id.id

    if relocation_assistance == 0 :
        relocation_assistance = True
    else :
        relocation_assistance = False

    if extra_documents == 0 :
        extra_documents = True
    else :
        extra_documents = False

    Job_Listing.objects.create(listing_description=listing_description, job_title=job_title, job_description=job_description,
        job_type_id=job_type, employer_id=employer_id, job_city=job_city,
        job_link_to_application=link_to_application, job_state=job_state, job_zip_code=job_zip, job_wage_range= wage_range,
        relocation_assistance=relocation_assistance, deadline_date=deadline_date, still_open=True,requires_additional_documents=extra_documents)

    context = {
        "message" : "Survey Submitted Successfully"
    }
    

    return redirect('http://127.0.0.1:8000/listings/',context)
    

def updateListingPageView(request):
    listing_description = request.POST.get('listing_description')
    job_title = request.POST.get('job_title')
    job_description = request.POST.get('job_description')
    
    job_city = request.POST.get('job_city')
    job_state = request.POST.get('job_state')
    job_zip = request.POST.get('job_zip')
    link_to_application = request.POST.get('link_to_application')
    wage_range = request.POST.get('wage_range')
    relocation_assistance = request.POST.get('relocation_assistance')
    extra_documents = request.POST.get('extra_documents')
    deadline_date = request.POST.get('deadline_date')


    deadline_date = request.POST.get('deadline_date')
    deadline_date = datetime.strptime(deadline_date, "%Y-%m-%d")

    job_type = request.POST.get('job_type')
    job_type = Job_Type.objects.get(job_type_description = job_type)
    job_type = job_type.id

    user_id = request.POST.get('user_id')
    user_id = int(user_id)

    employer_id = Employer.objects.get(user = user_id)
    employer_id = employer_id.id

    job_id = request.POST.get('job_id')
    job_id = int(job_id)

    if relocation_assistance == 0 :
        relocation_assistance = True
    else :
        relocation_assistance = False

    if extra_documents == 0 :
        extra_documents = True
    else :
        extra_documents = False

    listing_to_update = Job_Listing.objects.filter(id=job_id)
    print(job_id)
    listing_to_update.update(listing_description=listing_description, 
                            job_title=job_title, 
                            job_description=job_description,
                            job_type_id=job_type, job_city=job_city,
                            job_link_to_application=link_to_application, 
                            job_state=job_state, 
                            job_zip_code=job_zip, 
                            job_wage_range= wage_range,
                            relocation_assistance=relocation_assistance, 
                            deadline_date=deadline_date, 
                            still_open=True,
                            requires_additional_documents=extra_documents)

    context = {
        "message" : "Survey Updated Successfully"
    }
    

    return redirect('http://127.0.0.1:8000/listings/',context)

def editListingPageView(request,edit_id):
    job_to_edit = Job_Listing.objects.get(id=int(edit_id))
    
    context = { 
        "job" : job_to_edit
    }
    return render(request, 'homePage/addlisting.html', context)

def removeListingPageView(request):

    remove_id = request.POST.get('remove_id')
    remove_id = int(remove_id)
    Job_Listing.objects.get(id=remove_id).delete()
    return redirect('http://127.0.0.1:8000/listings/')