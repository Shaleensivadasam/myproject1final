from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from django.core.files.storage import FileSystemStorage
from django.shortcuts import render,redirect,HttpResponse
from django.http import JsonResponse
from .models import charge_profile,media_type,media_provider,staff,login,service_area,employee_area,monthly_settlement,installation,maintance,expense,user,complaint,feedback_reviews,request_public,advertisement_request,advertisement_assign,media
import random
import datetime
import smtplib
# Create your views here.



def homepage(request):
    return render(request,"admin/index.html")


def get_provider_name(request,nid):
    print("ok")
    media_obj = media_provider.objects.filter(MEDIATYPE=nid)
    print(media_obj)
    print("hi")
    res2=[]
    for ii in media_obj:
        ss = {'provider_name': ii.provider_name, 'id': ii.id}
        res2.append(ss)

    data = {"res2": res2}
    print(data)
    return JsonResponse(data)


def adm_add_charge_profile(request):
    mediatype=media_type.objects.all()
    mediaprovider=media_provider.objects.all()
    # mediaprovider=media_provider.objects.values('provider_name').distinct()
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
    mediaprovider=media_provider.objects.get(id=provider_name)
    print(provider_name)
    res=charge_profile(charge=charge,profilename=profile_name,MEDIATYPE=mediatype,MEDIAPROVIDER=mediaprovider)
    res.save()
    mediatype = media_type.objects.all()
    mediaprovider = media_provider.objects.all()
    # return render(request,"admin/ADD CHARGE PROFILE.html",{'data1':mediatype,'data2':mediaprovider})
    return HttpResponse(''''<script>alert('Successfully Added');window.location='/myapp/adm_add_charge/'</script>''')

def adm_add_employee_area(request):
    area_name = service_area.objects.all()
    name = staff.objects.filter(LOGIN_id__utype='Service employee')

    return render(request,"admin/ADD EMPLOYEE AREA.html",{'data1':area_name,'data2':name})

def adm_add_employee_area_post(request):
    area_name = request.POST['select']
    staff_name = request.POST['select2']
    aname= service_area.objects.all()
    sname = staff.objects.filter(LOGIN_id__utype='Service employee')

    res=employee_area(SERVICEAREA_id=area_name,STAFF_id=staff_name)
    res.save()
    # return render(request,"admin/ADD EMPLOYEE AREA.html",{'data1':aname,'data2':sname})
    return HttpResponse(''''<script>alert('Successfully Added');window.location='/myapp/adm_add_employee_area/'</script>''')


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
    # return render(request,"admin/ADD MEDIA PROVIDER.html",{'data1':mediatype})
    return HttpResponse('''<script>alert('Successfully Added');window.location='/myapp/adm_add_media_provider/'</script>''')


def adm_media_type(request):
    mediatype = media_type.objects.all()
    return render(request, "admin/ADD MEDIA TYPE.html", {'data1': mediatype})

def adm_media_type_post(request):
    type = request.POST['textfield']
    descrip = request.POST['textarea']
    img = request.FILES['fileField']
    fs = FileSystemStorage()
    filename = fs.save(img.name, img)
    image = fs.url(filename)
    res = media_type(media_type_name=type, description=descrip,images=image)
    res.save()
    # return render(request, "admin/ADD MEDIA TYPE.html")
    return HttpResponse('''<script>alert('Successfully Added');window.location='/myapp/adm_media_type/'</script>''')

def adm_service_area(request):
    return render(request,"admin/ADD SERVICE AREA.html")

def adm_service_area_post(request):
    area_name=request.POST['textfield']
    locality=request.POST['textfield2']
    district=request.POST['select']
    res=service_area(area_name=area_name, area_locality=locality, area_district=district)
    res.save()
    # return render(request,"admin/ADD SERVICE AREA.html")
    return HttpResponse('''<script>alert('Successfully Added');window.location='/myapp/adm_service_area/'</script>''')

def adm_add_staff(request):
    return render(request,"admin/ADD STAFF.html")

def adm_add_staff_post(request):
    print("jjj")
    name = request.POST['textfield']
    gender = request.POST['radio']
    dob = request.POST['date']
    # ar=[]
    # pp = str(dob)
    # ar=pp.split("-")
    # print(ar)
    # print("hlo")
    # kk=ar[2]+"-"+ar[1]+"-"+ar[0]
    # print(kk)
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
    s = smtplib.SMTP(host='smtp.gmail.com', port=587)
    s.starttls()
    s.login("swarnaadvertisersorg@gmail.com", "shaleen@97")
    msg = MIMEMultipart()  # create a message.........."
    message = "Message from Swarna Advertisers"
    msg['From'] = "swarnaadvertisersorg@gmail.com"
    msg['To'] = email_id
    msg['Subject'] = "Your Login details for  Website"
    body = "Your Username is:"+ email_id+"Your Password is:- - " + str(psw)
    msg.attach(MIMEText(body, 'plain'))
    s.send_message(msg)
    res1=login(username=email_id,password=psw,utype=staff_type)

    res1.save()
    print("lll")
    print("res1=",res1)
    # login_id=login.objects.get(id=res1.id)
    print("yyy")
    res=staff(name=name,gender=gender,dob=dob,houseno_name=hno_name,district=district,pincode=pincode,email=email_id,phno=pno,image=image,LOGIN_id=res1.id)
    res.save()
    print("hhh")
    return HttpResponse('''<script>alert('Successfully added');window.location='/myapp/adm_add_staff/'</script>''')


def adm_sent_reply_to_complaint(request,id):
    request.session["compid"]=id
    # res = complaint.objects.get(id=id)
    return render(request,"admin/ADMIN SENT REPLY TO COMPLAINT.html")

def adm_sent_reply_to_complaint_post(request):
    compid = request.session["compid"]
    # compl=request.POST['textarea2']
    reply = request.POST['textarea']
    complaintobj = complaint.objects.get(pk=compid)
    # complaintobj.complaint=compl
    complaintobj.reply = reply
    complaintobj.status = "Replied"
    complaintobj.save()
    # return render(request,"admin/ADMIN VIEW COMPLAINT.html")
    return HttpResponse('''<script>alert('Successfully Replied');window.location='/myapp/adm_view_complaint/'</script>''')


def adm_view_complaint(request):
    # res=complaint.objects.all()
    res=complaint.objects.all().order_by('-date')
    print(res)
    return render(request,"admin/ADMIN VIEW COMPLAINT.html",{'res':res})

def adm_view_complaint_post(request):
    date1 = request.POST['fdate']
    date2 = request.POST['tdate']
    res = complaint.objects.filter(date__range=(date1, date2))
    print(res)
    if res.exists():
        pass
    else:
        text = "<script>alert('No data on such dates');window.location='/myapp/adm_view_complaint/';</script>"
        return HttpResponse(text)
    return render(request,"admin/ADMIN VIEW COMPLAINT.html",{'res':res,'d1':date1,'d2':date2})

def adm_view_expense_mngt(request):
    res = expense.objects.all().order_by('-date')
    return render(request,"admin/ADMIN VIEW EXPENSE MNGT.html",{'res':res})

def adm_view_expense_mngt_post(request):
    date1 = request.POST['fdate']
    date2 = request.POST['tdate']
    # stf = staff.objects.get(LOGIN=request.session['LOGIN_id'])
    # area_name = employee_area.objects.filter(STAFF=stf)
    res = expense.objects.filter(date__range=(date1, date2))
    print(res)
    if res.exists():
        pass
    else:
        text = "<script>alert('No data on such dates');window.location='/myapp/adm_view_expense/';</script>"
        return HttpResponse(text)
    return render(request,"admin/ADMIN VIEW EXPENSE MNGT.html",{'res':res,'d1':date1,'d2':date2})

def adm_view_installation(request):
    res=installation.objects.all().order_by('-date')
    res1=service_area.objects.all()
    print(res1)
    return render(request,"admin/ADMIN VIEW INSTALLATION.html",{'res':res,'res1':res1})

def adm_view_installation_post(request):
    btn = request.POST['button']
    if btn == "SEARCH":
        # stf = staff.objects.get(LOGIN=request.session['LOGIN_id'])
        # area_name = employee_area.objects.filter(STAFF=stf)
        area = request.POST['select']
        aname = service_area.objects.get(pk=area)
        print(aname)
        res = installation.objects.filter(SERVICEAREA_id=aname)
        print(res)
        res1 = service_area.objects.all()
        if res.exists():
            pass
        else:
            text = "<script>alert('No data on such dates');window.location='/myapp/adm_view_installation/';</script>"
            return HttpResponse(text)
        return render(request,"admin/ADMIN VIEW INSTALLATION.html",{'res':res,'res1':res1})

    if btn=="GO":
        date1=request.POST['fdate']
        date2=request.POST['tdate']
        # stf = staff.objects.get(LOGIN=request.session['LOGIN_id'])
        # area_name = employee_area.objects.filter(STAFF=stf)
        res = installation.objects.filter(date__range=(date1, date2))
        print(res)
        if res.exists():
            pass
        else:
            text = "<script>alert('No data on such dates');window.location='/myapp/adm_view_installation/';</script>"
            return HttpResponse(text)
    return render(request, "admin/ADMIN VIEW INSTALLATION.html",{'res':res,'d1':date1,'d2':date2})

