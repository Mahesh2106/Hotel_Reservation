from django.urls import path
from Hotel_admin import views

urlpatterns=[



    path('admin_pg/',views.admin_pg,name="admin_pg"),
    path('login_save/',views.login_save,name="login_save"),

    path('Logout_admin/',views.Logout_admin,name="Logout_admin"),


############ Admin Page ###############

    path('Index_page/',views.Index_page,name="Index_page"),

################## Hotel Admin Side ################

    path('Hotel_pg/',views.Hotel_pg,name="Hotel_pg"),
    path('Hotel_save/',views.Hotel_save,name="Hotel_save"),

    path('Hotel_display/',views.Hotel_display,name="Hotel_display"),
    path('Hotel_edit/<int:infoid>',views.Hotel_edit,name="Hotel_edit"),

    path('Hotel_Details_del/<int:infoid>',views.Hotel_Details_del,name="Hotel_Details_del"),
    path('Hotel_Info_Update/<int:infoid>',views.Hotel_Info_Update,name="Hotel_Info_Update"),

################# Rooms ##########################

    path('Rooms_pg/',views.Rooms_pg,name="Rooms_pg"),
    path('Rooms_Save/',views.Rooms_Save,name="Rooms_Save"),

    path('display_rooms/',views.display_rooms,name="display_rooms"),
    path('Edit_rooms/<int:infoid>',views.Edit_rooms,name="Edit_rooms"),

    path('Update_Rooms/<int:infoid>',views.Update_Rooms,name="Update_Rooms"),
    path('Delete_rooms/<int:infoid>',views.Delete_rooms,name="Delete_rooms"),

################# Features #######################

    path('Hotel_feature_pg/',views.Hotel_feature_pg,name="Hotel_feature_pg"),

    path('Hotel_feature_save/',views.Hotel_feature_save,name="Hotel_feature_save"),
    path('Hotel_feature_display/',views.Hotel_feature_display,name="Hotel_feature_display"),

    path('Hotel_feature_edit/<int:infoid>',views.Hotel_feature_edit,name="Hotel_feature_edit"),
    path('Hotel_feature_update/<int:infoid>',views.Hotel_feature_update,name="Hotel_feature_update"),

    path('Hotel_Feature_delete/<int:infoid>',views.Hotel_Feature_delete,name="Hotel_Feature_delete"),


############### Amenity Section ##############

    path('Amenties_Add_pg/',views.Amenties_Add_pg,name="Amenties_Add_pg"),

    path('save_amenity/',views.save_amenity,name="save_amenity"),
    path('Disp_amenity/',views.Disp_amenity,name="Disp_amenity"),

    path('Edit_pg/<int:infoid>',views.Edit_pg,name="Edit_pg"),
    path('Update_amenity/<int:infoid>',views.Update_amenity,name="Update_amenity"),

    path('Dele_amenity/<int:infoid>',views.Dele_amenity,name="Dele_amenity"),

################ Hotel Team Section #################

    path('Team_add_pg/',views.Team_add_pg,name="Team_add_pg"),

    path('save_Team/',views.save_Team,name="save_Team"),
    path('Team_disp/',views.Team_disp,name="Team_disp"),

    path('Edit_team/<int:infoid>',views.Edit_team,name="Edit_team"),
    path('Delete_team/<int:infoid>',views.Delete_team,name="Delete_team"),

    path('update_team/<int:infoid>',views.update_team,name="update_team"),



    ##########################  Rooms #################################

    path('Add_Room/',views.Add_Room,name="Add_Room"),

    path('Room_save/',views.Room_save,name="Room_save"),
    path('display_room/',views.display_room,name="display_room"),

    path('Edit_Room_detail/<int:dataid>',views.Edit_Room_detail,name="Edit_Room_detail"),
    path('Update_room/<int:dataid>',views.Update_room,name="Update_room"),

    path('Delete_room_details/<int:dataid>',views.Delete_room_details,name="Delete_room_details"),

    #################### BEVERAGES AND FOODS ##############################

    path('Add_Beverages_Food/',views.Add_Beverages_Food,name="Add_Beverages_Food"),

    path('save_Beverages/',views.save_Beverages,name="save_Beverages"),
    path('Display_items/',views.Display_items,name="Display_items"),

    path('Edit_items/<int:infoid>',views.Edit_items,name="Edit_items"),
    path('Update_Beverages/<int:infoid>',views.Update_Beverages,name="Update_Beverages"),

    path('Delete_Items/<int:infoid>',views.Delete_Items,name="Delete_Items"),


#################################################
    path('User_Registration_Display/',views.User_Registration_Display,name="User_Registration_Display"),
    path('Report_User/<int:infoid>',views.Report_User,name="Report_User"),

    path('update_User_field/<int:infoid>',views.update_User_field,name="update_User_field"),


###################################################
    path('Mail_Customers_Display/',views.Mail_Customers_Display,name="Mail_Customers_Display"),
    path('View_Bookings_Display/',views.View_Bookings_Display,name="View_Bookings_Display"),

    path('Delete_Bookings_Single/<int:infoid>',views.Delete_Bookings_Single,name="Delete_Bookings_Single"),

###################################################






]