from django.shortcuts import render
from django.views import generic
from .models import PatientContact
 
class IndexView(generic.TemplateView):
    template_name = 'patientcontact/index.html'
    
def saveContactInfo(request):
    pc = PatientContact(
        user_name = request.session.get('member_id'),
        first_name = request.POST['contFirstName'],
        middle_name = request.POST['contMiddleName'],
        last_name = request.POST['contLastName'],
        address = request.POST['contAddress'],
        city = request.POST['contCity'],
        state = request.POST['contState'],
        zipCode = request.POST['contZip'],   
        homePhone = request.POST['contPhoneMain'],
        cellPhone = request.POST['contPhoneCell'],
        email = request.POST['contEmail'])
    pc.save()
    return render(request, 'patientinsurance/index.html')

class ModifyView(generic.TemplateView):
    template_name = 'patientcontact/modify.html'
    
def readData(request):
    if request.session.get('member_id'):
        contact = PatientContact.objects \
            .filter(user_name__exact = request.session.get('member_id')).values();
        return render(request, "patientcontact/modify.html", {"contact_list": contact,})
    return render(request, "login/index.html")

def updateContactInfo(request):
    if request.session.get('member_id'):
        pc = PatientContact.objects.get(user_name=request.session.get('member_id')) 
        pc.user_name = request.session.get('member_id')
        pc.first_name = request.POST['contFirstName']
        pc.middle_name = request.POST['contMiddleName']
        pc.last_name = request.POST['contLastName']
        pc.address = request.POST['contAddress']
        pc.city = request.POST['contCity']
        pc.state = request.POST['contState']
        pc.zipCode = request.POST['contZip']
        pc.homePhone = request.POST['contPhoneMain']
        pc.cellPhone = request.POST['contPhoneCell']
        pc.email = request.POST['contEmail']
        pc.save()
        return render(request, 'dashboard/index.html')
    else:
        return render(request, 'login/index.html')