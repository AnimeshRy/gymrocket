from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from .models import Member
from django.contrib.auth.decorators import login_required
from .forms import AddMemberForm
from django.contrib.auth.mixins import LoginRequiredMixin
import dateutil.relativedelta as delta
import dateutil.parser as parser
from django.urls import reverse
from wallpaper.models import Wallpaper


class LandingPage(TemplateView):
    template_name = "landing_page.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        if Wallpaper.objects.filter()[:1].exists():
            wallpaper = Wallpaper.objects.filter()[:1].get()
            context.update({
                'wallpaper': wallpaper
            })

        return context


def view_members(request):
    data = Member.objects.filter(stop=0).order_by('first_name')
    return render(request, "members/view_members.html", {
        'data': data
    })


class AddMemberView(LoginRequiredMixin, CreateView):
    template_name = 'members/add_member.html'
    form_class = AddMemberForm

    def get_success_url(self) -> str:
        return reverse("members:member-list")

    def form_valid(self, form):
        form.instance.registration_upto = parser.parse(form.cleaned_data['registration_date']) + delta.relativedelta(
            months=int(form.cleaned_data['subscription_period']))
        return super().form_valid(form)
