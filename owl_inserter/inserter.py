from owlready2 import sync_reasoner_pellet, destroy_entity


def inserter(file, onto, save_path, reasoner=False):
  with open(file, 'r') as f:
    triples = f.readlines()

  for triple in triples:
    t = triple.split('>')

    i = t[0].split('/')[-1]
    p = t[1].split('/')[-1]
    o = convertisor(t[2])

    if o != None: 
      s = onto.BikeStation(i)
      map_list = {'Name':s.Name, 
                  'Lat':s.Lat, 
                  'Long':s.Long, 
                  'Lastupdate':s.Lastupdate,
                  'AvailableBikes': s.AvailableBikes,
                  'AvailableBikeStands': s.AvailableBikeStands}
      map_list[p].append(o)
  pre_reasoner(onto)
  if reasoner:
    with onto:
      sync_reasoner_pellet()
  onto.save(save_path)


def pre_reasoner(onto):
  for i in onto.individuals():
    if i.AvailableBikes == i.AvailableBikeStands == [0]:
      destroy_entity(i)


def convertisor(data):
  data = data.split('xsd:')

  _type, o = data[-1], data[0]
  o = o.replace('^^<', '').replace('"', '')

  if _type == 'integer':
    try:
      res = int(o)
    except: 
      res = None
  elif _type == 'decimal':
    try:
      res = float(o)
    except:
      res = None
  elif _type == 'dateTime':
    res = o
  else: 
    res = o
  return res



  