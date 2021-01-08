hello_file = open('hello.txt', 'w')
ga_intro = "hello GA test"
hello_file.write(ga_intro) 
hello_file.close()

#txt_list = hello_file.split(' ').read()


car_file = open('car.txt', 'w')
new_car_list = 'Tesla Model S \nMercedez C300\nToyota Camry'
car_file.write(new_car_list)
#print(car_file.read())
car_file.close()


#Create a file
my_new_file = open('person.txt', 'w')
my_new_file.write('Ariel Strizower')
my_new_file.close()

with open('person.txt', 'w') as person_file:
    person_file.write('Romanowski')


#append to a file
with open('person.txt', 'a') as person_file:
    person_file.write('\nAriel')

with open('person.txt', 'r+') as person_file:
        person_file.read()


