#TODO: replace intial THEs, check for substrings

#%% Define source lists
# each list is in order of most good to least good. item 100 is at index 99. and game #1 (the best) is at index 0

#https://www.retro-sanctuary.com/Top-100-SNES-Games-Page-1.html
top100_rs = ["Legend of Zelda: A Link to the Past","Super Metroid","Chrono Trigger","Street Fighter II Turbo","Super Mario World","Final Fantasy VI","Super Mario Kart","Secret of Mana","Donkey Kong Country 2","Star Fox","Mega Man X2","Final Fantasy IV","Yoshi's Island","F-Zero","Super Mario RPG","Legend of the Mystical Ninja","Super Turrican 2","Terranigma","Teenage Mutant Ninja Turtles: Turtles in Time","EarthBound","Lufia II: Rise of the Sinistrals","R-Type III","Super Castlevania IV","Mortal Kombat II","ActRaiser","Spindizzy Worlds","Axelay","Contra III: The Alien Wars","Populous","Hagane","Wild Guns","Breath of Fire II","Super Bomberman","Earthworm Jim","Space Megaforce","Shadowrun","Illusion of Gaia","Magical Pop N'","Lufia and the Fortress of Doom","DoReMi Fantasy","Donkey Kong Country","Demon's Crest","Parodius","Sky Blazer","Bust-A-Move","Flashback","Super Punch-Out","Lemmings","Killer Instinct","Majuu Ou","Addams Family","Kirby's Avalanche","Mega Man and Bass","Super Ghouls n Ghosts","Lost Vikings","Super Turrican","Mega Lo Mania","Mega Man X","Metal Marines","Goof Troop","Pocky and Rocky 2","Cybernator","Harvest Moon","The Firemen","Secret of Evermore","Sparkster","Jungle Strike","Uniracers","Ogre Battle","PilotWings","Troddlers","Zombies Ate My Neighbors","Kirby Super Star","UN Squadron","SimCity","Super Tennis","Rainbow Bell Adventures","Umihara Kawase","Street Racer","Rendering Ranger","Castlevania: Dracula X","Zero the Kamikaze Squirrel ","NHL 94","PLok","EVO","Putty Squad","Soul Blazer","Tetris Attack","Zero the Kamikaze Squirrel ","Breath of Fire","Metal Warriors","NBA Jam","Equinox","Phalanx","Buster Bros","Sunset Riders","Madden NFL 94","Batman Returns","Pieces","Super Smash TV"]

#https://www.ign.com/lists/top-100-snes-games/100
top100_ign = ['Legend of Zelda: A Link to the Past', 'Chrono Trigger', 'Super Metroid', 'Final Fantasy VI', 'Super Mario World', 'Street Fighter II Turbo', "Yoshi's Island", 'Super Mario Kart', 'Star Fox', 'Super Mario RPG', 'Secret of Mana', 'Mega Man X', 'EarthBound', 'Final Fantasy IV', 'Tetris Attack', "Donkey Kong Country 2", 'Super Punch-Out', 'F-Zero', 'ActRaiser', 'Super Mario All-Stars', 'Super Castlevania IV', 'Mario Paint', 'The Magical Quest Starring Mickey Mouse', 'Contra III: The Alien Wars', 'Mortal Kombat II', 'Super Star Wars: Return of the Jedi', 'Tetris and Dr. Mario', 'Donkey Kong Country', "Wario's Woods", 'Lost Vikings', 'Mega Man X2', 'Legend of the Mystical Ninja', 'Metal Warriors', 'Lufia II: Rise of the Sinistrals', 'SimCity', 'NBA Jam', 'UN Squadron', "Kirby's Dream Course", 'Teenage Mutant Ninja Turtles: Turtles in Time', 'Earthworm Jim 2', 'Ogre Battle', 'EVO', 'Breath of Fire', "Demon's Crest", 'Gradius III', 'Harvest Moon', 'Kirby Super Star', 'Zombies Ate My Neighbors', 'Super Bomberman', "Yoshi's Cookie", "Super Ghouls n Ghosts", "Ken Griffey Jr's Winning Run", 'Breath of Fire II', 'Bust-A-Move', 'Axelay', 'Alien 3', 'Earthworm Jim', "Donkey Kong Country 3", "NHL 94", 'Aladdin', 'Joe and Mac 2: Lost in the Tropics', "Kirby's Dream Land 3", 'Fatal Fury 2', 'International Superstar Soccer', 'R-Type III', 'The Lion King', 'Mega Man X3', "Kirby's Avalanche", 'Out of This World', 'Populous', 'Jungle Strike', "Rock n Roll Racing", 'Pocky and Rocky 2', 'Illusion of Gaia', "Madden NFL 94", 'Soul Blazer', 'Shadowrun', 'X-Men: Mutant Apocalypse', 'Flashback', 'PilotWings', 'The Death and Return of Superman', 'Killer Instinct', 'Super Star Wars', 'Super Tennis', 'Spider-Man and Venom: Maximum Carnage', 'Stunt Race FX', 'Sparkster', 'Sunset Riders', 'Super Bomberman 2', 'Blackthorne', 'Super Star Wars: The Empire Strikes Back', 'Super Double Dragon', 'Super Turrican 2', 'The Adventures of Batman and Robin', 'Top Gear 2', 'Street Fighter Alpha 2', 'Ultimate Mortal Kombat 3', 'Uniracers', 'Tiny Toon Adventures: Buster Busts Loose', 'Final Fight']


