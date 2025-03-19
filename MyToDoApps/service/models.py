from django.db import models

class Property(models.Model):
    PROPERTY_TYPES = [
        ('House', 'House'),
        ('Flat', 'Flat'),
        ('Plot', 'Plot'),
        ('Commercial', 'Commercial Space'),
    ]

    FURNISHING_TYPES = [
        ('Furnished', 'Furnished'),
        ('Semi-Furnished', 'Semi-Furnished'),
        ('Unfurnished', 'Unfurnished'),
    ]

    AVAILABILITY = [
        ('Immediate', 'Immediate'),
        ('Within 1 Month', 'Within 1 Month'),
        ('Within 3 Months', 'Within 3 Months'),
        ('After 3 Months', 'After 3 Months'),
    ]

    title = models.CharField(max_length=100)
    description = models.TextField()
    property_type = models.CharField(max_length=20, choices=PROPERTY_TYPES)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    area = models.FloatField()
    furnishing = models.CharField(max_length=20, choices=FURNISHING_TYPES, default='Unfurnished')
    availability = models.CharField(max_length=20, choices=AVAILABILITY, default='Immediate')
    images = models.ImageField(upload_to='image/', null=True, blank=True)
    contact_name = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=15)
    email = models.EmailField()
    posted_date = models.DateTimeField(auto_now_add=True)





