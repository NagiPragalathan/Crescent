from django.db import models
from django.utils import timezone
# Create your models here.


class logo(models.Model):
    L_id = models.IntegerField(primary_key=True)
    Reson = models.CharField(max_length = 200)
    image = models.ImageField(upload_to='logo',default='images/user_image.png')
    last_updated_date = models.DateField(default=timezone.now())
    class Meta:
          get_latest_by = ['image']

class Gallery(models.Model):
    G_id = models.IntegerField(primary_key=True)
    image = models.ImageField(upload_to='Gallery/%Y/%m/%d',default='images/user_image.png')
    categories = models.CharField(max_length = 200)
    date = models.DateField(default=timezone.now())

class Events(models.Model):
    E_id = models.IntegerField(primary_key=True)
    image = models.ImageField(upload_to='Events/%Y/%m/%d',default='images/user_image.png')
    description = models.CharField(max_length = 200)
    categories = models.CharField(max_length = 200)
    type = models.CharField(max_length = 200)
    date = models.DateField(default=timezone.now())
    last_updated_date = models.DateField(default=timezone.now())

class Awards(models.Model):
    E_id = models.IntegerField(primary_key=True)
    Name = models.CharField(max_length = 200)
    image = models.ImageField(upload_to='Awards/%Y/%m/%d',default='images/user_image.png')
    description = models.CharField(max_length = 200)
    categories = models.CharField(max_length = 200)
    Awardee = models.CharField(max_length = 200)
    date = models.DateField(default=timezone.now())
    last_updated_date = models.DateField(default=timezone.now())

class Testimonials(models.Model):
    T_id = models.IntegerField(primary_key=True)
    Name = models.CharField(max_length = 200)
    position = models.CharField(max_length = 200)
    image = models.ImageField(upload_to='Testimonials/%Y/%m/%d',default='images/user_image.png')
    description = models.CharField(max_length = 200)
    categories = models.CharField(max_length = 200)
    last_updated_date = models.DateField(default=timezone.now())

class Team(models.Model):
    Team_id = models.IntegerField(primary_key=True)
    Name = models.CharField(max_length = 200)
    position = models.CharField(max_length = 200)
    image = models.ImageField(upload_to='Team/%Y/%m/%d',default='images/user_image.png')
    categories = models.CharField(max_length = 200)
    last_updated_date = models.DateField(default=timezone.now())


class Partners(models.Model):
    P_id = models.IntegerField(primary_key=True)
    categories = models.CharField(max_length = 200)
    image = models.ImageField(upload_to='Partners/%Y/%m/%d',default='images/user_image.png')
    Name = models.CharField(max_length = 200)

class Vision(models.Model):
    P_id = models.IntegerField(primary_key=True)
    list_detial = models.CharField(max_length = 200)
    last_updated_date = models.DateField(default=timezone.now())
    description = models.CharField(max_length = 200)

class Mission(models.Model):
    P_id = models.IntegerField(primary_key=True)
    list_detial = models.CharField(max_length = 200)
    last_updated_date = models.DateField(default=timezone.now())
    description = models.CharField(max_length = 200)

class Value(models.Model):
    P_id = models.IntegerField(primary_key=True)
    list_detial = models.CharField(max_length = 200)
    last_updated_date = models.DateField(default=timezone.now())
    description = models.CharField(max_length = 200)

class About(models.Model):
    P_id = models.IntegerField(primary_key=True)
    list_detial = models.CharField(max_length = 200)
    last_updated_date = models.DateField(default=timezone.now())
    description = models.CharField(max_length = 200)

class Latest_News(models.Model):
    L_id = models.IntegerField(primary_key=True)
    News = models.CharField(max_length = 200)
    last_updated_date = models.DateField(default=timezone.now())

class Facilities_developed(models.Model):
    FD_id = models.IntegerField(primary_key=True)
    topic = models.CharField(max_length = 200)
    content = models.CharField(max_length = 200)

class Carrer(models.Model):
    id              = models.IntegerField(primary_key=True)
    updated_date    = models.DateField(default=timezone.now())
    Name   = models.CharField(max_length = 200)
    image           = models.ImageField(upload_to='Carrer/%Y/%m/%d',default='carrer/Screenshot_3.png')
    Email            = models.CharField(max_length = 200)
    Message     = models.CharField(max_length = 200,default='designation')
    Subject      = models.CharField(max_length = 200,default='department')
    qualififcation  = models.CharField(max_length = 200,default='qualififcation')
    experience      = models.IntegerField(default=0)

