from django.urls import path
from Hotel_frontend import views


urlpatterns=[
    path('Registration_pg/', views.Registration_pg, name="Registration_pg"),
    path('Save_Registration/', views.Save_Registration, name="Save_Registration"),

    path('Login_Page/', views.Login_Page, name="Login_Page"),
    path('Login_fun/', views.Login_fun, name="Login_fun"),

    path('Logout_Pg/', views.Logout_Pg, name="Logout_Pg"),



    ############################################################################


    path('Home_pg/',views.Home_pg,name="Home_pg"),

    path('About_pg/',views.About_pg,name="About_pg"),
    path('Contact_pg/',views.Contact_pg,name="Contact_pg"),

    path('Services_page/<cat>',views.Services_page,name="Services_page"),
    path('Category_Single/<cat>',views.Category_Single,name="Category_Single"),

    path('Booking_page/',views.Booking_page,name="Booking_page"),
    path('Booking_save/',views.Booking_save,name="Booking_save"),

    path('Rating_desk/',views.Rating_desk,name="Rating_desk"),

    path('Profile_Pg/',views.Profile_Pg,name="Profile_Pg"),
    path('update_registration/<int:infoid>',views.update_registration,name="update_registration"),




    ########  Newsletter  #######3

    path('Newsletter_save/',views.Newsletter_save,name="Newsletter_save"),
    path('Payment_save/',views.Payment_save,name="Payment_save"),

    path('view_bookings/',views.view_bookings,name="view_bookings"),
    path('Delete_Bookings/<int:infoid>',views.Delete_Bookings,name="Delete_Bookings"),

    path('download_booking_pdf/<int:infoid>',views.download_booking_pdf,name="download_booking_pdf"),
    path('Contact_save/',views.Contact_save,name="Contact_save"),


]
