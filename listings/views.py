from django.shortcuts import render, redirect
from .models import Job_Listing, Employer, Job_Type, External_Application_Rating
# Create your views here.
def indexPageView(request):

    featured_list = []
    searched_list = []

    featured_list = Job_Listing.objects.all().order_by('deadline_date')

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

            employers = Employer.objects.filter(employer_name__contains=ss[i])
            job_types = Job_Type.objects.filter(job_type_description__contains=ss[i])

            if len(searched_list) == 0:

                searched_list = Job_Listing.objects.filter(
                        Q(listing_description__contains=ss[i]) |  
                        Q(job_title__contains=ss[i]) |
                        Q(employer_id__in=employers) |
                        Q(job_type_id__in=job_types) |
                        Q(job_state__contains=ss[i]) |
                        Q(job_city__contains=ss[i]) |
                        Q(job_description__contains=ss[i]) 
                        )
            else:
                next_word_search = Job_Listing.objects.filter(
                        Q(listing_description__contains=ss[i]) |  
                        Q(job_title__contains=ss[i]) |
                        Q(employer_id__in=employers) |
                        Q(job_type_id__in=job_types) |
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

def matchbox_recommender(org_id_value, job_id_value) :
    import urllib
    from urllib import request
    import json 
    import ast

    data =  {
            "Inputs": {
                    "input1":
                    {
                        "ColumnNames": ["organization_id", "job_title_id"],
                        "Values": [ [ org_id_value, job_id_value ], ]
                    },      }}
    body = str.encode(json.dumps(data))
    url = 'https://ussouthcentral.services.azureml.net/workspaces/1993b100a23d4cda87098e65eaad4e08/services/c723501ba2634ed6904ac66117f339b7/execute?api-version=2.0&details=true'
    api_key = 'fQzn6wIKxzgxA3gmGl+j8KnMAu6JPXIe9M8tgiFXWAbYuf2JSIaQ/4WM5B0sBQUpMURAwPqY3ip3/pZkgyfzdQ==' # Replace this with the API key for the web service
    headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

    req = urllib.request.Request(url, body, headers) 
    response = urllib.request.urlopen(req)

    result = response.read()
    result = result.decode('utf-8')
    result = ast.literal_eval(result)
    results = [
        result['Results']['output1']['value']['Values'][0][0],
        result['Results']['output1']['value']['Values'][0][1],
        result['Results']['output1']['value']['Values'][0][2],
        result['Results']['output1']['value']['Values'][0][3],
        result['Results']['output1']['value']['Values'][0][4],
        result['Results']['output1']['value']['Values'][0][5],
        result['Results']['output1']['value']['Values'][0][6],
        result['Results']['output1']['value']['Values'][0][7],
        result['Results']['output1']['value']['Values'][0][8],
        result['Results']['output1']['value']['Values'][0][9]
    ]
    return results

def jobPostView(request, job_title, jobListing_id):

    job_object = Job_Listing.objects.get(id = jobListing_id)
    results = matchbox_recommender(job_object.employer.id, jobListing_id)
    rec_jobs = []

    job_docs = job_object.requires_additional_documents

    reloc = job_object.relocation_assistance

    if reloc == True :
        reloc = 'Yes'
    else :
        reloc = 'No'

    if job_docs == True :
        job_docs = 'Yes'
    else :
        job_docs = 'No'

    for r in results :
        rec_jobs.append(Job_Listing.objects.get(id = r))

    context = {
        "job_object" : job_object,
        "job_title" : job_title,
        "jobListing_id" : jobListing_id,
        "recommender_results" : rec_jobs,
        "job_docs" : job_docs,
        "reloc" : reloc,
    }
    return render(request, 'listings/post.html', context)

def externalAppSurveyView(request):
    return render(request, 'listings/externalAppSurvey.html')

def surveySubmitView(request):
    ease = request.POST.get('ease')
    clarity = request.POST.get('clarity')
    extra = request.POST.get('extra')

    if extra == 0 :
        extra = True
    else :
        extra = False

    External_Application_Rating.objects.create(ease_of_application=ease, 
        clarity_of_application=clarity, more_than_resume=extra)

    context = {
        "message" : "Survey Submitted Successfully"
    }
    

    return redirect('https://bcr13.herokuapp.com/listings/', context)