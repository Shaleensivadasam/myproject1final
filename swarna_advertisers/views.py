from django.core.files.storage import FileSystemStorage
from django.shortcuts import render,redirect,HttpResponse
from .models import charge_profile,media_type,media_provider,staff,login,service_area,employee_area,monthly_settlement,installation,maintance,expense
import random
import datetime
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
    area_name = service_area.objects.all()
    name = staff.objects.all()

    return render(request,"admin/ADD EMPLOYEE AREA.html",{'data1':area_name,'data2':name})

def adm_add_employee_area_post(request):
    area_name = request.POST['select']
    staff_name = request.POST['select2']
    aname= service_area.objects.all()
    sname = staff.objects.all()
    res=employee_area(SERVICEAREA_id=area_name,STAFF_id=staff_name)
    res.save()
    return render(request,"admin/ADD EMPLOYEE AREA.html",{'data1':aname,'data2':sname})

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
        type = request.POST['textfield']
        descrip = request.POST['textarea']
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
    res=service_area(area_name=area_name, area_locality=locality, area_district=district)
    res.save()
    return render(request,"admin/ADD SERVICE AREA.html")

def adm_add_staff(request):
    return render(request,"admin/ADD STAFF.html")

def adm_add_staff_post(request):
    print("jjj")
    name = request.POST['textfield']
    gender = request.POST['radio']
    dob = request.POST['date']
    hno_name = request.POST['textfield2']
    district = request.POST['select2']
    pincode = request.POST['textfield3']
    email_id = request.POST['textfield4']
    pno = request.POST['textfield5']
    img = request.FILES['fileField']
    print("kkk")
    fs = FileSystemStorage()
    filename = fs.save(img.name, img)
    image = fs.url(filename)
    staff_type = request.POST['select3']
    psw=random.randint(0000,9999)
    print("ppp")
    res1=login(username=email_id,password=psw,utype=staff_type)

    res1.save()
    print("lll")
    print("res1=",res1)
    # login_id=login.objects.get(id=res1.id)
    print("yyy")
    res=staff(name=name,gender=gender,dob=dob,houseno_name=hno_name,district=district,pincode=pincode,email=email_id,phno=pno,image=image,LOGIN_id=res1.id)
    res.save()
    print("hhh")
    return render(request,"admin/ADD STAFF.html")

def adm_sent_reply_to_complaint(request):
    return render(request,"admin/ADMIN SENT REPLY TO COMPLAINT.html")

def adm_sent_reply_to_complaint_post(request):
    reply=request.POST['textarea']
    return render(request,"admin/ADMIN SENT REPLY TO COMPLAINT.html")

def adm_view_complaint(request):
    return render(request,"admin/ADMIN VIEW COMPLAINT.html")

def adm_view_expense_mngt(request):
    res = expense.objects.all()
    return render(request,"admin/ADMIN VIEW EXPENSE MNGT.html",{'res':res})

def adm_view_expense_mngt_post(request):
    date1 = request.POST['fdate']
    date2 = request.POST['tdate']
    # stf = staff.objects.get(LOGIN=request.session['LOGIN_id'])
    # area_name = employee_area.objects.filter(STAFF=stf)
    res = expense.objects.filter(date__range=(date1, date2))
    print(res)
    return render(request,"admin/ADMIN VIEW EXPENSE MNGT.html",{'res':res})

def adm_view_installation(request):
    res=installation.objects.all()
    res1=service_area.objects.all()
    print(res1)
    return render(request,"admin/ADMIN VIEW INSTALLATION.html",{'res':res,'res1':res1})

def adm_view_installation_post(request):
    btn = request.POST['button']
    if btn == "SEARCH":
        stf = staff.objects.get(LOGIN=request.session['LOGIN_id'])
        area_name = employee_area.objects.filter(STAFF=stf)
        area = request.POST['select']
        aname = service_area.objects.get(pk=area)
        print(aname)
        res = installation.objects.filter(SERVICEAREA_id=aname)
        print(res)
        res1 = service_area.objects.all()
        return render(request,"admin/ADMIN VIEW INSTALLATION.html",{'res':res,'res1':area_name,'res1':res1})

    if btn=="GO":
        date1=request.POST['fdate']
        date2=request.POST['tdate']
        stf = staff.objects.get(LOGIN=request.session['LOGIN_id'])
        area_name = employee_area.objects.filter(STAFF=stf)
        res = installation.objects.filter(date__range=(date1, date2))
        print(res)
    return render(request, "admin/ADMIN VIEW INSTALLATION.html",{'res':res,'res1':area_name})

