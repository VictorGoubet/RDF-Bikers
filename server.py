from flask import Flask, request
from owl_inserter.main import owl_inserter
from queries.main import queries_builder
from jsonld.main import load_all

app = Flask(__name__)

AvailableCity = ['Paris', 'Lyon', 'StEtienne']
querier = queries_builder([f'./ontology/{c}.owl' for c in AvailableCity])


@app.route('/api/reload_all')
def reload_all():
  global querier
  load_all()
  ontologies = owl_inserter(AvailableCity)
  querier = queries_builder(ontologies)

@app.route('/api/getinfo_by_id')
def getinfo_by_id():
  id = request.args.get('id', default = '10006', type = str)
  city = request.args.get('city', default = 'Paris', type = str).capitalize()
  response = querier[city].getInfo_by_id(id, disp=False)
  return str(response)
  
@app.route('/api/getAllCoord')
def getAllCoord():
  city = request.args.get('city', default = 'Paris', type = str).capitalize()
  if city in AvailableCity:
    response = querier[city].getAllCoord(disp=False)
  else:
    response = f"<h1>City unknown:{city} </h1>"
  return str(response)

app.run(host='0.0.0.0', port=5000)