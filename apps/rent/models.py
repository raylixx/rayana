from django.db import models

class Landlord(models.Model):
    name = models.CharField(
        max_length=50
    )
    surname = models.CharField(
        max_length=50,
        null=True,
        blank=True

    )
    album_count= models.PositiveIntegerField(
        default=0,
    )
    image = models.PositiveIntegerField(
        upload_to='landlords',
    )
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} {self.surname}"

    class Meta:
        verbose_name= 'Landlord'
        verbose_name_plural = 'Landlords'

class Apartment(models.Model):
        landlord = models.ForeingKey(Landlord, on_delete=models.CASCADE)
        name = models.CharField(max_length=250)
        apartment_image = models.ImageField(upload_to='apartments/image')
        file = models.FileField(upload_to='apartments')
        created_at= models.DateTimeField(auto_now_add=True)
        updated_at= models.DateTimeField(auto_now=True)

        def __str__(self):
            return self.name


        class Meta:
            verbose_name = 'Apartment'
            verbose_name_plural= 'Apartments'