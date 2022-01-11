import requests

params = {
  'collection': 'mutant-ape-yacht-club'
}

r= requests.get ("https://api.opensea.io/api/v1/assets", params=params)

print(r.json())