#https://www.ranker.com/crowdranked-list/best-super-nintendo-_snes_-games
#retrieved 2023-03-09
top150_ranker = ["Legend of Zelda: A Link to the Past", "Amazon", "Super Metroid", "Super Mario World", "Chrono Trigger", "Super Mario All-Stars", "Teenage Mutant Ninja Turtles: Turtles in Time", "Donkey Kong Country 2", "Final Fantasy VI", "Yoshi's Island", "Street Fighter II Turbo", "Mega Man X", "Super Mario RPG", "Donkey Kong Country", "Super Castlevania IV", "EarthBound", "Secret of Mana", "Super Mario Kart", "Mortal Kombat II", "Contra III: The Alien Wars", "NBA Jam", "Street Fighter II", "Super Punch-Out", "Final Fantasy IV", "Super Street Fighter II", "Kirby Super Star", "F-Zero", "Aladdin", "Donkey Kong Country 3", "Star Fox", "Super Bomberman", "Mega Man X2", "Zombies Ate My Neighbors", "Ultimate Mortal Kombat 3", "Super Ghouls'n Ghosts", "NBA Jam: Tournament Edition", "Super Bomberman 2", "Earthworm Jim", "Sunset Riders", "Killer Instinct", "Harvest Moon", "Kirby's Dream Land 3", "Final Fantasy V", "Mega Man X3", "Illusion of Gaia", "Mega Man 7", "Final Fight 3", "Goof Troop", "Breath of Fire II", "The Magical Quest Starring Mickey Mouse", "Mortal Kombat", "Lufia II: Rise of the Sinistrals", "Secret of Evermore", "Castlevania: Dracula X", "Rock n Roll Racing", "Tiny Toon Adventures: Buster Busts Loose", "ActRaiser", "Breath of Fire", "Demon's Crest", "Mortal Kombat 3", "Terranigma", "Battletoads in Battlemaniacs", "Super Star Wars: Return of the Jedi", "Kirby's Dream Course", "SimCity", "Batman Returns", "PilotWings", "Super Double Dragon", "Tetris", "Super Star Wars", "Trials of Mana", "Final Fight 2", "Tetris and Dr. Mario", "Final Fight", "The Lion King", "Super Smash TV", "Knights of the Round", "Super Star Wars: The Empire Strikes Back", "Shadowrun", "Lost Vikings", "Legend of the Mystical Ninja", "The Adventures of Batman and Robin", "Tetris Attack", "Gradius III", "NHL 94", "UN Squadron", "Mario Paint", "Top Gear", "Ogre Battle", "Teenage Mutant Ninja Turtles: Tournament Fighters", "Joe and Mac", "Super R-Type", "Final Fantasy: Mystic Quest", "Tecmo Super Bowl", "Wild Guns", "EVO", "International Superstar Soccer Deluxe", "Jurassic Park", "Star Fox 2", "Doom", "Ken Griffey Jr. Presents Major League Baseball", "Star Ocean", "The Simpsons: Bart's Nightmare", "Lufia and the Fortress of Doom", "Axelay", "Mickey Mania: The Timeless Adventures of Mickey Mouse", "Tales of Phantasia", "R-Type III", "Dragon Warrior I and II", "Blackthorne", "Primal Rage", "Cool Spot", "Top Gear 2", "Uniracers", "Dragon Warrior III", "Cybernator", "Indiana Jones' Greatest Adventures", "Soul Blazer", "Krusty's Fun House", "Super Turrican", "Metal Warriors", "Flashback", "Fire Emblem: Genealogy of the Holy War", "Hagane", "Super Turrican 2", "Saturday Night Slam Masters", "Sky Blazer", "Mighty Morphin Power Rangers: The Fighting Edition", "Yoshi's Cookie", "Shin Megami Tensei", "ClayFighter", "Sparkster", "International Superstar Soccer", "Super Off Road", "Biker Mice from Mars", "Space Megaforce", "King of Dragons", "Ken Griffey, Jr.'s Winning Run", "Arkanoid: Doh It Again", "MechWarrior 3050", "New Horizons", "Jetsons: The Invasion Of The Planet Pirates", "NHL 96", "Plok", "Top Gear 3000", "True Lies", "Road Runner's Death Valley Rally", "Metal Marines", "Firepower 2000", "The Mask"]

