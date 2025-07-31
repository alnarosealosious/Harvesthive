from django.urls import path,include
from Guest import views
app_name="Guest"

urlpatterns = [ path('signup/',views.signup,name="signup"), 
                path('ow/',views.owner,name="owner"),
                path('AjaxPlace/',views.ajaxplace,name="ajaxplace"),
                path('login/',views.login,name="login"),
                path('ownerregister/',views.ownerregister,name="ownerregister"),
                path('index/',views.index,name="index"),

]