def adm_view_maintance(request):
    res = maintance.objects.all()
    res1 = service_area.objects.all()
    print(res1)
    return render(request,"admin/ADMIN VIEW MAINTANCE.html",{'res':res,'res1':res1})

def adm_view_maintance_post(request):
    btn = request.POST['button']
    if btn == "SEARCH":
        # stf = staff.objects.get(LOGIN=request.session['LOGIN_id'])
        # area_name = employee_area.objects.filter(STAFF=stf)
        area = request.POST['select']
        aname = service_area.objects.get(pk=area)
        print(aname)
        res = maintance.objects.filter(SERVICEAREA_id=aname)
        if res.exists():
            pass
        else:
            text = "<script>alert('No data on such area name');window.location='/myapp/adm_view_maintance/';</script>"
            return HttpResponse(text)
        return render(request, "admin/ADMIN VIEW MAINTANCE.html",{'res': res})

    if btn == "GO":
        date1 = request.POST['fdate']
        date2 = request.POST['tdate']
        # stf = staff.objects.get(LOGIN=request.session['LOGIN_id'])
        # area_name = employee_area.objects.filter(STAFF=stf)
        # placename = installation.objects.filter(STAFF=stf)
        # code = installation.objects.filter(STAFF=stf)
        res = maintance.objects.filter(date__range=(date1, date2))
        print(res)
        if res.exists():
            pass
        else:
            text = "<script>alert('No data on such dates');window.location='/myapp/adm_view_maintance/';</script>"
            return HttpResponse(text)
        return render(request,"admin/ADMIN VIEW MAINTANCE.html",{'res': res,'d1':date1,'d2':date2})
    return render(request,"admin/ADMIN VIEW INSTALLATION.html")

def adm_view_new_request_more(request,pk):
    request.session['id'] = pk
    data = advertisement_request.objects.get(id=pk)
    data2 = advertisement_request.objects.get(id=pk)
    name = staff.objects.filter(LOGIN_id__utype='Designer')
    return render(request,"admin/ADMIN VIEW NEW REQUEST MORE.html",{'data':data,'data2':data2,'data3':data2.filename,'data4':name})

def adm_view_new_request_more_post(request):

    btn = request.POST['btn']
    if btn == "ASSIGN":
        id = request.session['id']
        res = advertisement_request.objects.get(id=id)
        res.status = "ASSIGNED"
        res.save()
        designer_name = request.POST['select3']
        dname = staff.objects.get(id=designer_name)
        date = datetime.datetime.now()
        res = advertisement_assign(STAFF=dname, date=date,ADVERTISEMENTREQUEST=res)
        res.save()
        return HttpResponse('''<script>alert('Assigned Successfully');window.location='/myapp/adm_view_new_request/'</script>''')

    if btn == "DOWNLOAD":
        id = str(request.session['id'])
        print(id)
        print("ll")
        aa = request.POST['hi']
        print(aa)
        lst = []
        lst = str(aa).split("/")
        print(lst)
        print("hlo")
        import wget

        print('Beginning file download with wget module')

        url = 'http://localhost:8000' + aa
        wget.download(url, 'C:/Users/user/Downloads/' + lst[2])

        return HttpResponse('''<script>alert('Downloaded Successfully');window.location='/myapp/adm_view_new_request/'</script>''')
    return render(request,"admin/ADMIN VIEW NEW REQUEST.html")

def adm_view_new_request(request):
    res = advertisement_request.objects.filter(status="ACCEPTED").order_by('-date') \
          # | advertisement_request.objects.filter(status="ASSIGNED").order_by('-date')
    # res2 = advertisement_request.objects.filter(status="ASSIGNED")
    return render(request,"admin/ADMIN VIEW NEW REQUEST.html",{'res':res})

def adm_view_new_request_post(request):
    date1 = request.POST['fdate']
    date2 = request.POST['tdate']
    res = advertisement_request.objects.filter(date__range=(date1, date2)).order_by('-date') & advertisement_request.objects.filter(status="ACCEPTED").order_by('-date')
    print(res)
    if res.exists():
        pass
    else:
        text = "<script>alert('No data on such dates');window.location='/myapp/adm_view_new_request/';</script>"
        return HttpResponse(text)
    return render(request,"admin/ADMIN VIEW NEW REQUEST.html",{'res':res,'d1':date1,'d2':date2})

def adm_view_created_media(request):
    res = advertisement_request.objects.filter(status="ASSIGNED").order_by('-date') | advertisement_request.objects.filter(status="RECREATE").order_by('-date') | advertisement_request.objects.filter(status="OK").order_by('-date')| advertisement_request.objects.filter(status="UPLOADED").order_by('-date') | advertisement_request.objects.filter(status="REUPLOADED").order_by('-date')
    print("begin")
    # staffz = request.session['LOGIN_id']
    # staffid = staff.objects.get(LOGIN=staffz)
    # print(staffid)
    new_obj = advertisement_assign.objects.all()
    print(new_obj)
    print("hlo")
    ar = []
    for i in new_obj:
        print(i)
        q1 = i.ADVERTISEMENTREQUEST.id
        ar.append(q1)
    print(ar)
    ar3 = []

    for j in ar:
        print(j)
        ob22 = advertisement_request.objects.get(id=j)
        print(ob22)
        try:
            print("try block")
            res1 = advertisement_assign.objects.get(ADVERTISEMENTREQUEST=ob22)
            print(res1)
            s = { 'filename':ob22.filename,'username':ob22.USER.name,'content':ob22.content,'date':ob22.date,'status':ob22.status,'designername': res1.STAFF.name, 'pk': res1.ADVERTISEMENTREQUEST_id, 'mid': j}
            print(s)
            ar3.append(s)
        except:
            print("error")
    # res2 = advertisement_request.objects.filter(status="ASSIGNED")
    return render(request,"admin/ADMIN VIEW CREATED MEDIA.html",{'res1':ar3})

def adm_view_created_media_post(request):
    date1 = request.POST['fdate']
    date2 = request.POST['tdate']
    # res = advertisement_request.objects.filter(date__range=(date1, date2)).order_by('-date')

          # | advertisement_request.objects.filter(status="ASSIGNED").order_by('-date') | advertisement_request.objects.filter(status="RECREATE").order_by('-date') | advertisement_request.objects.filter(status="OK").order_by('-date')
    res = advertisement_request.objects.filter(date__range=(date1, date2),status="ASSIGNED").order_by('-date')|advertisement_request.objects.filter(date__range=(date1, date2),status="RECREATE").order_by('-date') | advertisement_request.objects.filter(date__range=(date1, date2),status="OK").order_by('-date')| advertisement_request.objects.filter(date__range=(date1, date2),status="UPLOADED").order_by('-date')| advertisement_request.objects.filter(date__range=(date1, date2),status="REUPLOADED").order_by('-date')

    print(res)
    print("qqqqqqqqqqqqq")
    new_obj = advertisement_assign.objects.all()
    print(new_obj)
    print("hlo")
    ar = []
    for i in new_obj:
        print(i)
        q1 = i.ADVERTISEMENTREQUEST.id
        ar.append(q1)
    print(ar)
    ar3 = []

    for j in ar:
        print(j)
        # ob22 = advertisement_request.objects.get(id=j)
        # print(ob22)
        try:
            ob22=advertisement_request.objects.filter(date__range=(date1, date2), status="ASSIGNED",id=j).order_by('-date') | advertisement_request.objects.filter(date__range=(date1, date2), status="RECREATE",id=j).order_by('-date') | advertisement_request.objects.filter(date__range=(date1, date2), status="OK",id=j).order_by('-date') | advertisement_request.objects.filter(date__range=(date1, date2), status="UPLOADED",id=j).order_by('-date') | advertisement_request.objects.filter(date__range=(date1, date2),status="REUPLOADED",id=j).order_by('-date')
            print(ob22)
            print("try block")
            for m in ob22:
                res1 = advertisement_assign.objects.get(ADVERTISEMENTREQUEST=m)
                print(res1)
                s = {'filename': m.filename, 'username': m.USER.name, 'content': m.content, 'date': m.date,
                     'status': m.status, 'designername': res1.STAFF.name, 'pk': res1.ADVERTISEMENTREQUEST_id, 'mid': j}
                print(s)
                ar3.append(s)
        except:
            print("error")
    if res.exists():
        pass
    else:
        text = "<script>alert('No data on such dates');window.location='/myapp/adm_view_created_media/';</script>"
        return HttpResponse(text)
    return render(request,"admin/ADMIN VIEW CREATED MEDIA.html",{'res1':ar3,'d1':date1,'d2':date2})