#https://www.complex.com/pop-culture/the-100-best-super-nintendo-games
top100_complex = ["Chrono Trigger", "Legend of Zelda: A Link to the Past", "Super Metroid", "Final Fantasy III", "Super Mario World", "Street Fighter II Turbo", "Super Mario Kart", "Super Mario RPG", "Teenage Mutant Ninja Turtles: Turtles in Time", "Super Mario All-Stars", "EarthBound", "Mortal Kombat II", "Super Castlevania IV", "Yoshi's Island", "Mega Man X", "Secret of Mana", "Donkey Kong Country 2", "Super Punch-Out", "Final Fantasy II", "Super Star Wars: The Empire Strikes Back", "Contra III: The Alien Wars", "Super Ghouls'n Ghosts", "UN Squadron", "Star Fox", "Donkey Kong Country", "Super Street Fighter II", "Breath of Fire", "Battletoads and Double Dragon", "Ninja Gaiden Trilogy", "Saturday Night Slam Masters", "F-Zero", "R-Type III", "ActRaiser", "Ogre Battle", "Mario Paint", "Sunset Riders", "Super Bomberman", "Super Star Wars", "Battletoads in Battlemaniacs", "Samurai Shodown", "Secret of Evermore", "Aladdin", "Flashback", "NBA Jam: Tournament Edition", "The Adventures of Batman and Robin", "Gradius III", "Doom", "Zombies Ate My Neighbors", "Mickey Mania: The Timeless Adventures of Mickey Mouse", "SimCity", "Kirby Super Star", "Uniracers", "Killer Instinct", "Earthworm Jim", "Indiana Jones' Greatest Adventures", "Darius Twin", "Mega Man X2", "Final Fight 3", "Demon's Crest", "Out of This World", "Mega Man Soccer", "World Heroes", "Spider-Man and Venom: Maximum Carnage", "Tetris Attack", "Donkey Kong Country 3", "Final Fantasy: Mystic Quest", "Super Star Wars: Return of the Jedi", "Ultimate Mortal Kombat 3", "Joe and Mac", "Lemmings", "Street Fighter Alpha 2", "Harvest Moon", "Mega Man X3", "Fatal Fury: King of Fighters", "Breath of Fire II", "Final Fight 2", "PilotWings", "The Lion King", "Captain Commando", "Super Adventure Island", "ActRaiser 2", "Castlevania: Dracula X", "Art of Fighting", "Rock n Roll Racing", "Captain America and the Avengers", "Illusion of Gaia", "Final Fight", "Cool Spot", "Knights of the Round", "Stunt Race FX", "Ken Griffey Jr Presents Major League Baseball", "Tiny Toon Adventures: Buster Busts Loose", "Lost Vikings", "Dragon: The Bruce Lee Story", "Bulls vs. Blazers and the NBA Playoffs", "Blackthorne", "Batman Returns", "Populous", "Mortal Kombat", "The Death and Return of Superman"]

