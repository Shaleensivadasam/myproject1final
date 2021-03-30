from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from .models import charge_profile,media_type,media_provider,staff,login
import random
# Create your views here.



def adm_add_charge_profile(request):
    mediatype=media_type.objects.all()
    mediaprovider=media_provider.objects.all()

    return render(request,"admin/ADD CHARGE PROFILE.html",{'data1':mediatype,'data2':mediaprovider})

def adm_add_charge_profile_post(request):
    profile_name=request.POST['textfield']
    print(profile_name)
    type=request.POST['select']
    print(media_type)
    provider_name=request.POST['select2']
    print(provider_name)
    charge=request.POST['textfield2']
    print(charge)
    mediatype=media_type.objects.get(pk=type)
    print(media_type)
    mediaprovider=media_provider.objects.get(pk=provider_name)

    res=charge_profile(charge=charge,profilename=profile_name,MEDIATYPE=mediatype,MEDIAPROVIDER=mediaprovider)
    res.save()
    mediatype = media_type.objects.all()
    mediaprovider = media_provider.objects.all()
    return render(request,"admin/ADD CHARGE PROFILE.html",{'data1':mediatype,'data2':mediaprovider})

def adm_add_employee_area(request):
    return render(request,"admin/ADD EMPLOYEE AREA.html")

def adm_add_employee_area_post(request):
    area_name=request.POST['select']
    staff_name=request.POST['select2']
    return render(request,"admin/ADD EMPLOYEE AREA.html")

def adm_add_media_provider(request):
    mediatype = media_type.objects.all()
    return render(request,"admin/ADD MEDIA PROVIDER.html",{'data1':mediatype})

def adm_add_media_provider_post(request):
    if request.method=='POST':
        provider_name=request.POST['textfield']
        place=request.POST['textfield2']
        city=request.POST['textfield3']
        district=request.POST['select']
        pincode=request.POST['textfield4']
        emailid=request.POST['textfield5']
        phno=request.POST['textfield6']
        img=request.FILES['fileField']
        meditype=request.POST['select2']
        fs=FileSystemStorage()
        filename=fs.save(img.name,img)
        image=fs.url(filename)
        # mediatype = media_type.objects.get(pk=type)
        res=media_provider(provider_name=provider_name,place=place,city=city,district=district,pincode=pincode,image=image,phno=phno,email=emailid,MEDIATYPE_id=meditype)
        res.save()
    mediatype = media_type.objects.all()
    return render(request,"admin/ADD MEDIA PROVIDER.html",{'data1':mediatype})


def adm_media_type(request):
    mediatype = media_type.objects.all()
    return render(request, "admin/ADD MEDIA TYPE.html", {'data1': mediatype})

def adm_media_type_post(request):
    mediatype = media_type.objects.all()
    if request.method=='POST':
        type = request.POST['select']
        descrip = request.POST['textfield']
        # mediatype = media_type.objects.get(pk=type)
        # descr = descrip.objects.get(pk=descrip)
        res = media_type(media_type_name=type, description=descrip)
        res.save()
    return render(request, "admin/ADD MEDIA TYPE.html",{'data1': mediatype})
def adm_service_area(request):
    return render(request,"admin/ADD SERVICE AREA.html")

def adm_service_area_post(request):
    area_name=request.POST['textfield']
    locality=request.POST['textfield2']
    district=request.POST['select']
    return render(request,"admin/ADD SERVICE AREA.html")

def adm_add_staff(request):
    return render(request,"admin/ADD STAFF.html")

def adm_add_staff_post(request):
    name = request.POST['textfield']
    gender = request.POST['radio']
    dob = request.POST['select']
    hno_name = request.POST['textfield2']
    district = request.POST['select2']
    pincode = request.POST['textfield3']
    email_id = request.POST['textfield34']
    pno = request.POST['textfield5']
    img = request.POST['fileField']
    fs = FileSystemStorage()
    filename = fs.save(img.name, img)
    image = fs.url(filename)
    staff_type = request.POST['select3']
    psw=random.randint(0000,9999)
    res1=login(username=email_id,password=psw,utype=staff_type)
    res1.save()
    res=staff(name=name,gender=gender,dob=dob,houseno_name=hno_name,district=district,pincode=pincode,email=email_id,phno=pno,image=image)
    res.save()
    return render(request,"admin/ADD STAFF.html")

def adm_sent_reply_to_complaint(request):
    return render(request,"admin/ADMIN SENT REPLY TO COMPLAINT.html")

