from django.shortcuts import render
# from django.http import HttpResponse
from .models import User, Container, Rental, SibTransLog, Notification

def dataset_view(request):
    users = User.objects.all()
    containers = Container.objects.all()
    rentals = Rental.objects.all()
    sibtranslogs = SibTranslog.objects.all()
    notifications = Notification.objects.all()

    return render(request, 'dataset.html', {
        'users': users,
        'containers': containers,
        'rentals': rentals,
        'sibtranslogs': sibtranslogs,
        'notifications': notifications
    })