# https://gamefaqs.gamespot.com/boards/916396-super-nintendo/76022917
top100_gf = ["Legend of Zelda: A Link to the Past", "Chrono Trigger", "Super Mario World", "Final Fantasy III", "Super Metroid", "Super Mario RPG", "Super Mario Kart", "Super Mario All-Stars", "Donkey Kong Country 2", "Yoshi's Island", "Donkey Kong Country", "EarthBound", "Secret of Mana", "Final Fantasy II", "Mega Man X", "Kirby Super Star", "Lufia II: Rise of the Sinistrals", "Terranigma", "Final Fantasy V", "Teenage Mutant Ninja Turtles: Turtles in Time", "Trials of Mana", "Donkey Kong Country 3", "Super Castlevania IV", "Contra III: The Alien Wars", "Tales of Phantasia", "Street Fighter II Turbo", "Super Punch-Out", "Tetris Attack", "Star Fox", "F-Zero", "Illusion of Gaia", "Super Street Fighter II", "Secret of Evermore", "Breath of Fire II", "Harvest Moon", "Zombies Ate My Neighbors", "Mega Man X3", "Lufia and the Fortress of Doom", "Killer Instinct", "Street Fighter II", "Mega Man X2", "EVO", "Star Ocean", "ActRaiser", "Ogre Battle", "Super Ghouls n Ghosts", "Breath of Fire", "Rock n Roll Racing", "NBA Jam: Tournament Edition", "Soul Blazer", "Uniracers", "Gradius III", "Bahamut Lagoon", "Super Smash TV", "Mortal Kombat II", "UN Squadron", "Super Bomberman 2", "SimCity", "Mega Man 7", "Tecmo Super Bowl", "PilotWings", "Ken Griffey Jr Presents Major League Baseball", "R-Type III", "Tetris and Dr. Mario", "Goof Troop", "Kirby's Dream Course", "Mortal Kombat 3", "Sunset Riders", "Shadowrun", "Umihara Kawase", "Mario Paint", "Top Gear", "International Superstar Soccer Deluxe", "NBA Jam", "Super Double Dragon", "NHL 94", "Super Bomberman 5", "Mega Man and Bass", "Shin Megami Tensei", "Ultimate Mortal Kombat 3", "Demon's Crest", "Ken Griffey Jr's Winning Run", "Earthworm Jim", "Shin Kidou Senshi Gundam W: Endless Duel", "Tactics Ogre", "Winter Olympic Games: Lillehammer 94", "Final Fantasy: Mystic Quest", "Front Mission", "New Horizons", "Live-a-Live", "Street Fighter Alpha 2", "Super Tennis", "Legend of the Mystical Ninja", "Battletoads in Battlemaniacs", "Earthworm Jim 2", "Spider-Man and Venom: Maximum Carnage", "Space Megaforce", "Battletoads and Double Dragon", "Dragon Quest V", "Super Bomberman"]

