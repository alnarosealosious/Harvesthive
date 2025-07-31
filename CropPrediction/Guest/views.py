from django.shortcuts import render,redirect
from Admin.models import *
from Guest.models import *
from User.models import *
from Owner.models import *

def signup(request):
    dis=tbl_district.objects.all()
    if request.method=="POST":      
        password=request.POST.get("textp")
        cpassword=request.POST.get("textcp")
        emailcount=tbl_user.objects.filter(user_email=request.POST.get("txte")).count()
        owneremailcount=tbl_owner.objects.filter(owner_email=request.POST.get("txte")).count()
        if emailcount > 0:
            return render(request,'Guest/signup.html',{'msg':"Email Already Exist"})
        elif owneremailcount > 0:
            return render(request,'Guest/signup.html',{'msg':"Email Already Exist"})
        else:
            if password==cpassword:
                tbl_user.objects.create(
                    user_name=request.POST.get("textn"),
                    user_photo=request.FILES.get("txtp"),
                    user_contact=request.POST.get("txtc"),
                    user_pass=request.POST.get("txtpass"),
                    user_address=request.POST.get("txta"),
                    user_email=request.POST.get("txte"),
                    user_confirm=request.POST.get("txtps"),
                    place=tbl_place.objects.get(id=request.POST.get("sel_place"))
                )
                return redirect("Guest:login")
            else:
                return render(request,'Guest/signup.html',{'msg':"Password Mismatch",'district':dis})
    else:
        return render(request,'Guest/signup.html',{'district':dis})

def owner(request):
    return render(request,'Guest/owner.html')    

def ajaxplace(request):
    dis = tbl_district.objects.get(id=request.GET.get("did"))
    place = tbl_place.objects.filter(district=dis)
    return render(request,"Guest/AjaxPlace.html",{"place":place})

def login(request):
    if request.method=="POST":
        admincount=tbl_register.objects.filter(admin_email=request.POST.get('txte'),
                                               admin_pass=request.POST.get('txtpass')).count()
        usercount=tbl_user.objects.filter(user_email=request.POST.get('txte'),
                                               user_pass=request.POST.get('txtpass')).count() 
        ownercount=tbl_owner.objects.filter(owner_email=request.POST.get('txte'),
                                               owner_pass=request.POST.get('txtpass')).count()                                                                            
        if admincount>0:
            admin=tbl_register.objects.get(admin_email=request.POST.get('txte'),
                                           admin_pass=request.POST.get('txtpass'))
            request.session['aid']=admin.id
            return redirect('Admin:homepage') 
        elif usercount>0:
            user=tbl_user.objects.get(user_email=request.POST.get('txte'),
                                         user_pass=request.POST.get('txtpass'))
            request.session['uid']=user.id
            return redirect('User:homepage')
        elif ownercount>0:
            owner=tbl_owner.objects.get(owner_email=request.POST.get('txte'),
                                         owner_pass=request.POST.get('txtpass'))
            request.session['oid']=owner.id
            return redirect('Owner:homepage')                                      
        else:
            return render(request,'Guest/Login.html',{'msg':'invalid'}) 
    else:                                               
        return render(request,'Guest/Login.html')     

def ownerregister(request):
    if request.method=="POST":
        password=request.POST.get("textp")
        cpassword=request.POST.get("textcp")
        emailcount=tbl_user.objects.filter(user_email=request.POST.get("txte")).count()
        owneremailcount=tbl_owner.objects.filter(owner_email=request.POST.get("txte")).count()
        if emailcount > 0:
            return render(request,'Guest/signup.html',{'msg':"Email Already Exist"})
        elif owneremailcount > 0:
            return render(request,'Guest/signup.html',{'msg':"Email Already Exist"})
        else:    
            if password==cpassword:
                tbl_owner.objects.create(
                    owner_name=request.POST.get("textn"),
                    owner_email=request.POST.get("txte"),
                    owner_pass=request.POST.get("txtpass"),
                    owner_address=request.POST.get("txta"),
                    owner_proof=request.FILES.get("txtp"),
                )
                return redirect("Guest:login")
            else:
                return render(request,'Guest/OwnerRegister.html',{'msg':"Password Mismatch"})
    else:
        return render(request,'Guest/OwnerRegister.html')
        
def index(request):
    return render(request,'Guest/index.html')        