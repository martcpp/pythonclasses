countryfile = open('country.txt', 'r')
#print(countryfile.readlines())

for a in countryfile.readlines():
    print(a)


countryfile.close()
