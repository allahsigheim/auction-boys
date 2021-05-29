
from django.db import models
from home.models import Agent
from django.contrib.auth.models import User
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

class Apartment(models.Model):
    living_rooms = models.IntegerField(null=True)
    bedrooms = models.IntegerField(null=True)
    bath_rooms = models.IntegerField(null=True)
    garages = models.IntegerField(null=True)
    under_roof_sqm = models.IntegerField(null=True)
    rates_taxes = models.IntegerField(null=True)
    levis = models.IntegerField(null=True)
    carport = models.IntegerField(null=True)
    security = models.CharField(max_length=100, null=True)
    laundry= models.CharField( 
        max_length = 20, 
        choices = YES_NO_CHOICES, 
        null=True,
        ) 
    outside_space = models.CharField( 
        max_length = 20, 
        choices = OUTSIDE_SPACE_CHOICES, 
        null=True,
        ) 
    view = models.CharField(max_length=100, blank=True, null=True)
    pool = models.CharField( 
        max_length = 20, 
        choices = YES_NO_CHOICES, 
        default = 'No',
        null=True,
        ) 
    fibre = models.CharField( 
        max_length = 20, 
        choices = YES_NO_CHOICES, 
        blank=True, null=True,
        ) 
    auction_date = models.DateTimeField(null=True)
    province = models.CharField( 
        max_length = 20, 
        choices = PROVINCE_CHOICES, 
        null=True,
        ) 
    town_or_city = models.CharField(max_length=100, null=True)
    agent_name = models.CharField(max_length=50)
    agent_email = models.ForeignKey(Agent, to_field='email', on_delete=models.CASCADE)
    main_image = models.ImageField(upload_to='images/')
    start_price = models.DecimalField(max_digits=12, decimal_places=2)
    street_address = models.CharField(max_length=100, null=True)
    property_type = models.CharField(max_length=120, null=True)

    def __str__(self):
        return f"{self.town_or_city}, {self.province} {self.bedrooms} bedroom by {self.agent_name}"

    class Meta:
        ordering = ('auction_date',)

    def class_name(self):
        return f"{self.__class__.__name__}"


class Extra_Images_Apartment(models.Model):
    img = models.ImageField(upload_to='images/')
    apartment = models.ForeignKey("Apartment", verbose_name="Apartment",  on_delete=models.CASCADE)

class Apartment_Bid(models.Model):
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.amount}"
