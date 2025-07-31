from django.shortcuts import render

def add(request):
    if request.method=="POST":
        Number1=int(request.POST.get("num1"))
        Number2=int(request.POST.get("num2"))
        Result=Number1+Number2
        return render(request,"Basics/Add.html",{'add':Result})
    else:
        return render(request,'Basics/Add.html')

def largest(request):
    if request.method=="POST":
        Number1=int(request.POST.get("num1"))
        Number2=int(request.POST.get("num2"))
        if Number1 > Number2:
            Result=Number1
        else:
            Result=Number2    
        return render(request,"Basics/Largest.html",{'largest':Result})
    else:     
        return render(request,'Basics/Largest.html')

def calculator(request):
    if request.method=="POST":
        Number1=int(request.POST.get("num1"))
        Number2=int(request.POST.get("num2"))
        a=request.POST.get("a")
        if a == "+":
            Result=Number1+Number2
        elif a == "-":
            Result=Number1-Number2   
        elif a =="/":
            Result=Number1/Number2
        elif a == "*":
            Result=Number1*Number2   
        else:
            Result="Invalid Operation" 
        return render(request,"Basics/Calculator.html",{'calculator':Result})   
    else:            
        return render(request,'Basics/Calculator.html')    
