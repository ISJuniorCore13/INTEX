from django.shortcuts import render
from listings.models import Job_Listing, Employer, Job_Type, External_Application_Rating

def indexPageView(request):
    aJobListing = ["Web Developer", "Software Engineer", "Data Analyst"]

    context = {
        "JobListings" : aJobListing
    }
    return render(request, 'homePage/index.html', context)

def addListingPageView(request):
    return render(request, 'homePage/addlisting.html')
    
def editListingPageView(request,edit_id):
    job_to_edit = Job_Listing.objects.get(id=int(edit_id))
    
    context = { 
        "job" : job_to_edit
    }
    return render(request, 'homePage/addlisting.html', context)