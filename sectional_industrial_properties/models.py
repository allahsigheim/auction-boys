from django.db import models
from home.models import Agent
# Create your models here.

PROVINCE_CHOICES = (
    ("Eastern Cape", "Eastern Cape"), 
    ("Freestate", "Freestate"),
    ("Gauteng", "Gauteng"),
    ("Kwazulu-Natal", "Kwazulu-Natal"),
    ("Limpopo", "Limpopo"), 
    ("Mpumulanga", "Mpumulanga"),
    ("North West", "North West"),
    ("Northen Cape", "Northen Cape"),  
    ("Western Cape", "Western Cape"), 
)
OUTBUILDING_CHOICES = (
    ("Store room", "Store room"),   
    ("Workshop", "Workshop"),
    ("Flatlet", "Flatlet"),
    ("None", "None"),
)
OUTSIDE_SPACE_CHOICES = (
    ("Balcony", "Balcony"), 
    ("Garden", "Garden"),
    ("None", "None"),
    )

FULL_OR_SECTIONAL_CHOICES = (
    ("Full Title Town House", "Full Title Town House"), 
    ("Sectional Title Town House", "Sectional Title Town House"),
)

BUSINESS_RETAIL_CHOICES = (
    ("Business", "Business"), 
    ("Retail", "Retail"),
)
FLOOR_CHOICES = ( 
    ("Heavy Industrial", "Heavy Industrial"), 
    ("Light Industria", "Light Industrial"),
) 
YES_NO_CHOICES = (
    ("Yes", "Yes"), 
    ("No", "No"),
)
ZONING_CHOICES = ( 
    ("Residential 1", "Residential 1"), 
    ("Residential 2", "Residential 2"),
    ("Residential 3", "Residential 3"), 
    ("Commercial-Business", "Commercial-Business"),
    ("Commercial-Retail", "Commercial-Retail"),
    ("Industrial", "Industrial"),
    ("Agriculture", "Agriculture"),
    ("Residential", "Residential"),
) 

class Sectional_Industrial_Property(models.Model):
    amps = models.IntegerField(null=False)
    generator = models.CharField( 
        max_length = 20, 
        choices = YES_NO_CHOICES, 
        default = 'No',
        null=False,
        ) 
    backup_water = models.CharField( 
        max_length = 20, 
        choices = YES_NO_CHOICES, 
        blank=True, null=True,
        ) 
    under_roof_sqm = models.IntegerField(null=False)
    yard_space_sqm = models.IntegerField(null=False)
    rates_taxes = models.IntegerField(null=False)
    levis = models.IntegerField(null=False)
    parking_bays = models.IntegerField(null=False, default=0)
    offices = models.IntegerField(null=False)
    kitchens = models.IntegerField(null=False)
    bathrooms = models.IntegerField(null=False)
    security = models.CharField(max_length=100, null=False)
    auction_date = models.DateTimeField(null=False)
    province = models.CharField( 
        max_length = 20, 
        choices = PROVINCE_CHOICES, 
        null=False,
        ) 
    town_or_city = models.CharField(max_length=100, null=False)
    agent_name = models.CharField(max_length=50)
    agent_email = models.ForeignKey(Agent, to_field='email', on_delete=models.CASCADE)
    main_image = models.ImageField(upload_to='images/')
    start_price = models.DecimalField(max_digits=12, decimal_places=2)
    street_address = models.CharField(max_length=100, null=False)


    class Meta:
        ordering = ('auction_date',)

class Extra_Images_Sectional_Industrial_Property(models.Model):
    img = models.ImageField(upload_to='images/')
    sectional_industrial_property = models.ForeignKey("Sectional_Industrial_Property", verbose_name="Sectional_Industrial_Property",  on_delete=models.CASCADE)