def adm_view_maintance(request):
    res = maintance.objects.all()
    res1 = service_area.objects.all()
    print(res1)
    return render(request,"admin/ADMIN VIEW MAINTANCE.html",{'res':res})

def adm_view_maintance_post(request):
    btn = request.POST['button']
    if btn == "SEARCH":
        stf = staff.objects.get(LOGIN=request.session['LOGIN_id'])
        area_name = employee_area.objects.filter(STAFF=stf)
        area = request.POST['select']
        aname = service_area.objects.get(pk=area)
        print(aname)
        res = maintance.objects.filter(SERVICEAREA_id=aname)
        return render(request, "admin/ADMIN VIEW MAINTANCE.html",{'res': res, 'res1': area_name})

    if btn == "GO":
        date1 = request.POST['fdate']
        date2 = request.POST['tdate']
        stf = staff.objects.get(LOGIN=request.session['LOGIN_id'])
        area_name = employee_area.objects.filter(STAFF=stf)
        placename = installation.objects.filter(STAFF=stf)
        code = installation.objects.filter(STAFF=stf)
        res = maintance.objects.filter(date__range=(date1, date2))
        print(res)
        return render(request,"admin/ADMIN VIEW MAINTANCE.html",{'res': res, 'res1': area_name, 'res1': placename, 'res1': code})
    return render(request,"admin/ADMIN VIEW INSTALLATION.html")

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

def adm_edit_media_type(request,pk):
    request.session['id'] = pk
    res = media_type.objects.get(id=pk)
    return render(request,"admin/EDIT MEDIA TYPE.html",{'res':res})

def adm_edit_media_type_post(request):
    id = request.session['id']
    mediatype = request.POST['textfield']
    description = request.POST['textarea']
    if request.method=='POST':
        res = media_type.objects.get(id=id)
        res.media_type_name=mediatype
        res.description=description
        res.save()
    return adm_view_media_type(request)

def adm_edit_employee_area(request,pk):
    area_name = service_area.objects.all()
    name = staff.objects.all()
    request.session['id'] = pk
    res = employee_area.objects.get(id=pk)
    return render(request,"admin/EDIT EMPLOYEE AREA.html",{'area_name':area_name,'STAFF':name,'res':res})

def adm_edit_employee_area_post(request):
    id = request.session['id']
    area_id = request.POST['select']
    staff_id = request.POST['select2']
    if request.method=='POST':
        res = employee_area.objects.get(id=id)
        res.SERVICEAREA_id=area_id
        res.STAFF_id=staff_id
        res.save()
    return adm_view_employee_area(request)

def adm_edit_media_provider(request,pk):
    request.session['id'] = pk
    res = media_provider.objects.get(id=pk)
    return render(request,"admin/EDIT MEDIA PROVIDER.html",{'res':res})

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

    if request.method=='POST':
        res = media_provider.objects.get(id=id)
        res.provider_name=provider_name
        res.place=place
        res.city=city
        res.district=district
        res.pincode=pincode
        res.email=emailid
        res.phno=phno
        res.image=img
        res.MEDIATYPE_id=media_type
        res.save()
    return adm_view_media_provider(request)

def adm_edit_service_area(request,pk):
    request.session['id']=pk
    res=service_area.objects.get(id=pk)
    return render(request,"admin/EDIT SERVICE AREA.html",{'res':res})

def adm_edit_service_area_post(request):
    id = request.session['id']
    area_name = request.POST['textfield']
    locality = request.POST['textfield2']
    district = request.POST['select']

    if request.method=='POST':
        res=service_area.objects.get(id=id)
        res.area_name=area_name
        res.area_locality=locality
        res.area_district=district
        res.save()
    return adm_view_service_area(request)

def adm_edit_staff(request,pk):
    request.session['id']=pk
    res=staff.objects.get(id=pk)
    return render(request,"admin/EDIT STAFF.html",{'res':res})

def adm_edit_staff_post(request):
    id=request.session['id']
    name = request.POST['textfield']
    gender = request.POST['radio']
    dob = request.POST['date']
    hno_name = request.POST['textfield2']
    district = request.POST['select2']
    pincode = request.POST['textfield3']
    email_id = request.POST['textfield4']
    pno = request.POST['textfield5']
    staff_type = request.POST['select3']
    print("qwerty")
    res = staff.objects.get(id=id)
    if 'fileField' in request.FILES:
        img = request.FILES['fileField']
        if img.name=='':
            pass
        else:
            fs = FileSystemStorage()
            filename = fs.save(img.name, img)
            image = fs.url(filename)
            res.image = image
    if request.method=='POST':

        res.name=name
        res.gender=gender
        res.dob=dob
        res.hno_name=hno_name
        res.district=district
        res.pincode=pincode
        res.email=email_id
        res.phno=pno
        res.staff_type=staff_type

        res.save()
    return adm_view_staff(request)

