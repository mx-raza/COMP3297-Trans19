from django import forms
from .models import Patient, Visit, Location
from django.forms import inlineformset_factory
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Fieldset, Div, HTML, ButtonHolder, Submit
from .custom_layout_object import *


class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = '__all__'


class DateInput(forms.DateInput):
    input_type = 'date'


class VisitForm(forms.ModelForm):
    class Meta:
        model = Visit
        fields = '__all__'
        widgets = {
            'date_from': DateInput(),
            'date_to': DateInput(),
        }


PatientFormSet = inlineformset_factory(
    Patient,
    Visit,
    form=VisitForm,
    extra=1,
    can_delete=True,
)


class PatientForm(forms.ModelForm):

    class Meta:
        model = Patient
        exclude = ()
        widgets = {
            'date_case_confirmed': DateInput(),
            'date_of_birth': DateInput(),
        }

    def __init__(self, *args, **kwargs):
        super(PatientForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-3 create-label'
        self.helper.field_class = 'col-md-9'
        self.helper.layout = Layout(
            Div(
                Field('patient_name'),
                Field('patient_id'),
                Field('date_of_birth'),
                Field('date_case_confirmed'),
                Field('case_number'),
                Fieldset('Add Visits',
                        Formset('visits')),
                HTML("<br>"),
                ButtonHolder(Submit('submit', 'Save')),
                )
            )
