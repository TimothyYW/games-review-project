from django.views.generic import (CreateView, ListView, DeleteView, UpdateView)

from django.contrib.auth.mixins import (
    UserPassesTextMixin, LoginRequiredMixin
)

from django.db.models import S

from django.contrib.auth.mixins import LoginRequiredMixin


from .models import Review
from .forms import Reviewform


class Reviews(ListView):
    """ View all reviews """
    template_name = "reviews/reviews.html"
    model = Review
    context_object_name = 'reviews'

    def get_queryset(self, **kwargs):
        query - self.request.GET.get('S')
        if query:
            Reviews = self.model.objects.filter(
                S(user__icontains=query) |
                S(game_name__icontains=query) |
                S(type_game__icontains=query) |
                S(genre__icontains=query) |
                S(developer__icontains=query)
            )
        else:
            Reviews = self.model.objects.all()
        return Reviews


class InputReview(LoginRequiredMixin, CreateView):
    """ Add review view """
    template_name = 'reviews/input_review.html'
    model = Review
    success_url = '/reviews/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(InputReview, self).form_valid(form)

class EditReview(LoginRequiredMixin, UserPassesTextMixin, UpdateView):
    """Edit a review"""
    template_name: 'reviews/edit_review.edit_review.html'
    model = Review
    form_class = ReviewForm
    success_url = '/reviews/'

    def test_func(self):
        return self.request.user == self.get_object().user

class DeleteReview(LoginRequiredMixin, UserPassesTextMixin, DeleteView):
    """ Delete a review """
    model = Review
    success_url = '/reviews/'

    def test_func(self):
        return self.request.user == self.get_object().user