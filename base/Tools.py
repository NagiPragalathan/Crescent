from .models import Gallery,Team,logo

def get_vals(request,data):
    datas = []
    for i in data:
        datas.append(request.POST.get(i))
    return data

def get_images():
    images = Gallery.objects.all()
    cat = []
    temp = []
    items = []
    for i in images:
        cat.append(i.categories)
    for i in list(set(cat)):
        temp = []
        for j in images:
            if i == j.categories :
                temp.append(j)
        items.append(temp)
    return [items,images]

def get_team():
    images = Team.objects.all()
    cat = []
    temp = []
    items = []
    for i in images:
        cat.append(i.categories)
    for i in list(set(cat)):
        temp = []
        for j in images:
            if i == j.categories :
                temp.append(j)
        items.append(temp)
    return items

def reguler_datas(data=False):
    out = dict()
    logo_ = logo.objects.all()
    last_logo = logo.objects.latest("L_id")
    if data:
        out = {'logo':last_logo,'logo_collection':logo_[::-1]}
        out = dict(out,**data)
    else:
        out = {'logo':last_logo,'logo_collection':logo_[::-1]}
    return out
