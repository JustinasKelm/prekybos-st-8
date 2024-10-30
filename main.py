"""
# Prekybos robotas (simple)

### Užduotis

Parašykite programą, kuri imituotų prekybos automatą. Programa turėtų paprašyti vartotojo įvesti pinigų sumą, kurią jis nori išleisti, ir tada parodyti prekių, kurias jis gali įsigyti pagal įvestą pinigų sumą, sąrašą.

1. Prekybos automate yra šios prekės ir kainos:
    - Saldainiai: 0,50€
    - Traškučiai: 1,00€
    - Gėrimas: 1,50€
    - Kramtomoji guma: 0,75€
2. Programa turėtų paprašyti vartotojo įvesti pinigų sumą.
    - Jei vartotojas įveda mažesnę nei 0,50€ sumą, rodomas klaidos pranešimas: "Jūsų įvestos sumos nepakanka jokiems daiktams įsigyti."
    - Jei vartotojas įveda sumą, didesnę ar lygią 0,50€, programa turėtų parodyti prekes, kurias jis gali įsigyti pagal įvestą sumą:
        - Jei suma mažesnė nei 0,75€, vartotojas gali rinktis tik iš "Saldainiai".
        - Jei suma yra tarp 0,75€ ir 1,00€, vartotojas gali rinktis iš "Saldainiai" arba "Kramtomoji guma".
        - Jei suma yra tarp 1,00€ ir 1,50€, vartotojas gali rinktis iš "Saldainiai", "Traškučiai" arba "Kramtomoji guma".
        - Jei suma yra didesnė nei 1,50€, rodomas visas prekių sąrašas.
3. Programa turi paprašyti vartotojo pasirinkti prekę ir parodyti likutį po pirkimo. Jei likutis yra mažesnis nei 0,50€, rodomas pranešimas: "Dėkojame už Jūsų pirkinį. Jūsų likęs likutis yra [likutis]."

### Pastabos

- Naudokite funkciją `input()`, kad paprašytumėte vartotojo įvesti duomenis.
- Naudokite `if...else` struktūras, kad nuspręstumėte, kokius veiksmus atlikti pagal vartotojo įvestą pinigų sumą.

### Veikimo pavyzdys:

```
Įveskite sumą, kurią norėtumėte išleisti: €0.60
Galite įsigyti:
1. Saldainiai - €0.50
Įveskite pasirinkimo numerį: 1
Pasirinkote Saldainiai. Jūsų likutis yra €0.10.
Dėkojame už Jūsų pirkinį. Jūsų likutis yra €0.10.
```

"""




