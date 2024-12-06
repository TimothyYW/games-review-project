from django.views.generic import ListView
from reviews.models import Review
from django.shortcuts import render


class Index(ListView):
    template_name = "home/index.html"
    model = Review
    context_object_name = 'reviews'

    def get_queryset(self):
        return self.model.objects.order_by('-created_at')[:3]

def handler404(request, exception):
    return render(request, 'errors/404.html', status=404)

def handler500(request):
    return render(request, 'errors/500.html', status=500)
