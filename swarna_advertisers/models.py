from django.db import models

# Create your models here.
class login(models.Model):
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    utype=models.CharField(max_length=50)

class user(models.Model):
    name=models.CharField(max_length=50)
    gender=models.CharField(max_length=50)
    dob=models.DateField(max_length=50)
    email=models.CharField(max_length=50)
    phno=models.CharField(max_length=50)
    houseno_name=models.CharField(max_length=50)
    district=models.CharField(max_length=50)
    pincode=models.CharField(max_length=50)
    image=models.CharField(max_length=300)
    LOGIN=models.ForeignKey(login,on_delete=models.CASCADE)


class staff(models.Model):
    name=models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    dob = models.DateField(max_length=50)
    email= models.CharField(max_length=50)
    phno = models.CharField(max_length=50)
    houseno_name = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    pincode = models.CharField(max_length=50)
    image = models.CharField(max_length=300)
    LOGIN = models.ForeignKey(login, on_delete=models.CASCADE)

class service_area(models.Model):
    area_name=models.CharField(max_length=50)
    area_locality=models.CharField(max_length=50)
    area_district=models.CharField(max_length=50)

class employee_area(models.Model):
    STAFF=models.ForeignKey(staff, on_delete=models.CASCADE)
    SERVICEAREA=models.ForeignKey(service_area, on_delete=models.CASCADE)

class media_type(models.Model):
    media_type_name=models.CharField(max_length=50)
    description=models.CharField(max_length=200)


class media_provider(models.Model):
    provider_name=models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phno = models.CharField(max_length=50)
    place = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    pincode = models.CharField(max_length=50)
    image = models.CharField(max_length=300)
    MEDIATYPE=models.ForeignKey(media_type, on_delete=models.CASCADE)

class charge_profile(models.Model):
    charge=models.CharField(max_length=50)
    profilename=models.CharField(max_length=50)
    MEDIATYPE = models.ForeignKey(media_type, on_delete=models.CASCADE)
    MEDIAPROVIDER= models.ForeignKey(media_provider, on_delete=models.CASCADE)


class advertisement_request(models.Model):
    content=models.CharField(max_length=300)
    date=models.DateField(max_length=50)
    status=models.CharField(max_length=50)
    filename = models.CharField(max_length=300)
    USER=models.ForeignKey(user, on_delete=models.CASCADE)

class monthly_settlement(models.Model):
    year=models.CharField(max_length=50)
    month=models.CharField(max_length=50)
    date = models.DateField(max_length=50)
    amount=models.CharField(max_length=50)
    MEDIAPROVIDER = models.ForeignKey(media_provider, on_delete=models.CASCADE)

class request_public(models.Model):
    provider_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    dob = models.DateField(max_length=50)
    emailid = models.CharField(max_length=50)
    phno = models.CharField(max_length=50)
    houseno_name = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    pincode = models.CharField(max_length=50)
    image = models.CharField(max_length=300)


class complaint(models.Model):
    complaint= models.CharField(max_length=200)
    date = models.DateField(max_length=50)
    reply=models.CharField(max_length=200)
    status = models.CharField(max_length=50)
    USER = models.ForeignKey(user, on_delete=models.CASCADE)


class feedback_reviews(models.Model):
    feedback=models.CharField(max_length=200)
    date = models.DateField(max_length=50)
    USER = models.ForeignKey(user, on_delete=models.CASCADE)


class media(models.Model):
     media_title=models.CharField(max_length=50)
     filename = models.CharField(max_length=200)
     description = models.CharField(max_length=200)
     date = models.DateField(max_length=50)
     path=models.CharField(max_length=200)
     ADVERTISEMENTREQUEST=models.ForeignKey(advertisement_request, on_delete=models.CASCADE)

class installation(models.Model):
    date = models.DateField(max_length=50)
    narration=models.CharField(max_length=200)
    placename=models.CharField(max_length=50)
    code=models.CharField(max_length=50)
    SERVICEAREA=models.ForeignKey(service_area, on_delete=models.CASCADE)
    STAFF=models.ForeignKey(staff, on_delete=models.CASCADE)


class expense(models.Model):
    date = models.DateField(max_length=50)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    amount=models.CharField(max_length=50)
    EMPLOYEEAREA=models.ForeignKey(employee_area, on_delete=models.CASCADE)

class maintance(models.Model):
    date = models.DateField(max_length=50)
    maintance = models.CharField(max_length=200)
    amount = models.CharField(max_length=50)
    SERVICEAREA = models.ForeignKey(service_area, on_delete=models.CASCADE)
    STAFF = models.ForeignKey(staff, on_delete=models.CASCADE)
    INSTALLATION=models.ForeignKey(installation, on_delete=models.CASCADE)








