ages = [12, 13, 14, 18]
people = ["Naman", "Anshita", "Pratheek"]
peopleWithAges = ["Naman", 22, "Anshita", 21.4]
pep = people[:]
print(id(pep), id(people))
ages[:3] = [6, 7]
