# calculate the ideal salad ingredient ratio

# GLOBAL VARIABLES #
GREENS = "Greens"
VEGGIES = "Veggies"
PROTEIN = "Protein"
DRESSING = "Dressing"
OTHER = "Other"

perfectRatios = {GREENS: 0.3,VEGGIES: 0.3,
                    PROTEIN: 0.2, DRESSING: 0.1,
                    OTHER: 0.1}

def calculateRatios(category_dict):
    ourSaladRatios = {}
    for category in category_dict.keys():
        ourSaladRatios[category]=len(category_dict[category])
    total = sum(ourSaladRatios.values())
    if total == 0: #there are no ingredients
        return perfectRatios #treat it as if we have an ideal salad so far
    for category in category_dict.keys():
        ourSaladRatios[category] = ourSaladRatios[category]/float(total)
    return ourSaladRatios

def warnAboutRatios(perfectDict, ourRatioDict):
    warnings = []
    for category in perfectDict.keys():
        if ourRatioDict[category] < perfectDict[category]/2.:
            warnings.append(category)
    return warnings
