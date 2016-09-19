from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.urls import reverse
import datetime

from .models import Salad, Ingredient
from .saladMath import perfectRatios, calculateRatios, warnAboutRatios
from .forms import SaladForm, IngredientForm

# GLOBAL VARIABLES #
GREENS = "Greens"
VEGGIES = "Veggies"
PROTEIN = "Protein"
DRESSING = "Dressing"
OTHER = "Other"


def saladStatus(request, salad_id):
    try:
        this_salad = Salad.objects.get(pk=salad_id)
    except Salad.DoesNotExist:
        raise Http404("That salad does not exist")

    # INGREDIENTS
    # finding all ingredients for this salad
    ingredient_list = []
    for ingredient in Ingredient.objects.all():
        if ingredient.salad == this_salad:
            ingredient_list.append(ingredient)
    # sorting them by type
    ingredient_dict = {GREENS:[], VEGGIES:[],
                        PROTEIN:[], DRESSING:[],
                        OTHER:[]}
    for ingredient in ingredient_list:
        ing_type = ingredient.ingredient_type
        # prepping the html for each ingredient bullet
        ing = ingredient.ingredient
        owner = ingredient.ingredient_owner
        ing_pretty = ing+" - "+owner
        ingredient_dict[ing_type].append(ing_pretty)

    # SALAD LOGISTICS
    # prepping date and time info for html
    this_date = this_salad.salad_date
    date_beautified = this_date.strftime("%A, %B %d")

    # CHECKING SALAD RATIOS
    ourRatioDict = calculateRatios(ingredient_dict)
    warnings = warnAboutRatios(perfectRatios, ourRatioDict)
    if warnings:
        warning_message = "Warning! For this salad to approach Ideal Ingredient Ratios we need more: "
        warnings_beautified = warning_message+", ".join(warnings)
    else:
        warnings_beautified = ""

    form=IngredientForm()

    context = {"ingredient_dict": ingredient_dict,
            "greens_list": ingredient_dict[GREENS],
            "veggie_list": ingredient_dict[VEGGIES],
            "protein_list": ingredient_dict[PROTEIN],
            "dressing_list": ingredient_dict[DRESSING],
            "other_list": ingredient_dict[OTHER],
            "salad_id":salad_id, #weird! no .s in these key strings
            "salad_date":date_beautified,
            "salad_time":this_salad.salad_time,
            "salad_location":this_salad.salad_location,
            "warnings_beautified":warnings_beautified,
            "form":form,
            }

    return render(request, "saladStatus.html", context)


def commitment(request, salad_id):
    try:
        this_salad = Salad.objects.get(pk=salad_id)
    except Salad.DoesNotExist:
        raise Http404("That salad does not exist")

    if request.POST:
        ingredient = request.POST['ingredient']
        ingredient_type = request.POST['ingredient_type']
        ingredient_owner = request.POST['ingredient_owner']
        #add this to the database
        newIngredient = Ingredient(salad=this_salad, ingredient=ingredient,
                ingredient_type=ingredient_type, ingredient_owner=ingredient_owner)
        newIngredient.save()
    else: print("no ingredient brought")
    return HttpResponseRedirect(reverse('salads:saladStatus', args=(salad_id,)))

def createSalad(request):
    form = SaladForm()
    return render(request, "createSalad.html", {'form': form})

def saladCreated(request):
    if request.POST:
        time = request.POST['salad_time']
        location = request.POST['salad_location']
        month = int(request.POST['salad_date_month'])
        day = int(request.POST['salad_date_day'])
        year = int(request.POST['salad_date_year'])
        date = datetime.date(year, month, day)

        #add this to the database
        newSalad = Salad(salad_date=date, salad_time=time, salad_location=location)
        newSalad.save()
        salad_id = newSalad.id
        return HttpResponseRedirect(reverse('salads:saladStatus', args=(salad_id,)))
    else:
        return HttpResponse("your attempt to create a new salad didn't work :(")


