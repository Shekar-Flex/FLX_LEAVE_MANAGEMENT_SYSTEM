from re import X
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

from .models import Usrdata,Superuser,Leavedata


# Create your views here.

def home(request):
    return render(request,'home.html')

def logins(request):
    return render(request,'login.html')

def logouts(request):
    logout(request)
    return render(request,'login.html')


def user(request):
    if request.method=='POST':
        global user,usrname
        usrname=request.POST['username']
        usrpass=request.POST['password']
        user=authenticate(request,username=usrname,password=usrpass)
        if user is not None:
            lis=Superuser.objects.filter(name=usrname)
            if len(lis)==1:
                print(lis[0].id)
                x=lis[0].id
                for i in lis:
                    print(i)
                obj_susr=Superuser.objects.all()
                obj_leave=Leavedata.objects.all()
                print(obj_leave)
                for j in obj_leave:
                    if x==j.ref_id_id:
                        print(j.name)
                login(request,user=user)
                message=f"{user.username} Super user login Sucessfully..."
                return render(request,'supusr.html',{'mess':message,'us':user,'id':x,'lev':obj_leave})
            else:
                login(request,user=user)
                message=f"{user.username} User login Sucessfully..."
                lev=Leavedata.objects.filter(name=user.username)
                for i in lev:
                    print(i.name)
                return render(request,'user.html',{'mess':message,'us':user,'data':lev})
        else:
            # return redirect('login')
            message="Incorrect username or password"
            # return redirect('login')
            messages.error(request,message=message)
            return redirect('login')
    return render(request,'login.html')

def superuser(request):
    return render(request,'supusr.html')

def update(request):
    print(user.username)
    la=Usrdata.objects.filter(name=user.username)
    if len(la) == 1:
        if request.method == 'POST':
            COLL=Leavedata()
            COLL.rogno=la[0].rogno
            COLL.name=la[0].name
            COLL.startdate=request.POST['d1']
            COLL.enddate=request.POST['d2']
            COLL.reasontype=request.POST['r1']
            COLL.reason=request.POST['r2']
            COLL.status='pending'
            COLL.ref_id_id=la[0].adv_id_id
            COLL.save()
            lev=Leavedata.objects.filter(name=user.username)
            print(lev)
            return render(request,'user.html',{'data':lev})
        lev=Leavedata.objects.filter(name=user.username)
        print(lev)
        return render(request,'user.html',{'data':lev})
    lev=Leavedata.objects.filter(name=user.username)
    print(lev)
    return render(request,'user.html',{'data':lev})
    
def accept(request):
    if request.method=='POST':
        obj_leave=Leavedata.objects.all()
        p=request.POST['num']
        print("primary",p)
        # cal=Leavedata.objects.filter(pk=p).update(status="Accept")
        # print(cal.startdate)
        # cal.rogno=request.POST['ro']
        if request.POST['select'] == 'Accept':
            Leavedata.objects.filter(pk=p).update(status="Accept")

        #     cal.status='Accept'
            
        elif request.POST['select'] == 'Reject':
            Leavedata.objects.filter(pk=p).update(status="Reject")

        #     cal.status='Reject'
        # cal.save()
        lis=Superuser.objects.filter(name=usrname)
        if len(lis)==1:
            print(lis[0].id)
            x=lis[0].id
            for i in lis:
                print(i)
            obj_susr=Superuser.objects.all()
            obj_leave=Leavedata.objects.all()
            print(obj_leave)
            for j in obj_leave:
                if x==j.ref_id_id:
                    print(j.name)
            # login(request,user=user)
            message="Accept Successfully..."
            return render(request,'supusr.html',{'mess':message,'us':user,'id':x,'lev':obj_leave})
        # message="Accept Successfully..."
        # return render(request,'supusr.html',{'mess':message,'us':user,'id':x,'lev':obj_leave})
    return render(request,'home.html')

# def reject(request):
#     if request.method=='POST':
#         obj_leave=Leavedata.objects.all()
#         p=request.POST['num']
#         cal=Leavedata(pk=p)
#         cal.status='Reject'
#         cal.save()
#         message="Reject Successfully..."
#         return render(request,'supusr.html',{'mess':message,'us':user,'id':x,'lev':obj_leave})
#     return render(request,'home.html')