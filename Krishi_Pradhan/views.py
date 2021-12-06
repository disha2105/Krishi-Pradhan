from os import PathLike
from django.db import connection
from django.db.models.query_utils import Q
from django.shortcuts import render, redirect
import mysql.connector
# Create your views here.
#from django.contrib.auth.forms import User
from django.contrib import messages
from operator import itemgetter
from .models import User, question,cropdata






def home(request):
    return render(request, 'home.html')

def home2(request):
    return render(request, 'home2.html')

def registration (request):
    
    if request.method =="POST":
        
        user = User()

        user.username= request.POST['username']
        user.email= request.POST['email']
        user.password1= request.POST['password1']
        user.password2= request.POST['password2']
        if user.password1 != user.password2:
            messages.warning(request,"Passwords didn't match")
            return redirect("registration")
        elif user.email == "" or user.username=="" or user.password1=="" or user.password2=="":
            messages.warning(request, "Some feilds are empty")
            return redirect("registration")
        else:
            user.save()
            messages.success(request, "Registration Successful")
            return render(request, "home.html")
            
        
        
    else:
        return render(request, 'registration.html')


def login (request):
    connection = mysql.connector.connect(host="localhost",user="root",password="$Dishak123$",database="accounts")
    cursor=connection.cursor()
    connection2 = mysql.connector.connect(host="localhost",user="root",password="$Dishak123$",database="accounts")
    cursor2=connection2.cursor()
    sqlcommand = "select email from Krishi_Pradhan_user"
    sqlcommand2 = "select password1 from Krishi_Pradhan_user"
    cursor.execute(sqlcommand)
    cursor2.execute(sqlcommand2)

    e=[]
    p=[]
    for i in cursor:
        e.append(i)
    for j in cursor2:
        p.append(j)
    res = list(map(itemgetter(0),e))
    res2 = list(map(itemgetter(0),p))
    
    if request.method == "POST":
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        i=1
        k=len(res)
        while i<k:
            if res[i]==email and res2[i]==password1:
                messages.success(request,"Login Successful")
                return render(request,'home2.html')
                break
            i+=1
        else:
            messages.warning(request,"Check Email and Password")
            return redirect('login')

    else:
        return render(request, 'login.html')

def about (request):
    return render(request, 'about.html')

def organic(request):
    return render(request, 'organic.html')

def organic2(request):
    return render(request, 'organic2.html')

def about2 (request):
    return render(request, 'about2.html')

def questionnare (request):
    if request.method=='POST':

        quest=question()
        quest.region= request.POST.get('region')
        quest.soil=request.POST.get('soil')
        quest.previous=request.POST.get('previous')
    
        quest.save()
        connection3 = mysql.connector.connect(host="localhost",user="root",password="$Dishak123$",database="accounts")
        cursor3=connection3.cursor()
        connection4 = mysql.connector.connect(host="localhost",user="root",password="$Dishak123$",database="accounts")
        cursor4=connection4.cursor()
        connection5 = mysql.connector.connect(host="localhost",user="root",password="$Dishak123$",database="accounts")
        cursor5=connection5.cursor()
        connection6 = mysql.connector.connect(host="localhost",user="root",password="$Dishak123$",database="accounts")
        cursor6=connection6.cursor()
        sqlcommand3 = "select id from Krishi_Pradhan_cropdata"
        sqlcommand4 = "select region1 from Krishi_Pradhan_cropdata"
        sqlcommand5 = "select soil1 from Krishi_Pradhan_cropdata"
        sqlcommand6 = "select crop1 from Krishi_Pradhan_cropdata"
        cursor3.execute(sqlcommand3)
        cursor4.execute(sqlcommand4)
        cursor5.execute(sqlcommand5)
        cursor6.execute(sqlcommand6)

        id=[]
        r=[]
        s=[]
        c=[]
        global ans
        ans={}
        for i in cursor3:
            id.append(i)
        for j in cursor4:
            r.append(j)
        for k in cursor5:
            s.append(k)
        for l in cursor6:
            c.append(l)
        res3 = list(map(itemgetter(0),id))
        res4 = list(map(itemgetter(0),r))
        res5 = list(map(itemgetter(0),s))
        res6 = list(map(itemgetter(0),c))

        region1= request.POST.get('region')
        soil1= request.POST.get('soil')
        print(region1,soil1)
        
        key=1


        for w in range(0,303):
            print("test6",w)
            try:
                if w<303:
                    if res4[w]==region1 and res5[w]==soil1:
                        print(res6[w])
                        key2=str(key)
                        ans[key2]=res6[w]
                        key+=1    
                    else:
                        print("test3")
                elif w==303:
                    messages.warning(request,"Please select the appropiate crop and soil")
                    return render(request,'questionnare.html')
            except IndexError:
                pass

        else:
            pass

        res = not ans        
        if res==True:
            print(ans)
            messages.warning(request,"Please select the appropiate crop and soil")
            return render(request,'questionnare.html')
        else:
            print(ans)
            
            return render(request,'solution.html',{'ans':ans})
   
    else:
        return render(request, 'questionnare.html')