# https://gamefaqs.gamespot.com/boards/916396-super-nintendo/78764676
top150_gf2 = ["Super Mario World", "Legend of Zelda: A Link to the Past", "Chrono Trigger", "Super Metroid", "Final Fantasy III", "Super Mario RPG", "Super Mario All-Stars", "Mega Man X", "Donkey Kong Country 2", "Yoshi's Island", "EarthBound", "Donkey Kong Country", "Final Fantasy II", "Lufia II: Rise of the Sinistrals", "Kirby Super Star", "Tetris Attack", "Mega Man X2", "Super Street Fighter II", "Secret of Mana", "Teenage Mutant Ninja Turtles: Turtles in Time", "Super Castlevania IV", "Contra III: The Alien Wars", "Donkey Kong Country 3", "Mega Man X3", "Wild Guns", "Breath of Fire II", "Street Fighter II Turbo", "Demon's Crest", "Ogre Battle", "International Superstar Soccer Deluxe", "Super Mario Kart", "Illusion of Gaia", "Super Punch-Out", "Tetris and Dr. Mario", "Ninja Warriors", "Sunset Riders", "ActRaiser", "NBA Jam: Tournament Edition", "Shadowrun", "Ultimate Mortal Kombat 3", "UN Squadron", "Street Fighter Alpha 2", "Kirby's Dream Land 3", "New Horizons", "Soul Blazer", "Rock n Roll Racing", "Secret of Evermore", "R-Type III", "Harvest Moon", "Lost Vikings", "Super Turrican 2", "Street Fighter II", "Cybernator", "Lost Vikings II: Norse by Norsewest", "Zombies Ate My Neighbors", "Tecmo Super Bowl", "Top Gear", "Top Gear 3000", "Space Megaforce", "Pocky and Rocky 2", "Mortal Kombat II", "Final Fight 3", "Star Fox", "Pocky and Rocky", "F-Zero", "Ken Griffey Jr's Winning Run", "Gradius III", "Mega Man 7", "Super Bomberman 2", "Biker Mice from Mars", "Hagane", "NBA Jam", "SimCity", "International Superstar Soccer", "Killer Instinct", "Legend of the Mystical Ninja", "The Adventures of Batman and Robin", "Sparkster", "Robotrek", "King of Dragons", "EVO", "Breath of Fire", "Saturday Night Slam Masters", "Axelay", "Top Gear 2", "Metal Warriors", "Ken Griffey Jr Presents Major League Baseball", "Flashback", "The Magical Quest Starring Mickey Mouse", "Earthworm Jim 2", "Super Bomberman", "Uniracers", "Super Ghouls n Ghosts", "Mortal Kombat 3", "Bust-A-Move", "Super Turrican", "Aladdin", "Ninja Gaiden Trilogy", "Donald Duck in Maui Mallard: Cold Shadow", "Aero Fighters", "Blackthorne", "Lufia and the Fortress of Doom", "Star Fox 2", "The Great Circus Mystery", "True Lies", "X-Men: Mutant Apocalypse", "Indiana Jones' Greatest Adventures", "Goof Troop", "Sky Blazer", "Batman Returns", "WeaponLord", "Earth Defense Force E.D.F.", "Super Star Wars: Return of the Jedi", "Earthworm Jim", "Knights of the Round", "Super Adventure Island II", "Prince of Persia", "Mario Paint", "PilotWings", "Plok", "Arkanoid: Doh It Again", "Out of This World", "Super Star Wars: The Empire Strikes Back", "Judge Dredd", "Super Smash TV", "Wario's Woods", "Final Fight 2", "Castlevania: Dracula X", "Marvel Super Heroes: War of the Gems", "Battletoads and Double Dragon", "Super Star Wars", "WWF Raw", "Kirby's Dream Course", "Spider-Man and Venom: Maximum Carnage", "Battle Clash", "Lemmings", "Super Tennis", "Super Double Dragon", "Captain Commando", "WWF Royal Rumble", "Tiny Toon Adventures: Buster Busts Loose", "Teenage Mutant Ninja Turtles: Tournament Fighters", "Brain Lord", "Venom and Spider-Man: Separation Anxiety", "Super R-Type", "Kirby's Avalanche", "Samurai Shodown", "Alien 3", "Desert Strike: Return to the Gulf", "Tetris 2"]

#https://www.reddit.com/r/snes/comments/l7yzdc/the_snes_subreddit_top_100_games_of_all_time/
top100_reddit = ["Super Mario World", "Legend of Zelda: A Link to the Past", "Chrono Trigger", "Super Metroid", "Final Fantasy III", "EarthBound", "Donkey Kong Country 2", "Donkey Kong Country", "Yoshi's Island", "Mega Man X", "Super Mario RPG", "Teenage Mutant Ninja Turtles: Turtles in Time", "Super Mario Kart", "Super Mario All-Stars", "Secret of Mana", "Super Castlevania IV", "Contra III: The Alien Wars", "F-Zero", "Final Fantasy II", "Donkey Kong Country 3", "Mega Man X2", "Terranigma", "Star Fox", "Street Fighter II Turbo", "SimCity", "NBA Jam", "Soul Blazer", "Zombies Ate My Neighbors", "ActRaiser", "Super Punch-Out", "Super Ghouls n Ghosts", "Axelay", "Tetris Attack", "Legend of the Mystical Ninja", "Kirby Super Star", "Pocky and Rocky", "Breath of Fire II", "International Superstar Soccer Deluxe", "Street Fighter II", "Sunset Riders", "Trials of Mana", "UN Squadron", "Lufia II: Rise of the Sinistrals", "Super Street Fighter II", "Wild Guns", "Space Megaforce", "Demon's Crest", "Illusion of Gaia", "Aladdin", "Final Fantasy V", "Mega Man X3", "Super Bomberman 2", "EVO", "Breath of Fire", "Earthworm Jim", "Killer Instinct", "Gradius III", "Mortal Kombat II", "Goof Troop", "Secret of Evermore", "Rock n Roll Racing", "Harvest Moon", "Super Bomberman", "Hagane", "Super Smash TV", "Ninja Warriors", "Metal Warriors", "PilotWings", "Live-a-Live", "Ogre Battle", "New Horizons", "Tactics Ogre", "Top Gear", "The Magical Quest Starring Mickey Mouse", "Mega Man 7", "Kirby's Dream Land 3", "Shadowrun", "Tecmo Super Bowl III", "Front Mission Gun Hazard", "Uniracers", "Tecmo Super Bowl", "Out of This World", "Ken Griffey Jr Presents Major League Baseball", "Cybernator", "R-Type III", "Dragon Quest V", "Tetris Battle Gaiden", "Kirby Avalanche", "Blackthorne", "Metal Marines", "Final Fantasy: Mystic Quest", "Lufia and the Fortress of Doom", "Kirby's Dream Course", "Sparkster", "Mortal Kombat", "Fire Emblem: Genealogy of the Holy War", "Super Star Wars", "Front Mission", "Castlevania: Dracula X", "Star Ocean"]

