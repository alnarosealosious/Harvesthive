from django.urls import path,include
from Owner import views
app_name="Owner"
urlpatterns = [ path('pl/',views.plot,name="plot"), 
                path('gl/<int:id>',views.gallery,name="gallery"),
                path('plott/<int:id>',views.plottype,name="plottype"),
                path('plottype_del/<int:id>/<int:pid>',views.plottype_del,name="plottype_del"),
                path('ch/',views.changepass,name="changepass"),
                path('ed/',views.editprof,name="editprof"),
                path('my/',views.myprof,name="myprofile"),
                path('complaint/',views.complaint,name="complaint"), 
                path('condition/<int:id>',views.condition,name="condition"),
                path('viewreq/',views.viewreq,name="viewreq"),
                path('homepage/',views.homepage,name="homepage"),
                path('accept/<int:id>',views.accept,name="accept"), 
                path('reject/<int:id>',views.reject,name="reject"),
                path('logout/',views.logout,name="logout"),
                
]