def adm_view_media_more(request,pk):
    try:
        print(pk)
        request.session['id'] = pk
        data = media.objects.get(ADVERTISEMENTREQUEST_id=pk)
        return render(request, "admin/ADMIN VIEW MEDIA MORE.html", {'data': data, 'data3': data.path})
        print(data)
    except:
        print("error")
    return render(request, "admin/ADMIN VIEW MEDIA MORE.html")


def adm_view_media_more_post(request):
    btn = request.POST['btn']
    if btn == "OK":
        id = request.session['id']
        res = advertisement_request.objects.get(id=id)
        res.status = "OK"
        res.save()
        # obj1=res.status
        # if obj1!="OK" & obj1!="RECREATE":
        #     pass
        # else:
        #     text = "<script>alert('Already send message');window.location='/myapp/adm_view_created_media/';</script>"
        #     return HttpResponse(text)
        return HttpResponse('''<script>alert('Created media ok');window.location='/myapp/adm_view_created_media/'</script>''')
    if btn == "RECREATE":
        id = request.session['id']
        res = advertisement_request.objects.get(id=id)
        res.status = "RECREATE"
        res.save()
        return HttpResponse('''<script>alert('Recreate media');window.location='/myapp/adm_view_created_media/'</script>''')

    if btn == "DOWNLOAD":
        id = str(request.session['id'])
        print(id)
        print("ll")
        aa = request.POST['hi']
        print(aa)
        lst = []
        lst = str(aa).split("/")
        print(lst)
        print("hlo")
        import wget

        print('Beginning file download with wget module')

        url = 'http://localhost:8000' + aa
        wget.download(url, 'C:/Users/user/Downloads/' + lst[2])

        return HttpResponse('''<script>alert('Downloaded Successfully');window.location='/myapp/adm_view_created_media/'</script>''')

    return render(request,"admin/ADMIN VIEW MEDIA MORE.html")


def adm_view_registered_user(request):
    res = user.objects.all()
    return render(request,"admin/ADMIN VIEW REGISTERED USER.html",{'res':res})

def adm_view_registered_user_post(request):
    name=request.POST['textfield']
    res1 = user.objects.filter(name__contains=name)
    if res1.exists():
        pass
    else:
        text = "<script>alert('No data on such user name');window.location='/myapp/adm_view_registered_user/';</script>"
        return HttpResponse(text)
    return render(request,"admin/ADMIN VIEW REGISTERED USER.html",{'res':res1})



# def adm_view_rejected_request(request):
#     res3 = advertisement_request.objects.filter(status="REJECTED")
#     return render(request,"admin/ADMIN VIEW REJECTED REQUEST.html",{'res3':res3})

def adm_allocate_to_designer(request):
    return render(request,"admin/ALLOCATE TO DESIGNER.html")

def adm_edit_charge_profile(request,pk):
    request.session['id'] = pk
    res = charge_profile.objects.get(id=pk)
    print(res)
    mtype=media_type.objects.all()
    pname=media_provider.objects.all()
    return render(request,"admin/EDIT CHARGE PROFILE.html",{'res':res,'data1':mtype,'data2':pname})

def adm_edit_charge_profile_post(request):
    if request.method == 'POST':
        id = request.session['id']
        profile_name=request.POST['textfield']
        media_type=request.POST['select']
        provider_name=request.POST['select2']
        charge=request.POST['textfield2']
        res = charge_profile.objects.get(id=id)

        res.profilename=profile_name
        res.media_type_name=media_type
        res.provider_name=provider_name
        res.charge=charge
        res.save()
    # return render(request,"admin/EDIT CHARGE PROFILE.html")
    return HttpResponse('''<script>alert('Successfully Edited');window.location='/myapp/adm_view_charge_profile/'</script>''')

# def adm_edit_charge_profile_post(request):
#     return render(request,"admin/EDIT CHARGE PROFILE.html")

def adm_edit_media_type(request,pk):
    request.session['id'] = pk
    res = media_type.objects.get(id=pk)
    return render(request,"admin/EDIT MEDIA TYPE.html",{'res':res})

def adm_edit_media_type_post(request):
    id = request.session['id']
    mediatype = request.POST['textfield']
    description = request.POST['textarea']
    res = media_type.objects.get(id=id)
    if 'fileField' in request.FILES:
        img = request.FILES['fileField']
        if img.name=='':
            pass
        else:
            fs = FileSystemStorage()
            filename = fs.save(img.name, img)
            image = fs.url(filename)
            res.images= image
    if request.method=='POST':

        res.media_type_name=mediatype
        res.description=description
        res.save()
    # return adm_view_media_type(request)
    return HttpResponse('''<script>alert('Successfully Edited');window.location='/myapp/adm_view_media_type/'</script>''')

def adm_edit_employee_area(request,pk):
    area_name = service_area.objects.all()
    # name = staff.objects.all()
    # area_name = service_area.objects.all()
    name = staff.objects.filter(LOGIN_id__utype='Service employee')
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
    # return adm_view_employee_area(request)
    return HttpResponse('''<script>alert('Successfully Edited');window.location='/myapp/adm_view_employee_area/'</script>''')


def adm_edit_media_provider(request,pk):
    request.session['id'] = pk
    res = media_provider.objects.get(id=pk)
    mediatype = media_type.objects.all()
    return render(request,"admin/EDIT MEDIA PROVIDER.html",{'res':res,'data1':mediatype})

def adm_edit_media_provider_post(request):
    id = request.session['id']
    provider_name = request.POST['textfield']
    place = request.POST['textfield2']
    city = request.POST['textfield3']
    district = request.POST['select']
    pincode = request.POST['textfield4']
    emailid = request.POST['textfield5']
    phno = request.POST['textfield6']
    # img = request.POST['fileField']
    media_type = request.POST['select2']
    res = media_provider.objects.get(id=id)
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
        res.provider_name=provider_name
        res.place=place
        res.city=city
        res.district=district
        res.pincode=pincode
        res.email=emailid
        res.phno=phno
        # res.image=img
        res.MEDIATYPE_id=media_type
        res.save()
    # return adm_view_media_provider(request)
    return HttpResponse('''<script>alert('Successfully Edited');window.location='/myapp/adm_view_media_provider/'</script>''')


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
    # return adm_view_service_area(request)
    return HttpResponse('''<script>alert('Successfully Edited');window.location='/myapp/adm_view_service_area/'</script>''')



def adm_edit_staff(request,pk):
    request.session['id']=pk
    res=staff.objects.get(id=pk)
    return render(request,"admin/EDIT STAFF.html",{'res':res})

def adm_edit_staff_post(request):
    id=request.session['id']
    name = request.POST['textfield']
    gender = request.POST['radio']
    dob = request.POST['date']
    # ar = []
    # pp = str(dob)
    # ar = pp.split("-")
    # print(ar)
    # print("hlo")
    # kk = ar[2] + "-" + ar[1] + "-" + ar[0]
    # print(kk)
    hno_name = request.POST['textfield2']
    district = request.POST['select2']
    pincode = request.POST['textfield3']
    # email_id = request.POST['textfield4']
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
        # res.email=email_id
        res.phno=pno
        res.staff_type=staff_type

        res.save()
    # return adm_view_staff(request)
    return HttpResponse('''<script>alert('Successfully Edited');window.location='/myapp/adm_view_staff/'</script>''')
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
                return HttpResponse('''<script>alert('Successfully Logged in');window.location='/myapp/semp_homepage/'</script>''')
            elif yy.utype=="admin":
                return HttpResponse('''<script>alert('Successfully Logged in');window.location='/myapp/adm_homepage/'</script>''')
            elif yy.utype=="Designer":
                return HttpResponse('''<script>alert('Successfully Logged in');window.location='/myapp/dsgnr_homepage/'</script>''')

            else:
                return HttpResponse('''<script>alert('Invalid Username or Password');window.location='/myapp/'</script>''')
        else:
            return HttpResponse('''<script>alert('Invalid Username or Password');window.location='/myapp/'</script>''')


def adm_monthly_settlement_entry(request):
    pname=media_type.objects.all()
    # pname = media_provider.objects.values('provider_name').distinct()
    return render(request,"admin/MONTHY SETTLEMENT ENTRY.html",{'data1':pname})

def adm_monthly_settlement_entry_post(request):
    print("jjj")
    provider_id=request.POST['select2']
    year=request.POST['select3']
    month=request.POST['select4']
    amount=request.POST['textfield2']
    print("jj22")
    date=datetime.datetime.now().date()
    print("hhh")
    # qq=media_provider.objects.get(id=provider_name)
    # pname=provider_name.objects.get(pk=provider_name)
    res=monthly_settlement(MEDIAPROVIDER_id=provider_id,year=year,month=month,amount=amount,date=date)
    res.save()
    print("ppp")
    pname=media_provider.objects.all()
    print("uuu")
    # return render(request,"admin/MONTHY SETTLEMENT ENTRY.html",{'data1':pname})
    return HttpResponse('''<script>alert('Successfully Added');window.location='/myapp/adm_monthly_settlement/'</script>''')


