from django.shortcuts import render

# Create your views here.
def my_view(request):
    return render(request,'home/index.html')

def custom_404(request, exception=None):
    return render(request, '404.html',status=404)