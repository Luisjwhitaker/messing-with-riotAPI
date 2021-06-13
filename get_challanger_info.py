import random
import cassiopeia as cass
api_key = 'api goes here'

cass.set_riot_api_key(api_key)
cass.set_default_region('NA')

summoner = cass.get_summoner(name='Kalturi')
print(f'{summoner.name} is a level {summoner.level} cummoner on the {summoner.region} server')

champions = cass.get_champions()
random_champion = random.choice(champions)
print(f'He enjoys playing champions such as {random_champion.name}')
