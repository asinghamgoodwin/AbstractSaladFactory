from django import forms
from salads.models import Salad
from django.forms.extras.widgets import SelectDateWidget

# GLOBAL VARIABLES #
GREENS = "Greens"
VEGGIES = "Veggies"
PROTEIN = "Protein"
DRESSING = "Dressing"
OTHER = "Other"

class SaladForm(forms.Form):
    salad_date = forms.DateTimeField(widget=SelectDateWidget(
                                        empty_label=("Choose Year", 
                                                    "Choose Month", 
                                                    "Choose Day")))
    salad_time = forms.TimeField()
    salad_location = forms.CharField(max_length=100)

class IngredientForm(forms.Form):
    ingredient = forms.CharField(max_length=100)
    ingredient_type = forms.ChoiceField(label="Type", choices=[(GREENS, GREENS),
                                                                (VEGGIES, VEGGIES),
                                                                (PROTEIN, PROTEIN),
                                                                (DRESSING, DRESSING),
                                                                (OTHER, OTHER)])
    ingredient_owner = forms.CharField(label="Your Name", max_length=100)
