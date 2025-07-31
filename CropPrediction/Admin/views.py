from django.shortcuts import render,redirect
from Admin.models import *
from Owner.models import *
from Guest.models import *

def homepage(request):
    if "aid" in request.session:
        return render(request,'Admin/Homepage.html')     
    else:
        return redirect("Guest:login")

def brand(request):
    brand=tbl_brand.objects.all()
    if request.method=="POST":
        tbl_brand.objects.create(brand_name=request.POST.get("brand"))
        return redirect("Admin:brand")
    else:    
        return render(request,'Admin/brand.html',{'brand':brand}) 

def brandl(request,id):
    tbl_brand.objects.get(id=id).delete()
    return redirect("Admin:brand")  

def editbrand(request,id):
    editbrand=tbl_brand.objects.get(id=id)
    if request.method=="POST":
        editbrand.brand_name=request.POST.get("brand")
        editbrand.save()
        return redirect("Admin:brand")
    else:    
        return render(request,'Admin/brand.html',{'brandi':editbrand})                 


def category(request):
    category=tbl_category.objects.all()
    if request.method=="POST":
        tbl_category.objects.create(category_name=request.POST.get("category"))
        return redirect("Admin:category")
    else:    
        return render(request,'Admin/category.html',{'category':category})

def categoryl(request,id):
    tbl_category.objects.get(id=id).delete()
    return redirect("Admin:category") 

def editcategory(request,id):
    editcategory=tbl_category.objects.get(id=id)
    if request.method=="POST":
        editcategory.category_name=request.POST.get("category")
        editcategory.save()
        return redirect("Admin:category")
    else:    
        return render(request,'Admin/category.html',{'categoryi':editcategory})         

def district(request):
    if "aid" in request.session: 
        district= tbl_district.objects.all()
        if request.method=="POST":
            districtcount=tbl_district.objects.filter(district_name=request.POST.get("district").strip().title()).count()
            if districtcount > 0:
                return render(request,'Admin/District.html',{'msg':"District Already Exist"})
            else:    
                tbl_district.objects.create(district_name=request.POST.get("district"))
                return redirect("Admin:district")
        else:    
            return render(request,'Admin/District.html',{'district':district})
    else:
        return redirect("Guest:login")       

def dist(request,id):  
    tbl_district.objects.get(id=id).delete()
    return redirect("Admin:district") 

def editdistrict(request,id):
    editdistrict=tbl_district.objects.get(id=id)
    if request.method=="POST":
        editdistrict.district_name=request.POST.get("district")
        editdistrict.save()
        return redirect("Admin:district")
    else:    
        return render(request,'Admin/District.html',{'districtl':editdistrict})
  
def register(request):
    if "aid" in request.session:
        register=tbl_register.objects.all()
        if request.method=="POST":
            tbl_register.objects.create(admin_name=request.POST.get("adname"),
                                        admin_email=request.POST.get("ademail"),
                                        admin_pass=request.POST.get("adpass"))
            return redirect("Admin:register")
        else:    
            return render(request,'Admin/register.html',{'register':register})   
    else:
         return redirect("Guest:login")         

def registerl(request,id):
    tbl_register.objects.get(id=id).delete()
    return redirect("Admin:register")            

def editregister(request,id):
    editregister=tbl_register.objects.get(id=id)
    if request.method=="POST":
        editregister.admin_name=request.POST.get("adname")
        editregister.admin_email=request.POST.get("ademail")
        editregister.admin_pass=request.POST.get("adpass")
        editregister.save()
        return redirect("Admin:register")
    else:    
        return render(request,'Admin/register.html',{'registeri':editregister}) 

def place(request):
    if "aid" in request.session:
        dis=tbl_district.objects.all()
        place= tbl_place.objects.all()
        if request.method=="POST":
            tbl_place.objects.create(district=tbl_district.objects.get(id=request.POST.get("sel_district")),place_name=request.POST.get("txtpl"))
            return redirect("Admin:place")
        else:    
            return render(request,'Admin/place.html',{'district':dis,'place':place}) 
    else:
         return redirect("Guest:login")          

def placedelete(request,id):  
    tbl_place.objects.get(id=id).delete()
    return redirect("Admin:place")   