def adm_view_advertisement_request_approve(request):
    res = advertisement_request.objects.all().order_by('-date')
    res2 = user.objects.all()
    return render(request,"admin/VIEW ADVERTISEMENT REQUEST APPROVE.html",{'res':res,'res2':res2})

def adm_view_advertisement_request_approve_post(request):
    date1 = request.POST['fdate']
    date2 = request.POST['tdate']
    res = advertisement_request.objects.filter(date__range=(date1, date2))
    print(res)
    if res.exists():
        pass
    else:
        text = "<script>alert('No data on such dates');window.location='/myapp/adm_view_advertisement_request_approve/';</script>"
        return HttpResponse(text)
    return render(request,"admin/VIEW ADVERTISEMENT REQUEST APPROVE.html",{'res':res,'d1':date1,'d2':date2})


def adm_view_advertisement_request_approved_more(request,pk):
    request.session['id'] = pk
    data = advertisement_request.objects.get(id=pk)
    data2 = advertisement_request.objects.get(id=pk)
    return render(request,"admin/VIEW ADVERTISEMENT REQUEST APPROVED MORE.html",{'data':data,'data2':data2,'data3':data2.filename})

def adm_view_advertisement_request_approved_more_post(request):
    btn = request.POST['btn']
    if btn == "ACCEPT":
        id = request.session['id']
        res = advertisement_request.objects.get(id=id)
        res.status = "ACCEPTED"
        res.save()
        return HttpResponse('''<script>alert('Accepted Successfully');window.location='/myapp/adm_view_advertisement_request_approve/'</script>''')
    if btn == "REJECT":
        id = request.session['id']
        res = advertisement_request.objects.get(id=id)
        res.status = "REJECTED"
        res.save()
        return HttpResponse('''<script>alert('Rejected Successfully');window.location='/myapp/adm_view_advertisement_request_approve/'</script>''')
    if btn == "DOWNLOAD":
        id = str(request.session['id'])
        print(id)
        print("ll")
        aa=request.POST['hi']
        print(aa)
        lst=[]
        lst=str(aa).split("/")
        print(lst)
        print("hlo")
        import wget

        print('Beginning file download with wget module')

        url = 'http://localhost:8000'+aa
        wget.download(url, 'C:/Users/user/Downloads/'+lst[2])

        return HttpResponse('''<script>alert('Downloaded Successfully');window.location='/myapp/adm_view_advertisement_request_approve/'</script>''')
    return render(request,"admin/VIEW ADVERTISEMENT REQUEST APPROVED MORE.html")

def adm_view_charge_profile(request):
    res=charge_profile.objects.all()
    res2=media_type.objects.all()
    return render(request,"admin/VIEW CHARGE PROFILE.html",{'res':res,'res2':res2})

def adm_view_charge_profile_del(request,pk):
    res = charge_profile.objects.get(id=pk)
    res.delete()
    # return adm_view_employee_area(request)
    return HttpResponse('''<script>alert('Successfully Deleted');window.location='/myapp/adm_view_charge_profile/'</script>''')
    return render(request,"admin/VIEW CHARGE PROFILE.html")

def adm_view_charge_profile_post(request):
    btn=request.POST['button']
    if btn == "SEARCH":
        pname=request.POST['textfield']
        res=charge_profile.objects.filter(profilename__contains=pname)
        if res.exists():
            pass
        else:
            text = "<script>alert('No charge profile');window.location='/myapp/adm_view_charge_profile/';</script>"
            return HttpResponse(text)
    if btn == "GO":
        mtype = request.POST['select']
        print(mtype)
        type=media_type.objects.get(id=mtype)
        res = charge_profile.objects.filter(MEDIATYPE=type)
        if res.exists():
            pass
        else:
            text="<script>alert('No charge profile');window.location='/myapp/adm_view_charge_profile/';</script>"
            return  HttpResponse(text)
        print(res)
    res2 = media_type.objects.all()
    return render(request,"admin/VIEW CHARGE PROFILE.html",{'res':res,'res2':res2})


def adm_view_employee_area(request):
    res=employee_area.objects.all()
    print(res)
    return render(request,"admin/VIEW EMPLOYEE AREA.html",{'res':res})

def adm_view_employee_area_post(request):
    print("begin")
    area = request.POST['textfield']
    print(area)
    print("oo")
    try:
        print("aaaa")
        area1=service_area.objects.get(area_name=area)
        print(area1)
        print("hlo")
        res = employee_area.objects.filter(SERVICEAREA=area1)
        print(res)
        print("pp")
        if res.exists():
            pass
        else:
            text = "<script>alert('No data on such area name');window.location='/myapp/adm_view_employee_area/';</script>"
            return HttpResponse(text)
        return render(request, "admin/VIEW EMPLOYEE AREA.html", {'res': res})
    except:
        print("error")
        return render(request, "admin/VIEW EMPLOYEE AREA.html")





def adm_view_employee_area_del(request,pk):
    res=employee_area.objects.get(id=pk)
    res.delete()
    # return adm_view_employee_area(request)
    return HttpResponse('''<script>alert('Successfully Deleted');window.location='/myapp/adm_view_employee_area/'</script>''')


def adm_view_feedback_reviews(request):
    # res=feedback_reviews.objects.all()
    res=feedback_reviews.objects.all().order_by('-date')
    return render(request,"admin/VIEW FEEDBACK REVIEWS.html",{'res':res})

def adm_view_feedback_reviews_post(request):
    date1 = request.POST['fdate']
    date2 = request.POST['tdate']
    res = feedback_reviews.objects.filter(date__range=(date1, date2))
    print(res)
    if res.exists():
        pass
    else:
        text = "<script>alert('No data on such dates');window.location='/myapp/adm_view_feedback/';</script>"
        return HttpResponse(text)
    return render(request,"admin/VIEW FEEDBACK REVIEWS.html",{'res':res,'d1':date1,'d2':date2})

def adm_view_media_provider(request):
    res = media_provider.objects.all()
    return render(request,"admin/VIEW MEDIA PROVIDER.html",{'res':res})

def adm_view_media_provider_del(request,pk):
    res = media_provider.objects.get(id=pk)
    res.delete()
    # return adm_view_media_provider(request)
    return HttpResponse('''<script>alert('Successfully Deleted');window.location='/myapp/adm_view_media_provider/'</script>''')


def adm_view_media_provider_post(request):
    pname = request.POST['textfield']
    print(pname)
    res = media_provider.objects.filter(provider_name__contains=pname)
    print(res)
    if res.exists():
        pass
    else:
        text = "<script>alert('No data on such media provider');window.location='/myapp/adm_view_media_provider/';</script>"
        return HttpResponse(text)
    return render(request,"admin/VIEW MEDIA PROVIDER.html",{'res':res})

def adm_view_media_type(request):
    res=media_type.objects.all()
    return render(request,"admin/VIEW MEDIA TYPE.html",{'res':res})

def adm_view_media_type_del(request,pk):
    res = media_type.objects.get(id=pk)
    res.delete()
    # return adm_view_media_type(request)
    return HttpResponse('''<script>alert('Successfully Deleted');window.location='/myapp/adm_view_media_type/'</script>''')

def adm_view_media_type_post(request):
    mtype = request.POST['textfield']
    print(mtype)
    res = media_type.objects.filter(media_type_name__contains=mtype)
    print(res)
    if res.exists():
        pass
    else:
        text = "<script>alert('No data on such media type name');window.location='/myapp/adm_view_media_type/';</script>"
        return HttpResponse(text)
    return render(request,"admin/VIEW MEDIA TYPE.html",{'res':res})

def adm_view_monthy_settlement_entry(request):
    res=monthly_settlement.objects.all().order_by('-date')
    return render(request,"admin/VIEW MONTHLY SETTLEMENT ENTRY.html",{'res':res})

def adm_view_monthy_settlement_entry_post(request):
    btn = request.POST['button']
    if btn == "GO":
        date1 = request.POST['fdate']
        date2 = request.POST['tdate']
        res = monthly_settlement.objects.filter(date__range=(date1, date2))
        print(res)
        if res.exists():
            pass
        else:
            text = "<script>alert('No data on such dates');window.location='/myapp/adm_view_monthly_settlement/';</script>"
            return HttpResponse(text)
        return render(request, "admin/VIEW MONTHLY SETTLEMENT ENTRY.html",{'res':res,'d1':date1,'d2':date2})
    # if btn == "SEARCH":
    #     pname = request.POST['textfield']
    #     print(pname)
    #     try:
    #         print("enter")
    #         prname=media_provider.objects.get(provider_name=pname)
    #         print(prname)
    #         print("hlo")
    #         res = monthly_settlement.objects.filter(MEDIAPROVIDER_id=prname)
    #         print(res)
    #         print("ppp")
    #         if res.exists():
    #             pass
    #         else:
    #             text = "<script>alert('No data on such provider name');window.location='/myapp/adm_view_monthly_settlement/';</script>"
    #             return HttpResponse(text)
    #         return render(request, "admin/VIEW MONTHLY SETTLEMENT ENTRY.html",{'res':res})
    #     except:
    #         print("error")
    #         return render(request,"admin/VIEW MONTHLY SETTLEMENT ENTRY.html")

