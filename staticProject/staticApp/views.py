from django.shortcuts import render

# Create your views here.
def view1(request):
    name="rakesh"
    animal="rottweiler"
    skill="python"
    d={"name1":name,"animal1":animal,"skill1":skill}
    return render(request,"staticApp/1.html",d)
