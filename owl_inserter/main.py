from owlready2 import get_ontology
from owl_inserter.inserter import inserter


def owl_inserter(AvailableCity):
  ontologies = []
  for city in AvailableCity:
    onto = get_ontology("./ontology/bike.owl").load()
    inserter(f'./rdf_data/Triple_Bike{city}.obj', onto, f'./ontology/{city}.owl', reasoner=True)
    ontologies.append(f'./ontology/{city}.owl')
  return ontologies


