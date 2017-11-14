import swapi

# return a list of planets and order by diameter.
def q1(): 
    planets = swapi.get_all("planets").order_by("diameter")
    return planets

# count the total number of pilots.
def q2():
    pilots = set()
    people = swapi.get_all("people").iter()
    for person in people:
        for sh in person.get_starships().iter():
            if sh:
                pilots.add(person)
                break
    return list(pilots)

# return the max atmosphering speed for the vehicles.
def q3():
    vehicles = swapi.get_all("vehicles").iter()
    maxAtmosphering = [vi.max_atmosphering_speed for vi in vehicles]
    return maxAtmosphering

# return the films that species "Dug" has been in. 
def q4():
    species = swapi.get_all("species").iter()
    for spec in species:
        if spec.name == "Dug":
            target = spec
            break
    films = target.get_films().iter()
    return films
# print the species that a person belongs to.
def q5(person_id):
    person = swapi.get_person(person_id)
    species = person.get_species().iter()
    names = [sp.name for sp in species]
    return names
