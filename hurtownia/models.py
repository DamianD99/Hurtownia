from datetime import timezone
from django.urls import reverse
from django.db import models
from django.contrib.auth.models import User

CATEGORY = (
    ('nie', 'nie'),
    ('tak', 'tak'),
    ('całkowicie zepsute', 'całkowicie zepsute'),
)

class Produkty(models.Model):
    nazwa = models.CharField(max_length=200, null=True)
    kategoria = models.CharField(max_length=20, null=True)
    uszkodzony = models.CharField(max_length=50, choices=CATEGORY, null=True)
    ilosc = models.PositiveIntegerField(null=True)
    cena = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    available =models.BooleanField(default=True)
    slug = models.SlugField(max_length=200, db_index=True, null=True)
    image = models.ImageField(null=True, blank=True)

    class Meta:
        ordering = ('nazwa',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.nazwa

    def get_absolute_url(self):
        return reverse('pokaz_produkt',
                       args=[self.id, self.slug])

class Zamówienia(models.Model):

    STATUS = (
        ('Pending', 'Pending'),
        ('Out for delivery', 'Out for delivery'),
        ('Delivered', 'Delivered'),
    )
    produkt = models.ForeignKey(Produkty, null=True, on_delete=models.CASCADE)
    klijent = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)
def __str__(self):
    return self.produkt.nazwa

class Feedback(models.Model):
    name = models.CharField(max_length=200, help_text="Name of the sender")
    email = models.EmailField(max_length=200)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Feedback"

    def __str__(self):
        return self.name + "-" +  self.email

class Zwrot(models.Model):

    nr_zwrotu = models.CharField(max_length=30, null=True)
    klijent = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    produkt = models.ForeignKey(Produkty, null=True, on_delete=models.CASCADE)
    przyczyna = models.CharField(max_length=30, null=True)
    data = models.DateTimeField(auto_now_add=True)