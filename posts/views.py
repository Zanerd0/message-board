from django.views.generic import ListView
from .models import Post


class HomePageView(ListView):
    model = Post
    template_name = "home.html"

    # CODIUM ADDED CODE BELOW:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["posts_list"] = (
            self.get_queryset()
        )  # Assuming you want to display all posts
        return context


# Create your views here.
