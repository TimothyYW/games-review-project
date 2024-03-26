from django.views.generic import CreateView, ListView, DeleteView

from django.contrib.auth.mixins import (
    UserPassesTextMixin, LoginRequiredMixin
)

from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Review
from .forms import Reviewform


class Reviews(ListView):
    """ View all reviews """
    template_name = "reviews/reviews.html"
    model = Review
    context_object_name = 'reviews'


class InputReview(LoginRequiredMixin, CreateView):
    """ Add review view """
    template_name = 'reviews/input_review.html'
    model = Review
    success_url = '/reviews/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(InputReview, self).form_valid(form)

class DeleteReview(LoginRequiredMixin, UserPassesTextMixin, DeleteView):
    """ Delete a review """
    model = Review
    success_url = '/reviews/'

    def test_func(self):
        return self.request.user == self.get_object().user