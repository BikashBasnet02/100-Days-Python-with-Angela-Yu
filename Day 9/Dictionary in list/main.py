Travel_log = [
{
   "country":"France",
   "cities_visited":["Paris", "Lille", "Dijon"],
   "total_visits":12
},
{
   "country":"Germany",
   "cities_visited":["Berlin", "Hamburg", "Stuttgart"],
   "total_visits":5
},
]
def get_city(travel_dict, country):
    for city in travel_dict:
        if city["country"] == country:
            return city["cities_visited"]

print(get_city(Travel_log, "Germany"))