class blog(models.Model):
    id              = models.IntegerField(primary_key=True)
    title           = models.CharField(max_length = 200,default='UnTitled')
    description     = models.CharField(max_length = 200,default = "Author not provied any description")
    content         = models.CharField(max_length = 2000,default = "Author not provied any description")
    blog_profile_img = models.CharField(max_length = 2000,default = "https://www.equalityhumanrights.com/sites/default/files/styles/listing_image/public/default_images/blog-teaser-default-full_5.jpg?itok=YOsTg-7X")
    categories = models.CharField(max_length = 200)
    updated_date    = models.DateField(default=timezone.now())

class Birac(models.Model):
    id              = models.IntegerField(primary_key=True)
    title           = models.CharField(max_length = 200,default='UnTitled')
    subtitle           = models.CharField(max_length = 200)
    description     = models.CharField(max_length = 200,default = "Author not provied any content")
    overview     = models.CharField(max_length = 200,default = "Author not provied any content")
    updated_date    = models.DateField(default=timezone.now())
    
class Tbi(models.Model):
    id              = models.IntegerField(primary_key=True)
    title           = models.CharField(max_length = 200,default='UnTitled')
    subtitle           = models.CharField(max_length = 200)
    description     = models.CharField(max_length = 200,default = "Author not provied any content")
    overview     = models.CharField(max_length = 200,default = "Author not provied any content")
    updated_date    = models.DateField(default=timezone.now())
    
class Sisfs(models.Model):
    id              = models.IntegerField(primary_key=True)
    title           = models.CharField(max_length = 200,default='UnTitled')
    subtitle           = models.CharField(max_length = 200)
    description     = models.CharField(max_length = 200,default = "Author not provied any content")
    overview     = models.CharField(max_length = 200,default = "Author not provied any content")
    updated_date    = models.DateField(default=timezone.now())
    
class EventsForm(models.Model):
    id              = models.IntegerField(primary_key=True)
    updated_date    = models.DateField(default=timezone.now())
    title = models.CharField(max_length = 200,default='title')
    Name   = models.CharField(max_length = 200)
    image           = models.ImageField(upload_to='EventsForm/%Y/%m/%d',default='carrer/Screenshot_3.png')
    Email            = models.CharField(max_length = 200)
    company     = models.CharField(max_length = 200,default='company')
    event      = models.CharField(max_length = 200,default='event')
    linkedin  = models.CharField(max_length = 200,default='linkedin')
    website      = models.CharField(max_length = 200,default='website')


class MentorConnectDB(models.Model):
    id              = models.IntegerField(primary_key=True)
    Content   = models.CharField(max_length = 2000)
    updated_date    = models.DateField(default=timezone.now())
    
    def __str__(self):
        return self.Content 

class MentorClinicDB(models.Model):
    id              = models.IntegerField(primary_key=True)
    Content   = models.CharField(max_length = 2000)
    updated_date    = models.DateField(default=timezone.now())
    
    def __str__(self):
        return self.Content 

class GlobalMarketConnectDB(models.Model):
    id              = models.IntegerField(primary_key=True)
    Content   = models.CharField(max_length = 2000)
    updated_date    = models.DateField(default=timezone.now())
    
    def __str__(self):
        return self.Content 

class DemodayDB(models.Model):
    id              = models.IntegerField(primary_key=True)
    Content   = models.CharField(max_length = 2000)
    updated_date    = models.DateField(default=timezone.now())
    
    def __str__(self):
        return self.Content 

class StateGovernmentFundingDB(models.Model):
    id              = models.IntegerField(primary_key=True)
    Content   = models.CharField(max_length = 2000)
    updated_date    = models.DateField(default=timezone.now())
    
    def __str__(self):
        return self.Content 

class CentralGovernmentFundingDB(models.Model):
    id              = models.IntegerField(primary_key=True)
    Content   = models.CharField(max_length = 2000)
    updated_date    = models.DateField(default=timezone.now())
    
    def __str__(self):
        return self.Content 

class AngelInvestorsDB(models.Model):
    id              = models.IntegerField(primary_key=True)
    Content   = models.CharField(max_length = 2000)
    updated_date    = models.DateField(default=timezone.now())
    
    def __str__(self):
        return self.Content 

