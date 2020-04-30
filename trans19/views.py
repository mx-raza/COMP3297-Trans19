from django.shortcuts import render
from django.http import HttpResponse

from .models import Patient, TravelHistory

# Create your views here.
def index(request):
  """View function for home page of site."""
  # Generate counts of some of the main objects
  num_Cases = Patient.objects.all().count()

  # Render the HTML template index.html with the data in the context variable.
  return render(request, "index.html", context={"num_Cases": num_Cases})


from django.views import generic


class PatientListView(generic.ListView):
    """Generic class-based list view for a list of Patients."""
    model = Patient
    paginate_by = 10

class TravelListView(generic.ListView):
    # Comment corrected by Nicholas on 28th April, should be "a list of TravelHistory"
    """Generic class-based list view for a list of TravelHistory."""
    model = TravelHistory
    paginate_by = 10

class PatientDetailView(generic.DetailView):
    """Generic class-based detail view for an Patient."""
    model = Patient
  
class TravelHistoryDetailView(generic.DetailView):
    # Comment corrected by Nicholas on 28th April, should be "view for a TravelHistory"
    """Generic class-based detail view for a TravelHistory."""
    model = TravelHistory


class PatientCreate(generic.edit.CreateView):
    model = Patient
    fields = '__all__'
    initial = {'caseNum': Patient.objects.all().count()}
    # permission_required = 'catalog.can_mark_returned'

class TravelHistoryCreate(generic.edit.CreateView):
    model = TravelHistory
    fields = '__all__'
    # initial = {'caseNum': Patient.objects.all().count()}
    # permission_required = 'catalog.can_mark_returned'


# deleteView for TravelHistory by Nicholas on 28th April
class TravelHistoryDelete(generic.edit.DeleteView): 
    # specify the model you want to use 
    model = TravelHistory
      
    # url to redirect after sucessfully
    #success_url ="/"                    # may need configuration later
    def get_success_url(self):
      return reverse('trans19:travels')