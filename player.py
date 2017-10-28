'''
Defines a class Player
Data Members:
  data # a dictionary of the high-level log info. contains:
    logs
      date
      id
      title
    results # number of results (capped at 1000 games)
    success # false if retrieval url was formatted bad
Methods:
  __init__(self, id64)
  load_data(self, id64)
  
Tools:
  Sample urls:
    url1 = 'http://logs.tf/json_search?&player=76561198055233348'
    url2 = 'http://logs.tf/json_search?&player=76561198064873161'
'''

import urllib.request
import json

class Player:
  def __init__(self, id64):
    load_data(self,id64)
  
  def load_data(self, id64):
    url = "http://logs.tf/json_search?&player=" + steam_id_64
    json = urllib.request.urlopen(url1)
    output_string = json.read().decode('utf-8')
    self.data = json.loads(output_string)
    