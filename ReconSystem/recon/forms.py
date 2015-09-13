from django import forms
from django.forms.extras.widgets import SelectDateWidget
from django.contrib.admin.widgets import AdminDateWidget

class PeriodForm(forms.Form):
    YEAR_CHOICES=('2010','2011','2012','2013','2014',
                  '2015','2016','2017','2018','2019',
                  '2020','2021','2022','2023','2024',
                  '2025','2026','2027','2028','2029',
                  '2030','2031','2032','2033','2034')
    start_date=forms.DateField(widget=SelectDateWidget(years=YEAR_CHOICES))
    end_date=forms.DateField(widget=SelectDateWidget(years=YEAR_CHOICES))