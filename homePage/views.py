from django.shortcuts import render

def indexPageView(request):
    aJobListing = ["Web Developer", "Software Engineer", "Data Analyst"]

    context = {
        "JobListings" : aJobListing
    }
    return render(request, 'homePage/index.html', context)

def addListingPageView(request):
    return render(request, 'homePage/addlisting.html')
