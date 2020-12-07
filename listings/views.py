from django.shortcuts import render
from .models import Job_Listing
# Create your views here.
def indexPageView(request):

    featured_list = []
    top_few = []
    searched_list = []

    few = 5

    featured_list = Job_Listing.objects.all().order_by('deadline_date')



    # if len(featured_list) < 5:
    #     few = len(featured_list)

    # for i in range(few):
    #     if len(searched_list) == 0:
    #         top_few = featured_list[i]
    #     else:
    #         top_few = top_few + featured_list[i]

    # featured_list = top_few 

    context = {
        "message" : "feat",
        "featured" : featured_list,
        "searched" : searched_list
    }

    return render(request, 'listings/listings.html', context)

def searchPageView(request):
    from django.db.models import Q
    import re
    from collections import Counter
    from itertools import repeat, chain

    featured_list = []
    searched_list = []

    ss = request.POST.get('search')

    if ss is not None:
        ss = ss.split()
        print(ss)
        for i in range(len(ss)):
            if len(searched_list) == 0:
                searched_list = Job_Listing.objects.filter(
                        Q(listing_description__contains=ss[i]) |  
                        Q(job_title__contains=ss[i]) |
                        # Q(employer__employer_name__contains=ss[i]) |
                        Q(job_state__contains=ss[i]) |
                        Q(job_city__contains=ss[i]) |
                        Q(job_description__contains=ss[i]) 
                        )
            else:
                next_word_search = Job_Listing.objects.filter(
                        Q(listing_description__contains=ss[i]) |  
                        Q(job_title__contains=ss[i]) |
                        # Q(employer__employer_name__contains=ss[i]) |
                        Q(job_state__contains=ss[i]) |
                        Q(job_city__contains=ss[i]) |
                        Q(job_description__contains=ss[i]) 
                        )
                if len(next_word_search) > 0:
                    searched_list= list(chain(searched_list,next_word_search))


        if len(searched_list) > 1:
            # searched_list = sorted(searched_list,key=searched_list.count,reverse=True)
            unique = []
            [unique.append(item) for item in searched_list if item not in unique]
            searched_list = unique

    # for j in searched_list:
    #     print(j.job_title)
    #     print(j.employer_id)
    #     print(j.listing_description)
    #     print(j.job_description)

    context = {
        "message" : "",
        "featured" : featured_list,
        "searched" : searched_list
    }

    return render(request, 'listings/listings.html', context)

def jobPostView(request, job_title, jobListing_id):

    job_object = Job_Listing.objects.get(id = jobListing_id)
    context = {
        "job_object" : job_object,
        "job_title" : job_title,
        "jobListing_id" : jobListing_id
    }
    return render(request, 'listings/post.html', context)