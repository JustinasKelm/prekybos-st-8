l1=[
    'Volvo 7700A (2004) Nr. 701',
    'Volvo 7700A (2004) Nr. 702',
    'Volvo 7700A (2004) Nr. 703',
    'Volvo 7700A (2004) Nr. 706',
    'Volvo 7700A (2004) Nr. 708',
    'Volvo 7700A (2004) Nr. 709'

    'Volvo 7700 (2004) Nr. 710',
    'Volvo 7700 (2004) Nr. 711',
    'Volvo 7700 (2004) Nr. 715',
    'Volvo 7700 (2004) Nr. 717',
    'Volvo 7700 (2004) Nr. 719',
    'Volvo 7700 (2004) Nr. 720',
    'Volvo 7700 (2004) Nr. 721',
    'Volvo 7700 (2004) Nr. 722',
    'Volvo 7700 (2004) Nr. 724',
    'Volvo 7700 (2004) Nr. 728',
    'Volvo 7700 (2004) Nr. 729'
]

l2=[
    3499.99,
    2699.99,
    1749.99,
    2129.99,
    1409.49,
    5799.99,

    699.69,
    3000.99,
    2899.99,
    2949.99,
    2909.99,
    2649.49,
    3475.79,
    1199.99,
    2199.99,
    2389.99,
    2359.99,
]

p=float(input("Įveskite sumą, kurią norėtumėte išleisti: €"))

while True:
    for i in range(len(l2)):  
        if l2[i]>p:
            l1.insert(i,0)
            l1.pop(i+1)
            l2.insert(i,0)
            l2.pop(i+1)
    l1=[i for i in l1 if i != 0]
    l2=[i for i in l2 if i != 0]
    if l2==[]:
        print(f'Dėkojame už Jūsų pirkinį. Jūsų likutis yra €{p:.2f}.')
        break
    else:
        print('Galite įsigyti:')
        for i in range(len(l1)):
            print(f'{str(i+1)}. {l1[i]} - €{str(l2[i])}')
        r=int(input("Įveskite pasirinkimo numerį: "))
        p-=l2[r-1]
        print(f'Pasirinkote {(l1[r-1])}. Jūsų likutis yra €{p:.2f}.')