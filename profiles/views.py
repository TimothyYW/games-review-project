from django.view.generic import TemplateView

from .models import Profile


class Profiles(TemplateView):
    """User Profile View"""

    template_name = "profiles/profile.html"

    def get_context_data(self, **kwargs):
        profile = Profile.objects.get(user=self.kwargs["pk"])
        context = {"profile": profile}

        return context


# Create your views here.
