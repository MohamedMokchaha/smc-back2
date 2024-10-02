from django.db import models

class Demande(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    city = models.CharField(max_length=50)
    parking_address = models.BooleanField()
    birth_date = models.DateField()

    # Champs pour l'objectif
    selected_option = models.CharField(max_length=50)
    moto_option = models.CharField(max_length=50, blank=True)
    annulation = models.BooleanField()
    purchase_date = models.DateField()
    project_purchase = models.BooleanField()

    # Champs pour les informations sur le véhicule
    vehicle_brand = models.CharField(max_length=50)
    engine_capacity = models.CharField(max_length=10)
    model = models.CharField(max_length=50)
    vehicle_type = models.CharField(max_length=50)
    registration_number = models.CharField(max_length=50)
    first_registration_date = models.DateField()
    acquisition_date = models.DateField(null=True, blank=True)  # Autoriser NULL

    # Champs pour le permis
    permis_a1 = models.DateField(null=True, blank=True)  # Autoriser NULL
    permis_a2 = models.DateField(null=True, blank=True)  # Autoriser NULL
    permis_a = models.DateField(null=True, blank=True)  # Autoriser NULL
    permis_b = models.DateField(null=True, blank=True)  # Autoriser NULL
    annulation_a1 = models.BooleanField()
    annulation_a2 = models.BooleanField()
    annulation_a = models.BooleanField()
    annulation_b = models.BooleanField()

    # Champs pour la confirmation
    additional_info = models.TextField(blank=True)
    comment = models.TextField(blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
