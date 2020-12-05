from django.db import models
from datetime import datetime

# Create your models here.
class Minority_Types(models.Model):
    minority_type = models.CharField(max_length=50)
    def __str__(self):
        return str(self.minority_type)

class Education(models.Model):
    education_level_description = models.CharField(max_length=50)
    def __str__(self):
        return str(self.education_level_description)

class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email_address = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=10)
    street_address = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=2)
    zip_code = models.CharField(max_length=10)
    birth_date = models.DateTimeField(default=datetime.now)
    # resume = models.FileField(upload_to='documents/%Y/%m/%d')
    photo = models.ImageField(upload_to='photos', blank=True)
    education_lvl = models.ForeignKey(Education, on_delete=models.CASCADE)
    minority_status = models.ManyToManyField(Minority_Types)

    def __str__(self):
        return str(self.first_name) + ' ' + str(self.last_name)


skill_set = (
    ('a/btesting','A/BTESTING')
    ,('adobeillustrator','ADOBEILLUSTRATOR')
    ,('adobephotoshop','ADOBEPHOTOSHOP')
    ,('ai','AI')
    ,('ajax','AJAX')
    ,('analytical','ANALYTICAL')
    ,('analytics','ANALYTICS')
    ,('android','ANDROID')
    ,('angular','ANGULAR')
    ,('angularjs','ANGULARJS')
    ,('apache','APACHE')
    ,('apex','APEX')
    ,('apirest','APIREST')
    ,('apis','APIS')
    ,('arduino','ARDUINO')
    ,('asp.net','ASP.NET')
    ,('asp.netcore','ASP.NETCORE')
    ,('asp.netmvc','ASP.NETMVC')
    ,('assembleur','ASSEMBLEUR')
    ,('assembly','ASSEMBLY')
    ,('autocad','AUTOCAD')
    ,('autonome','AUTONOME')
    ,('awk','AWK')
    ,('aws','AWS')
    ,('backend','BACKEND')
    ,('bash','BASH')
    ,('bigdata','BIGDATA')
    ,('bootstrap','BOOTSTRAP')
    ,('c++','C++')
    ,('cassandra','CASSANDRA')
    ,('centreon','CENTREON')
    ,('certifications','CERTIFICATIONS')
    ,('cgi','CGI')
    ,('cics','CICS')
    ,('cisco','CISCO')
    ,('cloudcomputing','CLOUDCOMPUTING')
    ,('coaching','COACHING')
    ,('cobol','COBOL')
    ,('codeigniter','CODEIGNITER')
    ,('cognos','COGNOS')
    ,('collaboration','COLLABORATION')
    ,('communication','COMMUNICATION')
    ,('consulting','CONSULTING')
    ,('contentmarketing','CONTENTMARKETING')
    ,('continuousintegration','CONTINUOUSINTEGRATION')
    ,('controlsystems','CONTROLSYSTEMS')
    ,('cordova','CORDOVA')
    ,('creatingdata','CREATINGDATA')
    ,('css','CSS')
    ,('cucumber','CUCUMBER')
    ,('customerservice','CUSTOMERSERVICE')
    ,('cvs','CVS')
    ,('dataanalytics','DATAANALYTICS')
    ,('dataengineers','DATAENGINEERS')
    ,('datamanagement','DATAMANAGEMENT')
    ,('datamining','DATAMINING')
    ,('dataquality','DATAQUALITY')
    ,('datavisualisation','DATAVISUALISATION')
    ,('datavisualization','DATAVISUALIZATION')
    ,('datawarehouse','DATAWAREHOUSE')
    ,('databasedevelopers','DATABASEDEVELOPERS')
    ,('databases','DATABASES')
    ,('dax','DAX')
    ,('db','DB')
    ,('deeplearning','DEEPLEARNING')
    ,('design','DESIGN')
    ,('designpatterns','DESIGNPATTERNS')
    ,('designer','DESIGNER')
    ,('desk','DESK')
    ,('devops','DEVOPS')
    ,('diagnostics','DIAGNOSTICS')
    ,('digitalmarketing','DIGITALMARKETING')
    ,('django','DJANGO')
    ,('documentation','DOCUMENTATION')
    ,('dom','DOM')
    ,('drupal','DRUPAL')
    ,('dynamodb','DYNAMODB')
    ,('e-commerce','E-COMMERCE')
    ,('eclipse','ECLIPSE')
    ,('electronics','ELECTRONICS')
    ,('engineering','ENGINEERING')
    ,('ensemble','ENSEMBLE')
    ,('entityframework','ENTITYFRAMEWORK')
    ,('etl','ETL')
    ,('extjs','EXTJS')
    ,('fortran','FORTRAN')
    ,('foundation','FOUNDATION')
    ,('frontend','FRONTEND')
    ,('full-stack','FULL-STACK')
    ,('g\\xc\\xanielogiciel','G\\XC\\XANIELOGICIEL')
    ,('git','GIT')
    ,('go','GO')
    ,('googlemaps','GOOGLEMAPS')
    ,('grav','GRAV')
    ,('groovy','GROOVY')
    ,('grunt','GRUNT')
    ,('gsm','GSM')
    ,('gulp','GULP')
    ,('gwt','GWT')
    ,('hadoop','HADOOP')
    ,('hardware','HARDWARE')
    ,('hbase','HBASE')
    ,('hibernate','HIBERNATE')
    ,('hive','HIVE')
    ,('html','HTML')
    ,('http','HTTP')
    ,('ia','IA')
    ,('implementation','IMPLEMENTATION')
    ,('informationsecurity','INFORMATIONSECURITY')
    ,('innovation','INNOVATION')
    ,('insights','INSIGHTS')
    ,('internet','INTERNET')
    ,('interpersonal','INTERPERSONAL')
    ,('ios','IOS')
    ,('iot','IOT')
    ,('iphone','IPHONE')
    ,('itil','ITIL')
    ,('javascript','JAVASCRIPT')
    ,('jcl','JCL')
    ,('jenkins','JENKINS')
    ,('joomla','JOOMLA')
    ,('jquery','JQUERY')
    ,('jsf','JSF')
    ,('json','JSON')
    ,('jsp','JSP')
    ,('junit','JUNIT')
    ,('laravel','LARAVEL')
    ,('leadership','LEADERSHIP')
    ,('less','LESS')
    ,('linux','LINUX')
    ,('listening','LISTENING')
    ,('lua','LUA')
    ,('mac','MAC')
    ,('machinelearning','MACHINELEARNING')
    ,('mariadb','MARIADB')
    ,('math\\xc\\xamatiques','MATH\\XC\\XAMATIQUES')
    ,('mathematics','MATHEMATICS')
    ,('matlab','MATLAB')
    ,('maven','MAVEN')
    ,('mentoring','MENTORING')
    ,('microsoft','MICROSOFT')
    ,('microsoftaccess','MICROSOFTACCESS')
    ,('microsoftazure','MICROSOFTAZURE')
    ,('microsoftexcel','MICROSOFTEXCEL')
    ,('microsoftoffice','MICROSOFTOFFICE')
    ,('microsoftpowerbi','MICROSOFTPOWERBI')
    ,('microsoftproject','MICROSOFTPROJECT')
    ,('microsoftvisual','MICROSOFTVISUAL')
    ,('microsoftwindows','MICROSOFTWINDOWS')
    ,('microstrategy','MICROSTRATEGY')
    ,('mobile','MOBILE')
    ,('mockito','MOCKITO')
    ,('modeling','MODELING')
    ,('mongodb','MONGODB')
    ,('msaccess','MSACCESS')
    ,('msexcel','MSEXCEL')
    ,('mssqlserver','MSSQLSERVER')
    ,('msvisio','MSVISIO')
    ,('msword','MSWORD')
    ,('multitasking','MULTITASKING')
    ,('mvvm','MVVM')
    ,('mysql','MYSQL')
    ,('nagios','NAGIOS')
    ,('networks','NETWORKS')
    ,('neuralnetworks','NEURALNETWORKS')
    ,('nhibernate','NHIBERNATE')
    ,('nlp','NLP')
    ,('node.js','NODE.JS')
    ,('nodejs','NODEJS')
    ,('nosql','NOSQL')
    ,('obiee','OBIEE')
    ,('objectivec','OBJECTIVEC')
    ,('operatingsystem','OPERATINGSYSTEM')
    ,('optimisations','OPTIMISATIONS')
    ,('oracle','ORACLE')
    ,('organizational','ORGANIZATIONAL')
    ,('pca','PCA')
    ,('pentaho','PENTAHO')
    ,('perl','PERL')
    ,('phonegap','PHONEGAP')
    ,('php','PHP')
    ,('pl/sql','PL/SQL')
    ,('postgresql','POSTGRESQL')
    ,('powerpoint','POWERPOINT')
    ,('powershell','POWERSHELL')
    ,('presentation','PRESENTATION')
    ,('prestashop','PRESTASHOP')
    ,('priorities','PRIORITIES')
    ,('problemsolving','PROBLEMSOLVING')
    ,('processing','PROCESSING')
    ,('programming','PROGRAMMING')
    ,('projectmanagement','PROJECTMANAGEMENT')
    ,('projectmanager','PROJECTMANAGER')
    ,('prototyping','PROTOTYPING')
    ,('pspice','PSPICE')
    ,('python','PYTHON')
    ,('qc','QC')
    ,('qlikview','QLIKVIEW')
    ,('r\\xc\\xaseau','R\\XC\\XASEAU')
    ,('redis','REDIS')
    ,('reporting','REPORTING')
    ,('reportingtools','REPORTINGTOOLS')
    ,('ruby','RUBY')
    ,('s\\xc\\xacurit\\xc\\xainformatique','S\\XC\\XACURIT\\XC\\XAINFORMATIQUE')
    ,('sap','SAP')
    ,('sas','SAS')
    ,('sass','SASS')
    ,('scala','SCALA')
    ,('scrum','SCRUM')
    ,('sdkandroid','SDKANDROID')
    ,('selenium','SELENIUM')
    ,('senchatouch','SENCHATOUCH')
    ,('sharepoint','SHAREPOINT')
    ,('shellunix','SHELLUNIX')
    ,('shiny','SHINY')
    ,('sip','SIP')
    ,('sixsigma','SIXSIGMA')
    ,('sketchup','SKETCHUP')
    ,('soa','SOA')
    ,('soap','SOAP')
    ,('softwareknowledge','SOFTWAREKNOWLEDGE')
    ,('spark','SPARK')
    ,('spring','SPRING')
    ,('springmvc','SPRINGMVC')
    ,('sql','SQL')
    ,('sqlserver','SQLSERVER')
    ,('sqlite','SQLITE')
    ,('strategicthinking','STRATEGICTHINKING')
    ,('svn','SVN')
    ,('swift','SWIFT')
    ,('swing','SWING')
    ,('symfony','SYMFONY')
    ,('t-sql','T-SQL')
    ,('tableau','TABLEAU')
    ,('technical','TECHNICAL')
    ,('telecom','TELECOM')
    ,('teradata','TERADATA')
    ,('training','TRAINING')
    ,('typescript','TYPESCRIPT')
    ,('ui/ux','UI/UX')
    ,('uml','UML')
    ,('unix','UNIX')
    ,('vb.net','VB.NET')
    ,('vba','VBA')
    ,('verbalcommunication','VERBALCOMMUNICATION')
    ,('visio','VISIO')
    ,('visualbasic','VISUALBASIC')
    ,('vmware','VMWARE')
    ,('wcf','WCF')
    ,('webanalytics','WEBANALYTICS')
    ,('webservices','WEBSERVICES')
    ,('webgl','WEBGL')
    ,('wi-fi','WI-FI')
    ,('wimax','WIMAX')
    ,('windows','WINDOWS')
    ,('windows','WINDOWS')
    ,('word','WORD')
    ,('wordpress','WORDPRESS')
    ,('wpf','WPF')
    ,('wsdl','WSDL')
    ,('xaml','XAML')
    ,('xhtml','XHTML')
    ,('xml','XML')
)

