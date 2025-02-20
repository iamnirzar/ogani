from django.shortcuts import render,HttpResponse,redirect
from .models import*

# Create your views here.
def home(request):
    return HttpResponse("this is homepage.")

def login(request):
    if request.POST:
        username=request.POST['username']
        password=request.POST['password']
        confirmpassword = request.POST['confirmpassword']
        User.objects.create(username=username,password=password,confirmpassword=confirmpassword)
        if password == confirmpassword:
            return redirect(index)
        else:
            contaxt={
            "msg":"Password Not Match",
            }
        return render(request,"login.html",contaxt)
    else:
        return render(request,"login.html")

def blog(request):
    return render(request,'blog.html')

def blogdetails(request):
    return render(request,'blogdetails.html')

def checkout(request):
    return render(request,'checkout.html')

def contact(request):
    return render(request,'contact.html') 

def index(request):
    dept_id = Department.objects.all()
    pid = Product.objects.all()
    uid = request.GET.get('uid')
    if uid:
        pid=Product.objects.filter(Department=uid)
    else:
        pid=Product.objects.all()

    contaxt = {
        "dept_id":dept_id,
        "pid":pid,
        "uid":uid,
    }
    return render(request,'index.html',contaxt)

def main(request):
    return render(request,'main.html')

def shopdetails(request):
    return render(request,'shopdetails.html')

def shopgrid(request):
    dept_id = Department.objects.all()
    pid = Product.objects.all()
    uid = request.GET.get("uid")
    cid = Color.objects.all()

    if uid:
        pid=Product.objects.filter(Department=uid)
    else:
        pid=Product.objects.all()

    contaxt = {
        "dept_id":dept_id,
        "pid":pid,
        "uid":uid,
        "cid":cid,
    }
    return render(request,'shopgrid.html',contaxt)

def shopingcart(request):
    return render(request,'shopingcart.html')

def clr_filter(request):
    cid = Color.objects.all()
    cf = request.POST.get('colorname')
    print(cf)
    l1 = []

    if cf:
        pid = Product.objects.filter(Color__colorname=cf)
        l1.extend(pid)
        print(l1)
    else:
        pid = Product.objects.all()

    contaxt = {
        "cid":cid,
        "cf":cf,
        "pid":l1,
    }
    
    return render(request,"shopgrid.html",contaxt)