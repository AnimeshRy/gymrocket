from django.shortcuts import render
from django.urls.conf import path
from apps.members.models import Member
from apps.payments.models import Payments
from django.db.models import Sum, Avg
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

today = datetime.today()

month_dictionary = {
    -1: 'December',
    -2: 'November',
    -3: 'October',
    -4: 'September',
    -5: 'August',
    -6: 'July',
    -7: 'June',
    -8: 'May',
    -9: 'April',
    -10: 'March',
    -11: 'February',
    0: 'January',
    1: 'February',
    2: 'March',
    3: 'April',
    4: 'May',
    5: 'June',
    6: 'July',
    7: 'August',
    8: 'September',
    9: 'October',
    10: 'November',
    11: 'December'		}


@login_required
def dashboard(request):
    total_revenue_till_date = Payments.objects.aggregate(
        Sum('payment_amount')).get('payment_amount__sum')
    total_members = Member.objects.filter(stop=0).count()
    members_this_mon = Member.objects.filter(stop=0, registration_date__year=today.year,
                                             registration_date__month=today.month).count()
    pending_payment_members = Member.objects.filter(
        fee_status='pending').count()
    pending_payment_members_this_month = Member.objects.filter(stop=0,
                                                               fee_status='pending', registration_upto__year=today.year, registration_upto__month=today.month).count()
    avg_revenue = Payments.objects.aggregate(
        Avg('payment_amount')).get('payment_amount__avg')
    context = {
        "members_this_mon": members_this_mon,
        "total_members": total_members,
        "total_revenue_till_date": total_revenue_till_date,
        "pending_payment_members": pending_payment_members,
        "pending_payment_members_this_month": pending_payment_members_this_month,
        "avg_revenue": avg_revenue
    }
    return render(request, "dashboard/board.html", context=context)


@login_required
def member_chart(request):
    data = []
    labels = []
    recent_months = [today.month - 3, today.month - 2, today.month -
                     1, today.month]
    for months in recent_months:
        data.append(Member.objects.filter(stop=0, registration_date__year=today.year,
                                          registration_date__month=months).count())
        labels.append(month_dictionary[months])

    return JsonResponse(data={
        'labels': labels,
        'data': data,
    })


@login_required
def payment_chart(request):
    data = []
    labels = []
    recent_months = [today.month - 6, today.month - 5, today.month - 4, today.month - 3, today.month - 2, today.month -
                     1, today.month]
    for months in recent_months:
        data.append(Payments.objects.filter(payment_date__year=today.year, payment_date__month=months).aggregate(
            Avg('payment_amount')).get('payment_amount__avg', 0))
        labels.append(month_dictionary[months])
    return JsonResponse(data={
        'data': data,
        'labels': labels,
    })