def adm_view_registered_user_more(request):
    return render(request,"admin/VIEW REGISTERED USER.html")

def adm_request_from_public_for_media_provider(request):
    res=request_public.objects.all()
    return render(request,"admin/VIEW REQUEST FROM PUBLIC FOR MEDIA PROVIDER.html",{'res':res})

def adm_request_from_public_for_media_provider_post(request):
    name = request.POST['textfield']
    res1 = request_public.objects.filter(provider_name__contains=name)
    if res1.exists():
        pass
    else:
        text = "<script>alert('No data on such provider name');window.location='/myapp/adm_request_from_public_for_media_provider/';</script>"
        return HttpResponse(text)
    return render(request,"admin/VIEW REQUEST FROM PUBLIC FOR MEDIA PROVIDER.html",{'res':res1})

def adm_request_from_public(request,pk):
    request.session['id'] = pk
    data = request_public.objects.get(id=pk)
    return render(request,"admin/VIEW REQUEST FROM PUBLIC.html",{'data':data})

def adm_view_service_area(request):
    res=service_area.objects.all()
    print(res)
    return render(request,"admin/VIEW SERVICE AREA.html",{'res':res})


def adm_view_service_area_post(request):
    area=request.POST['textfield']
    res1=service_area.objects.filter(area_name__contains=area)
    if res1.exists():
        pass
    else:
        text = "<script>alert('No data on such area name');window.location='/myapp/adm_view_service_area/';</script>"
        return HttpResponse(text)
    return render(request, "admin/VIEW SERVICE AREA.html", {'res': res1})


def adm_view_service_area_del(request,pk):
    res=service_area.objects.get(id=pk)
    res.delete()
    # return adm_view_service_area(request)
    return HttpResponse('''<script>alert('Successfully Deleted');window.location='/myapp/adm_view_service_area/'</script>''')


def adm_view_staff(request):
    res=staff.objects.all()
    # print(res.LOGIN.utype)
    return render(request,"admin/VIEW STAFF.html",{'res1':res})

def adm_view_staff_del(request,pk):

    res=staff.objects.get(id=pk)
    res.delete()
    # print(res.LOGIN.utype)
    # return adm_view_staff(request)
    return HttpResponse('''<script>alert('Successfully Deleted');window.location='/myapp/adm_view_staff/'</script>''')

def adm_view_staff_post(request):
    btn=request.POST['button']
    if btn=="SEARCH":
        stafftype = request.POST['select']
        res = staff.objects.all()
        res1 = staff.objects.filter(LOGIN_id__utype=stafftype)
        if res1.exists():
            pass
        else:
            text = "<script>alert('No data on such staff type');window.location='/myapp/adm_view_staff/';</script>"
            return HttpResponse(text)
        return render(request, "admin/VIEW STAFF.html", {'res': res, 'res1': res1})
    if btn=="GO":
        empname = request.POST['textfield']
        res = staff.objects.all()
        res1 = staff.objects.filter(name__contains=empname)
        if res1.exists():
            pass
        else:
            text = "<script>alert('No data on such employee name');window.location='/myapp/adm_view_staff/';</script>"
            return HttpResponse(text)
        return render(request, "admin/VIEW STAFF.html", {'res': res, 'res1': res1})


def adm_view_rejected_request(request):
    res = advertisement_request.objects.filter(status="REJECTED")
    return render(request,"admin/ADMIN VIEW REJECTED REQUEST.html",{'res':res})

def adm_view_rejected_request_post(request):
    date1 = request.POST['fdate']
    date2 = request.POST['tdate']
    res = advertisement_request.objects.filter(date__range=(date1, date2)).order_by('-date') & advertisement_request.objects.filter(status="REJECTED").order_by('-date')
    print(res)
    if res.exists():
        pass
    else:
        text = "<script>alert('No data on such dates');window.location='/myapp/adm_view_rejected_request/';</script>"
        return HttpResponse(text)
    return render(request,"admin/ADMIN VIEW REJECTED REQUEST.html",{'res':res,'d1':date1,'d2':date2})

def adm_view_rejected_request_more(request,pk):
    request.session['id'] = pk
    data = advertisement_request.objects.get(id=pk)
    data2 = advertisement_request.objects.get(id=pk)
    return render(request,"admin/ADMIN VIEW REJECTED REQUEST MORE.html",{'data':data,'data2':data2})

def adm_homepage(request):
    return render(request, "admin/adm_homepage.html")

def designer_index(request):
    return render(request, "designer/designer_index.html")

def dsgnr_homepage(request):
    return render(request, "designer/dsg_homepage.html")

def dsgnr_edit_create_media(request,pk,id2):
    print("kkkk")
    request.session['id'] = pk
    request.session['id2'] = id2
    res = media.objects.get(id=pk)
    print(res)
    print("lllll")
    return render(request, "designer/DESIGNER EDIT CREATE MEDIA.html",{'res':res})

def dsgnr_edit_create_media_post(request):
    id = request.session['id']
    media_title = request.POST['textfield']
    filename22 = request.POST['textfield2']
    description = request.POST['textarea']
    res = media.objects.get(id=id)
    mm=""
    if 'fileField' in request.FILES:
        print("akl")
        img = request.FILES['fileField']
        if img.name == '':
            pass
        else:
            print("hlo")
            fs = FileSystemStorage()
            filename = fs.save(img.name, img)
            image = fs.url(filename)
            res.path = image
            print(res.path)
            print("kkk")
    if request.method == 'POST':
        print("yyyyy")
        res.media_title = media_title
        res.filename = filename22
        res.description = description
        res.save()
        qq=request.session['id2']
        new_ob=advertisement_request.objects.get(id=qq)
        new_ob.status="REUPLOADED"
        new_ob.save()

    return HttpResponse('''<script>alert('Successfully Edited');window.location='/myapp/dsgnr_view_media/'</script>''')
    # return render(request, "designer/DESIGNER EDIT CREATE MEDIA.html")

def dsgnr_edit_profile(request,pk):
    request.session['LOGIN_id'] = pk
    res = staff.objects.get(id=pk)
    return render(request, "designer/DESIGNER EDIT PROFILE.html",{'data':res})

def dsgnr_edit_profile_post(request):
    id = request.session['LOGIN_id']
    name = request.POST['textfield']
    gender = request.POST['radio']
    dob = request.POST['date']
    hno_name = request.POST['textfield2']
    district = request.POST['select2']
    pincode = request.POST['textfield3']
    # email_id = request.POST['textfield4']
    pno = request.POST['textfield5']
    print("qwerty")
    res = staff.objects.get(LOGIN=login.objects.get(id=id))
    if 'fileField' in request.FILES:
        img = request.FILES['fileField']
        if img.name == '':
            pass
        else:
            fs = FileSystemStorage()
            filename = fs.save(img.name, img)
            image = fs.url(filename)
            res.image = image
    if request.method == 'POST':
        res.name = name
        res.gender = gender
        res.dob = dob
        res.houseno_name = hno_name
        res.district = district
        res.pincode = pincode
        # res.email=email_id
        res.phno = pno
        res.save()
        emp_obj = staff.objects.get(LOGIN=login.objects.get(id=id))
    # return render(request, "designer/DESIGNER VIEW PROFILE.html",{'data':emp_obj})
    return HttpResponse('''<script>alert('Successfully Edited');window.location='/myapp/dsgnr_view_profile/'</script>''')


def dsgnr_upload_media(request):
    return render(request, "designer/DESIGNER UPLOAD CREATED MEDIA.html")