def editplace(request,id):
    dis=tbl_district.objects.all()
    editplace=tbl_place.objects.get(id=id)
    if request.method=="POST":
        editplace.place_name=request.POST.get("txtpl")
        editplace.district=tbl_district.objects.get(id=request.POST.get("sel_district"))
        editplace.save()
        return redirect("Admin:place")
    else:    
        return render(request,'Admin/place.html',{'placei':editplace,'district':dis})       

def chatbot(request):
    if "aid" in request.session: 
        chat=tbl_chatbot.objects.all()
        if request.method=="POST":
            tbl_chatbot.objects.create(questions=request.POST.get("txtq"),answers=request.POST.get("txta"),)
            return redirect("Admin:chatbot")
        else:    
            return render(request,'Admin/Chatbot.html',{'chat':chat}) 
    else:
        return redirect("Guest:login")


def chatbot_del(request,id):
    tbl_chatbot.objects.get(id=id).delete()
    return redirect("Admin:chatbot")             


def type(request):
    if "aid" in request.session:
        types=tbl_type.objects.all()
        if request.method=="POST":
            typecount=tbl_type.objects.filter(type=request.POST.get("txttype").strip().title()).count()
            if typecount > 0:
                return render(request,'Admin/Type.html',{'msg':"Type Already Exist"})
            else:    
                tbl_type.objects.create(type=request.POST.get("txttype"))
                return redirect("Admin:type")
        else:
            return render(request,'Admin/Type.html',{'type':types})
    else:
        return redirect("Guest:login")       

def typedel(request,id):
    tbl_type.objects.get(id=id).delete()
    return redirect("Admin:type")

def typeedit(request,id):
    typ=tbl_type.objects.get(id=id)
    if request.method=="POST":
        typ.type=request.POST.get("txttype")
        typ.save()
        return redirect("Admin:type")
    else:
        return render(request,'Admin/Type.html',{'typ':typ})

def viewcomplaint(request): 
    if "aid" in request.session: 
        user=tbl_user.objects.all()
        owner=tbl_owner.objects.all()
        usertl=tbl_complain.objects.filter(user__in=user)
        ownertl=tbl_complain.objects.filter(owner__in=owner)
        return render(request,'Admin/ViewComplaint.html',{'usertl':usertl,'ownertl':ownertl})
    else:
         return redirect("Guest:login")         

def reply(request,id):
    comp=tbl_complain.objects.get(id=id)
    if request.method=="POST":
        comp.comp_reply=request.POST.get("txtr")
        comp.comp_status=1
        comp.save()
        return redirect("Admin:viewcomplaint")    
    else:
        return render(request,'Admin/Reply.html')  

def index(request):
    return render(request,'Admin/index.html') 

def crop(request):
    crop=tbl_crop.objects.all()
    if request.method=="POST":
        tbl_crop.objects.create(crop_name=request.POST.get("textc"))
        return redirect("Admin:crop")
    else:
        return render(request,'Admin/Crop.html',{'crop':crop})

def cropdel(request,id):
    tbl_crop.objects.get(id=id).delete()
    return redirect("Admin:crop")   

def fertilizer(request):
    crop = tbl_crop.objects.all()
    fertilizer=tbl_fertilizer.objects.all()
    if request.method=="POST":
        tbl_fertilizer.objects.create(fert_name=request.POST.get("textf"),fert_details=request.POST.get("textd"),crop=tbl_crop.objects.get(id=request.POST.get("sel_crop")))
        return redirect("Admin:fertilizer")
    else:
        return render(request,'Admin/fertilizer.html',{'fertilizer':fertilizer,"crop":crop})

def fertdel(request,id):
    tbl_fertilizer.objects.get(id=id).delete()
    return redirect("Admin:fertilizer") 

def addpest(request):
    crop = tbl_crop.objects.all()
    pest = tbl_pest.objects.all()
    if request.method == "POST":
        tbl_pest.objects.create(pest=request.POST.get("txt_pest"),crop=tbl_crop.objects.get(id=request.POST.get("sel_crop")))
        return redirect("Admin:addpest")
    else:
        return render(request,"Admin/Addpest.html",{"crop":crop,"pest":pest})

def deletepest(request, id):
    tbl_pest.objects.get(id=id).delete()
    return redirect("Admin:addpest")          

def logout(request):
    del request.session['aid']   
    return redirect('Guest:login')                  