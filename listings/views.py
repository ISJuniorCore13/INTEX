from django.shortcuts import render

# Create your views here.
def indexPageView(request):

    featured_list = ["Web Developer", "Software Engineer"]
    searched_list = []

    context = {
        "featured" : featured_list,
        "searched" : searched_list
    }

    return render(request, 'listings/listings.html', context)

def searchPageView(request):
    featured_list = []
    searched_list = []

    context = {
        "featured" : featured_list,
        "searched" : searched_list
    }

    return render(request, 'listings/listings.html', context)

def jobPostView(request, job_title, jobListing_id):
    context = {
        "job_title" : job_title,
        "jobListing_id" : jobListing_id
    }
    return render(request, 'listings/post.html', context)