from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from .models import Service
from .forms import ServiceForm

# Create your views here.

def services(request):
    services = Service.objects.all()
    return render(request, 'services/services.html', {'services': services})

def add_service(request):
    if request.method == 'POST':
        form = ServiceForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Service added successfully')
            return redirect('services')
        else:
            messages.error(request, 'Failed to add service')
    else:
        form = ServiceForm()

    return render(request, 'services/add_service.html', {'form': form})

def edit_service(request,id):
    service = get_object_or_404(Service, pk=id)

    if request.method == 'POST':
        form = ServiceForm(request.POST, request.FILES, instance=service)
        if form.is_valid():
            form.save()
            messages.success(request, 'Service updated successfully')
            return redirect('services')
        else:
            messages.error(request, 'Failed to update service')
    else:
        form = ServiceForm(instance=service)

    return render(request, 'services/edit_service.html', {'form': form,'service': service})


def delete_service(request, id):
    service = get_object_or_404(Service, pk=id)
    if request.method == 'POST':
        service.delete()
        messages.success(request, 'Service deleted successfully')
        return redirect('services')
    return render(request, 'services/delete_service.html', {'service': service})