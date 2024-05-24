from django.db import models


class Organization(models.Model):
    name = models.CharField(max_length=200, verbose_name="نام محل ثبت")

    def __str__(self):
        return self.name


class Patient (models.Model):
    name = models.CharField(max_length=200, verbose_name="نام بیمار")
    phone_number = models.CharField(max_length=11, verbose_name="تلفن")
    national_id = models.IntegerField(null=False, unique=True, verbose_name="کد ملی")
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, verbose_name="محل ثبت")
    file_number = models.BigIntegerField(null=False, verbose_name="شماره پرونده مرکز")
    date_created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Image (models.Model):
    patient_national_id = models.ForeignKey(Patient, on_delete=models.CASCADE, verbose_name="تصاویر پرونده")
    image = models.ImageField(upload_to='uploads/% Y/% m/% d/', verbose_name="تصویر")
    date_uploaded = models.DateTimeField(auto_now_add=True)

