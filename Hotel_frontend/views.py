from django.shortcuts import render,redirect
from Hotel_admin.models import Hotel,Hotel_staff,Features,Amenities,Advanced_Category,Room,Food_And_Beverages
from Hotel_frontend.models import Registration,Newsletter,Booking,Rating,PaymentDB,Contact_DB
from django.db.models import Q
from django.contrib.staticfiles.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib import messages
from reportlab.pdfgen import canvas
from django.shortcuts import get_object_or_404
from django.http import HttpResponse


# Create your views here.
def Home_pg(req,):
    x=Hotel.objects.all()
    a=Hotel_staff.objects.all()
    return render(req,"Home.html",{'key':x,'a':a})

def About_pg(req):
    x = Hotel.objects.all()
    return render(req,"About.html",{'key':x})

def Contact_pg(req):
    z=Room.objects.all()
    x = Hotel.objects.all()
    return render(req,"Contact.html",{'key':x,'z':z})

def Services_page(req,cat):
    y = Hotel.objects.all()
    x=Features.objects.filter(Category_name=cat)
    z = Rating.objects.all()
    return render(req,"Services.html",{'x':x,'y':y,'z':z})


def Category_Single(req,cat):
    y=Amenities.objects.all()
    x = Hotel.objects.all()
    z = Advanced_Category.objects.filter(Product=cat)
    return render(req,"Category Single Info.html",{'key':x,'z':z,'y':y})


################################ Booking Functions #####################

def Booking_page(request):
    z = Room.objects.all()
    x = Hotel.objects.all()
    y = Food_And_Beverages.objects.all()
    pro = Registration.objects.get(Email=request.session['Email'])
    bookings = Booking.objects.filter(Email=request.session['Email'])
    total = 0
    for booking in bookings:
        total += booking.Total_Price
    return render(request,"Booking Page.html",{'z':z,'x':x,'y':y,'pro':pro,'total':total})

######################################################################
def Payment_save(req):
    if req.method=="POST":
        card_Holder=req.POST.get('name')
        Amt=req.POST.get('Amt')
        cvv=req.POST.get('cvv')
        expiry=req.POST.get('exp')
        card_Num=req.POST.get('card_num')
        user_email = req.session['Email']
        registration = get_object_or_404(Registration, Email=user_email)
        if registration:
            x=PaymentDB(Customer_ID=registration,CardHolder_Name=card_Holder,Amount=Amt,CVV=cvv,Expiry_Date=expiry,Card_Num=card_Num)
            messages.success(req,"Payment Succesfull Enjoy Your Stay")
            x.save()
            user_booking = Booking.objects.filter(Email=user_email)
            for booking in user_booking:
                booking.Total_Price = 0
                booking.save()
            return redirect(Home_pg)
        else:
            messages.warning(req, "Invalid Customer ID")
            return redirect(Home_pg)





######################################################################



######################################################################



def Booking_save(req):
    if req.method == "POST":
        checkin = req.POST.get('start_date')
        checkin_time = req.POST.get('start_Time')
        checkout = req.POST.get('end_date')
        checkout_time = req.POST.get('End_Time')
        room_num = req.POST.get('Room_Num')
        total_price = float(req.POST.get('Total_Price'))
        customer_email = req.POST.get('email')


        customer = Registration.objects.filter(Email=customer_email).first()
        if customer is None:

            messages.warning(req,"No Customer With Registered Mail")

        room = Room.objects.get(Room_Num=room_num)
        # bookings_overlap = Q(Check_in__lt=checkout) & Q(Check_out__gt=checkin)
        bookings_overlap = (Q(Check_in__lt=checkout) & Q(Check_out__gt=checkin)) | (
                    Q(Check_in__lt=checkin) & Q(Check_out__gt=checkin))
        bookings = Booking.objects.filter(Room_Num=room).filter(bookings_overlap)
        if bookings.exists():
            messages.warning(req,"Current Room Not Available For Given Date Range")

        else:
            booking = Booking(
                Check_in=checkin,
                Check_in_Time=checkin_time,
                Check_Out_Time=checkout_time,
                Check_out=checkout,
                Total_Price=total_price,
                Room_Num=room,
                Cust_ID=customer,Email=customer_email
            )
            messages.success(req, "Booked Successfully")
            booking.save()


        return redirect(Booking_page)


##########################################################################################
##########################################################################################


def Registration_pg(req):
    return render(req,"Registration.html")

def Save_Registration(request):
    if request.method=="POST":
        cus_name=request.POST.get('cname')
        mob=request.POST.get('mob')
        username=request.POST.get('uname')
        email=request.POST.get('email')
        address=request.POST.get('Address')
        pro_typ=request.POST.get('Proof_Type')
        prof_ID=request.POST.get('Proof_Id')
        passwrd=request.POST.get('pwd')
        Img=request.FILES['IDImage']
        x=Registration(Customer_Name=cus_name,Proof_Type=pro_typ,Proof_Id=prof_ID,Proof_Image=Img,Username=username,Password=passwrd,Email=email,Address=address,Phone_number=mob)
        messages.success(request, "Registration Saved Successfully")
        x.save()
        return redirect(Login_Page)

