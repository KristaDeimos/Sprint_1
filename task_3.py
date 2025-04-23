world_champions = {
    2002: 'Бразилия',
    2006: 'Италия',
    2010: 'Испания',
    2014: 'Германия',
    2018: 'Франция',
}

new_champion = {2022 : 'Аргентина'}
world_champions.update(new_champion)

print(world_champions)

country = 'Италия'

if country in world_champions:
    print('Италия становилась чемпионом мира по футболу в 21 веке!')
else:
    print('Италия не выигрывала чемпионат мира по футболу в 21 веке.')