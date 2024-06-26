from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class Category(models.Model):
     name = models.CharField(max_length=200)
     
     class Meta:
         db_table = 'tbl_category'
     def __str__(self) :
          return super.name
      
      
class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10,decimal_places=2)
    image = CloudinaryField('image', default='')
    category = models.ForeignKey(Category,
                                 related_name='products',
                                 on_delete=models.RESTRICT)
    class Meta:
        db_table= 'tbl_product'
    
    def __str__(self):
         return self.name