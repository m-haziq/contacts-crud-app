from django.db import models


class Contact(models.Model):
    person_name = models.CharField(max_length=50, null=False, blank=False)
    contact_name = models.EmailField(null=False, blank=False)
    contact_gst_number = models.CharField(max_length=20, null=False, blank=False)
