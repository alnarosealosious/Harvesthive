import os
import pandas as pd
import joblib  # Import joblib to load the model
from django.shortcuts import render,redirect
from Admin.models import*
from Guest.models import *
from Owner.models import *
from User.models import *
from django.http import JsonResponse

# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  
# MODEL_PATH = os.path.join(BASE_DIR, 'Assets', 'Model', 'knn_model.pkl')

# model = load_model(MODEL_PATH)

def CropRecommend(request):
    MODEL_PATH = os.path.join("Assests\Model\knn_model.pkl")
    model = joblib.load(MODEL_PATH)
    # model = load_model(MODEL_PATH)

    if request.method == 'POST':
        # Get input values from the form
        nitrogen = float(request.POST['nitrogen'])
        potassium = float(request.POST['potassium'])
        temperature = float(request.POST['temperature'])
        humidity = float(request.POST['humidity'])
        rainfall = float(request.POST['rainfall'])
        soiltype = int(request.POST['soiltype']) 
        print(soiltype)
        soil_depth = float(request.POST['soil_depth'])

        # Create DataFrame for model prediction
        input_data = pd.DataFrame({
            'N': [nitrogen],
            'K': [potassium],
            'temperature': [temperature],
            'humidity': [humidity],
            'rainfall': [rainfall],
            'soiltype': [soiltype],
            'Soil_Depth_cm': [soil_depth]
        })

        # Make prediction
        prediction = model.predict(input_data)
        recommended_crop = prediction[0]

        return render(request, 'User/CropRecommendation.html', {'res': recommended_crop})

    return render(request, 'User/CropRecommendation.html')


def homepage(request):
    if "uid" in request.session:
        return render(request,'User/Homepage.html')
    else:
        return redirect("Guest:login")   

def changepass(request):
    if "uid" in request.session:
        cp = tbl_user.objects.get(id=request.session['uid'])
        if request.method=="POST":
            current=request.POST.get("txtp")
            new=request.POST.get("txtnp")
            confirm=request.POST.get("txtcp")
            if cp.user_pass == current:
                if new == confirm:
                    cp.user_pass = confirm
                    cp.save()
                    return render(request,"User/myprofile.html",{"msg":"Password Updated..."})
                else:
                    return render(request,"User/changepass.html",{"msg":"Confirm Password Error..."})  
            else:
                return render(request,"User/changepass.html",{"msg":"Current Password Error..."}) 
        else:              
            return render(request,'User/changepass.html')
    else:
        return redirect("Guest:login")         

def editprof(request):
    if "uid" in request.session:
        user=tbl_user.objects.get(id=request.session['uid'])
        if request.method=="POST":
            name=request.POST.get("txtn")
            email=request.POST.get("txte")
            address=request.POST.get("txta")
            user.user_name=name
            user.user_email=email
            user.user_address=address
            user.save()
            return render(request,"User/myprofile.html",{"msg":"Profile Updated..."})
        else:    
            return render(request,'User/editprof.html',{"user":user})
    else:
        return redirect("Guest:login")        

def myprof(request):
    if "uid" in request.session:
        user=tbl_user.objects.get(id=request.session['uid'])
        return render(request,'User/myprofile.html',{"user":user}) 
    else:
        return redirect("Guest:login")        

def complaint(request):
    if "uid" in request.session:
        us=tbl_user.objects.get(id=request.session['uid'])
        comp=tbl_complain.objects.filter(user=us)
        if request.method=="POST":
            tbl_complain.objects.create(title=request.POST.get("txtl"),content=request.POST.get("txtc"),user=us)
            return redirect("User:complaint") 
        else:       
            return render(request,'User/Complaint.html',{'comp':comp}) 
    else:
        return redirect("Guest:login")         

