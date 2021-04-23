from django.db import models
from datetime import date


SUBSCRIPTION_TYPE_CHOICES = (
    ('gym', 'Gym'),
    ('cross_fit', 'Cross Fit'),
    ('gym_and_cross_fit', 'Gym + Cross Fit'),
    ('pt', 'Personal Training')
)

SUBSCRIPTION_PERIOD_CHOICES = (
    ('1', '1 Month'),
    ('2', '2 Months'),
    ('3', '3 Months'),
    ('4', '4 Months'),
    ('5', '5 Months'),
    ('6', '6 Months'),
    ('7', '7 Months'),
    ('8', '8 Months'),
    ('9', '9 Months'),
    ('10', '10 Months'),
    ('11', '11 Months'),
    ('12', '12 Months'),
)

FEE_STATUS = (
    ('paid', 'Paid'),
    ('pending', 'Pending'),
)

STATUS = (
    (0, 'Start'),
    (1, 'Stop'),
)

BATCH = (
    ('morning', 'Morning'),
    ('evening', 'Evening'),
)

GENDER = (
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Other', 'Other')
)


class Member(models.Model):
    """ Initial Member Model """
    member_id = models.AutoField(primary_key=True)
    first_name = models.CharField(('First Name'), max_length=50)
    last_name = models.CharField(('Last Name'), max_length=50)
    gender = models.CharField(
        ('Gender'), choices=GENDER, max_length=7)
    mobile_number = models.CharField(
        ('Mobile Number'), max_length=10, unique=True)
    email = models.EmailField(null=True, blank=True)
    address = models.CharField(max_length=300, blank=True)
    medical_history = models.CharField(
        ('Medical History'), max_length=300, blank=True, default='None')
    admitted_on = models.DateField(auto_now_add=True)
    registration_date = models.DateField(
        ('Registration Date'))
    registration_upto = models.DateField()
    dob = models.DateField()
    subscription_type = models.CharField(
        ('Subscription Type'),
        max_length=30,
        choices=SUBSCRIPTION_TYPE_CHOICES,
        default=SUBSCRIPTION_TYPE_CHOICES[0][0]
    )
    subscription_period = models.CharField(
        ('Subscription Period'),
        max_length=30,
        choices=SUBSCRIPTION_PERIOD_CHOICES,
        default=SUBSCRIPTION_PERIOD_CHOICES[0][0]
    )
    amount = models.CharField(max_length=30)
    fee_status = models.CharField(
        ('Fee Status'),
        max_length=30,
        choices=FEE_STATUS,
        default=FEE_STATUS[0][0]
    )
    batch = models.CharField(
        max_length=30,
        choices=BATCH,
        default=BATCH[0][0]
    )
    photo = models.FileField(upload_to='photos/', blank=True)
    stop = models.IntegerField(
        ('Status'), choices=STATUS, default=STATUS[0][0], blank=True)

    def calculate_age(self):
        today = date.today()
        return today.year - self.dob.year - ((today.month, today.day) < (self.dob.month, self.dob.day))

    @property
    def get_month(self):
        return int(self.registration_date.strftime("%m"))

    def __str__(self):
        return self.first_name + ' ' + self.last_name