class VentureCapitalistDB(models.Model):
    id              = models.IntegerField(primary_key=True)
    Content   = models.CharField(max_length = 2000)
    updated_date    = models.DateField(default=timezone.now())
    
    def __str__(self):
        return self.Content 

class angelInvestorDB(models.Model):
    id              = models.IntegerField(primary_key=True)
    Content   = models.CharField(max_length = 2000)
    updated_date    = models.DateField(default=timezone.now())
    
    def __str__(self):
        return self.Content 

class new_venturesDB(models.Model):
    id              = models.IntegerField(primary_key=True)
    Content   = models.CharField(max_length = 2000)
    updated_date    = models.DateField(default=timezone.now())
    
    def __str__(self):
        return self.Content 


class WhoAreWe(models.Model):
    id              = models.IntegerField(primary_key=True)
    SubHeading   = models.CharField(max_length = 2000)
    Point1   = models.CharField(max_length = 2000)
    Point2   = models.CharField(max_length = 2000)
    Point3   = models.CharField(max_length = 2000)
    Point4   = models.CharField(max_length = 2000)
    image           = models.ImageField(upload_to='WhoAreWe/%Y/%m/%d',default='carrer/Screenshot_3.png')
    
    updated_date    = models.DateField(default=timezone.now())
    
    def __str__(self):
        return self.SubHeading 

class HOME_TESTIMONIAL(models.Model):
    id              = models.IntegerField(primary_key=True)
    Testimonial_content   = models.CharField(max_length = 2000)
    Name   = models.CharField(max_length = 2000)
    Designation   = models.CharField(max_length = 2000)
    image           = models.ImageField(upload_to='HOME_TESTIMONIAL/%Y/%m/%d',default='carrer/Screenshot_3.png')
    updated_date    = models.DateField(default=timezone.now())
    
    def __str__(self):
        return self.Testimonial_content

class Contact_SECTION(models.Model):
    id              = models.IntegerField(primary_key=True)
    Title   = models.CharField(max_length = 2000)
    Address   = models.CharField(max_length = 2000)
    Phone_number   = models.CharField(max_length = 2000)
    E_Mail           = models.ImageField(upload_to='HOME_TESTIMONIAL/%Y/%m/%d',default='carrer/Screenshot_3.png')
    updated_date    = models.DateField(default=timezone.now())
    
    def __str__(self):
        return self.Title


class Investors(models.Model):
    id              = models.IntegerField(primary_key=True)
    Title   = models.CharField(max_length = 2000)
    image           = models.ImageField(upload_to='Investors/%Y/%m/%d',default='carrer/Screenshot_3.png')
    updated_date    = models.DateField(default=timezone.now())
    
    def __str__(self):
        return self.Title

class International_Partners(models.Model):
    id              = models.IntegerField(primary_key=True)
    Title   = models.CharField(max_length = 2000)
    image           = models.ImageField(upload_to='Investors/%Y/%m/%d',default='carrer/Screenshot_3.png')
    updated_date    = models.DateField(default=timezone.now())
    
    def __str__(self):
        return self.Title

class Govt_Tie(models.Model):
    id              = models.IntegerField(primary_key=True)
    Title   = models.CharField(max_length = 2000)
    image           = models.ImageField(upload_to='Investors/%Y/%m/%d',default='carrer/Screenshot_3.png')
    updated_date    = models.DateField(default=timezone.now())
    
    def __str__(self):
        return self.Title

class UploadImage(models.Model):
    id              = models.IntegerField(primary_key=True)
    Title   = models.CharField(max_length = 2000)
    content   = models.CharField(max_length = 2000)
    image           = models.ImageField(upload_to='Investors/%Y/%m/%d',default='carrer/Screenshot_3.png')
    updated_date    = models.DateField(default=timezone.now())
    
    def __str__(self):
        return self.Title

class OurStartup(models.Model):
    id              = models.IntegerField(primary_key=True)
    Title   = models.CharField(max_length = 2000)
    program   = models.CharField(max_length = 2000)
    image           = models.ImageField(upload_to='Investors/%Y/%m/%d',default='carrer/Screenshot_3.png')
    date    = models.DateField(default=timezone.now())
    categories = models.CharField(max_length = 2000)
    updated_date    = models.DateField(default=timezone.now())
    
    def __str__(self):
        return self.Title