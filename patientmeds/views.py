from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import render

from simple_rest import Resource

from .models import PatientMeds

def index(request):
    if request.session.get('member_id'):
        return render(request, "patientmeds/index.html")
    else:
        return render(request, "login/index.html")


class Meds(Resource):

    def get(self, request):
        if request.session.get('member_id'):
            meds = PatientMeds.objects.all() \
                .filter(user_name__exact = request.session.get('member_id'));       
            return HttpResponse(self.to_json(meds), content_type = "application/json", status = 200)
        else:
            return render(request, "login/index.html")

    def post(self, request):
        if request.session.get('member_id'):
            meds = PatientMeds(
                user_name = request.session.get('member_id'),
                meds_name = request.POST.get("meds_name"),
                meds_strength = request.POST.get("meds_strength"),
                meds_dir = request.POST.get("meds_dir"),
                meds_status = request.POST.get("meds_status"),
                meds_date = request.POST.get("meds_date")
            )
            meds.save()
            meds = PatientMeds.objects.all() \
                .filter(meds_name__contains = request.POST.get("meds_name")); 
            return HttpResponse(self.to_json(meds), content_type = "application/json", status = 201)
        else:
            return render(request, "login/index.html")

    def put(self, request, patientmeds_id):
        if request.session.get('member_id'):
            meds = PatientMeds.objects.get(pk = patientmeds_id, user_name=request.session.get('member_id'))  
            meds.meds_name = request.PUT.get("meds_name")
            meds.meds_strength = request.PUT.get("meds_strength")
            meds.meds_dir = request.PUT.get("meds_dir")
            meds.meds_status = request.PUT.get("meds_status")
            meds.meds_date = request.PUT.get("meds_date")
            meds.save()
            return HttpResponse(status = 200)
        else:
            return render(request, "login/index.html")

    def delete(self, request, patientmeds_id):
        meds = PatientMeds.objects.get(pk = patientmeds_id)
        meds.delete()
        return HttpResponse(status = 200)

    def to_json(self, objects):
        return serializers.serialize("json", objects)