class Skill(models.Model):
    skill_description = models.CharField(max_length=30, choices=skill_set, default='a/btesting')

class User_Skills(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    skill_id = models.ForeignKey(Skill, on_delete=models.CASCADE)
    proficiency_lvl = models.IntegerField()
    def __str__(self):
        return str(self.user_id) + ' has ' + str(self.skill_id) + ' skill at ' + str(self.proficiency_lvl) + ' proficiency.'

class Employer_Size(models.Model):
    size_description = models.CharField(max_length=50)
    def __str__(self):
        return str(self.size_description)
class Employer(models.Model):
    size_id = models.ForeignKey(Employer_Size, on_delete=models.CASCADE)
    employer_name = models.CharField(max_length=30)
    employer_email= models.CharField(max_length=30)
    employer_logo = models.ImageField(upload_to='photos', blank=True)


class Job_Type(models.Model):
    job_type_description = models.CharField(max_length=30)


wage_ranges = (
    ('state minimum hourly wage', 'State Minimum Hourly Wage')
    ('10-19k yearly','10-19K Yearly'),
    ('20k-39k yearly','20k-39K Yearly'),
    ('40k-64k yearly','40k-64K Yearly'),
    ('65k-70k yearly','65k-70K Yearly'),
    ('70-99k yearly','70-99K Yearly'),
    ('100k+','100K+'),
    ('undisclosed','Undisclosed'),
)
class Job_Listing(models.Model):
    listing_description = models.CharField(max_length=30)
    job_title = models.CharField(max_length=30)
    job_description = models.CharField(max_length=255)
    job_type_id = models.ForeignKey(Job_Type, on_delete=models.CASCADE)
    job_street_address = models.CharField(max_length=50)
    job_city = models.CharField(max_length=50)
    job_state = models.CharField(max_length=2)
    job_zip_code = models.CharField(max_length=10)
    job_wage_range = models.CharField(max_length=50, choices=wage_ranges, default='state minimum hourly wage')
    relocation_assistance = models.BooleanField()
    transcript_required = models.BooleanField()
    cover_letter_required = models.BooleanField()
    gpa = models.BooleanField()
    letter_of_reccomendation = models.BooleanField()
    deadline_date = models.DateTimeField(default=datetime.now)
    still_open = models.BooleanField()
    def __str__(self):
        return self.listing_description

class Job_Skills(models.Model):
    job_listing_id = models.ForeignKey(Job_Listing, on_delete=models.CASCADE)
    skill_id = models.ForeignKey(Skill, on_delete=models.CASCADE)
    proficiency_lvl = models.IntegerField()
    def __str__(self):
        return str(self.job_listing_id) + ' has ' + str(self.skill_id) + ' skill at ' + str(self.proficiency_lvl) + ' proficiency.'


class External_Application_Rating(models.Model):
    ease_of_application = models.IntegerField()
    clarity_of_application = models.IntegerField()
    more_than_resume = models.BooleanField()
class Application(models.Model):
    rating = models.OneToOneField(External_Application_Rating, on_delete=models.CASCADE, blank=True)
    job_listing_id = models.ForeignKey(Job_Listing, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    application_date = models.DateTimeField(default=datetime.now)