def adm_sent_reply_to_complaint_post(request):
    reply=request.POST['textarea']
    return render(request,"admin/ADMIN SENT REPLY TO COMPLAINT.html")

def adm_view_complaint(request):
    return render(request,"admin/ADMIN VIEW COMPLAINT.html")

def adm_view_expense_mngt(request):
    return render(request,"admin/ADMIN VIEW EXPENSE MNGT.html")

def adm_view_installation(request):
    return render(request,"admin/ADMIN VIEW INSTALLATION.html")

def adm_view_maintance(request):
    return render(request,"admin/ADMIN VIEW MAINTANCE.html")

def adm_view_new_request_more(request):
    return render(request,"admin/ADMIN VIEW NEW REQUEST MORE.html")

def adm_view_new_request(request):
    return render(request,"admin/ADMIN VIEW NEW REQUEST.html")

def adm_view_registered_user(request):
    return render(request,"admin/ADMIN VIEW REGISTERED USER.html")

def adm_view_rejected_request_more(request):
    return render(request,"admin/ADMIN VIEW REJECTED REQUEST MORE.html")

def adm_view_rejected_request(request):
    return render(request,"admin/ADMIN VIEW REJECTED REQUEST.html")

def adm_allocate_to_designer(request):
    return render(request,"admin/ALLOCATE TO DESIGNER.html")

def adm_edit_charge_profile(request):
    return render(request,"admin/EDIT CHARGE PROFILE.html")

def adm_edit_charge_profile_post(request):
    profile_name=request.POST['textfield']
    media_type=request.POST['select']
    provider_name=request.POST['select2']
    charge=request.POST['textfield2']
    return render(request,"admin/EDIT CHARGE PROFILE.html")

def adm_edit_charge_profile_post(request):
    return render(request,"admin/EDIT CHARGE PROFILE.html")

def adm_edit_media_type(request):
    return render(request,"admin/EDIT MEDIA TYPE.html"),

def adm_edit_media_type_post(request):
    media_type = request.POST['select']
    description = request.POST['textfield']
    return render(request,"admin/EDIT MEDIA TYPE.html"),

def adm_edit_employee_area(request):
    return render(request,"admin/EDIT EMPLOYEE AREA.html")

def adm_edit_employee_area_post(request):
    staff_name = request.POST['select2']
    staff_name = request.POST['select2']
    return render(request,"admin/EDIT EMPLOYEE AREA.html")

def adm_edit_media_provider(request):
    return render(request,"admin/EDIT MEDIA PROVIDER.html")

def adm_edit_media_provider_post(request):
    provider_name = request.POST['textfield']
    place = request.POST['textfield2']
    city = request.POST['textfield3']
    district = request.POST['select']
    pincode = request.POST['textfield4']
    emailid = request.POST['textfield5']
    phno = request.POST['textfield6']
    img = request.POST['fileField']
    media_type = request.POST['select2']
    return render(request,"admin/EDIT MEDIA PROVIDER.html")

def adm_edit_service_area(request):
    return render(request,"admin/EDIT SERVICE AREA.html")

def adm_edit_service_area_post(request):
    area_name = request.POST['textfield']
    locality = request.POST['textfield2']
    district = request.POST['select']
    return render(request,"admin/EDIT SERVICE AREA.html")

def adm_edit_staff(request):
    return render(request,"admin/EDIT STAFF.html")

def adm_edit_staff_post(request):
    name = request.POST['textfield']
    gender = request.POST['radio']
    dob = request.POST['select']
    hno_name = request.POST['textfield2']
    district = request.POST['select2']
    pincode = request.POST['textfield3']
    email_id = request.POST['textfield34']
    pno = request.POST['textfield5']
    img = request.POST['fileField']
    staff_type = request.POST['select3']
    return render(request,"admin/EDIT STAFF.html")

def adm_login(request):
    return render(request,"admin/login.html")

def adm_monthly_settlement_entry(request):
    return render(request,"admin/MONTHY SETTLEMENT ENTRY.html")

def adm_monthly_settlement_entry_post(request):
    provider_name=request.POST['select']
    year=request.POST['textfield']
    month=request.POST['select2']
    amount=request.POST['textfield2']
    return render(request,"admin/MONTHY SETTLEMENT ENTRY.html")

def adm_view_advertisement_request_approve(request):
    return render(request,"admin/VIEW ADVERTISEMENT REQUEST APPROVE.html")

def adm_view_advertisement_request_approved_more(request):
    return render(request,"admin/VIEW ADVERTISEMENT REQUEST APPROVED MORE.html")

def adm_view_charge_profile(request):
    return render(request,"admin/VIEW CHARGE PROFILE.html")

