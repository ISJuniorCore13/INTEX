from django.contrib import admin
from .models import Minority_Type, Education, User, Skill, User_Skill, Employer_Size, Employer, Job_Type, Job_Listing, Job_Skill, External_Application_Rating, Application

# Register your models here.
admin.site.register(Minority_Type)
admin.site.register(Education)
admin.site.register(User)
admin.site.register(Skill)
admin.site.register(User_Skill)
admin.site.register(Employer_Size)
admin.site.register(Employer)
admin.site.register(Job_Type)
admin.site.register(Job_Listing)
admin.site.register(Job_Skill)
admin.site.register(External_Application_Rating)
admin.site.register(Application)