def addreq(request,id):
    if request.method=="POST":
        tbl_addrequest.objects.create(req_content=request.POST.get("txtc"),user=tbl_user.objects.get(id=request.session['uid']),plot=tbl_plot.objects.get(id=id))
        return redirect("User:addreq",id)
    else:
        return render(request,'User/AddRequest.html')    

# def predict(request):
#     if "uid" in request.session:
#         return render(request,'User/Prediction.html') 
#     else:
#         return redirect("Guest:login")     

def pestdetect(request):
    if "uid" in request.session:
        crop = tbl_crop.objects.all()
        return render(request,'User/PestDetection.html',{"crop":crop})
    else:
        return redirect("Guest:login")     

def fertili(request):
    if "uid" in request.session:
        crop = tbl_crop.objects.all()
        return render(request,'User/Fertilization.html',{"crop":crop})
    else:
        return redirect("Guest:login")         
               
def viewplot(request):
    if "uid" in request.session:
        plot=tbl_plot.objects.all()
        return render(request,'User/Viewplot.html',{'plot':plot}) 
    else:
        return redirect("Guest:login")        

def gallery(request,id):
    gal=tbl_gallery.objects.filter(plot_id=id)
    return render(request,'User/Gallery.html',{'gallery':gal}) 

def viewcondition(request,id):
    con=tbl_condition.objects.filter(plot_id=id)
    return render(request,'User/ViewCondition.html',{'condition':con})

def viewplottype(request,id):
    pl=tbl_plottype.objects.filter(plot=id)
    return render(request,'User/ViewPlottype.html',{'plottype':pl})   

def myrequest(request):
    if "uid" in request.session:
        req=tbl_addrequest.objects.all()
        return render(request,'User/Myrequest.html',{'req':req})
    else:
        return redirect("Guest:login")      

def chatbot(request):
    if "uid" in request.session:
        cha=tbl_chatbot.objects.all()
        return render(request,'User/Chatbot.html',{'cha':cha})
    else:
        return redirect("Guest:login")     

def ajaxanswer(request):
    did = request.GET.get("did")
    answer = tbl_chatbot.objects.get(id=did).answers  
    return JsonResponse({"answer":answer}) 
  

def ajaxFertilizer(request):
    crop = tbl_crop.objects.get(id=request.GET.get("did"))
    fertilizerData = tbl_fertilizer.objects.filter(crop=crop)
    return render(request,"User/AjaxFertilizer.html",{"fertilizerData":fertilizerData})  

def ajaxPest(request):
    crop = tbl_crop.objects.get(id=request.GET.get("did"))
    pestData = tbl_pest.objects.filter(crop=crop)
    return render(request,"User/AjaxPest.html",{"pestData":pestData})                
           
def logout(request):
    del request.session['uid']   
    return redirect('Guest:login') 

# from django.http import JsonResponse
# import pandas as pd
# import joblib

# # Load the model and label encoder
# knn_model = joblib.load("D:\\ML\\knn_model.pkl")
# label_encoder = joblib.load("D:\\ML\\label_encoder.pkl")

# # Load the model once when the server starts
# MODEL_PATH = os.path.join("Assests\Model\knn_model.pkl")
# encoder_PATH = os.path.join("Assests\Model\label_encoder.pkl")
# model = load_model(MODEL_PATH)


# def predict(request):
#     # Example input data
#     input_data = {
#         'N': float(request.GET.get('N')),
#         'P': float(request.GET.get('P')),
#         'K': float(request.GET.get('K')),
#         'temperature': float(request.GET.get('temperature')),
#         'humidity': float(request.GET.get('humidity')),
#         'ph': float(request.GET.get('ph')),
#         'rainfall': float(request.GET.get('rainfall'))
#     }
    
#     input_df = pd.DataFrame([input_data])
    
#     # Make prediction
#     prediction = knn_model.predict(input_df)
#     prediction_label = label_encoder.inverse_transform(prediction)
    
#     # Return prediction as JSON response
#     return JsonResponse({'prediction': prediction_label[0]}) 


