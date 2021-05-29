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
class Townhouse(models.Model):
    living_rooms = models.IntegerField(null=False)
    bedrooms = models.IntegerField(null=False)
    bath_rooms = models.IntegerField(null=False)
    garages = models.IntegerField(null=False)
    under_roof_sqm = models.IntegerField(null=False)
    rates_taxes = models.IntegerField(null=False)
    levis = models.IntegerField(null=False)
    carport = models.IntegerField(null=False)
    security = models.CharField(max_length=100, null=False)
    yard_space = models.CharField( 
        max_length = 20, 
        choices = YES_NO_CHOICES, 
        null=False,
        ) 
    laundry = models.CharField( 
        max_length = 20, 
        choices = YES_NO_CHOICES, 
        null=False,
        ) 
    pool = models.CharField( 
        max_length = 20, 
        choices = YES_NO_CHOICES, 
        default = 'No',
        null=False,
        ) 
    fibre = models.CharField( 
        max_length = 20, 
        choices = YES_NO_CHOICES, 
        blank=True, null=True,
        ) 
    full_or_sectional = models.CharField( 
        max_length = 100, 
        choices = FULL_OR_SECTIONAL_CHOICES, 
        default = 'Full Title Town House',
        null=False,
        ) 
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


    def __str__(self):
        return f"{self.town_or_city}, {self.province} {self.bedrooms} bedroom by {self.agent_name}"

    class Meta:
        ordering = ('auction_date',)

    def class_name(self):
            return f"{self.__class__.__name__}"


class Extra_Images_Townhouse(models.Model):
    img = models.ImageField(upload_to='images/')
    townhouse = models.ForeignKey("Townhouse", verbose_name="Townhouse",  on_delete=models.CASCADE)

