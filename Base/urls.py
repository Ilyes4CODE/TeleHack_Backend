from django.urls import path
from . import views
urlpatterns = [
    path('Centers/',views.Get_Centers),
    #####################################################
    path('TicketTech/',views.Post_Ticket_tech),
    path('Get_Related_Tickets/',views.Get_related_tickets),
    path('Delete_Ticket/<str:pk>/',views.Delete_Tickets),
    path('TicketTech/<str:pk>/', views.Get_Ticket_Tech_By_Id),
    ######################################################
    path('Post_Ticket_Center/',views.Center_Ticket_Post),
    path('Get_Tickets_Center/',views.Get_All_Center_Tickets),
    path('ticketCenter/<str:pk>/',views.Get_Ticket_By_Id),
    path('Delete_Center_Ticket/<str:pk>/',views.Delete_Center_Ticket),
    #######################################################
    path('Post_FeedBack/',views.Post_FeedBacks),
    path('Get_FeedBacks/',views.Get_FeedBacks),
    path('Delete_Feedback/<str:pk>/',views.Delete_FeedBack),
]
