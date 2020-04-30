from django.db import models
from django.urls import reverse
from datetime import date

class Patient(models.Model):
  patient_name = models.CharField("Name", max_length=200, help_text="Name of the Patient")
  patient_id = models.CharField("Patient Identity Document Number", max_length=10, help_text="Identity Document Number", null=True, blank=True)
  date_of_birth = models.DateField("Date of Birth", null=True, blank=True)
  date_case_confirmed = models.DateField("Date Case Confirmed", null=False, blank=False, default=date.today)
  case_number = models.IntegerField(
    "Case Number", 
    primary_key=True,
    null=False,
    blank=False, 
    default=0, #Patient.objects.all().count(),
    help_text="The case number of the Patient"
  )

  def __str__(self):
    return self.patient_name+" #"+str(self.case_number)

  def get_absolute_url(self):
      """Returns the url to access a particular author instance."""
      return reverse('detail', args=[str(self.case_number)])

class Location(models.Model):
  location_name = models.CharField("Location Visited", max_length=200, help_text="Name of the Location", blank=True)
  DISTRICT_CHOICES = [
    ('Hong Kong Island', (
            ('Central and Western', 'Central and Western'),
            ('Eastern', 'Eastern'),
            ('Southern', 'Southern'),
            ('Wan Chai', 'Wan Chai'),
        )
    ),
    ('Kowloon', (
            ('Sham Shui Po', 'Sham Shui Po'),
            ('Kowloon City', 'Kowloon City'),
            ('Kwun Tong', 'Kwun Tong'),
            ('Wong Tai Sin', 'Wong Tai Sin'),
            ('Yau Tsim Mong', 'Yau Tsim Mong'),
        )
    ),
    ('New Teritories', (
            ('Islands', 'Islands'),
            ('Kwai Tsing', 'Kwai Tsing'),
            ('North', 'North'),
            ('Sai Kung', 'Sai Kung'),
            ('Sha Tin', 'Sha Tin'),
            ('Tai Po', 'Tai Po'),
            ('Tsuen Wan', 'Tsuen Wan'),
            ('Tuen Mun', 'Tuen Mun'),
            ('Yuen Long', 'Yuen Long'),
        )
    ),
  ]
  district = models.CharField("District", max_length=200, choices=DISTRICT_CHOICES , help_text="District of the Location", default="Central and Western")
  address = models.CharField("Address", max_length=200, help_text="Address of the Location", blank=True, null=True)
  x_coord = models.FloatField("X Coord", help_text="X Coordiates/Longitude of the location", default=0)
  y_coord = models.FloatField("Y Coord", help_text="Y Coordiates/Latitude of the location", default=0)
  def __str__(self):
    return self.Location_Visited

class Visit(models.Model):
  patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
  location = models.ForeignKey(Location, on_delete=models.CASCADE)
  date_from = models.DateField("Date From", default=date.today)
  date_to = models.DateField("Date To", default=date.today)
  detail = models.CharField(max_length=65536, null=True, blank=True)
  CATEGORY_CHOICES = (
    (u'r', u'Residence'),
    (u'w', u'Workplace'),
    (u'v', u'Visit'),
    (u's', u'School'),
  )
  category = models.CharField("Category", max_length=1, choices=CATEGORY_CHOICES, default="v")
  def __str__(self):
    return self.location.location_name+" ("+str(self.date_from)+" - "+str(self.date_to)+")"
  def get_absolute_url(self):
    return reverse('travelhistory-detail', args=[str(self.id)])