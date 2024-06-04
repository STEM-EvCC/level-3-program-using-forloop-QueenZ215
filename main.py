mission_names = ['Apollo 11', 'Challenger', 'Curiosity Rover', 'Viking 1', 'Mars Pathfinder', 'Hubble Telescope', 'Apollo 13']
mission_years = [1969, 1986, 2012, 1975, 1996, 1990, 1970]
mission_success = [True, False, True, True, True, True, False]
totalMission=0
sucess=0
year=2000

for i,v in enumerate(mission_names): 
	totalMission += 1 
	if mission_success[i] == True:
		sucess +=1
sucessRate = (sucess / totalMission) * 100

print(f"Total number of missions: {totalMission}")
print(f"Number of successful missions: {sucess:.2f}%")
print(f"Success rate: {sucessRate}")
print(f"Missions launched before the year {year}")

for i,v in enumerate(mission_names):
	if mission_years[i] < year:
		print(f"-  {mission_names[i].ljust(20)}{year- mission_years[i]}")
