from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class ChaiVaraity(models.Model):
    CHAI_TYPE_CHOICE = [
        ('ML', 'MASALA'),
        ('GR', 'GINGER'),
        ('KL', 'KIWI'),
        ('PL', 'PLAIN'),
        ('EL', 'ELACHI'),
        ('GN', 'GREEN'),
        ('BL', 'BLACK'),
        ('WH', 'WHITE'),
        ('OG', 'OOLONG'),
        ('TI', 'TISANES'),
        ('RO', 'ROOIBOS'),
        ('MA', 'MATCHA'),
        ('PU', 'PU-ERH'),
        ('YE', 'YELLOW'),
        
    ]
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='chais/')
    date_added = models.DateTimeField(default=timezone.now) 
    type = models.CharField(max_length=2,choices=CHAI_TYPE_CHOICE)
    price = models.IntegerField(default=0)
    description = models.TextField(default='')
    
    def __str__(self):
        return self.name 
    
# One to many

class ChaiRiview(models.Model):
    chai = models.ForeignKey(ChaiVaraity,on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    date_added = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f'{self.user.username} review for {self.chai.name}' 
    
    
# Many to many

class Store(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    chai_varieties = models.ManyToManyField(ChaiVaraity,related_name='stores')
    
    def __str__(self):
        return self.name
    
# One to One

class ChaiCertificate(models.Model):
    chai = models.OneToOneField(ChaiVaraity,on_delete=models.CASCADE, related_name='certificate')
    certificate_number = models.CharField(max_length=100)
    issued_date = models.DateTimeField(default=timezone.now)
    valid_until = models.DateTimeField()
    
    def __str__(self):
        return f'Certificate for {self.name.chai}'   
    
class CustomerOrder(models.Model):
    name = models.CharField(max_length=100)
    number = models.CharField(max_length=15)
    location = models.CharField(max_length=255)
    tea_name = models.CharField(max_length=100)
    tea_price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    additional_tea = models.JSONField(blank=True, null=True)  # To store additional tea details
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order by {self.name} - {self.total_price}"