def dsgnr_upload_media_post(request,id):
    request.session["id"]=id
    if request.method == 'POST':
        print("ppp")
        mtitle = request.POST['textfield']
        fname = request.POST['textfield2']
        dsec = request.POST['textarea']
        print("lll")
        upload_file = request.FILES['pho']
        fs = FileSystemStorage()
        name = fs.save(upload_file.name, upload_file)
        url = "/media/" + upload_file.name
        print("ggg")
        date = datetime.datetime.now()
        # id = request.session['id']
        # res1 = advertisement_assign.objects.get(ADVERTISEMENTREQUEST_id=id)
        staffz = request.session['LOGIN_id']
        staffid = staff.objects.get(LOGIN=staffz)
        print(staffid)
        # adasign_obj = advertisement_assign.objects.get(STAFF=staffid.pk)
        print("id=",id)
        assign_obj = advertisement_assign.objects.get(ADVERTISEMENTREQUEST_id=id)
        print(assign_obj)
        adrequest = assign_obj.ADVERTISEMENTREQUEST.id
        adre_obj = advertisement_request.objects.get(id=adrequest)
        print(adre_obj)
        print(mtitle)
        print(fname)
        print(dsec)
        print(url)
        print(date)
        res = media(media_title=mtitle, filename=fname, description=dsec, path=url, ADVERTISEMENTREQUEST=adre_obj,
                    date=date)
        res.save()
        #
        btn=request.POST['btn']
        if btn == "CREATE":
            id = request.session['id']
            print(id)
            print("hlo")
            res = advertisement_request.objects.get(id=id)
            # if media.objects.filter(ADVERTISEMENTREQUEST_id=id).exists():
            #     print("value here")
            # else:
            #     print("no value")
            res.status = "UPLOADED"
            res.save()

    # return HttpResponse('''<script>alert('Uploaded media');window.location='/myapp/dsgnr_view_request_assigned/'</script>''')

    return render(request, "designer/DESIGNER UPLOAD CREATED MEDIA.html")
    # return HttpResponse('''<script>alert('Successfully Uploaded');window.location='/myapp/dsgnr_view_request_assigned/'</script>''')


def upload_media22(request):
    if request.method == 'POST':
        print("ppp")
        mtitle = request.POST['textfield']
        fname = request.POST['textfield2']
        dsec = request.POST['textarea']
        print("lll")
        upload_file = request.FILES['pho']
        fs = FileSystemStorage()
        name = fs.save(upload_file.name, upload_file)
        url = "/media/" + upload_file.name
        print("ggg")
        date = datetime.datetime.now()
        id = request.session['id']
        res1 = advertisement_assign.objects.get(pk=id)
        print(res1)
        adv_reqid=res1.ADVERTISEMENTREQUEST_id
        print("adv=",adv_reqid)
        adv_obj=advertisement_request.objects.get(pk=adv_reqid)
        print(adv_obj)
        res1 = media.objects.filter(ADVERTISEMENTREQUEST=adv_obj)
        print(res1)
        if res1.exists():
            print("eeee")
            return HttpResponse("exists....")
            # pass

        else:
            res = media(media_title=mtitle, filename=fname, description=dsec, path=url, ADVERTISEMENTREQUEST=adv_obj,
                        date=date)
            res.save()
            print("media ovr")
            # cccccc
            id = request.session['id']
            print(id)
            print("hlo")
            res = advertisement_request.objects.get(pk=adv_reqid)
            res.status = "UPLOADED"
            res.save()
            # return HttpResponse("ok")
        return HttpResponse('''<script>alert('Successfully Uploaded');window.location='/myapp/dsgnr_view_request_assigned/'</script>''')


def dsgnr_view_media_uploaded(request):
    staffz = request.session['LOGIN_id']
    staffid = staff.objects.get(LOGIN=staffz)
    print(staffid)
    new_obj=advertisement_assign.objects.filter(STAFF=staffid)
    print(new_obj)
    print("qwe")
    ar=[]
    for i in new_obj:
        print(i)
        q1=i.ADVERTISEMENTREQUEST.id
        ar.append(q1)
    print(ar)
    print("aaaaaaaaaaaaaa")
    print("ar ovr")
    ar3=[]

    for j in ar:
        print(j)
        ob22=advertisement_request.objects.get(id=j)
        print(ob22)
        try:
            print("try block")
            res = media.objects.get(ADVERTISEMENTREQUEST=ob22)
            print(res)
            s={'media_title':res.media_title,'filename':res.filename,'description':res.description,'date':res.date,'path':res.path,'usr':res.ADVERTISEMENTREQUEST.USER.name,'pk':res.id,'mid':j}
            ar3.append(s)
        except:
            print("error")
    return render(request, "designer/DESIGNER VIEW MEDIA UPLOADED.html",{'res':ar3})

def dsgnr_view_media_uploaded_post(request):
    staffz = request.session['LOGIN_id']
    mtitle=request.POST['textfield']
    staffid = staff.objects.get(LOGIN=staffz)
    print(staffid)
    new_obj = advertisement_assign.objects.filter(STAFF=staffid)
    print(new_obj)
    print("qwe")
    ar = []
    for i in new_obj:
        print(i)
        q1 = i.ADVERTISEMENTREQUEST.id
        ar.append(q1)
    print(ar)
    print("aaaaaaaaaaaaaa")
    print("ar ovr")
    ar3 = []

    for j in ar:
        print(j)
        ob22 = advertisement_request.objects.get(id=j)
        print(ob22)
        try:
            print("try block")
            res = media.objects.get(ADVERTISEMENTREQUEST=ob22,media_title__contains=mtitle)
            print(res)
            s = {'media_title': res.media_title, 'filename': res.filename, 'description': res.description,
                 'date': res.date, 'path': res.path, 'usr': res.ADVERTISEMENTREQUEST.USER.name, 'pk': res.id, 'mid': j}
            ar3.append(s)
        except:
            print("error")
    return render(request, "designer/DESIGNER VIEW MEDIA UPLOADED.html", {'res': ar3})



# def dsgnr_view_media_uploaded_del(request,pk):
#     res = media.objects.get(id=pk)
#     res.delete()
#     return HttpResponse('''<script>alert('Successfully Deleted');window.location='/myapp/dsgnr_view_media/'</script>''')
    # return render(request, "designer/DESIGNER VIEW MEDIA UPLOADED.html",{'res':res})


def dsgnr_view_profile(request):
    id = request.session['LOGIN_id']
    emp_obj = staff.objects.get(LOGIN_id=id)
    if request.method == 'POST':
        return render(request, "designer/DESIGNER EDIT PROFILE.html", {'data': emp_obj})
    return render(request, "designer/DESIGNER VIEW PROFILE.html",{'data':emp_obj})

def dsgnr_view_request_assigned(request):
    # res=advertisement_assign.objects.all().order_by('-date')
    # res1 = advertisement_request.objects.filter(status="ASSIGNED")
    # # res2 = user.objects.all()
    staffz = request.session['LOGIN_id']
    staffid = staff.objects.get(LOGIN=staffz)
    print(staffid)
    res = advertisement_assign.objects.filter(STAFF=staffid.pk).order_by('-date')
    print(res)
    return render(request, "designer/DESIGNER VIEW REQUEST ASSIGNED.html",{'res':res})

def dsgnr_view_request_assigned_post(request,id):
    print("lll")
    assign_obj=advertisement_assign.objects.get(id=id)
    print(assign_obj)
    pt=assign_obj.ADVERTISEMENTREQUEST.filename
    print(pt)
    import wget

    print('Beginning file download with wget module')

    url = 'http://localhost:8000' + pt
    wget.download(url, 'C:/Users/user/Downloads/a.pdf')

    return HttpResponse('''<script>alert('Downloaded Successfully');window.location='/myapp/dsgnr_view_request_assigned/'</script>''')

def dsgnr_view_request_post(request):
    print("hlo")
    staffz = request.session['LOGIN_id']
    staffid = staff.objects.get(LOGIN=staffz)
    print(staffid)
    date1 = request.POST['fdate']
    date2 = request.POST['tdate']
    print(date1)
    print(date2)
    res = advertisement_assign.objects.filter(date__range=(date1, date2),STAFF=staffid.pk)
    # , status="ASSIGNED").order_by('-date') | advertisement_assign.objects.filter(date__range=(date1, date2), status="RECREATE").order_by('-date') | advertisement_request.objects.filter(date__range=(date1, date2), status="OK").order_by('-date') | advertisement_assign.objects.filter(date__range=(date1, date2), status="UPLOADED").order_by('-date') | advertisement_assign.objects.filter(date__range=(date1, date2), status="REUPLOADED").order_by('-date')
    # print(res)
    if res.exists():
        pass
    else:
        text = "<script>alert('No data on such dates');window.location='/myapp/dsgnr_view_request_assigned/';</script>"
        return HttpResponse(text)
    print(res)
    return render(request, "designer/DESIGNER VIEW REQUEST ASSIGNED.html", {'res': res, 'd1': date1, 'd2': date2})

    # return render(request, "designer/DESIGNER VIEW REQUEST ASSIGNED.html", {'res': res, 'd1': date1, 'd2': date2})

    # return render(request, "designer/DESIGNER VIEW REQUEST ASSIGNED.html")

def public_index(request):
    return render(request,"public/index.html")

def public_homepage(request):
    return render(request,"public/public_homepage.html")

def public_to_admin(request):
    return render(request, "public/PUBLIC SENT REQUEST TO ADMIN BEING MEDIA PROVIDER.html")

