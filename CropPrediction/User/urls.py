from django.urls import path,include
from User import views
app_name="User"
urlpatterns = [ path('ch/',views.changepass,name="changepass"), 
                path('ed/',views.editprof,name="editprof"),
                path('my/',views.myprof,name="myprofile"),
                path('complaint/',views.complaint,name="complaint"),
                path('addreq/<int:id>',views.addreq,name="addreq"),
                # path('predict/',views.predict,name="predict"),
                path('homepage/',views.homepage,name="homepage"),
                path('viewplot/',views.viewplot,name="viewplot"),
                path('gallery/<int:id>',views.gallery,name="gallery"),
                path('viewcondition/<int:id>',views.viewcondition,name="viewcondition"),
                path('viewplottype/<int:id>',views.viewplottype,name="viewplottype"),
                path('myrequest/',views.myrequest,name="myrequest"),
                path('chatbot/',views.chatbot,name="chatbot"),
                path('ajaxanswer/',views.ajaxanswer,name="ajaxanswer"),
                path('logout/',views.logout,name="logout"),
                path('fertili/',views.fertili,name="fertili"), 
                path('ajaxFertilizer/',views.ajaxFertilizer,name="ajaxFertilizer"),
                path('pestdetect/',views.pestdetect,name="pestdetect"),
                path('ajaxPest/',views.ajaxPest,name="ajaxPest"),
                path('CropRecommend/',views.CropRecommend,name="CropRecommend"),
]