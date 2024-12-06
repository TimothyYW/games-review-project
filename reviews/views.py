from django.views.generic import (
    CreateView, ListView, DeleteView, UpdateView, DetailView)

from django.contrib.auth.mixins import (
    UserPassesTestMixin, LoginRequiredMixin
)

from django.db.models import Q
from django.contrib import messages
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Review
from .forms import ReviewForm


class Reviews(ListView):
    """ View all reviews """

    template_name = "reviews/reviews.html"
    model = Review
    context_object_name = 'reviews'
    paginate_by = 6

    def get_queryset(self, **kwargs):
        query = self.request.GET.get('q')
        if query:
            reviews = self.model.objects.filter(
                Q(game_name__icontains=query) |
                Q(type_game__icontains=query) |
                Q(genre__icontains=query) |
                Q(developer__icontains=query)
            )
        else:
            reviews = self.model.objects.all()
        return reviews


class ReviewDetail(DetailView):
    """View a single review"""

    template_name = "reviews/review_detail.html"
    model = Review
    context_object_name = "review"


class InputReview(LoginRequiredMixin, CreateView):
    """Add review view with proper feedback"""
    template_name = 'reviews/input_review.html'
    model = Review
    form_class = ReviewForm
    success_url = reverse_lazy('reviews')

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(
            self.request, 
            'Your review has been created successfully!'
        )
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(
            self.request, 
            'There was an error creating your review. Please check the form.'
        )
        return super().form_invalid(form)


class EditReview(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """Edit a review"""
    template_name = 'reviews/edit_review.html'
    model = Review
    form_class = ReviewForm
    success_url = reverse_lazy('reviews')

    def form_valid(self, form):
        messages.success(self.request, 'Review updated successfully!')
        return super().form_valid(form)

    def test_func(self):
        return self.request.user == self.get_object().user


class DeleteReview(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """ Delete a review """
    model = Review
    template_name = 'reviews/review_confirm_delete.html'
    success_url = reverse_lazy('reviews')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Review deleted successfully!')
        return super().delete(request, *args, **kwargs)

    def test_func(self):
        return self.request.user == self.get_object().user
        