def adm_login(request):
    return render(request,"admin/login.html")


def adm_login_post(request):
    if request.method=="POST":
        print("jjj")
        uname = request.POST['textfield']
        pword = request.POST['textfield2']

        if login.objects.filter(username=uname,password=pword).exists():
            yy=login.objects.get(username=uname,password=pword)
            request.session['LOGIN_id']=yy.id
            print("lid=",yy.id)

            if yy.utype=="Service employee":
                print("ppp")
                return render(request,"service employee/semp_homepage.html")
            elif yy.utype=="admin":
                return redirect("/myapp/adm_homepage/")
            else:
                return redirect("/myapp/dsgnr_homepage/")
    return render(request,"admin/login.html")

def adm_monthly_settlement_entry(request):
    pname=media_provider.objects.all()
    return render(request,"admin/MONTHY SETTLEMENT ENTRY.html",{'data1':pname})

def adm_monthly_settlement_entry_post(request):
    print("jjj")
    provider_name=request.POST['select']
    year=request.POST['textfield']
    month=request.POST['textfield3']
    amount=request.POST['textfield2']
    print("jj22")
    date=datetime.datetime.now().date()
    print("hhh")
    qq=media_provider.objects.get(id=provider_name)
    # pname=provider_name.objects.get(pk=provider_name)
    res=monthly_settlement(MEDIAPROVIDER=qq,year=year,month=month,amount=amount,date=date)
    res.save()
    print("ppp")
    pname=media_provider.objects.all()
    print("uuu")
    return render(request,"admin/MONTHY SETTLEMENT ENTRY.html",{'data1':pname})

def adm_view_advertisement_request_approve(request):
    return render(request,"admin/VIEW ADVERTISEMENT REQUEST APPROVE.html")

def adm_view_advertisement_request_approved_more(request):
    return render(request,"admin/VIEW ADVERTISEMENT REQUEST APPROVED MORE.html")

def adm_view_charge_profile(request):
    return render(request,"admin/VIEW CHARGE PROFILE.html")

def adm_view_employee_area(request):
    res=employee_area.objects.all()
    print(res)
    return render(request,"admin/VIEW EMPLOYEE AREA.html",{'res':res})

def adm_view_employee_area_post(request):
    area = request.POST['textfield']
    print(area)
    area1=service_area.objects.get(area_name=area)
    res = employee_area.objects.filter(SERVICEAREA=area1)
    return render(request, "admin/VIEW EMPLOYEE AREA.html", {'res': res})


def adm_view_employee_area_del(request,pk):
    res=employee_area.objects.get(id=pk)
    res.delete()
    return adm_view_employee_area(request)



def adm_view_feedback_reviews(request):
    return render(request,"admin/VIEW FEEDBACK REVIEWS.html")

def adm_view_media_provider(request):
    res = media_provider.objects.all()
    return render(request,"admin/VIEW MEDIA PROVIDER.html",{'res':res})

def adm_view_media_provider_del(request,pk):
    res = media_provider.objects.get(id=pk)
    res.delete()
    return render(request, "admin/admin_index.html")


def adm_view_media_provider_post(request):
    pname = request.POST['textfield']
    print(pname)
    res = media_provider.objects.filter(provider_name=pname)
    print(res)
    return render(request,"admin/VIEW MEDIA PROVIDER.html",{'res':res})

def adm_view_media_type(request):
    res=media_type.objects.all()
    return render(request,"admin/VIEW MEDIA TYPE.html",{'res':res})

def adm_view_media_type_del(request,pk):
    res = media_type.objects.get(id=pk)
    res.delete()
    return adm_view_media_type(request)

def adm_view_media_type_post(request):
    mtype = request.POST['textfield']
    print(mtype)
    res = media_type.objects.filter(media_type_name=mtype)
    print(res)
    return render(request,"admin/VIEW MEDIA TYPE.html",{'res':res})

def adm_view_monthy_settlement_entry(request):
    res=monthly_settlement.objects.all()
    return render(request,"admin/VIEW MONTHLY SETTLEMENT ENTRY.html",{'res':res})

