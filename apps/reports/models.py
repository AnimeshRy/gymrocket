from django.db import models
from django.forms import ModelForm
from django.db import models
import datetime
import calendar

YEAR_CHOICES = []
for year in range(2020, (datetime.datetime.now().year + 5)):
    YEAR_CHOICES.append((year, year))

BATCH = (
    ('morning', 'Morning'),
    ('evening', 'Evening'),
    ('', 'All')
)

MONTHS_CHOICES = tuple(
    zip(range(1, 13), (calendar.month_name[i] for i in range(1, 13))))


class GenerateReports(models.Model):
    # Reports model to generate reports according to year, month and batch
    month = models.IntegerField(
        choices=MONTHS_CHOICES, default=datetime.datetime.now().year, blank=True)
    year = models.IntegerField(
        choices=YEAR_CHOICES, default=datetime.datetime.now().year)
    batch = models.CharField(
        max_length=30,
        choices=BATCH,
        default=BATCH[2][0],
        blank=True)


class GenerateReportForm(ModelForm):
    # Report Form
    class Meta:
        model = GenerateReports
        fields = '__all__'
