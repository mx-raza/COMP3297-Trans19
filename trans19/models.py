from django.db import models
from datetime import date
# import uuid

from django.urls import reverse
# Create your models here.

#Location Model
class Location(models.Model):
  Location_Visited = models.CharField("Location Visited", max_length=200, help_text="Name of the Location", blank=True)
  Address = models.CharField("Address", max_length=200, help_text="Address of the Location", blank=True, null=True)
  District = models.CharField("District", max_length=200, help_text="District of the Location")
  XCoord = models.FloatField("X Coord", help_text="X Coordiates/Longitude of the location", default=0)
  YCoord = models.FloatField("Y Coord", help_text="Y Coordiates/Latitude of the location", default=0)
  def __str__(self):
    return self.Location_Visited
  pass


# class TravelHistory defined before class Patient for foreign key by Nicholas on 28th April
class TravelHistory(models.Model):
  
  # Add a primary key for class TravelHistory by Nicholas on 28th April
  #LocID = models.IntegerField(
  #  "Location ID", 
  #  primary_key=True,
  #  null=False,
  #  blank=False, 
  #  default=0, #Patient.objects.all().count(),
  #  help_text="The primary key for class TravelHistory"
  #)
  
  Location_Visited = models.CharField("Location Visited", max_length=200, help_text="Name of the Location", blank=True)
  Address = models.CharField("Address", max_length=200, help_text="Address of the Location", blank=True, null=True)
  District = models.CharField("District", max_length=200, help_text="District of the Location")
  XCoord = models.FloatField("X Coord", help_text="X Coordiates/Longitude of the location", default=0)
  YCoord = models.FloatField("Y Coord", help_text="Y Coordiates/Latitude of the location", default=0)
  DateFrom = models.DateField("Date From", default=date.today)
  DateTo = models.DateField("Date To", default=date.today)
  Detail = models.CharField(max_length=65536, null=True, blank=True)
  CATEGORY_CHOICES = (
    (u'r', u'Residence'),
    (u'w', u'Workplace'),
    (u'v', u'Visit'),
    (u's', u'School'),
  )
  Category = models.CharField("Category", max_length=1, choices=CATEGORY_CHOICES, default="v")
  # Category = models.TextChoices("Category", "Residence Workplace Visit School")
  
  # Remove the below foreign key by Nicholas on 28th April
  #Patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
  def __str__(self):
    return self.Location_Visited
  def get_absolute_url(self):
      """Returns the url to access a particular author instance."""
      return reverse('travelhistory-detail', args=[str(self.id)])



class Patient(models.Model):
  Name = models.CharField("Name", max_length=200, help_text="Name of the Patient")
  IDN = models.CharField("Identity Document Number", max_length=10, help_text="Identity Document Number", null=True, blank=True)
  DOB = models.DateField("Date of Birth", null=True, blank=True)
  DCC = models.DateField("Date Case Confirmed", null=False, blank=False, default=date.today)
  caseNum = models.IntegerField(
    "Case Number", 
    primary_key=True,
    null=False,
    blank=False, 
    default=0, #Patient.objects.all().count(),
    help_text="The case number of the Patient"
  )

  #test_input = models.CharField("this is testing", max_length=100)

  # Add a foreign key to TravelHistory by Nicholas on 28th April
  Location = models.ForeignKey(TravelHistory, on_delete=models.CASCADE, null=True)

  def __str__(self):
    return self.Name+" "+str(self.caseNum)

  def get_absolute_url(self):
      """Returns the url to access a particular author instance."""
      return reverse('patient-detail', args=[str(self.caseNum)])





# Below is the original location of class TravelHistroy, keep it commented and reuse if necessary by Nicholas on 28th April

#class TravelHistory(models.Model):
#  Location_Visited = models.CharField("Location Visited", max_length=200, help_text="Name of the Location", blank=True)
#  Address = models.CharField("Address", max_length=200, help_text="Address of the Location", blank=True, null=True)
#  District = models.CharField("District", max_length=200, help_text="District of the Location")
#  XCoord = models.FloatField("X Coord", help_text="X Coordiates/Longitude of the location", default=0)
#  YCoord = models.FloatField("Y Coord", help_text="Y Coordiates/Latitude of the location", default=0)
#  DateFrom = models.DateField("Date From", default=date.today)
#  DateTo = models.DateField("Date To", default=date.today)
#  Detail = models.CharField(max_length=65536, null=True, blank=True)
#  CATEGORY_CHOICES = (
#    (u'r', u'Residence'),
#    (u'w', u'Workplace'),
#    (u'v', u'Visit'),
#    (u's', u'School'),
#  )
#  Category = models.CharField("Category", max_length=1, choices=CATEGORY_CHOICES, default="v")
  # Category = models.TextChoices("Category", "Residence Workplace Visit School")
  
  # Remove the below foreign key by Nicholas on 28th April
  #Patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
#  def __str__(self):
#    return self.Location_Visited
#  def get_absolute_url(self):
#      """Returns the url to access a particular author instance."""
#      return reverse('travelhistory-detail', args=[str(self.id)])