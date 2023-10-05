from django.shortcuts import render,redirect
from Hotel_admin.models import Hotel,Hotel_staff,Features,Amenities,Advanced_Category,Room,Food_And_Beverages
from django.utils.datastructures import MultiValueDictKeyError
from django.core.files.storage import FileSystemStorage
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from Hotel_frontend.models import Registration,Newsletter,Booking

# Create your views here.

############# Login Page ################


def admin_pg(req):
    return render(req,"Admin Page.html")


def login_save(request):
    if request.method=="POST":
        unm=request.POST.get('username')
        pwd=request.POST.get('password')
        if User.objects.filter(username__contains=unm).exists():
            user=authenticate(username=unm,password=pwd)
            if user is not None:
                login(request,user)
                request.session['username']=unm
                request.session['password']=pwd
                messages.success(request, "Logged In Succesfully")
                return redirect(Index_page)
            else:
                messages.warning(request, "Please Check Your Credentials")
                return redirect(admin_pg)
        else:
            messages.warning(request, "Please Check Your Credentials")
            return redirect(admin_pg)
    else:
        messages.warning(request, "Please Check Your Credentials")
        return redirect(admin_pg)


def Logout_admin(request):
    del request.session['username']
    del request.session['password']
    messages.success(request, "Logout Succesfully")
    return redirect(admin_pg)


####### Hotel Section ###############

def Index_page(request):
    return render(request,"Index_pg.html")

def Hotel_pg(req):
    return render(req,"Add Hotel Info.html")

def Hotel_save(abc):
    if abc.method=="POST":
        Ro_des=abc.POST.get('Room_des')
        Ro_Cate=abc.POST.get('Room_cate')
        Ro_image=abc.FILES['Room_img']
        Ro_Price=abc.POST.get('Room_Price')
        x=Hotel(Category=Ro_Cate,Description=Ro_des,Image=Ro_image,Price_Range=Ro_Price)
        messages.success(abc, "Loggined In Succesfully")
        x.save()
        return redirect(Hotel_pg)

def Hotel_display(req):
    x=Hotel.objects.all()
    return render(req,"Display Hotel Information.html",{'key':x})

def Hotel_edit(req,infoid):
    x=Hotel.objects.get(id=infoid)
    return render(req,"Edit Page.html",{'key1':x})

def Hotel_Info_Update(abc,infoid):
    if abc.method=="POST":
        Ro_des=abc.POST.get('Room_des')
        Ro_Cate=abc.POST.get('Room_cate')
        Ro_Price=abc.POST.get('Room_Price')
        try:
            Ro_image = abc.FILES['Room_img']
            a=FileSystemStorage()
            b=a.save(Ro_image.name,Ro_image)
        except MultiValueDictKeyError:
            b=Hotel.objects.get(id=infoid).Image
            messages.success(abc,"Updated Succesfully")
        Hotel.objects.filter(id=infoid).update(Category=Ro_Cate,Description=Ro_des,Image=b,Price_Range=Ro_Price)
        return redirect(Hotel_display)

def Hotel_Details_del(req,infoid):
    x=Hotel.objects.filter(id=infoid)
    messages.warning(req, "Item Deleted")
    x.delete()
    return redirect(Hotel_display)

################ Features Section ##############

def Hotel_feature_pg(req):
    x=Hotel.objects.all()
    return render(req,"Hotel Features.html",{'x':x})

def Hotel_feature_save(req):
    if req.method=="POST":
        cat=req.POST.get('Category')
        prod=req.POST.get('Hotel_Prod')
        amt=req.POST.get('Price')
        ser=req.POST.get('Hotel_service')
        img=req.FILES['Img']
        y=Features(Category_name=cat,Amount=amt,Information=ser,Product=prod,Image=img)
        messages.success(req, "Added Succesfully")
        y.save()
        return redirect(Hotel_feature_pg)

def Hotel_feature_display(req):
    x=Features.objects.all()
    return render(req,"Display Departments.html",{'key':x})

def Hotel_feature_edit(req,infoid):
    y=Hotel.objects.all()
    x = Features.objects.get(id=infoid)
    return render(req,"Edit Department.html",{'x':x,'y':y})

def Hotel_feature_update(req,infoid):
    if req.method=="POST":
        cat=req.POST.get('Category')
        prod=req.POST.get('Hotel_Prod')
        amt=req.POST.get('Price')
        ser=req.POST.get('Hotel_service')
        try:
            img = req.FILES['Img']
            fs=FileSystemStorage()
            file=fs.save(img.name,img)
        except MultiValueDictKeyError:
            file=Features.objects.get(id=infoid).Image
            messages.success(req, "Updated Succesfully")

        Features.objects.filter(id=infoid).update(Category_name=cat,Amount=amt,Information=ser,Product=prod,Image=file)
        return redirect(Hotel_feature_display)


def Hotel_Feature_delete(req,infoid):
    x=Features.objects.filter(id=infoid)
    messages.warning(req,"Item Deleted Successfully")
    x.delete()
    return redirect(Hotel_feature_display)

#################### Amenties Section #####################