def adm_view_registered_user_more(request):
    return render(request,"admin/VIEW REGISTERED USER.html")

def adm_request_from_public_for_media_provider(request):
    return render(request,"admin/VIEW REQUEST FROM PUBLIC FOR MEDIA PROVIDER.html")

def adm_request_from_public(request):
    return render(request,"admin/VIEW REQUEST FROM PUBLIC.html")

def adm_view_service_area(request):
    res=service_area.objects.all()
    print(res)
    return render(request,"admin/VIEW SERVICE AREA.html",{'res':res})


def adm_view_service_area_post(request):
    area=request.POST['textfield']
    res1=service_area.objects.filter(area_name__contains=area)
    return render(request, "admin/VIEW SERVICE AREA.html", {'res': res1})


def adm_view_service_area_del(request,pk):
    res=service_area.objects.get(id=pk)
    res.delete()
    return adm_view_service_area(request)

def adm_view_staff(request):
    res=staff.objects.all()
    # print(res.LOGIN.utype)
    return render(request,"admin/VIEW STAFF.html",{'res1':res})

def adm_view_staff_del(request,pk):

    res=staff.objects.get(id=pk)
    res.delete()
    # print(res.LOGIN.utype)
    return adm_view_staff(request)

def adm_view_staff_post(request):
    btn=request.POST['button']
    if btn=="SEARCH":
        stafftype = request.POST['select']
        res = staff.objects.all()
        res1 = staff.objects.filter(LOGIN_id__utype=stafftype)
        return render(request, "admin/VIEW STAFF.html", {'res': res, 'res1': res1})
    if btn=="GO":
        empname = request.POST['textfield']
        res = staff.objects.all()
        res1 = staff.objects.filter(name=empname)
        return render(request, "admin/VIEW STAFF.html", {'res': res, 'res1': res1})


def adm_view_rejected_request(request):
    return render(request,"admin/ADMIN VIEW REJECTED REQUEST.html")

def adm_homepage(request):
    return render(request, "admin/adm_homepage.html")

def designer_index(request):
    return render(request, "designer/designer_index.html")

def dsgnr_homepage(request):
    return render(request, "designer/dsg_homepage.html")

def dsgnr_edit_create_media(request):
    return render(request, "designer/DESIGNER EDIT CREATE MEDIA.html")

def dsgnr_edit_create_media_post(request):
    media_title=request.POST['textfield']
    filename=request.POST['textfield2']
    description=request.POST['textfield3']
    date=request.POST['select']
    path=request.POST['textfield4']
    return render(request, "designer/DESIGNER EDIT CREATE MEDIA.html")

def dsgnr_edit_profile(request):
    return render(request, "designer/DESIGNER EDIT PROFILE.html")

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
    return render(request, "designer/DESIGNER EDIT PROFILE.html")


def dsgnr_upload_created_media(request):
    return render(request, "designer/DESIGNER UPLOAD CREATED MEDIA.html")

def dsgnr_view_media_uploaded(request):
    return render(request, "designer/DESIGNER VIEW MEDIA UPLOADED.html")

def dsgnr_view_profile(request):
    return render(request, "designer/DESIGNER VIEW PROFILE.html")

def dsgnr_view_request_assigned(request):
    return render(request, "designer/DESIGNER VIEW REQUEST ASSIGNED.html")

def public_homepage(request):
    return render(request,"public/public_homepage.html")

def public_to_admin(request):
    return render(request, "public/PUBLIC SENT REQUEST TO ADMIN BEING MEDIA PROVIDER.html")

def public_view_charge_profile(request):
    return render(request, "public/PUBLIC VIEW CHARGE PROFILE.html")

def public_view_media_provider(request):
    return render(request, "public/PUBLIC VIEW MEDIA PROVIDER.html")

def public_view_media_types(request):
    res = media_type.objects.all()
    return render(request, "public/PUBLIC VIEW MEDIA TYPES.html",{'res':res})

def semp_index(request):
    return render(request,"service employee/semp_index.html")

def semp_homepage(request):
    return render(request,"service employee/semp_homepage.html")

def semp_view_maintance(request):
    res = maintance.objects.all()
    stf = staff.objects.get(LOGIN=request.session['LOGIN_id'])
    area_name = employee_area.objects.filter(STAFF=stf)
    print(area_name)
    placename=installation.objects.filter(STAFF=stf)
    code=installation.objects.filter(STAFF=stf)
    return render(request, "service employee/SERIVCE EMPLOYEE VIEW MAINTANCE ENTRY.html",{'res':res,'res1':area_name,'res1':placename,'res1':code})


