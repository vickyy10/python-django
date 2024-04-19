from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Departments ,Doctors

from .models import Member
from .form import depform
# Create your views here.



def index(request):

    number = {
        'num1':[1,2,3,4,5,6,7,8,9,10],
    }

    return render(request,'index.html',number)




def about(request):
    print(request.COOKIES)
    visits=int(request.COOKIES.get('count',0))
    visits = visits+1
    
    response=render(request,'about.html',{'visit':visits})

    response.set_cookie('count',visits)
    
    return  response






def booking(request):
    return render(request,'booking.html')




def doctors(request):
    dict_2={
        'dict1':Doctors.objects.all()
    }
    
    return render(request,'doctors.html',dict_2)






def department(request):
     

    #  frm=depform()
    #  if request.POST:
    #      frm=depform(request.POST)
    #      if frm.is_valid():
    #          frm.save()


     dict_1={
        "dict":Departments.objects.get(dep_name='dermetology')
    }
    
    
     return render(request,'department.html',dict_1)




# -------------------crud---------------------------

def CRUD_index(request):
     mem_d={
        'mem':Member.objects.all()
        }
     return render(request,'crud-template/index.html',mem_d)


def CRUD_add(request):

    return render(request,'crud-template/add.html')




def addrec(request):
    x=request.POST['first']
    y=request.POST['last']
    z=request.POST['country']
    mem=Member(firstname=x,lastname=y,country=z)
    mem.save()
    return redirect('/crud')



def delete(request,id):
    mem=Member.objects.get(id = id)
    mem.delete()
    return redirect('crud')

def update(request,id):
     men_d={
         'mem':Member.objects.get(id=id)
     }
     return render(request,'crud-template/update.html',men_d)

def uprec(request,id):
    x=request.POST['first']
    y=request.POST['last']
    z=request.POST['country']
    mem=Member.objects.get(id=id)
    mem.firstname=x
    mem.lastname=y
    mem.country=z
    mem.save()
    return redirect('crud')