#http://www.sydlexia.com/top100snes.htm
top100_syd = ['Legend of Zelda: A Link to the Past', 'Super Metroid', 'Final Fantasy III', 'Super Mario World', 'Super Mario RPG', 'Chrono Trigger', 'Mega Man X', 'Final Fantasy II', 'EarthBound', 'Street Fighter II Turbo', 'Super Castlevania IV', 'Secret of Mana', 'ActRaiser', 'Contra III: The Alien Wars', "Yoshi's Island", 'Donkey Kong Country', 'Star Fox', 'Super Mario Kart', "Donkey Kong Country 2", 'Mortal Kombat II', 'Breath of Fire II', 'Illusion of Gaia', 'F-Zero', 'Zombies Ate My Neighbors', 'Teenage Mutant Ninja Turtles: Turtles in Time', 'Super Punch-Out', 'Mega Man X2', 'Soul Blazer', 'Ogre Battle', 'Secret of Evermore', 'SimCity', 'Spider-Man and Venom: Maximum Carnage', 'Mega Man X3', 'Killer Instinct', 'Mario Paint', 'Super Smash TV', 'Super R-Type', 'Earthworm Jim', 'Shadowrun', 'Lufia and the Fortress of Doom', 'Sparkster', 'Kirby Super Star', 'Super Star Wars', 'Super Mario All-Stars', 'Super Bomberman', 'Final Fight', 'PilotWings', 'Legend of the Mystical Ninja', 'EVO', 'Lufia II: Rise of the Sinistrals', 'Mega Man 7', 'Gradius III', "Super Ghouls n Ghosts", 'Super Bomberman 2', 'Battletoads in Battlemaniacs', 'Super Street Fighter II', 'Jurassic Park', 'Mortal Kombat 3', 'R-Type III', 'Super Double Dragon', 'Harvest Moon', 'WWF Royal Rumble', 'Tecmo Super Bowl III', 'Pocky and Rocky', 'Cybernator', 'ActRaiser 2', 'Knights of the Round', 'Castlevania: Dracula X', "Demon's Crest", "Donkey Kong Country 3", 'Breath of Fire', 'NBA Jam', 'Super Star Wars: The Empire Strikes Back', 'King of the Monsters', 'Super Adventure Island', 'X-Men: Mutant Apocalypse', 'Uniracers', 'Super Scope 6', 'The Adventures of Batman and Robin', 'Super Turrican', 'Tiny Toon Adventures: Buster Busts Loose', 'WCW SuperBrawl Wrestling', 'Batman Returns', 'Saturday Night Slam Masters', "Aladdin", 'Desert Strike: Return to the Gulf', 'Street Fighter II', 'Earthworm Jim 2', 'Mega Man Soccer', 'Super Star Wars: Return of the Jedi', 'Sunset Riders', 'Secret of the Stars', 'Final Fantasy: Mystic Quest', 'Tetris Attack', 'Out of This World', 'Ys III: Wanderers from Ys', 'Super Adventure Island II', 'The Death and Return Of Superman', 'Stunt Race FX', "NHL 94"]

