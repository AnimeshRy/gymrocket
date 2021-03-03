from django.http.response import HttpResponse
from django.shortcuts import render


def test_page(request):
    return render(request, "members/view_member.html")
