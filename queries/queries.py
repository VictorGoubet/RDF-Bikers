from owlready2 import *
from rdflib import *

class SparqlQueries:
  def __init__(self, onto_path, reasoner=False):
      my_world = World()
      my_world.get_ontology(onto_path).load() 
      if reasoner:
        sync_reasoner_pellet(my_world)
      self.graph = my_world.as_rdflib_graph()
    
  def extract_res(self, qres, params, disp):
    res = []
    for row in qres:
      l = {}
      for par in params:
        l[par] = row[par].toPython()
      res.append(l)
      if disp:
        print(l)
    return res
  
  # Some queries

  def selectAll(self):
      query = """PREFIX ns:<http://www.semanticweb.org/victo/ontologies/2021/2/bike#> 
                 SELECT ?s ?p ?o WHERE { 
                    ?s ?p ?o . 
                 }"""

      qres = self.graph.query(query)
      return self.extract_res(qres, ['s', 'p', 'o'])

  def getStandFreeStation(self, disp=True):
    query = """PREFIX rdf:<http://www.w3.org/1999/02/22-rdf-syntax-ns#>
               PREFIX  ns:<http://www.semanticweb.org/victo/ontologies/2021/2/bike#>
               SELECT ?name WHERE { 
                  ?s rdf:type ns:StandFreeStation . 
                  ?s ns:Name ?name .
               }"""
    qres = self.graph.query(query)
    return self.extract_res(qres, ['name'], disp)

  def getStandFullStation(self, disp=True):
    query = """PREFIX rdf:<http://www.w3.org/1999/02/22-rdf-syntax-ns#>
               PREFIX  ns:<http://www.semanticweb.org/victo/ontologies/2021/2/bike#>
               SELECT ?name WHERE { 
                  ?s rdf:type ns:StandFullStation . 
                  ?s ns:Name ?name .
               }"""
    qres = self.graph.query(query)
    return self.extract_res(qres, ['name'], disp)


  def getAllCoord(self, disp=True):
    query = """PREFIX rdf:<http://www.w3.org/1999/02/22-rdf-syntax-ns#>
               PREFIX  ns:<http://www.semanticweb.org/victo/ontologies/2021/2/bike#>
               SELECT ?x ?y WHERE { 
                  ?s ns:Lat ?x . 
                  ?s ns:Long ?y .
               }"""
    qres = self.graph.query(query)
    return self.extract_res(qres, ['x', 'y'], disp)