def semp_view_maintance_del(request,pk):
    res = maintance.objects.get(id=pk)
    res.delete()
    return semp_view_maintance(request)

def semp_view_maintance_post(request):
    btn = request.POST['button']
    if btn == "SEARCH":
        stf = staff.objects.get(LOGIN=request.session['LOGIN_id'])
        area_name = employee_area.objects.filter(STAFF=stf)
        area = request.POST['select']
        aname = service_area.objects.get(pk=area)
        print(aname)
        res = maintance.objects.filter(SERVICEAREA_id=aname)
        return render(request,"service employee/SERIVCE EMPLOYEE VIEW MAINTANCE ENTRY.html",{'res':res,'res1':area_name})

    if btn =="GO":
        date1 = request.POST['fdate']
        date2 = request.POST['tdate']
        stf = staff.objects.get(LOGIN=request.session['LOGIN_id'])
        area_name = employee_area.objects.filter(STAFF=stf)
        placename= installation.objects.filter(STAFF=stf)
        code= installation.objects.filter(STAFF=stf)
        res = maintance.objects.filter(date__range=(date1, date2))
        print(res)
        return render(request, "service employee/SERIVCE EMPLOYEE VIEW MAINTANCE ENTRY.html", {'res': res, 'res1': area_name,'res1':placename,'res1':code})
    return render(request, "service employee/SERIVCE EMPLOYEE VIEW MAINTANCE ENTRY.html")


def semp_edit_profile(request):
    return render(request, "service employee/SERVICE EMPLOYEE EDIT PROFILE.html")

def semp_expense_mngt(request):
    stf = staff.objects.get(LOGIN=request.session['LOGIN_id'])
    area_name = employee_area.objects.filter(STAFF=stf)
    print(request.session['LOGIN_id'])
    print("hihi")
    print(area_name)
    res=expense.objects.all()
    return render(request, "service employee/SERVICE EMPLOYEE EXPENSE MNGT.html",{'res':res,'data1':area_name})

def semp_expense_mngt_post(request):
    area=request.POST['select']
    tle=request.POST['textfield']
    desc=request.POST['textarea']
    amt=request.POST['textfield2']
    datez = datetime.date.today()
    aname = service_area.objects.get(pk=area)
    print(aname.pk)
    kk = login.objects.get(id=request.session['LOGIN_id'])
    stf = staff.objects.get(LOGIN=kk)
    print(stf)
    print("qqq")
    emparea=employee_area.objects.get(SERVICEAREA=aname,STAFF=stf)
    print("jjj")
    print(emparea)
    res = expense(title=tle, description=desc, amount=amt, date=datez, EMPLOYEEAREA=emparea)
    print(res)
    res.save()
    return render(request, "service employee/SERVICE EMPLOYEE EXPENSE MNGT.html")

def semp_installation(request):
    stf=staff.objects.get(LOGIN=request.session['LOGIN_id'])
    area_name = employee_area.objects.filter(STAFF=stf)
    print(request.session['LOGIN_id'])
    print("hihi")
    print(area_name)
    return render(request,"service employee/SERVICE EMPLOYEE INSTALLATION.html",{'data1':area_name})

def semp_installation_post(request):
    area = request.POST['select']
    print("ggg")
    print(area)
    date=request.POST['date']
    code=request.POST['textfield']
    narration=request.POST['textarea']
    placename=request.POST['textfield2']
    aname=service_area.objects.get(pk=area)
    print(aname.pk)
    kk=login.objects.get(id=request.session['LOGIN_id'])
    stf = staff.objects.get(LOGIN=kk)
    print("hjhjh")
    res=installation(date=date,code=code,narration=narration,placename=placename,SERVICEAREA=aname,STAFF=stf)
    print("yyy")
    res.save()
    print("ttt")
    print(res)
    return redirect("myapp:semp_installation")

def semp_maintance(request):
    print("oooo")
    kk=login.objects.get(id=request.session['LOGIN_id'])
    stf = staff.objects.get(LOGIN=kk)

    print("Stf=",stf.pk)
    area_name = employee_area.objects.filter(STAFF=stf)
    placename=installation.objects.filter(STAFF=stf)
    print("placename=",placename)
    code=installation.objects.filter(STAFF=stf)
    print("installation=",installation)
    return render(request, "service employee/SERVICE EMPLOYEE MAINTANCE ENTRY.html",{'data1':area_name,'data2':placename,'res':code})

