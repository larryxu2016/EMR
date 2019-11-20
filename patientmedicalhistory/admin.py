from django.contrib import admin
from .models import PatientMedHistory
from .models import MedHistoryInfo
# Register your models here.
admin.site.register(PatientMedHistory)
admin.site.register(MedHistoryInfo)