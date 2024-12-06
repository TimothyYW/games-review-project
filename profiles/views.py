from django.views.generic import TemplateView, UpdateView
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.contrib import messages
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from django.http import Http404
from django.core.paginator import Paginator

from .models import Profile
from .forms import ProfileForm

class Profiles(TemplateView):
    """Display user profile"""
    template_name = "profiles/profile.html"

    def get_context_data(self, **kwargs):
        try:
            profile = get_object_or_404(Profile, user=self.kwargs["pk"])
            # Paginate reviews
            reviews = profile.user.review_owner.all().order_by('-posted_date')
            paginator = Paginator(reviews, 5)  # Show 5 reviews per page
            page = self.request.GET.get('page')
            reviews_page = paginator.get_page(page)

            context = {
                'profile': profile,
                'reviews': reviews_page,
                'form': ProfileForm(instance=profile) if self.request.user == profile.user else None,
            }
            return context
        except Http404:
            messages.error(self.request, "Profile not found.")
            return redirect('home')

class EditProfile(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """Edit a profile"""
    form_class = ProfileForm
    model = Profile
    template_name = 'profiles/profile.html'

    def get_success_url(self):
        return reverse_lazy('profile', kwargs={'pk': self.object.user.id})

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Profile updated successfully!')
        return response

    def form_invalid(self, form):
        messages.error(
            self.request, 
            'Error updating profile. Please check the form and try again.'
        )
        return super().form_invalid(form)

    def test_func(self):
        profile = self.get_object()
        return self.request.user == profile.user

    def handle_no_permission(self):
        messages.error(self.request, "You don't have permission to edit this profile.")
        return redirect('profile', pk=self.kwargs['pk'])