def semp_maintance_post(request):
    area=request.POST['select']
    placename=request.POST['select2']
    print(placename)
    code=request.POST['select3']
    print(code)
    mtnce=request.POST['textarea']
    print(mtnce)
    amt=request.POST['textfield']
    print(amt)
    aname = service_area.objects.get(pk=area)
    print(aname.pk)
    stf = staff.objects.get(LOGIN=request.session['LOGIN_id'])
    print("hjhjh")
    datez=datetime.date.today()
    a=installation.objects.get(placename=placename,code=code)
    res=maintance(maintance=mtnce,amount=amt,SERVICEAREA=aname,STAFF=stf,INSTALLATION=a,date=datez)
    res.save()
    return redirect("myapp:semp_maintance")

def semp_view_expense(request):
    res=expense.objects.all()
    # stf = staff.objects.get(LOGIN=request.session['LOGIN_id'])
    # area_name = employee_area.objects.filter(STAFF=stf)
    # emparea = employee_area.objects.filter(EMPLOYEEAREA=area_name)
    # print(emparea)
    return render(request, "service employee/SERVICE EMPLOYEE VIEW EXPENSE.html",{'res':res})

def semp_view_expense_post(request):
    date1 = request.POST['fdate']
    date2 = request.POST['tdate']
    # stf = staff.objects.get(LOGIN=request.session['LOGIN_id'])
    # area_name = employee_area.objects.filter(STAFF=stf)
    res = expense.objects.filter(date__range=(date1, date2))
    print(res)
    return render(request, "service employee/SERVICE EMPLOYEE VIEW EXPENSE.html",{'res':res})

def semp_view_installation(request):
    res=installation.objects.all()
    stf = staff.objects.get(LOGIN=request.session['LOGIN_id'])
    area_name = employee_area.objects.filter(STAFF=stf)
    return render(request, "service employee/SERVICE EMPLOYEE VIEW INSTALLATION.html",{'res':res,'res1':area_name})


def semp_view_installation_del(request,pk):
    res = installation.objects.get(id=pk)
    res.delete()
    return semp_view_installation(request)

def semp_view_installation_post(request):
     btn = request.POST['button']
     if btn == "SEARCH":
         stf = staff.objects.get(LOGIN=request.session['LOGIN_id'])
         area_name = employee_area.objects.filter(STAFF=stf)
         area = request.POST['select']
         aname = service_area.objects.get(pk=area)
         print(aname)
         res=installation.objects.filter(SERVICEAREA_id=aname)
         print(res)
         return render(request, "service employee/SERVICE EMPLOYEE VIEW INSTALLATION.html",{'res': res, 'res1': area_name})

     if btn=="GO":
         date1=request.POST['fdate']
         date2=request.POST['tdate']
         stf = staff.objects.get(LOGIN=request.session['LOGIN_id'])
         area_name = employee_area.objects.filter(STAFF=stf)
         res = installation.objects.filter(date__range=(date1, date2))
         print(res)
         return render(request, "service employee/SERVICE EMPLOYEE VIEW INSTALLATION.html",{'res': res, 'res1': area_name})
     return render(request, "service employee/SERVICE EMPLOYEE VIEW INSTALLATION.html")


def semp_view_profile(request):
    return render(request, "service employee/SERVICE EMPLOYEE VIEW PROFILE.html")

def semp_view_service_area(request):
    staffz=request.session['LOGIN_id']
    staffid=staff.objects.get(LOGIN=staffz)
    print(staffid)
    res = employee_area.objects.filter(STAFF=staffid.pk)
    print(res)
    return render(request,"service employee/SERVICE EMPLOYEE VIEW SERVICE AREA.html",{'res':res})


def semp_view_service_area_post(request):
    print("kkkk")
    area = request.POST['textfield']
    print(area)
    staffz = request.session['LOGIN_id']
    staffid = staff.objects.get(LOGIN=staffz)
    print(staffid)
    #area1 = service_area.objects.get(area_name=area)
    #res1 = employee_area.objects.filter(STAFF=staffid.pk)
    res = employee_area.objects.filter(SERVICEAREA__area_name__contains=area,STAFF=staffid.pk)
    print(res)
    return render(request,"service employee/SERVICE EMPLOYEE VIEW SERVICE AREA.html",{'res': res})


def admin_index(request):
    return render(request,"admin/admin_index.html")
