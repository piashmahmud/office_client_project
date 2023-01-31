from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render, HttpResponse
from .models import Client, Role, Status, Details
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request, 'index.html')


def signup(request):

    if request.method == 'POST':
        username=request.POST['username']
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']

        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name=fname
        myuser.last_name=lname

        myuser.save()

        messages.success(request,"Your Account Has Been Created Successfully!")

        return redirect('signin')



    return render(request,'signup.html')

def signin(request):

    if request.method == 'POST':
        username=request.POST['username']
        #fname=request.POST['fname']
        #lname=request.POST['lname']
        #email=request.POST['email']
        pass1=request.POST['pass1']

        
        user=authenticate(username=username,password=pass1)



        if user is not None:
            login(request,user)
            #fname=user.first_name
            return render(request,'index.html')
        
        else:
            messages.error(request,"Bad Credentials!")
            return redirect('index.html')


    return render(request,'signin.html')

def signout(request):
    logout(request)
    return render(request, 'index.html')

def view_client(request):
    details = Details.objects.all()

    context={
        'details':details
    }

    return render(request, 'view_client.html',context)


def add_client(request):

    if request.method == 'POST':

        serial_num= int(request.POST['serial_num'])
        client_name=request.POST['client_name']
        project_name=request.POST['project_name']
       # project_details=request.POST['project_details']
       # project_role= int(request.POST['project_role'])
        team_lead= request.POST['team_lead']
        team_member=request.POST['team_member']
        scope=request.POST['scope']
        project_status= int(request.POST['project_status'])
        deadline=request.POST['deadline']

        try:

            starting_date=request.POST['starting_date']
            ending_date=request.POST['ending_date']
            new_details=Details(serial_num=serial_num, client_name=client_name, project_name=project_name, team_lead=team_lead, team_member=team_member, starting_date=starting_date, ending_date=ending_date, scope=scope, project_status_id=project_status, deadline=deadline)
            new_details.save()

        except:
            new_details=Details(serial_num=serial_num, client_name=client_name, project_name=project_name, team_lead=team_lead, team_member=team_member, scope=scope, project_status_id=project_status, deadline=deadline)
            new_details.save()


        
        return HttpResponse('Client Added Succesfully!')
    
    elif request.method == 'GET':
        return render(request,'add_client.html')
    
    else:
        return HttpResponse("An Exception Occured. Client Hasn't Been Added!")
    
    return render(request, 'add_client.html')

def remove_client(request):
    return render(request, 'remove_client.html')


def filter_client(request):

    if request.method=='POST':
        client_name = request.POST[ 'client_name']
        project_status = request.POST[ 'project_status']
        details= Details.objects.all()

        if client_name:
            details= details.filter(client_name__icontains=client_name)

        if project_status:
            details = details.filter(project_status__status__icontains=project_status)
        
        context={
            'details': details
        }

        return render(request, 'view_client.html',context)
    
    elif request.method =='GET':
        return render(request, 'filter_client.html')
    
    else:
        return HttpResponse('An Exception Occured!')

def view_project(request):
    details = Details.objects.filter(is_approved=True)

    context={
        'details':details
    }

    return render(request, 'view_project.html',context)

def project_details(request):
    if request.method=='POST':
        client_name = request.POST[ 'client_name']
        details= Details.objects.filter(is_approved=True)

        if client_name:
            details= details.filter(client_name__icontains=client_name)

        
        context={
            'details': details
        }

        return render(request, 'view_project.html',context)
    
    elif request.method =='GET':
        return render(request, 'project_details.html')
    
    else:
        return HttpResponse('An Exception Occured!')