def adm_view_employee_area(request):
    return render(request,"admin/VIEW EMPLOYEE AREA.html")

def adm_view_feedback_reviews(request):
    return render(request,"admin/VIEW FEEDBACK REVIEWS.html")

def adm_view_media_provider(request):
    return render(request,"admin/VIEW MEDIA PROVIDER.html")

def adm_view_media_type(request):
    return render(request,"admin/VIEW MEDIA TYPE.html")

def adm_view_monthy_settlement_entry(request):
    return render(request,"admin/VIEW MONTHLY SETTLEMENT ENTRY.html")

def adm_view_registered_user_more(request):
    return render(request,"admin/VIEW REGISTERED USER.html")

def adm_request_from_public_for_media_provider(request):
    return render(request,"admin/VIEW REQUEST FROM PUBLIC FOR MEDIA PROVIDER.html")

def adm_request_from_public(request):
    return render(request,"admin/VIEW REQUEST FROM PUBLIC.html")

def adm_view_service_area(request):
    return render(request,"admin/VIEW SERVICE AREA.html")

def adm_view_staff(request):
    return render(request,"admin/VIEW STAFF.html")


def adm_homepage(request):
    return render(request, "admin/adm_homepage.html")

def dsgnr_edit_create_media(request):
    return render(request, "templates/designer/DESIGNER EDIT CREATE MEDIA.html")

def dsgnr_edit_create_media_post(request):
    media_title=request.POST['textfield']
    filename=request.POST['textfield2']
    description=request.POST['textfield3']
    date=request.POST['select']
    path=request.POST['textfield4']
    return render(request, "templates/designer/DESIGNER EDIT CREATE MEDIA.html")

def dsgnr_edit_profile(request):
    return render(request, "templates/designer/DESIGNER EDIT PROFILE.html")

def dsgnr_edit_profile_post(request):
    name = request.POST['textfield']
    gender = request.POST['radio']
    dob = request.POST['select']
    hno_name = request.POST['textfield2']
    district = request.POST['select2']
    pincode = request.POST['textfield3']
    email_id = request.POST['textfield34']
    pno = request.POST['textfield5']
    img = request.POST['fileField']
    return render(request, "templates/designer/DESIGNER EDIT PROFILE.html")


def dsgnr_upload_created_media(request):
    return render(request, "templates/designer/DESIGNER UPLOAD CREATED MEDIA.html")

def dsgnr_view_media_uploaded(request):
    return render(request, "templates/designer/DESIGNER VIEW MEDIA UPLOADED.html")

def dsgnr_view_profile(request):
    return render(request, "templates/designer/DESIGNER VIEW PROFILE.html")

def dsgnr_view_request_assigned(request):
    return render(request, "templates/designer/DESIGNER VIEW REQUEST ASSIGNED.html")

def public_to_admin(request):
    return render(request, "templates/public/PUBLIC SENT REQUEST TO ADMIN BEING MEDIA PROVIDER.html")

def public_view_charge_profile(request):
    return render(request, "templates/public/PUBLIC VIEW CHARGE PROFILE.html")

def public_view_media_provider(request):
    return render(request, "templates/public/PUBLIC VIEW MEDIA PROVIDER.html")

def public_view_media_types(request):
    return render(request, "templates/public/PUBLIC VIEW MEDIA TYPES.html")

def semp_view_maintance(request):
    return render(request, "templates/service employee/SERIVCE EMPLOYEE VIEW MAINTANCE ENTRY.html")

def semp_edit_profile(request):
    return render(request, "templates/service employee/SERVICE EMPLOYEE EDIT PROFILE.html")

def semp_expense_mngt(request):
    return render(request, "templates/service employee/SERVICE EMPLOYEE EXPENSE MNGT.html")

def semp_installation(request):
    return render(request, "templates/service employee/SERVICE EMPLOYEE INSTALLATION.html")

def semp_maintance(request):
    return render(request, "templates/service employee/SERVICE EMPLOYEE MAINTANCE ENTRY.html")

def semp_view_expense(request):
    return render(request, "templates/service employee/SERVICE EMPLOYEE VIEW EXPENSE.html")

def semp_view_installation(request):
    return render(request, "templates/service employee/SERVICE EMPLOYEE VIEW INSTALLATION.html")

def semp_view_profile(request):
    return render(request, "templates/service employee/SERVICE EMPLOYEE VIEW PROFILE.html")

def semp_view_service_area(request):
    return render(request, "templates/service employee/SERVICE EMPLOYEE VIEW SERVICE AREA.html")
