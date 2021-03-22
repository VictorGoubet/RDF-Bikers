from flask import Flask, request
from owl_inserter.main import owl_inserter
from queries.main import queries_builder

app = Flask(__name__)

AvailableCity = ['Paris', 'Lyon', 'StEtienne']
querier = queries_builder([f'./ontology/{c}.owl' for c in AvailableCity])
print(querier)


@app.route('/api/reload_all')
def reload_all():
  global querier
  ontologies = owl_inserter(AvailableCity)
  querier = queries_builder(ontologies)
  
@app.route('/api/getAllCoord')
def getAllCoord():
  city = request.args.get('city', default = 'Paris', type = str)
  if city in AvailableCity:
    response = querier[city].getAllCoord(disp=False)
  else:
    response = "City unknown"
  return str(response)

app.run(host='0.0.0.0', port=5000)