def Amenties_Add_pg(req):
    return render(req,"Add Amenties.html")

def save_amenity(req):
    if req.method=="POST":
        amname=req.POST.get('Amenties')
        amdes=req.POST.get('AmeniDes')
        amimg=req.FILES['AImage']
        x=Amenities(Amenities_name=amname,Amenities_des=amdes,Amenities_image=amimg)
        messages.success(req, "Added Succesfully")
        x.save()
        return redirect(Amenties_Add_pg)

def Disp_amenity(req):
    x=Amenities.objects.all()
    return render(req,"Display Amenity.html",{'x':x})

def Edit_pg(req,infoid):
    x=Amenities.objects.get(id=infoid)
    return render(req,"Edit Amenity.html",{'x':x})

def Update_amenity(req,infoid):
    if req.method=="POST":
        amname=req.POST.get('Amenties')
        amdes=req.POST.get('AmeniDes')
        try:
            amimg = req.FILES['AImage']
            fs=FileSystemStorage()
            file=fs.save(amimg.name,amimg)
        except MultiValueDictKeyError:
            file=Amenities.objects.get(id=infoid).Amenities_image
            messages.success(req, "Updated Succesfully")
        Amenities.objects.filter(id=infoid).update(Amenities_name=amname,Amenities_des=amdes,Amenities_image=file)
        return redirect(Disp_amenity)

def Dele_amenity(req,infoid):
    x=Amenities.objects.filter(id=infoid)
    messages.warning(req, "Deleted Succesfully")
    x.delete()
    return redirect(Disp_amenity)

################## Hotel Team Section #####################

def Team_add_pg(req):
    return render(req,"Add Hotel Team.html")

def save_Team(req):
    if req.method=="POST":
        Sname=req.POST.get('sname')
        design=req.POST.get('desing')
        simg=req.FILES['Simg']
        x=Hotel_staff(Person_Name=Sname,Designation=design,Person_Image=simg)
        messages.success(req, "Added Succesfully")
        x.save()
        return redirect(Team_add_pg)

def Team_disp(req):
    x=Hotel_staff.objects.all()
    return render(req,"Display Team Details.html",{'x':x})

def Edit_team(req,infoid):
    x=Hotel_staff.objects.get(id=infoid)
    return render(req,"Edit Team Page.html",{'x':x})

def Delete_team(req,infoid):
    x=Hotel_staff.objects.filter(id=infoid)
    messages.warning(req, "Deleted Succesfully")
    x.delete()
    return redirect(Team_disp)

def update_team(req,infoid):
    if req.method=="POST":
        Sname=req.POST.get('sname')
        design=req.POST.get('desing')
        try:
            simg = req.FILES['Simg']
            fs=FileSystemStorage()
            file=fs.save(simg.name,simg)
        except MultiValueDictKeyError:
            file=Hotel_staff.objects.get(id=infoid).Person_Image
            messages.success(req, "Updated Succesfully")
        Hotel_staff.objects.filter(id=infoid).update(Person_Name=Sname,Designation=design,Person_Image=file)
        return redirect(Team_disp)


################# Advanced Category ########################

def Rooms_pg(req):
    x=Features.objects.all()
    return render(req,"Add Advanced Category Info.html",{'x':x})

def Rooms_Save(req):
    if req.method=="POST":
        Ro_des = req.POST.get('Room_des')
        Ro_Name = req.POST.get('Room')
        Pname=req.POST.get('Pname')
        Ro_image1 = req.FILES['Room_img1']
        Ro_image2 = req.FILES['Room_img2']
        Ro_image3 = req.FILES['Room_img3']
        Ro_Price = req.POST.get('Room_Price')
        x=Advanced_Category(Image1=Ro_image1,Image2=Ro_image2,Image3=Ro_image3,Name=Ro_Name,Description=Ro_des,Price=Ro_Price,Product=Pname)
        messages.success(req, "Added Succesfully")
        x.save()
        return redirect(Rooms_pg)

def display_rooms(req):
    x=Advanced_Category.objects.all()
    return render(req,"Display Advanced Category Info.html",{'x':x})

def Edit_rooms(req,infoid):
    y=Features.objects.all()
    x=Advanced_Category.objects.get(id=infoid)
    return render(req,"Edit Advanced Category.html",{'x':x,'y':y})

def Update_Rooms(req,infoid):
    if req.method == "POST":
        Ro_des = req.POST.get('Room_des')
        Ro_Name = req.POST.get('Room')
        Ro_Price = req.POST.get('Room_Price')
        Pname = req.POST.get('Pname')
        try:
            Ro_image1 = req.FILES['Room_img1']
            fs=FileSystemStorage()
            file=fs.save(Ro_image1.name,Ro_image1)
        except MultiValueDictKeyError:
            file=Advanced_Category.objects.get(id=infoid).Image1
        try:
            Ro_image2 = req.FILES['Room_img2']
            x=FileSystemStorage()
            y=x.save(Ro_image2.name,Ro_image2)
        except MultiValueDictKeyError:
            y=Advanced_Category.objects.get(id=infoid).Image2

        try:
            Ro_image3 = req.FILES['Room_img3']
            x = FileSystemStorage()
            d = x.save(Ro_image3.name, Ro_image3)
        except MultiValueDictKeyError:
            d = Advanced_Category.objects.get(id=infoid).Image3
            messages.success(req, "Updated Succesfully")

        Advanced_Category.objects.filter(id=infoid).update(Image1=file,Image2=y,Image3=d,Product=Pname,Name=Ro_Name,Description=Ro_des,Price=Ro_Price)
        return redirect(display_rooms)