def public_to_admin_post(request):
    name = request.POST['textfield']
    gender = request.POST['radio']
    dob = request.POST['date']
    place = request.POST['textfield2']
    district = request.POST['select']
    pincode = request.POST['textfield4']
    emailid = request.POST['textfield5']
    phno = request.POST['textfield6']
    img = request.FILES['fileField']
    fs = FileSystemStorage()
    filename = fs.save(img.name, img)
    image = fs.url(filename)
    res = request_public(provider_name=name, gender=gender, dob=dob, houseno_name=place, district=district,pincode=pincode, image=image, phno=phno, emailid=emailid)
    res.save()
    # return render(request, "public/PUBLIC SENT REQUEST TO ADMIN BEING MEDIA PROVIDER.html")
    return HttpResponse('''<script>alert('Successfully sended');window.location='/myapp/public_public_to_admin/'</script>''')





def public_view_charge_profile(request):
    res = charge_profile.objects.all()
    return render(request, "public/PUBLIC VIEW CHARGE PROFILE.html",{'res':res})

def public_view_media_provider(request):
    res = media_provider.objects.all()
    return render(request, "public/PUBLIC VIEW MEDIA PROVIDER.html",{'res':res})

def public_view_media_types(request):
    res = media_type.objects.all()
    return render(request, "public/PUBLIC VIEW MEDIA TYPES.html",{'res':res})
    # return render(request, "public/af.html",{'res':res})

# def public_af(request):
#     res = media_type.objects.all()
#     # return render(request, "public/PUBLIC VIEW MEDIA TYPES.html",{'res':res})
#     return render(request, "public/af.html",{'res':res})

def semp_index(request):
    return render(request,"service employee/semp_index.html")

def semp_homepage(request):
    return render(request,"service employee/semp_homepage.html")

def semp_view_maintance(request):
    res = maintance.objects.all()
    stf = staff.objects.get(LOGIN=request.session['LOGIN_id'])
    area_name = employee_area.objects.filter(STAFF=stf)
    print(area_name)
    # placename=installation.objects.filter(STAFF=stf)
    # code=installation.objects.filter(STAFF=stf)
    return render(request, "service employee/SERIVCE EMPLOYEE VIEW MAINTANCE ENTRY.html",{'res':res,'res1':area_name})


def semp_view_maintance_del(request,pk):
    res = maintance.objects.get(id=pk)
    res.delete()
    # return semp_view_maintance(request)
    return HttpResponse('''<script>alert('Successfully Deleted');window.location='/myapp/semp_view_maintance/'</script>''')


def semp_view_maintance_post(request):
    btn = request.POST['button']
    if btn == "SEARCH":
        stf = staff.objects.get(LOGIN=request.session['LOGIN_id'])
        area_name = employee_area.objects.filter(STAFF=stf)
        area = request.POST['select']
        aname = service_area.objects.get(pk=area)
        print(aname)
        res = maintance.objects.filter(SERVICEAREA_id=aname)
        if res.exists():
            pass
        else:
            text = "<script>alert('No data on such dates');window.location='/myapp/semp_view_maintance/';</script>"
            return HttpResponse(text)
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
        if res.exists():
            pass
        else:
            text = "<script>alert('No data on such dates');window.location='/myapp/semp_view_maintance/';</script>"
            return HttpResponse(text)
        return render(request, "service employee/SERIVCE EMPLOYEE VIEW MAINTANCE ENTRY.html", {'res': res, 'res1': area_name,'res1':placename,'res1':code,'d1':date1,'d2':date2})
    return render(request, "service employee/SERIVCE EMPLOYEE VIEW MAINTANCE ENTRY.html")


def semp_edit_profile(request,pk):
    request.session['LOGIN_id'] = pk
    res = staff.objects.get(id=pk)
    return render(request, "service employee/SERVICE EMPLOYEE EDIT PROFILE.html",{'data':res})

def semp_edit_profile_post(request):
    id = request.session['LOGIN_id']
    name = request.POST['textfield']
    gender = request.POST['radio']
    dob = request.POST['date']
    hno_name = request.POST['textfield2']
    district = request.POST['select2']
    pincode = request.POST['textfield3']
    # email_id = request.POST['textfield4']
    pno = request.POST['textfield5']
    print("qwerty")
    res = staff.objects.get(LOGIN=login.objects.get(id=id))
    if 'fileField' in request.FILES:
        img = request.FILES['fileField']
        if img.name == '':
            pass
        else:
            fs = FileSystemStorage()
            filename = fs.save(img.name, img)
            image = fs.url(filename)
            res.image = image
    if request.method == 'POST':
        res.name = name
        res.gender = gender
        res.dob = dob
        res.houseno_name = hno_name
        res.district = district
        res.pincode = pincode
        # res.email=email_id
        res.phno = pno
        res.save()
        emp_obj= staff.objects.get(LOGIN=login.objects.get(id=id))
    # return render(request, "service employee/SERVICE EMPLOYEE VIEW PROFILE.html",{'data':emp_obj})
    return HttpResponse('''<script>alert('Successfully Edited');window.location='/myapp/semp_view_profile/'</script>''')

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
    # return render(request, "service employee/SERVICE EMPLOYEE EXPENSE MNGT.html")
    return HttpResponse('''<script>alert('Successfully Added');window.location='/myapp/semp_expense_mngt/'</script>''')


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
    # return redirect("myapp:semp_installation")
    return HttpResponse('''<script>alert('Successfully Added');window.location='/myapp/semp_installation/'</script>''')


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
    # return redirect("myapp:semp_maintance")
    return HttpResponse('''<script>alert('Successfully Added');window.location='/myapp/semp_maintance/'</script>''')


def semp_view_expense(request):
    res=expense.objects.all().order_by('-date')
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
    if res.exists():
        pass
    else:
        text = "<script>alert('No data on such dates');window.location='/myapp/semp_view_expense/';</script>"
        return HttpResponse(text)
    return render(request, "service employee/SERVICE EMPLOYEE VIEW EXPENSE.html",{'res':res,'d1':date1,'d2':date2})

def semp_view_installation(request):
    res=installation.objects.all()
    stf = staff.objects.get(LOGIN=request.session['LOGIN_id'])
    area_name = employee_area.objects.filter(STAFF=stf)
    # area_name = employee_area.objects.filter(STAFF=request.session['LOGIN_id'])
    return render(request, "service employee/SERVICE EMPLOYEE VIEW INSTALLATION.html",{'res':res,'res1':area_name})


def semp_view_installation_del(request,pk):
    res = installation.objects.get(id=pk)
    res.delete()
    # return semp_view_installation(request)
    return HttpResponse('''<script>alert('Successfully Deleted');window.location='/myapp/semp_view_installation/'</script>''')



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
         if res.exists():
             pass
         else:
             text = "<script>alert('No data on such area name');window.location='/myapp/semp_view_installation/';</script>"
             return HttpResponse(text)
         return render(request, "service employee/SERVICE EMPLOYEE VIEW INSTALLATION.html",{'res': res, 'res1': area_name})

     if btn=="GO":
         date1=request.POST['fdate']
         date2=request.POST['tdate']
         stf = staff.objects.get(LOGIN=request.session['LOGIN_id'])
         area_name = employee_area.objects.filter(STAFF=stf)
         res = installation.objects.filter(date__range=(date1, date2))
         print(res)
         if res.exists():
             pass
         else:
             text = "<script>alert('No data on such dates');window.location='/myapp/semp_view_installation/';</script>"
             return HttpResponse(text)
         return render(request, "service employee/SERVICE EMPLOYEE VIEW INSTALLATION.html",{'res': res, 'res1': area_name,'d1':date1,'d2':date2})
     return render(request, "service employee/SERVICE EMPLOYEE VIEW INSTALLATION.html")


def semp_view_profile(request):
    id=request.session['LOGIN_id']
    emp_obj=staff.objects.get(LOGIN_id=id)
    if request.method == 'POST':
        return render(request, "service employee/SERVICE EMPLOYEE EDIT PROFILE.html", {'data': emp_obj})
    return render(request, "service employee/SERVICE EMPLOYEE VIEW PROFILE.html", {'data':emp_obj})

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
    if res.exists():
        pass
    else:
        text = "<script>alert('No data on such area name');window.location='/myapp/semp_view_service_area/';</script>"
        return HttpResponse(text)
    return render(request,"service employee/SERVICE EMPLOYEE VIEW SERVICE AREA.html",{'res': res})


def admin_index(request):
    return render(request,"admin/admin_index.html")


def and_user_login(request):
    if request.method=="POST":
        uname = request.POST['uname']
        pword = request.POST['passw']


        if login.objects.filter(username=uname,password=pword).exists():
            yy=login.objects.get(username=uname,password=pword)
            print(yy)
            if yy.utype == "user":
                data = {"status": "ok","lid":yy.id}
                return JsonResponse(data)
            else:
                return JsonResponse({'status':"no"})
        else:
            return JsonResponse({'status': "no"})

