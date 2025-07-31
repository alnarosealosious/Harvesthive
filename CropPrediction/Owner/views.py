from django.shortcuts import render,redirect
from Owner.models import *
from Admin.models import *
from User.models import *
from django.conf import settings
from django.core.mail import send_mail

def homepage(request):
    if "oid" in request.session:
        return render(request,'Owner/Homepage.html') 
    else:    
        return redirect("Guest:login")

def changepass(request):
    if "oid" in request.session:
        cp = tbl_owner.objects.get(id=request.session['oid'])
        if request.method=="POST":
            current=request.POST.get("txtp")
            new=request.POST.get("txtnp")
            confirm=request.POST.get("txtcp")
            if cp.owner_pass == current:
                if new == confirm:
                    cp.owner_pass = confirm
                    cp.save()
                    return render(request,"Owner/myprofile.html",{"msg":"Password Updated..."})
                else:
                    return render(request,"Owner/changepass.html",{"msg":"Confirm Password Error..."})  
            else:
                return render(request,"Owner/changepass.html",{"msg":"Current Password Error..."}) 
        else:              
            return render(request,'Owner/changepass.html')
    else:
        return redirect("Guest:login")  

def editprof(request):
    if "oid" in request.session:
        owner=tbl_owner.objects.get(id=request.session['oid'])
        if request.method=="POST":
            name=request.POST.get("txtn")
            email=request.POST.get("txte")
            address=request.POST.get("txta")
            owner.owner_name=name
            owner.owner_email=email
            owner.owner_address=address
            owner.save()
            return render(request,"Owner/myprofile.html",{"msg":"Profile Updated..."})
        else:    
            return render(request,'Owner/editprof.html',{"owner":owner})
    else:
        return redirect("Guest:login")        
               
def myprof(request):
    if "oid" in request.session:
        owner=tbl_owner.objects.get(id=request.session['oid'])
        return render(request,'Owner/myprofile.html',{"owner":owner})
    else:
        return redirect("Guest:login")      

def complaint(request):
    if "oid" in request.session:
        ow=tbl_owner.objects.get(id=request.session['oid'])
        comp=tbl_complain.objects.filter(owner=ow)
        if request.method=="POST":
            tbl_complain.objects.create(title=request.POST.get("txtl"),content=request.POST.get("txtc"),owner=ow)
            return redirect("Owner:complaint") 
        else:       
            return render(request,'Owner/Complaint.html',{'comp':comp})
    else:
        return redirect("Guest:login")   

def plot(request):
    if "oid" in request.session:
        dis=tbl_district.objects.all()
        plots=tbl_plot.objects.all()
        if request.method=="POST":
            tbl_plot.objects.create(landmetrics=request.POST.get("txtp"),place=tbl_place.objects.get(id=request.POST.get("sel_place")),owner=tbl_owner.objects.get(id=request.session['oid']))
            return redirect("Owner:plot")
        else:
            return render(request,'Owner/plot.html',{'district':dis,'plot':plots})
    else:
        return redirect("Guest:login")             

def condition(request,id):
    content=tbl_condition.objects.filter(plot=id)
    if request.method=="POST":
        tbl_condition.objects.create(content=request.POST.get("txtc"),plot=tbl_plot.objects.get(id=id))
        return redirect("Owner:condition",id)
    else:
        return render(request,'Owner/Conditions.html',{'condition':content})          


def gallery(request,id):
    photo=tbl_gallery.objects.filter(plot_id=id)
    if request.method=="POST":
        tbl_gallery.objects.create(photo=request.FILES.get("txtp"),plot_id=tbl_plot.objects.get(id=id))
        return redirect("Owner:gallery",id)
    else:
        return render(request,'Owner/gallery.html',{'gallery':photo})
        

def plottype(request,id):
    plot=tbl_plottype.objects.filter(plot=id)
    Type=tbl_type.objects.all()
    if request.method=="POST":
        tbl_plottype.objects.create(plot=tbl_plot.objects.get(id=id),Type=tbl_type.objects.get(id=request.POST.get("sel_type")))
        return redirect("Owner:plottype",id)
    else:
        return render(request,'Owner/plottype.html',{'plot':plot,'Type':Type,'pid':id})

def plottype_del(request,id,pid):
    tbl_plottype.objects.get(id=id).delete()
    return redirect("Owner:plottype",pid)          
                          
def viewreq(request):
    if "oid" in request.session:
        req=tbl_addrequest.objects.filter(plot__owner=request.session['oid'])
        return render(request,'Owner/ViewRequest.html',{'req':req})
    else:
        return redirect("Guest:login")       

def accept(request,id):
    req=tbl_addrequest.objects.get(id=id)
    userid=req.user.id
    user=tbl_user.objects.get(id=userid)
    email=user.user_email
    req.req_status=1
    req.save()
    send_mail(
    'Plot Buying Request Approved',  # subject
    "\rDear Customer,"
    "\rWe are pleased to inform you that your plot buying request has been approved."
    "\rIf you have any questions or need further clarification, please feel free to contact us."
    "\rThank you for choosing us."
    "\rBy"
    "\rHarvestHive",  # body
    settings.EMAIL_HOST_USER,
    [email],
    )
    return redirect("Owner:viewreq")

def reject(request,id):
    req=tbl_addrequest.objects.get(id=id)
    userid=req.user.id
    user=tbl_user.objects.get(id=userid)
    email=user.user_email
    req.req_status=2
    req.save()
    send_mail(
    'Plot Buying Request Rejected',  # subject
    "\rDear Customer,"
    "\rWe are sorry to inform you that your plot buying request has rejected."
    "\rWe will proceed with the necessary next steps and notify you accordingly."
    "\rThank you for choosing us."
    "\rBy"
    "\rHarvestHive",  # body
    settings.EMAIL_HOST_USER,
    [email],
   )
    return redirect("Owner:viewreq")   

def logout(request):
    del request.session['oid']   
    return redirect('Guest:login') 


       