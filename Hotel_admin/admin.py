from django.contrib import admin
from Hotel_admin.models import Hotel_staff,Hotel,Features,Amenities,Advanced_Category,Room,Food_And_Beverages
from Hotel_frontend.models import Registration,Booking,Newsletter,Rating,PaymentDB

# Register your models here.

admin.site.register(Registration)
admin.site.register(Booking)
admin.site.register(Newsletter)
admin.site.register(Rating)
admin.site.register(PaymentDB)



admin.site.register(Hotel)
admin.site.register(Hotel_staff)
admin.site.register(Features)
admin.site.register(Amenities)
admin.site.register(Advanced_Category)
admin.site.register(Room)
admin.site.register(Food_And_Beverages)