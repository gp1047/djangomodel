from django.db import models
from uuid import uuid4


def generateUUID():
    return str(uuid4())

# Create your models here.
class college(models.Model):
    collegeID = models.CharField(default=generateUUID, primary_key=True, max_length=36, unique=True, editable=False)
    collegeName = models.CharField(max_length=50)
    collegeAddressNumber = models.CharField(max_length=50)
    collegeAddressStreetName = models.CharField(max_length=50)
    collegeAddressMoreInfo = models.CharField(max_length=50)
    collegeCity = models.CharField(max_length=50)
    collegeZipcode = models.CharField(max_length=50)

    def __str__(self):
        return self.collegeName

class campusLiaison(models.Model):
    campusLiaisonID = models.CharField(default=generateUUID, primary_key=True, max_length=36, unique=True, editable=False)
    collegeID = models.ForeignKey(college)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    campusLiaisonEmail = models.CharField(max_length=50)
    campusLiaisonFirstName = models.CharField(max_length=50)
    campusLiaisonLastName = models.CharField(max_length=50)

    def __str__(self):
        return self.username

class campus(models.Model):
    campusID = models.CharField(default=generateUUID, primary_key=True, max_length=36, unique=True, editable=False)
    collegeID = models.ForeignKey(college)
    campusName = models.CharField(max_length=50)
    campusAddressNumber = models.CharField(max_length=50)
    campusAddressStreetName = models.CharField(max_length=50)
    campusAddressMoreInfo = models.CharField(max_length=50)
    campusCity = models.CharField(max_length=50)
    campusZipcode = models.CharField(max_length=50)

    def __str__(self):
        return self.campusName

class titleIX(models.Model):
    titleIXID = models.CharField(default=generateUUID, primary_key=True, max_length=36, unique=True, editable=False)
    collegeID = models.ForeignKey(college)
    titleIXName = models.CharField(max_length=50)
    titleIXAddressNumber = models.CharField(max_length=50)
    titleIXAddressStreetName = models.CharField(max_length=50)
    titleIXAddressMoreInfo = models.CharField(max_length=50)
    titleIXPhone = models.CharField(max_length=50)
    titleIXPhoneType = models.CharField(max_length=50)
    titleIXPhoneExtension = models.CharField(max_length=50)
    titleIXEmailName = models.CharField(max_length=50)
    titleIXEmail = models.CharField(max_length=50)

    def __str__(self):
        return self.titleIXName

class campusSafety(models.Model):
    campusSafetyID = models.CharField(default=generateUUID, primary_key=True, max_length=36, unique=True, editable=False)
    campusSafetyName = models.CharField(max_length=50)
    campusSafetyIsOnCampus = models.CharField(max_length=50)
    campusSafetyAddressNumber = models.CharField(max_length=50)
    campusSafetyAddressStreetName = models.CharField(max_length=50)
    campusSafetyAddressMoreInfo = models.CharField(max_length=50)
    campusSafetyCity = models.CharField(max_length=50)
    campusSafetyZipcode = models.CharField(max_length=50)
    campusSafetyPhone = models.CharField(max_length=50)
    campusSafetyPhoneType = models.CharField(max_length=50)
    campusSafetyPhoneExtension = models.CharField(max_length=50)
    campusSafetyWebsite = models.CharField(max_length=50)
    campusSafetyReportOnlineURL = models.CharField(max_length=50)
    campusSafetyReportOnlineType = models.CharField(max_length=50)

    def __str__(self):
        return self.campusSafetyName

class specialized(models.Model):
    specializedID = models.CharField(default=generateUUID, primary_key=True, max_length=36, unique=True, editable=False)
    campusID = models.ForeignKey(campus)
    specializedName = models.CharField(max_length=50)
    specializedAddressNumber = models.CharField(max_length=50)
    specializedAddressStreetName = models.CharField(max_length=50)
    specializedAddressMoreInfo = models.CharField(max_length=50)
    specializedCity = models.CharField(max_length=50)
    specializedZipcdoe = models.CharField(max_length=50)
    specializedPhone = models.CharField(max_length=50)
    specializedPhoneType = models.CharField(max_length=50)
    specializedPhoneExtension = models.CharField(max_length=50)
    specializedEmailName = models.CharField(max_length=50)
    specializedEmail = models.CharField(max_length=50)

    def __str__(self):
        return self.specializedName