def Login_Page(req):
    return render(req,"Login_Page.html")

def Login_fun(request):
    if request.method=="POST":
        em=request.POST.get('email')
        pwd=request.POST.get('pwd')
        if Registration.objects.filter(Email=em,Password=pwd).exists():
            request.session['Email']=em
            request.session['Password']=pwd
            messages.success(request, "Logged in Successfully")
            return redirect(Home_pg)
        else:
            messages.warning(request, "Check Your Credentials")
            return redirect(Login_Page)
    else:
        messages.warning(request, "Check Your Credentials Or Sign Up ")
        return redirect(Login_Page)

def Logout_Pg(request):

    del request.session['Email']
    del request.session['Password']
    messages.success(request, "Logged Out Successfully")
    return redirect(Login_Page)


######

def update_registration(request,infoid):
    if request.method == "POST":
        cus_name = request.POST.get('cusname')
        mob = request.POST.get('mob')
        username = request.POST.get('usrname')
        email = request.POST.get('email')
        address = request.POST.get('addr')
        address1=request.POST.get('addr1')
        state=request.POST.get('state')
        country=request.POST.get('country')
        prof_ID = request.POST.get('proofid')

        try:
            Img = request.FILES['IdImg']
            fs = FileSystemStorage()
            x = fs.save(Img.name, Img)
        except MultiValueDictKeyError:
            x = Registration.objects.get(Customer_id=infoid).Proof_Image


        Registration.objects.filter(Customer_id=infoid).update(
            Customer_Name=cus_name,
            Proof_Id=prof_ID,
            Proof_Image=x,
            Username=username,
            Email=email,
            Address=address,
            Address1=address1,
            State=state,
            Country=country,
            Phone_number=mob,
        )



        messages.success(request, "Your registration has been updated.")

        return redirect(Home_pg)
################################


def Profile_Pg(request):
    x = Hotel.objects.all()
    pro=Registration.objects.get(Email=request.session['Email'])
    session_messages = request.session.get('messages', '').split(',')
    y = len(session_messages)
    return render(request,"Profile_pg.html",{'pro':pro,'key':x,'y':y})


########################################

def Rating_desk(req):
    if req.method=="POST":
        ratin=req.POST.get('rating')
        txt=req.POST.get('message')
        cus=req.POST.get('cus')
        x=Rating(username=cus,rating=ratin,Description=txt)
        messages.success(req, "Rating Submitted Successfully")
        x.save()
        return redirect(Booking_page)



#######################################



def Newsletter_save(req):
    if req.method=="POST":
        em=req.POST.get('NewsLetter')
        obj=Newsletter(Email=em)
        messages.success(req, "Email Submitted Successfully")
        obj.save()
        return redirect(Home_pg)



############ view Bookings ##############
def view_bookings(req):
    x=Booking.objects.filter(Email=req.session['Email'])
    return render(req,"view Bookings.html",{'x':x})

def Delete_Bookings(req,infoid):
    x= Booking.objects.filter(Booking_ID=infoid)
    x.delete()
    messages.success(req,"Deleted Successfully")
    return redirect(view_bookings)


################################### PDF #######################

def download_booking_pdf(req, infoid):
    booking = get_object_or_404(Booking, Booking_ID=infoid)
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="booking_{booking.Booking_ID}.pdf"'
    p = canvas.Canvas(response)
    p.drawString(100, 750, f"Booking ID: {booking.Booking_ID}")
    p.drawString(100, 710, f"Check In Date: {booking.Check_in.strftime('%Y-%m-%d')}")
    p.drawString(100, 690, f"Check In Time: {booking.Check_in_Time}")
    p.drawString(100, 670, f"Check Out Time: {booking.Check_Out_Time}")
    p.drawString(100, 650, f"Check Out Date: {booking.Check_out.strftime('%Y-%m-%d')}")
    p.drawString(100, 630, f"Room Type: {booking.Room_Num.Room_Type}")
    p.drawString(100, 600, f"Room Num: {booking.Room_Num.Room_Num}")
    p.drawString(100, 580, f"Customer Id: {booking.Cust_ID.Customer_id}")
    p.drawString(100, 550, f"Email: {booking.Cust_ID.Email}")
    p.drawString(100, 510, f"Booked Date: {booking.Booking_Date.strftime('%Y-%m-%d')}")
    p.showPage()
    p.save()
    return response


def Contact_save(req):
    if req.method=="POST":
        msg=req.POST.get('message')
        nme=req.POST.get('name')
        mail=req.POST.get('email')
        phone=req.POST.get('phone')
        x=Contact_DB(Messages=msg,Name_User=nme,Email=mail,PhoneNumber=phone)
        x.save()
        messages.success(req,"Contact Details Submitted Successfully")
        return redirect(Home_pg)