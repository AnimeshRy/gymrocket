from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Member
from django.contrib.auth.decorators import login_required


class LandingPage(TemplateView):
    template_name = "landing_page.html"


def view_members(request):
    data = Member.objects.filter(stop=0).order_by('first_name')
    return render(request, "members/view_members.html", {
        'data': data
    })
