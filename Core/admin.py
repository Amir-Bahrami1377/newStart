from django.contrib import admin
from .models import Organization, Patient, Image
from django import forms


class PatientForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PatientForm, self).__init__(*args, **kwargs)
#        self.fields['name'].verbose_name = 'نام'

    class Meta:
        model = Patient
        exclude = ('',)


class PatientFormAdmin(admin.ModelAdmin):
    form = PatientForm
    list_display = ['id', 'name', 'get_organization', 'file_number']
    list_filter = ['organization']
    search_fields = ['national_id']

    @admin.display()
    def get_organization(self, obj):
        return obj.organization.name


admin.site.register(Patient, PatientFormAdmin)


class OrganizationFormAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


admin.site.register(Organization, OrganizationFormAdmin)


class ImageFormAdmin(admin.ModelAdmin):
    list_display = ['get_patient', 'image', 'date_uploaded']
    search_fields = ['get_patient']

    @admin.display()
    def get_patient(self, obj):
        return obj.patient_national_id.national_id


#admin.site.register(Image, ImageFormAdmin)
