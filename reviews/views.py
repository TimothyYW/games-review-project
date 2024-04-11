from django.views.generic import (CreateView, ListView, DeleteView, UpdateView, DetailView)

from django.contrib.auth.mixins import (
    UserPassesTestMixin, LoginRequiredMixin
)

from django.db.models import Q

from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Review
from .forms import ReviewForm


class Reviews(ListView):
    """ View all reviews """

    template_name = "reviews/reviews.html"
    model = Review
    context_object_name = 'reviews'

    def get_queryset(self, **kwargs):
        query = self.request.GET.get('Q')
        if query:
            reviews = self.model.objects.filter(
                Q(game_name=query) |
                Q(game_type=query)  |
                Q(genre=query)  |
                Q(developer=query)
            )
        else:
            reviews = self.model.objects.all()
        return reviews

class ReviewDetail(DetailView):
    """View a single recipe"""

    template_name = "reviews/review_detail.html"
    model = Review
    context_object_name = "review"

class InputReview(LoginRequiredMixin, CreateView):
    """ Add review view """
    template_name = 'reviews/input_review.html'
    model = Review
    form_class = ReviewForm
    success_url = '/reviews/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(InputReview, self).form_valid(form)

class EditReview(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """Edit a review"""
    template_name = 'reviews/edit_review.edit_review.html'
    model = Review
    form_class = ReviewForm
    success_url = '/reviews/'

    def test_func(self):
        return self.request.user == self.get_object().user

class DeleteReview(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """ Delete a review """
    model = Review
    success_url = '/reviews/'

    def test_func(self):
        return self.request.user == self.get_object().user