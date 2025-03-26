from django.shortcuts import render,HttpResponse,redirect
from .models import*
from django.core.paginator import Paginator

# Create your views here.
def home(request):
    return HttpResponse("this is homepage.")

def register(request):
    if request.POST:
        username=request.POST['username']
        password=request.POST['password']
        confirm_pas = request.POST['confirm_pas']
        email = request.POST['email']
        Register.objects.create(username=username,password=password,email=email)
        if password == confirm_pas:
            return redirect(login)
        else:
            contaxt={
            "msg":"Password Not Match",
            }
        return render(request,"register.html",contaxt)
    else:
        return render(request,"register.html")
    
def login(request):
    if 'email' in request.session:
        return redirect("index")
    try:
       if request.POST:
            email=request.POST['email']
            print(email)
            password=request.POST['password']
            print(password)
            uid= Register.objects.get(email=email)
            print(uid)
            if uid.email==email:
                request.session['email']=uid.email
                if uid.password==password:
                    return redirect("index")
                else:
                    con={"msg":"invalid password"}
                    return render(request,"login.html",con)
            else:
                con={"msg":"invalid Email or Username"}
                return render(request,"login.html",con)
                    
    except Register.DoesNotExist:
            con={"msg":"invalid Email"}
            return render(request,"register.html",con)
    else:
        return render(request,"login.html")
    
def logout(request):
    if 'email' in request.session:
        del request.session['email']
        return redirect('login')

def blog(request):
    uid = Register.objects.get(email=request.session['email'])
    total_cart_price = Cart.total_cart_price()
    cid = Cart.objects.all()

    contaxt = {"uid":uid,
               "cid":cid,
               "total_cart_price":total_cart_price,
               }
    return render(request,'blog.html',contaxt)

def blogdetails(request):
    uid = Register.objects.get(email=request.session['email'])
    total_cart_price = Cart.total_cart_price()
    cid = Cart.objects.all()

    contaxt = {"uid":uid,
               "cid":cid,
               "total_cart_price":total_cart_price,
               }
    return render(request,'blogdetails.html',contaxt)

def checkout(request):
    uid = Register.objects.get(email=request.session['email'])
    total_cart_price = Cart.total_cart_price()    
    cid = Cart.objects.all()
    indian_states = Billingdetails.INDIAN_STATES
    contaxt = {"uid":uid,
               "cid":cid,
               "total_cart_price":total_cart_price,
               "indian_states":indian_states,
               }
    return render(request,'checkout.html',contaxt)

def bill_detail(request):
    if request.POST:
        name = request.POST['name']
        lname = request.POST['lname']
        country = request.POST['country']
        address = request.POST['address']
        city = request.POST['city']
        state = request.POST['state']
        postcode = request.POST['postcode']
        phone = request.POST['phone']
        email = request.POST['email']
        Billingdetails.objects.create(name=name,lname=lname,country=country,address=address,city=city,state=state,postcode=postcode,phone=phone,email=email)
        return redirect("checkout")
    else:
        return render(request,"checkout.html")

def contact(request):
    uid = Register.objects.get(email=request.session['email'])
    total_cart_price = Cart.total_cart_price()
    cid = Cart.objects.all()
    wish_id = add_to_wishlist.objects.filter(user_id=uid)


    contaxt = {"uid":uid,
               "total_cart_price":total_cart_price,
               "cid":cid,
               "wish_id":wish_id,
               }
    return render(request,'contact.html',contaxt) 

def index(request):
    # if 'email' in request.session:
        uid=Register.objects.get(email=request.session['email'])
        dept_id = Department.objects.all()
        pid = Product.objects.all()
        did = request.GET.get('did')
        cid = Cart.objects.all()
        total_cart_price = Cart.total_cart_price()
        wish_id = add_to_wishlist.objects.filter(user_id=uid)
        
        if did:
            pid=Product.objects.filter(Department=did)
        else:
            pid=Product.objects.all()

        paginator = Paginator(pid,9)
        page_number = request.GET.get("page",1)
        try:
            page_number = int(page_number)
        except ValueError:
            page_number = 1 
        
        pid = paginator.get_page(page_number)
        show_page = paginator.get_elided_page_range(page_number,on_each_side=1,on_ends=1)

        contaxt = {
            "dept_id":dept_id,
            "pid":pid,
            "did":did,
            "uid":uid,
            "cid":cid,
            "total_cart_price":total_cart_price,
            "wish_id":wish_id,
            "show_page":show_page,
        }
        return render(request,'index.html',contaxt)

def main(request):
    return render(request,'main.html')

def shopdetails(request):
    dep_id = Department.objects.all()
    did= request.GET.get('id')
    pid = Product.objects.all()
    cid = Cart.objects.all()
    uid = Register.objects.get(email=request.session['email'])
    print(did)
    total_cart_price = Cart.total_cart_price()


    if did:
        pid = Product.objects.filter(dept_id=did)
    else:
        pid = Product.objects.all()

    contaxt = { "dep_id":dep_id,
                "did":did,
                "uid":uid,
               "pid":pid,
               "cid":cid,
               "total_cart_price":total_cart_price,
               }
    return render(request,'shopdetails.html',contaxt)

