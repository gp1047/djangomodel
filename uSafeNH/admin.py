from django.contrib import admin
from uSafeNH.models import college
from uSafeNH.models import campusLiaison
from uSafeNH.models import campus
from uSafeNH.models import titleIX
from uSafeNH.models import campusSafety
from uSafeNH.models import specialized
from uSafeNH.models import campusCounselingCenter
from uSafeNH.models import hospital
from uSafeNH.models import police
from uSafeNH.models import crisisCenter
from uSafeNH.models import campusCounsel
from uSafeNH.models import campusHospital
from uSafeNH.models import campusPolice
from uSafeNH.models import campusCrisis



# Register your models here.
class CollegeAdmin(admin.ModelAdmin):
    model = college
    list_display = ('collegeID','collegeName', 'collegeAddressNumber', 'collegeAddressStreetName', 'collegeAddressMoreInfo','collegeCity','collegeZipcode')

class CampusLiaisonAdmin(admin.ModelAdmin):
    model = campusLiaison
    list_display = ('campusLiaisonID','collegeID', 'username', 'password', 'campusLiaisonEmail','campusLiaisonFirstName','campusLiaisonLastName')

class CampusAdmin(admin.ModelAdmin):
    model = campus
    list_display = ('campusID','collegeID', 'campusName', 'campusAddressNumber', 'campusAddressStreetName','campusAddressMoreInfo','campusCity','campusZipcode')

class TitleIXAdmin(admin.ModelAdmin):
    model = titleIX
    list_display = ('titleIXID','collegeID','titleIXName', 'titleIXAddressNumber', 'titleIXAddressStreetName', 'titleIXAddressMoreInfo','titleIXPhone','titleIXPhoneType','titleIXPhoneExtension','titleIXEmailName','titleIXEmail',)

class CampusSafetyAdmin(admin.ModelAdmin):
    model = campusSafety
    list_display = ('campusSafetyID','campusSafetyName', 'campusSafetyIsOnCampus', 'campusSafetyAddressNumber', 'campusSafetyAddressStreetName','campusSafetyAddressMoreInfo','campusSafetyCity','campusSafetyZipcode','campusSafetyPhone','campusSafetyPhoneType','campusSafetyPhoneExtension','campusSafetyWebsite','campusSafetyReportOnlineURL','campusSafetyReportOnlineType',)

class SpecializedAdmin(admin.ModelAdmin):
    model = specialized
    list_display = ('specializedID','campusID','specializedName', 'specializedAddressNumber', 'specializedAddressStreetName', 'specializedAddressMoreInfo','specializedCity','specializedZipcdoe','specializedPhone','specializedPhoneType','specializedPhoneExtension','specializedEmailName','specializedEmail',)

class CampusCounselingCenterAdmin(admin.ModelAdmin):
    model = campusCounselingCenter
    list_display = ('cccID','cccName', 'cccConfidential', 'cccHours', 'cccAddressNumber','cccAddressStreetName','cccAddressMoreInfo','cccCity','cccZipcode','cccPhone','cccPhoneType','cccPhoneExtension','cccEmail','cccEmailName','cccWebsite',)

class HospitalAdmin(admin.ModelAdmin):
    model = hospital
    list_display = ('hospitalID','hospitalName', 'hospitalAddressNumber', 'hospitalAddressStreetName', 'hospitalAddressMoreInfo','hospitalCity','hospitalZipcdoe','hospitalPhone','hospitalPhoneType','hospitalPhoneExtension','hospitalLogo',)

class PoliceAdmin(admin.ModelAdmin):
    model = police
    list_display = ('policeID','policeName', 'policeCampus', 'policeAddressNumber', 'policeAddressStreetName','policeAddressMoreInfo','policeCity','policeZipcdoe','policePhone','policePhoneType','policePhoneExtension',)

class CrisisCenterAdmin(admin.ModelAdmin):
    model = crisisCenter
    list_display = ('ccID','ccName', 'ccIsOnCampus', 'ccAddressNumber', 'ccAddressStreetName','ccAddressMoreInfo','ccCity','ccZipcdoe','ccPhone','ccPhoneType','ccPhoneExtension','ccWebsite','ccLogo',)

class CampusCounselAdmin(admin.ModelAdmin):
    model = campusCounsel
    list_display = ('campusID','cccID',)

class CampusHospitalAdmin(admin.ModelAdmin):
    model = campusHospital
    list_display = ('campusID','hospitalID',)

class CampusPoliceAdmin(admin.ModelAdmin):
    model = campusPolice
    list_display = ('campusID','policeID',)

class CampusCrisisAdmin(admin.ModelAdmin):
    model = campusCrisis
    list_display = ('campusID','ccID',)

# and register it
admin.site.register(college, CollegeAdmin)
admin.site.register(campusLiaison, CampusLiaisonAdmin)
admin.site.register(campus, CampusAdmin)
admin.site.register(titleIX, TitleIXAdmin)
admin.site.register(campusSafety, CampusSafetyAdmin)
admin.site.register(specialized, SpecializedAdmin)
admin.site.register(campusCounselingCenter, CampusCounselingCenterAdmin)
admin.site.register(hospital, HospitalAdmin)
admin.site.register(police, PoliceAdmin)
admin.site.register(crisisCenter, CrisisCenterAdmin)
admin.site.register(campusCounsel, CampusCounselAdmin)
admin.site.register(campusHospital, CampusHospitalAdmin)
admin.site.register(campusPolice, CampusPoliceAdmin)
admin.site.register(campusCrisis, CampusCrisisAdmin)
