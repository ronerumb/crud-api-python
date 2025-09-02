import requests 
from pydantic import BaseModel

class PokemonSchema(BaseModel):
    name: str
    type: str

    class Config:
        orm_mode = True

URL = "https://pokeapi.co/api/v2/pokemon/25"

response = requests.get(URL)
data = response.json()
data_types = data['types']
types_list = []
for type_info in data_types:
    types_list.append(type_info['type']['name'])
types = ', '.join(types_list)

print(data['name'], types)