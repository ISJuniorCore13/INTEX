from django.shortcuts import render

# Create your views here.
def indexPageView(request):

    featured_list = []
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