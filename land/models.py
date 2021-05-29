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

class Land(models.Model):
    zoning = models.CharField( 
        max_length = 20, 
        choices = ZONING_CHOICES, 
        default = 'Industrial',
        null=False,
        ) 
    services = models.CharField( 
        max_length = 20, 
        choices = YES_NO_CHOICES, 
        default = 'No',
        null=False,
        ) 
    land_sqm = models.IntegerField(null=False)
    rates_taxes = models.IntegerField(null=False)
    auction_date = models.DateTimeField(null=False)
    province = models.CharField( 
        max_length = 20, 
        choices = PROVINCE_CHOICES, 
        null=False,
        ) 
    town_or_city = models.CharField(max_length=100, null=False)
    agent_name = models.CharField(max_length=50)
    agent_email = models.ForeignKey(Agent, to_field='email', on_delete=models.CASCADE)
    main_image = models.ImageField(upload_to='images/', null=True)
    start_price = models.DecimalField(max_digits=12, decimal_places=2)
    street_address = models.CharField(max_length=100, null=False)


    def __str__(self):
        return f"{self.town_or_city}, {self.province} Land by {self.agent_name}"

    def class_name(self):
            return f"{self.__class__.__name__}"

    class Meta:
        verbose_name_plural = "Land"
        ordering = ('auction_date',)

    
class Extra_Images_Land(models.Model):
    img = models.ImageField(upload_to='images/')
    land = models.ForeignKey("Land", verbose_name="Land",  on_delete=models.CASCADE)
