countries = {"Asia":"India", "Europe":"Netherlands", "Africa":"Sudan", "NA":"Canada"}

print(countries)
print(countries["Asia"])
print(countries.get("Asia"))
print(countries.get("Australia", "there is no country for Australia Continent"))

countries.setdefault("SA","Argentina")
print(countries)
countries["Antartica"] = "Antartica_C"
print(countries)
morecountries = {"Australia":"New Zealand", "Asia":"Pakistan"}
countries.update(morecountries)
print(countries)

countries = {}
print(countries)

countries["Asia"]="India"
countries["Europe"]="Turkey"
print(countries)

morecountries_pipe={"NA":"USA", "SA":"Brazil"}
countries=countries|morecountries_pipe
print(countries)

del countries["SA"]
print(countries)

x=countries.pop("NA")
print(x)
print(countries)

countries.clear()
print(countries)

countries = {"Asia":["India","Pakistan"], "Europe":["Netherlands","Spain"], "Africa":["Sudan","Ethopia"], "NA":["Canada","USA"]}
print(countries)
x=countries["Asia"]
print(x)

if countries["Asia"] == ["India","Pakistan"]:
    print("Same")
else:
    print("Different")

print(countries["Asia"][1])

print(countries.keys())
print(countries.values())
print(countries.items())

countries_keys = list(countries)
print(countries_keys)

for k in countries:
    print(k)

for v in countries.values():
    print(v)

for k,v in countries.items():
    print(k,v)

countries = {}
print(countries)
continent = ["SA", "NA"]
country=["Chile", "Mexico"]
countries=dict(zip(continent,country))
print(countries)



