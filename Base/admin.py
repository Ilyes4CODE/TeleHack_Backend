from django.contrib import admin
from .models import Client,TicketCenter,TicketTech,Center,FeedBack
# Register your models here.
admin.site.register(Client)
admin.site.register(Center)
admin.site.register(TicketCenter)
admin.site.register(TicketTech)
admin.site.register(FeedBack)