from django.shortcuts import render, redirect
from members.models import Member
import csv
from .models import GenerateReportForm
from django.db.models import Q


def reports(request):
    if request.method == 'POST':
        form = GenerateReportForm(request.POST)
        if form.is_valid():
            if request.POST.get('month') and request.POST.get('year') and request.POST.get('batch'):
                query = Q(
                    registration_date__month=request.POST.get('month'),
                    registration_date__year=request.POST.get('year'),
                    batch=request.POST.get('batch')
                )
            elif request.POST.get('month') and request.POST.get('year'):
                query = Q(
                    registration_date__month=request.POST.get('month'),
                    registration_date__year=request.POST.get('year')
                )
            elif request.POST.get('month') and request.POST.get('batch'):
                query = Q(
                    registration_date__month=request.POST.get('month'),
                    batch=request.POST.get('batch')
                )
            elif request.POST.get('year') and request.POST.get('batch'):
                query = Q(
                    registration_date__year=request.POST.get('year'),
                    batch=request.POST.get('batch')
                )
            else:
                query = Q(
                    registration_date__year=request.POST.get('year'),
                )
            users = Member.objects.filter(query)
            context = {
                'users': users,
                'form': form,
            }
            return render(request, 'reports/export.html', context)
    else:
        form = GenerateReportForm()
    return render(request, 'reports/export.html', {'form': form})
