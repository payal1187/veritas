from django.db import models

# Customer  Model
class Customer(models.Model):

    objects = None
    customer_no = models.CharField(null=True, blank=True, max_length=100)
    parent_id = models.IntegerField(null=True, blank=True)
    customer_type = models.CharField(null=True, blank=True, max_length=20 )
    title = models.CharField(null=True, blank=True, max_length=50)
    name = models.CharField(null=True, blank=True, max_length=100)
    surname = models.CharField(null=True, blank=True, max_length=100)
    birth_date = models.DateField(null=True, blank=True)
    client_vat = models.CharField(null=True, blank=True, max_length=20)
    passport_no = models.CharField(null=True, blank=True, max_length=20)
    iban_no = models.CharField(null=True, blank=True, max_length=50)
    contact_1 = models.CharField(null=True, blank=True, max_length=15)
    contact_2 = models.CharField(null=True, blank=True, max_length=15)
    email = models.EmailField(null=True, blank=True)
    company_name = models.CharField(null=True, blank=True, max_length=160)
    activity_area = models.CharField(null=True, blank=True, max_length=200)
    company_vat = models.CharField(null=True, blank=True, max_length=20)
    language = models.CharField(null=True, blank=True, max_length=20)
    internal_observations = models.TextField(null=True, blank=True)
    is_subscribed_to_newsletter = models.BooleanField(default=False)
    is_subscribed_to_catalog = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_buyer = models.BooleanField(default=False)
    is_seller = models.BooleanField(default=False)
    is_received_text = models.BooleanField(default=False)
    is_email_verified = models.BooleanField(default=False)
    old_password = models.CharField(null=True, blank=True, max_length=200)
    password = models.CharField(null=True, blank=True, max_length=200)
    token = models.TextField(null=True, blank=True)
    password2 = models.CharField(null=True, blank=True, max_length=200)

    def __str__(self):
        return str(self.customer_no) + ' - id - ' + str(self.id)

    class Meta:
        db_table = "customers"



