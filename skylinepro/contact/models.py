from django.db import models

# Create your models here.
# db to save records
class ContactForm(models.Model):
    name =models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.CharField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

#to enble the record to display in string format
    def __str__(self):
        #return self.name
        return f"{self.name} - {self.phone}"