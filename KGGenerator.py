from rdflib import Graph, Namespace, URIRef, Literal, BNode
from rdflib.namespace import RDF, RDFS, SKOS

g = Graph()

# Namespaces
r = Namespace("http://example.org/r/")
continents = Namespace("http://example.org/continents/")
countries = Namespace("http://example.org/countries/")
capitals = Namespace("http://example.org/capitals/")
languages = Namespace("http://example.org/languages/")

# Continents
g.add((continents.Europe, SKOS.prefLabel, Literal("Europe", lang='en')))

g.add((continents.Asia, SKOS.prefLabel, Literal("Asia", lang="en")))

g.add((continents.America, SKOS.prefLabel, Literal("America", lang="en")))

# continents.Australia doesn't have a label


# Languages
g.add((languages.German, SKOS.prefLabel, Literal("German", lang="en")))

g.add((languages.French, SKOS.prefLabel, Literal("French", lang="en")))

g.add((languages.Japanese, SKOS.prefLabel, Literal("Japanese", lang="en")))

g.add((languages.English, SKOS.prefLabel, Literal("English", lang="en")))

g.add((languages.UndefinableGibberish, SKOS.prefLabel, Literal("Undefinable Gibberish", lang="en")))

g.add((languages.Random, SKOS.prefLabel, Literal("RandomTndsfkjnebkjabd", lang="en")))

g.add((languages.HalfRandom, SKOS.prefLabel, Literal("Austria RandomTndsfkjnebkjabd", lang="en")))


# Countries
g.add((countries.Austria, SKOS.prefLabel, Literal("Austria", lang="en")))
g.add((countries.Austria, r.isOn, continents.Europe))
g.add((countries.Austria, r.speaks, languages.German))
g.add((countries.Austria, r.speaks, languages.UndefinableGibberish))
g.add((countries.Austria, r.speaks, languages.Random))
g.add((countries.Austria, r.undefinable, languages.Random))
g.add((countries.Austria, r.zerovec, languages.HalfRandom))

g.add((countries.Germany, SKOS.prefLabel, Literal("Germany", lang="en")))
g.add((countries.Germany, r.isOn, continents.Europe))
g.add((countries.Germany, r.speaks, languages.German))

g.add((countries.France, SKOS.prefLabel, Literal("France", lang="en")))
g.add((countries.France, r.isOn, continents.Europe))
g.add((countries.France, r.speaks, languages.French))

g.add((countries.Japan, SKOS.prefLabel, Literal("Japan", lang="en")))
g.add((countries.Japan, r.isOn, continents.Asia))
g.add((countries.Japan, r.speaks, languages.Japanese))

g.add((countries.USA, SKOS.prefLabel, Literal("U.S.A.", lang="en")))
g.add((countries.USA, r.isOn, continents.America))
g.add((countries.USA, r.speaks, languages.English))

g.add((countries.Australia, SKOS.prefLabel, Literal("Australia", lang="en")))
g.add((countries.Australia, r.isOn, continents.Australia))
g.add((countries.Australia, r.speaks, languages.English))


# Capitals
g.add((capitals.Vienna, SKOS.prefLabel, Literal("Vienna", lang="en")))
g.add((capitals.Vienna, r.isCapitalOf, countries.Austria))

g.add((capitals.Berlin, SKOS.prefLabel, Literal("Berlin", lang="en")))
g.add((capitals.Berlin, r.isCapitalOf, countries.Germany))

g.add((capitals.Paris, SKOS.prefLabel, Literal("Paris", lang="en")))
g.add((capitals.Paris, r.isCapitalOf, countries.France))

g.add((capitals.Tokyo, SKOS.prefLabel, Literal("Tokyo", lang="en")))
g.add((capitals.Tokyo, r.isCapitalOf, countries.Japan))

g.add((capitals.Washington, SKOS.prefLabel, Literal("Washington", lang="en")))
g.add((capitals.Washington, r.isCapitalOf, countries.USA))

g.add((capitals.Canberra, SKOS.prefLabel, Literal("Canberra", lang="en")))
g.add((capitals.Canberra, r.isCapitalOf, countries.Australia))


f = open("KGdemo.ttl", "wb")
f.write(g.serialize(format='turtle'))
f.close()
