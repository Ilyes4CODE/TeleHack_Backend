from rest_framework.permissions import IsAuthenticated
from .models import Center,TicketTech,TicketCenter,FeedBack
from rest_framework.decorators import api_view,permission_classes
from .serializer import get_centers,TechPost,CenterTicketPost,Get_Ticket_center,Post_FeedBack,Get_Feedback
from rest_framework.response import Response
from .models import Client
from rest_framework import status
from django.shortcuts import get_object_or_404
# Create your views here.

@api_view(['GET'])
def Get_Centers(request):
    centers = Center.objects.all()
    serializer = get_centers(centers,many=True)
    return Response({"centers" : serializer.data})


@api_view(['POST'])
def Post_Ticket_tech(request):
    data = request.data
    serializer = TechPost(data=data)
    if serializer.is_valid():
        nbr = TicketTech.objects.all().count()
        client_obj = Client.objects.get(user=request.user)
        if TicketTech.objects.filter(Client=client_obj).exists():
                return Response({"error": "You have already took a ticket"}, status=status.HTTP_400_BAD_REQUEST)
        TicketTech.objects.create(
            Title = data['Title'],
            Description = data['Description'],
            first_name = data['first_name'],
            last_name = data['last_name'],
            phone_number = data['phone_number'],
            adress = data['address'],
            place = nbr + 1 
        )
        return Response({'info':'Tech Ticket Created'})
    else:
        return Response({"error":serializer.errors})
    
@api_view(['GET'])
def Get_related_tickets(request):
     client = Client.objects.get(user=request.user)
     tickets = TicketTech.objects.filter(Client=client)
     serializer = TechPost(tickets,many=True)
     return Response({"info":serializer.data})

@api_view(['GET'])
def Get_Ticket_Tech_By_Id(request,pk):
    tech_ticket = get_object_or_404(TicketTech,pk=pk)
    serializer = TechPost(tech_ticket,many=False)
    return Response({"Info":serializer.data})

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def Delete_Tickets(request,pk):
    deleted_obj = get_object_or_404(TicketTech,pk=pk)
    if request.user == deleted_obj.Client.user:
        higher_tickets = TicketTech.objects.filter(place__gt=deleted_obj.place)
        for i in higher_tickets:
              i.place = i.place - 1
              i.save()
        deleted_obj.delete()
        return Response({'info':'obj Deleted'}) 
    else:
         return Response({'Error':'You Are Not authorized'},status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['POST'])
def Center_Ticket_Post(request):
     data = request.data
     serializer = CenterTicketPost(data=data)
     if serializer.is_valid():
        center_id = Center.objects.get(name=data['center']).pk
        primary = Center.objects.get(pk=center_id)
        TicketCenter.objects.create(
            Title = data['Title'],
            Description = data['Description'],
            Center = primary,
            place = TicketCenter.objects.all().count() +1
        )
        return Response({'info':'Ticket created'})
     else:
        return Response(serializer.errors)

@api_view(['GET'])
def Get_All_Center_Tickets(request):
    tickets = TicketCenter.objects.all()
    serializer = Get_Ticket_center(tickets,many=True)
    return Response({'Data':serializer.data})

@api_view(['GET'])
def Get_Ticket_By_Id(request,pk):
    tickets = TicketCenter.objects.get(pk=pk)
    serializer = Get_Ticket_center(tickets,many=False)
    return Response({'Data':serializer.data})

@api_view(['DELETE'])
def Delete_Center_Ticket(request,pk):
    ticket = get_object_or_404(TicketCenter,pk=pk)
    higher_places = TicketCenter.objects.filter(place__gt=ticket.place)
    for i in higher_places:
        i.place = i.place - 1
        i.save()
    ticket.delete()
    return Response({"Info":"Deleted Center Ticket"})

#######################################################
@api_view(['POST'])
def Post_FeedBacks(request):
    data = request.data
    serializer = Post_FeedBack(data=data)
    if serializer.is_valid():
        FeedBack.objects.create(
            Title = data['Title'],
            Description = data['Description'],
            center = data['center']
        )
        return Response({"Info":"Created"})
    else:
        return Response({serializer.errors})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def Get_FeedBacks(request):
    feedbacks = FeedBack.objects.all()
    serializer = Get_Feedback(feedbacks,many=True)
    return Response({serializer.data})

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def Delete_FeedBack(request,pk):
    deleted_feedback = get_object_or_404(FeedBack,pk=pk)
    if deleted_feedback.client.user != request.user:
        return Response({"info":"You Are Not Authorized"})
    else:
        deleted_feedback.delete()
        return Response({"Info":"Feed Back Deleted"})
    



