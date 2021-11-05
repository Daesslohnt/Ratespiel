def loeser(result, iteration, eingabe, grenze_ober, grenze_unter):
    supplement = int((grenze_ober + grenze_unter) / 2 ** iteration)
    if supplement == 0:
        supplement = 1
    return eingabe - supplement if (result) else eingabe + supplement


def function(grenze_ober, grenze_unter, rand_number):
    eingabe = 0
    richtung = False
    iteration = 0

    while (True):
        iteration += 1
        eingabe = loeser(richtung, iteration, eingabe, grenze_ober, grenze_unter)
        if (eingabe < rand_number):
            richtung = False
        elif (eingabe > rand_number):
            richtung = True
        else:
            return iteration, eingabe