from django.db import models

class Salad(models.Model):
    salad_date = models.DateField()
    salad_time = models.CharField(max_length=100)
    salad_location = models.CharField(max_length=100)

    def __str__(self):
        return "Salad #"+str(self.id)+" @ "+self.salad_location

class Ingredient(models.Model):
    salad = models.ForeignKey(Salad, on_delete=models.CASCADE)
    ingredient = models.CharField(max_length=100)
    ingredient_type = models.CharField(max_length=100)
    ingredient_owner = models.CharField(max_length=100)

    def __str__(self):
        return self.ingredient_owner+" is bringing "+self.ingredient+" which is a "+self.ingredient_type+" to... "+self.salad.__str__()
