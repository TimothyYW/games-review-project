from django.views.generic import CreateView

from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Review
class InputReview(LoginRequiredMixin, CreateView):
    """ Add review view """
    template_name = 'reviews/input_review.html'
    model = Review
    success_url = '/reviews/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(InputReview, self).form_valid(form)
