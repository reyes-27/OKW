from django.db import models

# Create your models here.

class Country(models.Model):
    country_id = models.AutoField(primary_key=True)
    country_name = models.CharField(max_length=200, null=True, blank=True)
    country_initials = models.CharField(max_length=3, null=True, blank=True)

    def __str__(self):
        return self.country_name


class State(models.Model):
    state_id = models.AutoField(primary_key=True)
    state_name = models.CharField(max_length=75, null=True, blank=True)
    state_initials = models.CharField(max_length=3, null=True, blank=True)
    state_area_code = models.CharField(max_length=50, null=True, blank=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return self.state_name


class City(models.Model):
    city_id = models.AutoField(primary_key=True)
    city_name = models.CharField(max_length=200, null=True, blank=True)
    state = models.ForeignKey(State, on_delete=models.CASCADE)

    def __str__(self):
        return self.city_name


class District(models.Model):
    district_id = models.AutoField(primary_key=True)
    district_name = models.CharField(max_length=200, null=True, blank=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    def __str__(self):
        return self.district_name


class Street(models.Model):
    street_id = models.AutoField(primary_key=True)
    street_zip_code = models.CharField(max_length=9, null=True, blank=True)
    street_type = models.CharField(max_length=20, null=True, blank=True)
    street_name = models.CharField(max_length=70, null=True, blank=True)
    district = models.ForeignKey(District, on_delete=models.CASCADE)

    def __str__(self):
        return self.street_name