def productdetails(request,id):
    pid = Product.objects.get(id=id)
    uid = Register.objects.get(email=request.session['email'])
    contaxt = {"uid":uid,
               "pid":pid,
               }
    print(pid)
    return render(request,"shopdetails.html",contaxt)

def shopgrid(request):

    uid = Register.objects.get(email=request.session['email'])
    dept_id = Department.objects.all()
    pid = Product.objects.all()
    did = request.GET.get("did")
    Cid = Color.objects.all()
    sid = Size.objects.all()
    cid = Cart.objects.all()
    total_cart_price = Cart.total_cart_price()

    wish_id = add_to_wishlist.objects.filter(user_id=uid)
    l1 = []
    for i in wish_id:
        l1.append(i.product_id)
    print(l1)

    if did:
        pid=Product.objects.filter(Department=did)
    else:
        pid=Product.objects.all()

    paginator = Paginator(pid,9)
    page_number = request.GET.get("page",1)
    try:
            page_number = int(page_number)
    except ValueError:
        page_number = 1 
        
    pid = paginator.get_page(page_number)
    show_page = paginator.get_elided_page_range(page_number,on_each_side=1,on_ends=1)

    contaxt = {
        "dept_id":dept_id,
        "pid":pid,
        "wish_id":wish_id,
        "l1":l1,
        "did":did,
        "Cid":Cid,
        "sid":sid,
        "uid":uid,
        "cid":cid,
        "total_cart_price":total_cart_price,
        "show_page":show_page,
    }
    return render(request,'shopgrid.html',contaxt)

def shopingcart(request):
    uid = Register.objects.get(email=request.session['email'])
    cid = Cart.objects.all()
    total_cart_price = Cart.total_cart_price()
    contaxt = {"uid":uid,
               "cid":cid,
               "total_cart_price":total_cart_price,
               }
    return render(request,'shopingcart.html',contaxt)

def addtocart(request,id):
    uid = Register.objects.get(email=request.session['email'])
    pid = Product.objects.get(id=id)
    print(pid)

    if pid:
        qty = int(request.POST.get('qty',1))
        total_price = pid.price*qty
        Cart.objects.create(image=pid.image,name=pid.name,price=pid.price,qty=1,total_price=total_price,user_id=uid)
    return redirect("shopingcart")

def wishlist_product(request,id):
    uid = Register.objects.get(email=request.session['email'])
    pid = Product.objects.get(id=id)
    
    peid = add_to_wishlist.objects.filter(user_id=uid,product_id=pid).exists()
    if peid:
        add_to_wishlist.objects.filter(user_id=uid, product_id=pid).delete()
        return redirect("shopgrid")
    else:
        add_to_wishlist.objects.create(product_id=pid,user_id=uid,name=pid.name ,price=pid.price,image=pid.image)
        return redirect("shopgrid")


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

def size_filter(request):
    sid = Size.objects.all()
    sf = request.POST.get('sizename')
    print(sf)
    l2 = []

    if sf:
        pid = Product.objects.filter(Size__sizename=sf)
        l2.extend(pid)
        print(l2)
    else:
        pid = Product.objects.all()

    context ={
        "sid":sid,
        "sf":sf,
        "pid":l2
    }

    return render(request,"shopgrid.html", context)

def price_filter(request):
    pid = Product.objects.all()


    if request.POST:
        min = request.POST['min']
        max = request.POST['max']

        pid=Product.objects.filter(price__lte=max,price__gte=min)

        contaxt={
        
        "pid":pid,
        "max":max,
        "min":min,
        }
        print(min)
        print(max)
        return render(request,"shopgrid.html",contaxt)
    else:
        pid = Product.objects.all()

    contaxt={
        
        "pid":pid,
        "max":None,
        "min":None,
        }
    return render(request,"shopgrid.html",contaxt)

def profile(request):
    uid = Register.objects.get(email=request.session['email'])

    contaxt = {"uid":uid,
               }
    return render(request,"profile.html",contaxt)

def update(request,id):
    uid = Register.objects.get(id=id)
    if request.POST:
        username=request.POST['username']
        email=request.POST['email']
        address=request.POST['address']
        number=request.POST['number']
        image=request.FILES.get('image')
        uid.username=username
        uid.email=email
        uid.address=address
        uid.number=number
        if image:
            uid.image = image
        uid.save()
        request.session['email']=uid.email
        return redirect("profile")
    else:
        return render(request,"profile.html")
    
def pluscart(request,id):
    peid = Cart.objects.get(id=id)
    peid.qty = peid.qty+1
    peid.total_price = peid.qty * peid.price
    peid.save()
    return redirect(shopingcart)

def minuscart(request,id):
    peid = Cart.objects.get(id=id)
    if peid.qty > 1:
        peid.qty -= 1
        peid.total_price = peid.qty * peid.price
        peid.save()
    else:
        peid.delete()
    return redirect(shopingcart)

def removecart(request,id):
    peid=Cart.objects.get(id=id)
    peid.delete()
    return redirect(shopingcart)

def search_filter(request):
    pid = Product.objects.all()
    # if request.POST:

    pass