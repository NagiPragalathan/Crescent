from django.shortcuts import render
from .models import Gallery,Team,logo
from .Tools import get_images,get_team,reguler_datas

# Create your views here.

def home(request):
    return render(request,"old/home.html")

def admin(request):
    item = get_images()
    return render(request,"pages/empty.html",reguler_datas({"categories":item[0],"images":item[1]}))


#...............gallery.......................................
def gallery(request):
    item = get_images()
    return render(request,"about_us/gallery.html",reguler_datas({"categories":item[0],"images":item[1]}))
#............................................................
# upload image...............................................
def upload_image(request):
    categories = request.POST.get("Category")
    image = request.FILES["image_file"]
    update = Gallery(image=image,categories=categories)
    update.save()
    return render(request,"about_us/team.html")

def delete_image(request):
    id = request.POST.get("id")
    image = Gallery.objects.get(G_id=id)
    image.delete()
    return render(request,"about_us/team.html")
#..............................................................

def aboutus(request):
    return render(request,"about_us/team.html",reguler_datas({"team":get_team()}))


# upload team ...............................
def admin_team(request):
    return render(request,'pages/team.html',reguler_datas({"team":get_team()}))

def update_team(request):
    name = request.POST.get("name")
    Category = request.POST.get("Category")
    position = request.POST.get("position")
    image = request.FILES["image_file"]
    db_obj = Team(Name=name,categories=Category,image=image,position=position)
    db_obj.save()
    obj = Team.objects.all()
    for i in obj:
        print(i.Name,i.image)

    return render(request,'pages/team.html')

def delete_team(request):
    id = request.POST.get("id")
    image = Team.objects.get(Team_id=id)
    image.delete()
    return render(request,"about_us/team.html",reguler_datas())

#............................................................
#...............Logo.........................................
def update_logo(request):
    return render(request,"home/logo.html",reguler_datas())

def upload_logo(request):
    Reson = request.POST.get("#reson")
    image = request.FILES["#fileInput-single"]
    update = logo(image=image,Reson=Reson)
    update.save()
    return render(request,"home/logo.html")

def delete_logo(request):
    id = request.POST.get("id")
    size = len(logo.objects.all())
    if size > 1:
        image = logo.objects.get(L_id=id)
        image.delete()
    else:
        pass
    return render(request,"home/logo.html")

def set_logo(request):
    id = request.POST.get("id")
    image = logo.objects.get(L_id=id)
    image_ = image.image
    reson = image.Reson
    image.delete()
    obj = logo(image=image_,Reson=reson)
    obj.save()
    return render(request,"home/logo.html")
#............................................................

#...............birac........................................
def birac(request):
    return render(request,"about_us/birac.html",reguler_datas())