class campusCounselingCenter(models.Model):
    cccID = models.CharField(default=generateUUID, primary_key=True, max_length=36, unique=True, editable=False)
    cccName = models.CharField(max_length=50)
    cccConfidential = models.CharField(max_length=50)
    cccHours = models.CharField(max_length=50)
    cccAddressNumber = models.CharField(max_length=50)
    cccAddressStreetName = models.CharField(max_length=50)
    cccAddressMoreInfo = models.CharField(max_length=50)
    cccCity = models.CharField(max_length=50)
    cccZipcode = models.CharField(max_length=50)
    cccPhone = models.CharField(max_length=50)
    cccPhoneType = models.CharField(max_length=50)
    cccPhoneExtension = models.CharField(max_length=50)
    cccEmail = models.CharField(max_length=50)
    cccEmailName = models.CharField(max_length=50)
    cccWebsite = models.CharField(max_length=50)

    def __str__(self):
        return self.cccName

class hospital(models.Model):
    hospitalID = models.CharField(default=generateUUID, primary_key=True, max_length=36, unique=True, editable=False)
    hospitalName = models.CharField(max_length=50)
    hospitalAddressNumber = models.CharField(max_length=50)
    hospitalAddressStreetName = models.CharField(max_length=50)
    hospitalAddressMoreInfo = models.CharField(max_length=50)
    hospitalCity = models.CharField(max_length=50)
    hospitalZipcdoe = models.CharField(max_length=50)
    hospitalPhone = models.CharField(max_length=50)
    hospitalPhoneType = models.CharField(max_length=50)
    hospitalPhoneExtension = models.CharField(max_length=50)
    hospitalLogo = models.CharField(max_length=50)

    def __str__(self):
        return self.hospitalName

class police(models.Model):
    policeID = models.CharField(default=generateUUID, primary_key=True, max_length=36, unique=True, editable=False)
    policeName = models.CharField(max_length=50)
    policeCampus = models.CharField(max_length=50)
    policeAddressNumber = models.CharField(max_length=50)
    policeAddressStreetName = models.CharField(max_length=50)
    policeAddressMoreInfo = models.CharField(max_length=50)
    policeCity = models.CharField(max_length=50)
    policeZipcdoe = models.CharField(max_length=50)
    policePhone = models.CharField(max_length=50)
    policePhoneType = models.CharField(max_length=50)
    policePhoneExtension = models.CharField(max_length=50)

    def __str__(self):
        return self.policeName

class crisisCenter(models.Model):
    ccID = models.CharField(default=generateUUID, primary_key=True, max_length=36, unique=True, editable=False)
    ccName = models.CharField(max_length=50)
    ccIsOnCampus = models.CharField(max_length=50)
    ccAddressNumber = models.CharField(max_length=50)
    ccAddressStreetName = models.CharField(max_length=50)
    ccAddressMoreInfo = models.CharField(max_length=50)
    ccCity = models.CharField(max_length=50)
    ccZipcdoe = models.CharField(max_length=50)
    ccPhone = models.CharField(max_length=50)
    ccPhoneType = models.CharField(max_length=50)
    ccPhoneExtension = models.CharField(max_length=50)
    ccWebsite = models.CharField(max_length=50)
    ccLogo = models.CharField(max_length=50)

    def __str__(self):
        return self.ccName

class campusCounsel(models.Model):
    campusID = models.ForeignKey(campus)
    cccID = models.ForeignKey(campusCounselingCenter)

class campusHospital(models.Model):
    campusID = models.ForeignKey(campus)
    hospitalID = models.ForeignKey(hospital)

class campusPolice(models.Model):
    campusID = models.ForeignKey(campus)
    policeID = models.ForeignKey(police)

class campusCrisis(models.Model):
    campusID = models.ForeignKey(campus)
    ccID = models.ForeignKey(crisisCenter)
