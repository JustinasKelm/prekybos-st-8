l1=[
    'Volvo 7700A (2004) Nr. 701',
    'Volvo 7700A (2004) Nr. 702',
    'Volvo 7700A (2004) Nr. 703',
    'Volvo 7700A (2004) Nr. 706',
    'Volvo 7700A (2004) Nr. 708',
    'Volvo 7700A (2004) Nr. 709',
]

l2=[
    3499.99,
    2699.99,
    1749.99,
    2129.99,
    1409.49,
    5799.99

]

l=[]

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