def and_user_signup(request):
    if request.method=="POST":
        name=request.POST['name']
        gender=request.POST['gender']
        dob=request.POST['dob']
        email=request.POST['email']
        phno=request.POST['phno']
        houseno_name=request.POST['houseno_name']
        district=request.POST['district']
        pincode=request.POST['pincode']


        image=request.POST['image']

        import base64
        imgdata = base64.b64decode(image)

        nam = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M")
        filename1 = nam + ".jpg"

        filename = 'C:\\Users\\user\\PycharmProjects\\myproject1\\media\\' + filename1
        url = '/media/' + filename1
        with open(filename, 'wb') as f:
            f.write(imgdata)

        # username=request.POST['username']
        password=request.POST['password']
        log=login(username=email,password=password,utype='user')
        log.save()
        res=user(name=name,gender=gender,dob=dob,email=email,phno=phno,houseno_name=houseno_name,district=district,pincode=pincode,image=url,LOGIN=log)
        res.save()

        return JsonResponse({'status':"ok"})


def and_user_view_service_area(request):
    res2=[]
    res=service_area.objects.all()
    for ii in res:
        ss = {'area_name': ii.area_name, 'area_locality':ii.area_locality,'area_district':ii.area_district,'id':ii.id}
        res2.append(ss)

    data = {"status": "ok", "res2": res2}
    return JsonResponse(data)


def and_user_view_media_type(request):
    res2=[]
    res=media_type.objects.all()
    for ii in res:
        ss = {'media_type_name': ii.media_type_name, 'description':ii.description,'images':ii.images,'id':ii.id}
        res2.append(ss)

    data = {"status": "ok", "res2": res2}
    return JsonResponse(data)




def and_user_view_media_provider(request):
    res2 = []
    print("hi")
    typeid=request.POST['typeid']
    res = media_provider.objects.filter(MEDIATYPE_id=typeid)
    print(res)
    print("hhh")
    for ii in res:
        ss = {'provider_name': ii.provider_name, 'address': ii.place+"\n"+ii.city+"\n"+ii.district+"\n"+ii.pincode, 'email': ii.email,'mobile': ii.phno,'image': ii.image,'id':ii.id}
        res2.append(ss)

    data = {"status": "ok", "res2": res2}
    return JsonResponse(data)




def and_user_view_charge_profile(request):
    res2 = []
    print("fgg")
    typeid=request.POST['typeid']
    print(typeid)
    media_obj=media_provider.objects.get(id=typeid)
    print(media_obj)
    res = charge_profile.objects.filter(MEDIAPROVIDER=media_obj)
    print(res)
    print("hi")
    for ii in res:
        ss = {'profilename': ii.profilename, 'charge': ii.charge}
        res2.append(ss)

    data = {"status": "ok", "res2": res2}
    return JsonResponse(data)

def and_user_change_password(request):
    if request.method=="POST":
        newpass=request.POST['newpass']
        id=request.POST['LOGIN_id']
        res=login.objects.get(id=id)
        res.password=newpass
        res.save()
        data= {"status": "ok"}
    return JsonResponse(data)

def and_user_send_complaint(request):
    print("lll")
    compl = request.POST['complaint']
    print(compl)
    print("kk")
    lid = request.POST['lid']
    logobj=login.objects.get(id=lid)
    uobj=user.objects.get(LOGIN=logobj)
    print(lid)
    print("hi")
    print("jj")
    compobj = complaint()
    compobj.complaint = compl
    compobj.reply = "pending"
    compobj.status = "pending"
    compobj.date = datetime.datetime.now()
    compobj.complaint =compl
    compobj.USER=uobj
    compobj.save()
    return JsonResponse({'status': 'ok'})



def and_user_view_complaint(request):
    print("hi")
    res2=[]
    userid=request.POST['lid']
    print(userid)
    logobj=login.objects.get(id=userid)
    useobj=user.objects.get(LOGIN=logobj)
    res=complaint.objects.filter(USER=useobj).order_by('-date')
    print(res)
    for ii in res:
        ss = {'complaint': ii.complaint, 'date':ii.date.strftime("%m/%d/%Y"),'reply':ii.reply,'status':ii.status,'id':ii.id}
        res2.append(ss)

    data = {"status": "ok", "res2": res2}
    return JsonResponse(data)



def and_user_send_feedback(request):
    print("lll")
    feed = request.POST['feedback']
    print(feed)
    print("kk")
    lid = request.POST['lid']
    logobj=login.objects.get(id=lid)
    uobj=user.objects.get(LOGIN=logobj)
    print(lid)
    print("hi")
    print("jj")
    feedobj =feedback_reviews()
    feedobj.feedback = feed
    # feedobj.status = "pending"
    feedobj.date = datetime.datetime.now()
    feedobj.feedback =feed
    feedobj.USER=uobj
    feedobj.save()
    return JsonResponse({'status': 'ok'})



def and_user_view_feedback(request):
    print("hi")
    res2=[]
    userid=request.POST['lid']
    print(userid)
    logobj=login.objects.get(id=userid)
    useobj=user.objects.get(LOGIN=logobj)
    res=feedback_reviews.objects.filter(USER=useobj).order_by('-date')
    print(res)
    for ii in res:
        ss = {'feedback': ii.feedback, 'date':ii.date.strftime("%m/%d/%Y"),'id':ii.id}
        res2.append(ss)

    data = {"status": "ok", "res2": res2}
    return JsonResponse(data)


def and_user_view_profile(request):
    res2 = []
    lid=request.POST["lid"]
    print(lid)
    ma = user.objects.get(LOGIN_id=lid)
    data = {"status": "ok", "name": ma.name,"houseno_name":ma.houseno_name,"gender":ma.gender,"dob":ma.dob,"district":ma.district,"pincode":ma.pincode,"phno":ma.phno,"image":ma.image}
    print(data)
    return JsonResponse(data)

def and_user_update_profile(request):

    if request.method=="POST":
        name=request.POST['name']
        print(name)
        gender=request.POST['gender']
        print(gender)
        dob=request.POST['dob']
        print(dob)
        houseno_name=request.POST['houseno_name']
        print(houseno_name)
        district=request.POST['district']
        print(district)
        pincode=request.POST['pincode']
        print(pincode)
        phno=request.POST['phno']
        print(phno)
        image=request.POST['image']
        print("jj")
        lid=request.POST['lid']
        print(lid)
        res = user.objects.get(LOGIN_id=lid)
        if image=="0":
            print("no image")
            res.name = name
            res.gender = gender
            res.dob = dob
            res.houseno_name = houseno_name
            res.district = district
            res.pincode = pincode
            res.phno = phno
            res.save()
        else:
            print("image")
            print("kk")
            res.name=name
            res.gender=gender
            res.dob=dob
            res.houseno_name=houseno_name
            res.district=district
            res.pincode=pincode
            res.phno=phno
            import base64
            import time, datetime

            timestr = time.strftime("%Y%m%d-%H%M%S")
            print(timestr)


            imgdata = base64.b64decode(image)

            path = "/media/" + str(timestr) + ".jpg"
            print("jjjj22")
            filename = 'C:/Users/user/PycharmProjects/myproject1/media/' + str(timestr) + ".jpg"
            with open(filename, 'wb') as f:
                f.write(imgdata)
            res.image=path
            res.save()
    data = {"status": "ok"}
    return JsonResponse(data)

def and_user_send_enquiry_adrequest(request):
    print("lll")
    content = request.POST['content']
    print(content)
    file=request.POST['filename']
    print("kk")

    import base64
    imgdata = base64.b64decode(file)

    nam = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M")
    filename1 = nam + ".pdf"

    filename = 'C:\\Users\\user\\PycharmProjects\\myproject1\\media\\' + filename1
    url = '/media/' + filename1
    with open(filename, 'wb') as f:
        f.write(imgdata)

    lid = request.POST['lid']
    logobj=login.objects.get(id=lid)
    uobj=user.objects.get(LOGIN=logobj)
    print(lid)
    print("hi")
    print("jj")
    adobj = advertisement_request()
    adobj.content= content
    adobj.date = datetime.datetime.now()
    adobj.filename=url
    adobj.status = "pending"
    adobj.USER=uobj
    adobj.save()
    return JsonResponse({'status': 'ok'})


def and_user_view_enquiry_adrequest(request):
    print("hi")
    res2=[]
    userid=request.POST['lid']
    print(userid)
    logobj=login.objects.get(id=userid)
    print(logobj)
    useobj=user.objects.get(LOGIN=logobj)
    print(useobj)
    res=advertisement_request.objects.filter(USER=useobj).order_by('-date')
    print(res)
    for ii in res:
        ss = {'content': ii.content, 'date':ii.date.strftime("%m/%d/%Y"),'filename':ii.filename,'status':ii.status,'id':ii.id}
        res2.append(ss)
        print(res2)
    data = {"status": "ok", "res2": res2}
    print(data)
    print("finish")
    return JsonResponse(data)


def and_user_view_enquiry_adrequest_del(request):
    id22=request.POST['eid']
    res = advertisement_request.objects.get(id=id22)
    res.delete()
    data = {"status": "ok"}
    print(data)
    print("finish")
    return JsonResponse(data)