ranking_lists = [top100_rs, top100_ign, top150_ranker, top100_complex, top100_gf, top150_gf2, top100_reddit, top100_syd]
top100_lists = [ranking[:100] for ranking in ranking_lists]

combinedset = set()
for ranking in ranking_lists:
    combinedset = combinedset | set(ranking)

N = len(combinedset)
print(N)

distinctPairs = [(x,y) for x in combinedset for y in combinedset if x!=y]




# %%
# Borda Count (tournament style)
from collections import Counter

borda = Counter()
for ranking in ranking_lists:
    for i, game in enumerate(ranking):
        borda[game] += N-i

borda.most_common()










































#%% 
# Schulze method

# Step 1: compute d(x,y) for each pair. 
# d(x,y) is the number of people who prefer x to y

dSchulze = Counter()

def checkPreference(ranking,x,y):
    # returns 1 if x ranked higher than y. Else returns 0
    if x not in ranking: return 0
    if y not in ranking: return 1
    return int(ranking.index(x) < ranking.index(y))

for x,y in distinctPairs:
    for ranking in ranking_lists:
        if checkPreference(ranking,x,y):
            dSchulze[(x,y)] += 1

# values of d implicitly define a directed graph.
# but we dont't want 2-cycles, so in the next step we'll ignore a connection 
# if the connection going the other way is stronger.

# Step 2: Initialize the values of path strength
# the strength of a given path is the lowest value of d along links in that path
# we want to find p(x,y), the strongest path connecting each x,y
# we start by setting p(x,y) according to the following rule:
# - if x would win against y when running 1-on-1, (d(x,y) > d(y,x)), set p(x,y)=d(x,y)
# - otherwise, set p(x,y) to zero.

pSchulze = Counter()
pred = dict()

for x,y in distinctPairs:
    if dSchulze[(x,y)] > dSchulze[(y,x)]: 
        pSchulze[(x,y)] = dSchulze[(x,y)]
    pred[(x,y)] = x

# Step 3: check for stronger indirect paths
# compare to Floyd–Warshall algorithm
# the strength of a path through a combined path is the strength of the lower of the two parts of the path
# "width" seems a better term than "strength".

for z in combinedset:
    for x,y in distinctPairs:
        new_p = min(pSchulze[(x,z)],pSchulze[(z,y)])
        if (x!=z and y!=z) and (new_p > pSchulze[(x,y)]):
            pSchulze[(x,y)] = new_p
            pred[(x,y)] = z


#%%
# Step 4: Combine these pairwise strengths into a ranking?
# somehow?
# Something has gone wrong. I am getting ties and the ties  do not define equivalence classes
# does  schulze require a complete ranking from each voter?
# define a binary relation 0

OSchulze = dict()
nonWinners = set()

for x,y in distinctPairs:
    if pSchulze[(x,y)] > pSchulze[(y,x)]:
        OSchulze[(x,y)] = True
        nonWinners.add(y)
    else:
        OSchulze[(x,y)] = False

combinedset-nonWinners

#%%
# Check to make sure the ordering is transitive
for z in combinedset:
    for x,y in distinctPairs:
        if (x!=z and y!=z):
            if OSchulze[(x,z)] and OSchulze[(z,y)]:
                assert OSchulze[(x,y)]

# This works. And it is evident from the definitions that the relationship is irreflexive and antisymmetric
# is it a graded poset though? (no)

#%%
# Use python graph libary to find ranking from partial ordering
# OSchulze is a binary relation defined by O(x,y) = True iff p(x,y) > p(y,x)
# In other words, O(x,y) means x would beat y in a one-on-one matchup.
import networkx as nx

OSchulze = nx.DiGraph()

for x,y in distinctPairs:
    if pSchulze[(x,y)] > pSchulze[(y,x)]:
        OSchulze.add_edge(x,y)

trOSchulze = nx.transitive_reduction(OSchulze)
list(trOSchulze.edges)

# In this transitive reduction, the successors of a game A
# are the games B which that game can beat, 
# with no third game C betwixt such that A beats C beats B

winners = []
for game in combinedset:
    if len(trOSchulze.pred[game]) == 0: winners.append(game)
assert len(winners) == 1
winner = winners[0]

losers = []
for game in combinedset:
    if len(trOSchulze.succ[game]) == 0: losers.append(game)

print(winners)
print(losers)

#%%
# crawl down the layers of the poset.
# we'll find out if the poset is graded or not

