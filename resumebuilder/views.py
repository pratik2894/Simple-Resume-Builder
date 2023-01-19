from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import redirect



def home(request):
    return render(request,"index.html")

def form(request):
    try:
        if request.method=="POST":
            name = request.POST.get('fname')
            lname = request.POST.get('lname')
            email = request.POST.get('email')
            bod = request.POST.get('bod')
            mobile = request.POST.get('mobile')
            specialization = request.POST.get('specialization')
            city = request.POST.get('city')
            skill1 = request.POST.get('skill1')
            skill2 = request.POST.get('skill2')
            skill3 = request.POST.get('skill3')
            skill4 = request.POST.get('skill4')
            skill5 = request.POST.get('skill5')
            skill6 = request.POST.get('skill6')
            certi1 = request.POST.get('certi1')
            certi2 = request.POST.get('certi2')
            certi3 = request.POST.get('certi3')
            certi4 = request.POST.get('certi4')
            certi5 = request.POST.get('certi5')
            lang1 = request.POST.get('lang1')
            lang2 = request.POST.get('lang2')
            lang3 = request.POST.get('lang3')
            self = request.POST.get('self')
            pc1 = request.POST.get('pc1')
            pc1y1 = request.POST.get('pc1y1')
            pc1y1r1 = request.POST.get('pc1y1r1')
            pc2 = request.POST.get('pc2')
            pc2y2 = request.POST.get('pc2y2')
            pc2y2r2 = request.POST.get('pc2y2r2')
            pc3 = request.POST.get('pc3')
            pc3y3 = request.POST.get('pc3y3')
            pc3r3 = request.POST.get('pc3r3')
            tenth = request.POST.get('tenth')
            tenthyr = request.POST.get('tenthyr')
            twelc = request.POST.get('twelc')
            twelcyr = request.POST.get('twelcyr')
            university = request.POST.get('university')
            unipassyr = request.POST.get('unipassyr')


            print(request)

    except:
        pass

    return render(request,"Form.html")


def resume(request):
    data={}

    try:
        if request.method=="POST":
            name = request.POST.get("fname")
            lastname = request.POST.get("lname")
            email = request.POST.get("email")
            bod = request.POST.get('bod')
            mobile = request.POST.get('mobile')
            specialization = request.POST.get('specialization')
            city = request.POST.get('city')
            skill1 = request.POST.get('skill1')
            skill2 = request.POST.get('skill2')
            skill3 = request.POST.get('skill3')
            skill4 = request.POST.get('skill4')
            skill5 = request.POST.get('skill5')
            skill6 = request.POST.get('skill6')
            certi1 = request.POST.get('certi1')
            certi2 = request.POST.get('certi2')
            certi3 = request.POST.get('certi3')
            certi4 = request.POST.get('certi4')
            certi5 = request.POST.get('certi5')
            lang1 = request.POST.get('lang1')
            lang2 = request.POST.get('lang2')
            lang3 = request.POST.get('lang3')
            self = request.POST.get('self')
            pc1 = request.POST.get('pc1')
            pc1y1 = request.POST.get('pc1y1')
            pc1y1r1 = request.POST.get('pc1y1r1')
            pc2 = request.POST.get('pc2')
            pc2y2 = request.POST.get('pc2y2')
            pc2y2r2 = request.POST.get('pc2y2r2')
            pc3 = request.POST.get('pc3')
            pc3y3 = request.POST.get('pc3y3')
            pc3y3r3 = request.POST.get('pc3y3r3')
            tenth = request.POST.get('tenth')
            tenthyr = request.POST.get('tenthyr')
            twelc = request.POST.get('twelc')
            twelcyr = request.POST.get('twelcyr')
            university = request.POST.get('university')
            unipassyr = request.POST.get('unipassyr')


            print(name,lastname,email,twelc,tenth)
            data={
                'name':name,
                'lastname':lastname,
                'email':email,
                'bod':bod,
                'mobile':mobile,
                'specialization':specialization,
                'city':city,
                'skill1':skill1,
                'skill2':skill2,
                'skill3':skill3,
                'skill4':skill4,
                'skill5':skill5,
                'skill6':skill6,
                'certi1':certi1,
                'certi2':certi2,
                'certi3':certi3,
                'certi4':certi4,
                'certi5':certi5,
                'lang1':lang1,
                'lang2':lang2,
                'lang3':lang3,
                'self':self,
                'pc1':pc1,
                'pc1y1':pc1y1,
                'pc1y1r1':pc1y1r1,
                'pc2':pc2,
                'pc2y2':pc2y2,
                'pc2y2r2' : pc2y2r2,
                'pc3':pc3,
                'pc3y3':pc3y3,
                'pc3y3r3':pc3y3r3,
                'tenth':tenth,
                'tenthyr':tenthyr,
                'twelc':twelc,
                'twelcyr':twelcyr,
                'university':university,
                'unipassyr':unipassyr,
            }


    except:
        pass
    return render(request,"resume.html",data)



