from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from .models import Service,Testimonial
from .forms import ServiceForm,TestimonialForm
from django.contrib.auth.decorators import login_required

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
    else:
        messages.error(request, 'Failed to delete service')
        
    return render(request, 'services/delete_service.html', {'service': service})


def view_testimonials(request):
    testimonials = Testimonial.objects.select_related('service','user').all()
    return render(request, 'services/testimonials.html', {'testimonials': testimonials})

@login_required
def add_testimonial(request):
    if request.method == 'POST':
        form = TestimonialForm(request.POST)
        if form.is_valid():
            testimonial = form.save(False)
            testimonial.user = request.user
            testimonial.save()
            messages.success(request, 'Testimonial added successfully')
            return redirect('view_testimonials')
        else:
            messages.error(request, 'Failed to add testimonial')
    else:
        form = TestimonialForm()

    return render(request, 'services/add_testimonial.html', {'form': form})

@login_required
def edit_testimonial(request,id):
    testimonial = get_object_or_404(Testimonial, pk=id)
    
    if testimonial.user != request.user:
        messages.error(request, 'You do not have permission to edit this testimonial')
        return redirect('view_testimonials')

    if request.method == 'POST':
        form = TestimonialForm(request.POST, instance=testimonial)
        if form.is_valid():
            form.save()
            messages.success(request, 'Testimonial updated successfully')
            return redirect('view_testimonials')
        else:
            messages.error(request, 'Failed to update testimonial')
    else:
        form = TestimonialForm(instance=testimonial)

    return render(request, 'services/edit_testimonial.html', {'form': form,'testimonial': testimonial})

@login_required
def delete_testimonial(request, id):
    testimonial = get_object_or_404(Testimonial, pk=id)
    if request.method == 'POST':
        if testimonial.user != request.user:
            messages.error(request, 'You do not have permission to delete this testimonial')
            return redirect('view_testimonials')
        testimonial.delete()
        messages.success(request, 'Testimonial deleted successfully')
        return redirect('view_testimonials')
    else:
        messages.error(request, 'Failed to delete testimonial')
        
    return render(request, 'services/delete_testimonial.html', {'testimonial': testimonial})