# It is not, in fact, graded.
# games can appear in multiple "ranks".

# assign ranks to them anyways, based on shortest path in tr to winner

layers = [winners]
currentLayer = winners
layerIndex = 1
rankMap = {winner: 0}

while True:
    #print(currentLayer)
    newLayer = set()
    for game in currentLayer:
        newLayer = newLayer | set(trOSchulze.succ[game])
    # add newly seen games to the rank mapping
    for game in newLayer:
        if game not in rankMap:
            rankMap[game] = layerIndex
    # go on to the next layer
    if len(newLayer) > 0:
        layers.append(newLayer)
        currentLayer = newLayer
        layerIndex += 1
    else:
        break


#%%
from collections import defaultdict
inferiorGames = defaultdict(list)
for x,y in distinctPairs:
    if pSchulze[(x,y)] > pSchulze[(y,x)]:
        inferiorGames[x].append(y)

winCounts = Counter({game: len(inferiorGames[game]) for game in inferiorGames.keys()})
winCounts.most_common()


#%%

# check to make sure equally ranked candidates actually would actually tie
# check to make sure higher-ranked candidates would beat all lower candidates
for x, y in distinctPairs:
    bundle = (x,y,winCounts[x],winCounts[y])
    if winCounts[x]==winCounts[y]:
        if pSchulze[(x,y)] != pSchulze[(y,x)]: print("Equivalence ERROR:", bundle)
    if winCounts[x] > winCounts[y]:
        if pSchulze[(x,y)] <= pSchulze[(y,x)]: print("Ranking ERROR:", bundle)


#%%
# Now check whether the pseudo-rank agrees with the #wins rule
for x, y in distinctPairs:
    bundle = (x,y,winCounts[x],winCounts[y], rankMap[x], rankMap[y])
    if winCounts[x]==winCounts[y]:
        if rankMap[x] != rankMap[y]: print("Equivalence ERROR:", bundle)
    if winCounts[x] > winCounts[y]:
        if rankMap[x] >= rankMap[y]: print("Ranking ERROR:", bundle)


# Section 5.1
# https://arxiv.org/ftp/arxiv/papers/1804/1804.02973.pdf
# > The Schulze relation , as defined in (2.2.1), is only a strict partial order.
# However, sometimes, a linear order is needed. In this section, we will show
# how the Schulze relation  can be completed to a linear order final(σ,μ)
# without having to sacrifice any of the desired criteria.

#%% Step 1: calculate TBRL
# Tie-Breaking Ranking of the Links

# Several ways to define >D. See 2.1
# I will use the margin method.

TBRL = nx.DiGraph()

edgeMargin = {(x,y): max(0,dSchulze[(x,y)] - dSchulze[(y,x)]) for x,y in distinctPairs}
edgeScoreToEdges = defaultdict(list)
for edge, margin in edgeMargin.items():
    edgeScoreToEdges[margin].append([edge])

totalCount = 0
for s1 in range(8,0,-1):
    for s2 in range(s1):
        totalCount += len(edgeScoreToEdges[s2])*len(edgeScoreToEdges[s1])

print("Edge to edge relation will have this many true entries:", totalCount)

# 1203205846 That's a lot!!!!!!
# still technically doable with optimization but eughh.
# not gonna calculate this one in place.

# I'm not going to try to calculate the linear ranking for Schulze.
# I think it's just not suited to this kind of analysis with very big C and very small N






















# %%
# Do some checks for duplicate titles
# Won't let me 
combinedset = set()
for ranking in ranking_lists:
    combinedset = combinedset | set(ranking)

for x in combinedset:
    for y in combinedset:
        if x!=y and (x in y):
            print(x)
            print(y)
            print()



# %%
# combine rankings
# https://stats.stackexchange.com/questions/178399/what-statistics-can-i-use-to-combine-multiple-rankings-in-order-to-create-a-fina
# https://stats.stackexchange.com/questions/56852/overall-rank-from-multiple-ranked-lists
# https://jmlr.org/papers/volume7/demsar06a/demsar06a.pdf

# No perfect options (see Arrow's Theorem)

# options:
# - take geometric mean of rankings
# - take arithmetic mean of rankings
# - Schulze method?
# - Borda Count

# handling missing values:
# assign missing items to rank 150?








#%%
