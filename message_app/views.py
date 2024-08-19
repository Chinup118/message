from django.shortcuts import render, HttpResponse, redirect
from .models import Msg

# Create your views here.
def demo(request):
    return HttpResponse('hello! working properly...')

def create(request):
    #print('Request is:', request.method)
    if request.method=='POST':
        name=request.POST['uname']
        email=request.POST['uemail']
        mobile=request.POST['mobile']
        msg=request.POST['msg']
        m=Msg.objects.create(name=name, email=email, mobile=mobile, msg=msg)
        m.save()
        # print("Name: ", name)
        # print("Email ID: ", email)
        # print("Mobile no.: ", mob)
        # print("Message: ", msg)
        return redirect('/')
        # return HttpResponse('Data Fetched successfully')
    else:
        return render(request, 'create.html')

def dashboard(request):
    m=Msg.objects.all()
    # print(m)
    context={}
    context['data']=m
    return render(request, 'dashboard.html', context) 
    # return HttpResponse("Data fetched from database!!!")

def delete(request, rid):
    # print("Id to be deleted: ", rid)
    m=Msg.objects.filter(id=rid)
    print(m)
    m.delete()
    return redirect('/')
    # return HttpResponse("Id deleted: "+rid)

def edit(request, rid):
    # print("Id to be edited: ", rid)
    if request.method=='POST':  #update data
        uname=request.POST['uname']
        uemail=request.POST['uemail']
        umobile=request.POST['mobile']
        umsg=request.POST['msg']
        m=Msg.objects.filter(id=rid) 
        m.update(name=uname, email=uemail, mobile=umobile, msg=umsg)
        return redirect('/')
    
    else:
        # m=Msg.objects.filter(id=rid)  #<QuerySet [<Msg: Msg object (4)>]>  ---> in alist form for which we need to apply for loop
        m=Msg.objects.get(id=rid)   #get(): this by default gives Msg object (4) 
        print(m)
        context={}
        context['data']=m
        return render(request, 'edit.html', context)
    # return HttpResponse("Id to be edited: "+rid)