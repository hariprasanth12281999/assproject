from django.db import models

# Create your models here.
class Request(models.Model):
    customer_name = models.CharField(max_length=100)
    customer_email = models.EmailField()
    customer_code = models.CharField(max_length=100)
    customer_number = models.CharField(max_length=100)
    sales_contact = models.CharField(max_length=100, blank=True, null=True)
    customer_comment = models.TextField(blank=True, null=True)
    source_email = models.FileField(upload_to='documents/')
    reference_code = models.CharField(max_length=100)
    request_type = models.CharField(max_length=50)
    request_id = models.CharField(max_length=100)  # corrected placement
    request_status = models.CharField(max_length=50)
    total_parts_count = models.PositiveIntegerField(default=0)
    matched_parts_count = models.PositiveIntegerField(default=0)
    unmatched_parts_count = models.PositiveIntegerField(default=0)

class TotalParts(models.Model):
    requestid_requesttype = models.CharField(max_length=100)  # Stores combined ID and type
    description = models.TextField()
    cpn = models.CharField(max_length=100)
    mpn = models.CharField(max_length=100, blank=True, null=True)


class MatchedParts(models.Model):
    requestid_requesttype = models.CharField(max_length=100)
    cpn = models.CharField(max_length=100)
    mpn = models.CharField(max_length=100)
    mfr = models.CharField(max_length=100)


class UnmatchedParts(models.Model):
    requestid_requesttype = models.CharField(max_length=100)
    cpn = models.CharField(max_length=100)
    mpn = models.CharField(max_length=100, blank=True, null=True)
    mfr = models.CharField(max_length=100, blank=True, null=True)