def Delete_rooms(req,infoid):
    x=Advanced_Category.objects.filter(id=infoid)
    messages.warning(req, "Deleted Succesfully")
    x.delete()
    return redirect(display_rooms)


################################################### Room #########################################################


def Add_Room(req):
    return render(req,"Add Room Details.html")

def Room_save(req):
    if req.method=="POST":
        rt=req.POST.get('Room_Type')
        pr=req.POST.get('Room_Price')
        cat=req.POST.get('cate')
        im=req.FILES['Room_img']
        X=Room(Room_Type=rt,Price=pr,Room_Image=im,Category=cat)
        messages.success(req, "Added Succesfully")
        X.save()
        return redirect(Add_Room)

def display_room(req):
    x=Room.objects.all()
    return render(req,"Display Room.html",{'x':x})

def Edit_Room_detail(req,dataid):
    x=Room.objects.get(Room_Num=dataid)
    return render(req,"Edit Room Details.html",{'x':x})

def Update_room(req,dataid):
    if req.method=="POST":
        rt = req.POST.get('Room_Type')
        pr = req.POST.get('Room_Price')
        cat = req.POST.get('cate')
        try:
            im = req.FILES['Room_img']
            fs=FileSystemStorage()
            file=fs.save(im.name,im)
        except MultiValueDictKeyError:
            file=Room.objects.get(Room_Num=dataid).Room_Image
            messages.success(req, "Updated Succesfully")
        Room.objects.filter(Room_Num=dataid).update(Room_Type=rt,Price=pr,Room_Image=file,Category=cat)
        return redirect(display_room)



def Delete_room_details(req,infoid):
    x=Room.objects.filter(Room_Num=infoid)
    messages.warning(req, "Deleted Succesfully")
    x.delete()
    return redirect(display_room)

###############################################
################# Beverages Section ###########

def Add_Beverages_Food(req):
    return render(req,"Add Beverages Food.html")

def save_Beverages(req):
    if req.method=="POST":
        item_type=req.POST.get('Item_Type')
        item_name=req.POST.get('Item_Name')
        pr=req.POST.get('Item_Price')
        im=req.FILES['Item_img']
        x=Food_And_Beverages(Item_Type=item_type,Item_Name=item_name,Item_Price=pr,Item_Image=im)
        messages.success(req, "Added Succesfully")
        x.save()
        return redirect(Add_Beverages_Food)

def Display_items(req):
    x=Food_And_Beverages.objects.all()
    return render(req,"Display Items.html",{'x':x})

def Edit_items(req,infoid):
    x=Food_And_Beverages.objects.get(Item_Id=infoid)
    return render(req,"Edit Items.html",{'x':x})

def Update_Beverages(req,infoid):
    if req.method=="POST":
        item_type=req.POST.get('Item_Type')
        item_name=req.POST.get('Item_Name')
        pr=req.POST.get('Item_Price')
        try:
            im = req.FILES['Item_img']
            fs=FileSystemStorage()
            file=fs.save(im.name,im)
        except MultiValueDictKeyError:
            file=Food_And_Beverages.objects.get(Item_Id=infoid).Item_Image
            messages.success(req, "Updated Succesfully")
        Food_And_Beverages.objects.filter(Item_Id=infoid).update(Item_Type=item_type,Item_Name=item_name,Item_Price=pr,Item_Image=file)
        return redirect(Display_items)

def Delete_Items(req,infoid):
    x=Food_And_Beverages.objects.filter(Item_Id=infoid)
    messages.warning(req, "Deleted Succesfully")
    x.delete()
    return redirect(Display_items)

################################

def User_Registration_Display(req):
    x=Registration.objects.all()
    return render(req,"User Registration Page.html",{'x':x})

def Report_User(req,infoid):
    x=Registration.objects.get(Customer_id=infoid)
    return render(req,"Report User.html",{'x':x})

def update_User_field(request, infoid):
    if request.method == "POST":
        remark = request.POST.get('txt')
        messages.success(request,"Message Sent Succesfully")
        Registration.objects.filter(Customer_id=infoid).update(Messages=remark)
        return redirect(Index_page)


################################################

def Mail_Customers_Display(req):
    y = Newsletter.objects.all()
    b = Newsletter.objects.count()
    return render(req,"Mail Customers Display.html",{'y':y,'b':b})


def View_Bookings_Display(req):
    x=Booking.objects.all()
    return render(req,"Display Bookings.html",{'x':x})

def Delete_Bookings_Single(req,infoid):
    x= Booking.objects.filter(Booking_ID=infoid)
    x.delete()
    messages.success(req,"Deleted Successfully")
    return redirect(View_Bookings_Display)