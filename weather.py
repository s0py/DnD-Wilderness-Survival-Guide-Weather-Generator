import random
# first we ask for the region
region = input("Region:\n1. Arctic\n2. Subarctic\n3. Temperate\n4. Subtropical\n5. Tropical\n")
# pick your biome
biome = input("Biome:\n1. Desert\n2. Forest\n3. Hills\n4. Mountains\n5. Plains\n6. Seacoast\n")

years = int(input('How many years?\n'))

region = int(region)-1
biome = int(biome)-1

temp_id = region*6 + biome

temp = [ [[0,4,7], [2,6,10], [5,9,11], [9,10,13], [9,10,12], [5,7,10], [3,6,9], [0,3,7], [0,1,7], [0,1,6], [0,1,7], [0,2,7]],  [[0,3,6], [1,4,8], [2,5,8], [3,6,11], [3,6,10], [2,5,9], [2,4,7], [1,4,7], [0,2,4], [0,1,4], [0,1,3], [0,2,5]],  [[0,3,6], [1,4,8], [2,5,8], [3,6,11], [3,6,10], [2,5,9], [2,4,7], [1,4,7], [0,2,4], [0,1,4], [0,1,3], [0,2,5]],  [[0,3,6], [1,4,8], [2,5,8], [3,6,11], [3,6,10], [2,5,9], [2,4,7], [1,4,7], [0,2,4], [0,1,4], [0,1,3], [0,2,5]],  [[0,4,7], [2,6,10], [5,9,11], [9,10,13], [9,10,12], [5,7,10], [3,6,9], [0,3,7], [0,1,7], [0,1,6], [0,1,7], [0,2,7]],  [[0,4,9], [2,6,10], [5,9,13], [9,10,15], [9,10,13], [4,8,11], [2,6,9], [0,4,8], [0,2,8], [0,2,7], [0,1,7], [0,2,7]],   [[2,6,9], [5,10,12], [9,11,13], [10,12,16], [9,12,16], [6,10,16], [5,7,12], [2,4,11], [0,2,8], [0,3,8], [0,3,9], [1,4,9]],  [[3,9,11], [7,10,13], [9,11,15], [10,12,17], [9,12,17], [8,10,15], [4,9,11], [1,7,10], [0,5,9], [0,4,9], [0,4,8], [1,6,10]],  [[2,6,9], [5,10,13], [9,11,13], [9,12,15], [8,12,15], [6,10,12], [3,9,11], [1,6,10], [0,3,9], [0,3,8], [0,3,8], [1,5,9]],  [[1,7,11], [4,9,12], [8,10,12], [9,11,13], [8,12,14], [6,10,12], [3,9,11], [1,5,10], [0,3,9], [0,2,8], [0,3,8], [0,5,9]],  [[2,6,9], [5,10,12], [9,11,13], [10,12,16], [9,12,16], [6,10,16], [5,7,12], [2,4,11], [0,2,8], [0,3,8], [0,3,9], [1,4,9]],  [[3,9,12], [7,10,13], [9,11,17], [10,12,17], [10,12,17], [9,11,15], [4,10,12], [2,7,11], [0,5,10], [1,5,10], [1,6,10], [2,7,10]],   [[12,13,22], [12,15,23], [15,15,25], [20,24,25], [20,24,25], [16,22,24], [13,18,23], [11,17,23], [10,12,17], [10,12,18], [10,12,19], [11,12,19]],  [[7,11,15], [10,13,20], [12,15,21], [12,18,23], [12,18,23], [11,15,21], [9,13,17], [5,9,11], [3,9,11], [2,5,11], [1,5,10], [4,10,15]],  [[8,11,17], [9,14,19], [9,16,23], [9,19,24], [11,19,24], [10,16,22], [9,13,19], [5,10,15], [2,9,12], [1,8,11], [2,9,12], [4,10,15]],  [[4,10,16], [5,11,18], [10,14,21], [11,16,23], [10,16,22], [8,13,20], [4,11,18], [2,10,17], [1,9,11], [0,8,11], [1,8,12], [2,9,13]],  [[6,11,18], [10,13,20], [11,15,23], [12,18,24], [12,18,24], [10,15,22], [6,11,18], [4,10,16], [2,9,12], [1,7,12], [2,7,13], [3,10,16]],  [[10,11,18], [10,12,19], [11,14,22], [12,15,23], [12,15,22], [11,14,22], [10,11,19], [6,10,15], [4,10,12], [4,9,12], [5,10,13], [8,10,16]],   [[13,19,23], [14,19,23], [17,21,24], [19,23,25], [19,23,25], [17,20,24], [15,20,24], [13,18,23], [12,15,22], [11,15,19], [11,15,20], [12,18,22]],  [[13,19,22], [13,19,23], [15,20,23], [15,20,23], [15,20,23], [14,20,22], [13,20,22], [12,18,21], [11,18,21], [11,19,20], [11,19,21], [12,19,21]],  [[12,18,21], [13,19,22], [14,20,23], [15,20,23], [15,20,24], [13,18,23], [12,16,21], [11,15,18], [10,13,17], [10,13,16], [10,14,17], [11,16,20]],  [[11,15,19], [12,16,20], [13,16,20], [13,15,19], [13,14,17], [11,14,17], [11,13,16], [11,13,16], [10,12,15], [10,12,15], [10,12,16], [11,15,18]],  [[13,18,23], [17,21,23], [18,22,24], [19,22,25], [19,22,25], [18,21,24], [16,21,24], [12,17,20], [11,15,18], [11,13,17], [10,14,18], [12,17,20]],  [[11,15,23], [12,16,23], [12,18,24], [13,18,24], [13,18,24], [12,17,23], [11,16,22], [10,14,20], [10,12,20], [11,12,20], [10,12,21], [10,14,22]],   [[15,20,23], [16,21,24], [19,22,25], [21,24,25], [21,24,25], [20,23,24], [20,21,23], [17,20,22], [16,18,21], [15,17,20], [15,18,19], [15,19,22]],  [[14,20,23], [14,20,23], [16,20,23], [16,20,23], [16,20,23], [16,20,23], [15,20,23], [14,20,22], [12,20,22], [12,20,22], [11,20,22], [12,20,22]],  [[15,17,20], [15,19,23], [16,20,24], [18,22,25], [18,22,25], [18,21,24], [16,19,22], [14,17,20], [13,16,19], [12,15,17], [13,15,19], [13,17,19]],  [[14,16,19], [14,16,20], [14,16,20], [13,15,19], [13,15,19], [13,15,19], [13,15,18], [12,15,18], [12,15,18], [12,15,17], [13,15,18], [13,16,19]],  [[15,17,20], [17,22,24], [19,22,24], [19,22,25], [19,22,25], [19,22,24], [17,21,24], [15,18,22], [13,17,20], [12,15,17], [13,16,19], [13,17,20]],  [[16,19,23], [16,19,23], [17,19,24], [17,19,23], [17,19,23], [17,19,22], [16,18,21], [16,18,21], [15,17,21], [15,18,20], [15,18,21], [14,19,22]] ]
hi = ["-20", "-15", "-5", "0", "10", "18", "25", "30", "35", "40", "50", "60", "65", "70", "70", "75", "80", "80", "85", "85", "90", "90", "95", "100", "105", "115"]
lo = ["-40", "-30", "-20", "-10", "0", "10", "10", "15", "15", "20", "30", "40", "45", "50", "55", "55", "60", "65", "65", "70", "70", "75", "75", "80", "80", "85"]

rain = [ [[0,1,0], [0,1,0], [0,1,0], [0,1,0]], [[0,0,1], [0,0,1], [0,0,1], [0,0,1]], [[0,0,1], [0,0,1], [0,0,1], [0,0,1]], [[0,0,1], [0,0,1], [0,0,1], [0,0,1]], [[0,2,1], [0,3,1], [0,1,1], [0,1,1]], [[0,2,1], [0,2,1], [0,2,1], [0,1,0]],  [[0,0,1], [0,0,1], [0,1,0], [0,1,0]], [[1,3,2], [1,3,2], [1,2,1], [0,2,1]], [[0,2,1], [1,2,1], [0,2,1], [0,1,1]], [[1,3,2], [1,2,1], [0,2,1], [0,1,1]], [[1,3,2], [1,3,2], [1,2,1], [0,2,1]], [[0,2,1], [1,3,2], [0,2,1], [0,1,1]],  [[0,1,0], [0,1,0], [0,0,0], [0,1,0]], [[2,4,3], [2,3,3], [2,3,3], [1,3,2]], [[2,4,3], [2,4,3], [1,3,2], [1,3,2]], [[0,3,2], [0,2,1], [0,3,2], [0,3,2]], [[2,4,3], [2,4,3], [1,3,2], [0,2,1]], [[1,3,2], [0,2,1], [2,4,3], [2,4,3]],  [[0,1,0], [0,0,0], [0,1,0], [0,1,0]], [[3,5,4], [3,5,4], [3,4,4], [3,4,4]], [[2,4,3], [2,4,3], [1,3,2], [1,2,2]], [[2,4,3], [2,3,3], [1,3,2], [1,3,2]], [[1,4,2], [1,3,2], [0,2,1], [0,2,1]], [[2,4,3], [2,5,3], [0,2,1], [1,3,2]],  [[0,1,0], [0,2,1], [0,1,0], [0,1,0]], [[3,5,4], [3,5,4], [3,5,4], [3,5,4]], [[0,1,0], [0,2,1], [1,3,2], [0,1,0]], [[1,3,2], [3,4,4], [1,3,2], [3,4,4]], [[0,1,0], [2,4,3], [3,4,3], [2,4,3]], [[0,1,0], [2,5,3], [4,5,5], [0,2,1]] ]

special_weather=[
[[4,1,3,3],[4,1,3,3],[4,1,3,3,],[4,1,3,3]],
[[4,1,3,3],[4,1,3,3],[4,1,3,3,],[4,1,3,3]],
[[4,1,3,5],[4,1,3,9],[4,1,3,3,],[4,1,3,3]],
[[4,1,3,5],[4,1,5,9],[4,1,3,5,],[4,1,3,3]],
[[1,4,3,5],[8,1,3,9],[4,1,3,9,],[4,1,3,3]],
[[1,4,5,9],[4,1,5,9],[4,1,5,9,],[4,1,3,3]],

[[4,1,3,3],[1,6,3,3],[4,1,3,3,],[4,1,3,3]],
[[1,8,3,9],[8,1,9,3],[1,8,5,3,],[4,1,3,9]],
[[1,4,3,9],[1,8,9,3],[4,1,5,3,],[4,1,5,3]],
[[1,8,5,9],[1,8,9,3],[4,1,5,3,],[4,1,3,5]],
[[1,8,3,9],[9,1,9,3],[4,1,3,9,],[4,1,5,3]],
[[4,1,5,9],[8,1,9,5],[1,4,5,9,],[4,1,5,9]],

[[4,6,3,9],[4,6,3,9],[6,4,3,9,],[1,6,3,9]],
[[4,8,5,9],[4,8,5,9],[1,8,5,9,],[1,8,5,9]],
[[1,8,9,7],[1,8,3,9],[1,8,3,9,],[1,8,5,9]],
[[1,8,5,9],[1,8,3,9],[8,1,3,9,],[1,8,5,3]],
[[1,8,7,9],[8,4,3,9],[8,1,3,9,],[1,4,3,9]],
[[1,8,5,9],[1,8,5,9],[1,8,5,9,],[1,8,5,9]],

[[4,6,3,9],[4,6,3,9],[4,6,3,9,],[1,6,3,9]],
[[8,4,9,5],[8,8,9,5],[1,8,5,9,],[8,1,5,9]],
[[1,8,3,7],[8,4,3,9],[1,8,9,5,],[1,8,3,9]],
[[1,8,9,5],[8,4,9,3],[8,1,9,5,],[1,8,3,9]],
[[8,4,7,9],[8,4,3,9],[4,1,3,9,],[1,8,3,9]],
[[2,8,5,9],[1,8,5,9],[1,8,3,9,],[1,8,3,9]],

[[4,6,3,9],[4,6,3,9],[4,6,3,9,],[1,6,3,9]],
[[8,8,9,5],[8,8,9,5],[8,8,5,9,],[8,8,5,9]],
[[4,8,3,9],[4,8,3,9],[4,4,9,3,],[1,4,3,9]],
[[1,8,5,9],[8,4,9,5],[1,4,5,9,],[1,8,5,9]],
[[4,8,3,9],[6,8,9,3],[4,8,9,3,],[4,8,3,9]],
[[1,8,5,9],[1,8,5,9],[8,1,9,5,],[8,1,3,9]]
]
special_weather_type = ["Not Special", "Cold Wave", "Cyclone/Hurricane/Typhoon", "Drought", "Gale", "Mist/Fog", "Sandstorm/Duststorm/Blowing Snow", "Tornado", "Extreme Precipitation", "Heat Wave"]

humidity = ['llll', 'llll', 'llll', 'llll', 'llll', 'llll',  'llll', 'mmll', 'llll', 'mlll', 'mmll', 'mmll',  'llll', 'hmmm', 'hhmm', 'mlml', 'hhmm', 'mmhh',  'llll', 'hhhh', 'hhhm', 'hhhm', 'hmlm', 'hhmm',  'llll', 'hhhh', 'mhmm', 'hhhm', 'hhhm', 'hhmm']
humidity_eff_temp = [ [0,0,0,0,0], [0,0,0,0,0], [5,0,0,0,0], [10,5,0,0,0], [10,5,0,0,0],  [0,0,0,0,0], [0,0,0,0,0], [5,0,0,0,0], [10,5,0,0,0], [10,5,5,0,0],  [0,0,0,0,0], [5,0,0,0,0], [5,5,0,0,0], [10,5,5,0,0], [15,10,5,0,0],  [0,0,0,0,0], [5,5,0,0,0], [10,5,5,0,0], [15,10,5,5,0], [20,15,10,5,0],  [0,0,0,0,0], [10,5,0,0,0], [15,10,5,5,0], [20,15,10,5,5], [25,20,15,10,5] ]

rain_type = ["No Precipitation", "Trace Rain (<1/8 inch)", "Light Rain (<1/2 inch)", "Moderate Rain (<3/4 inch)", "Heavy Rain (<1.5 inch)", "Downpour Rain (>1.5 inch)"]
snow_type = ["No Precipitation", "Trace Snow (1/2 inch)", "Light Snow (1 inch)", "Moderate Snow (2 inch)", "Heavy Snow (4 inch)", "Noreaster Snow (>4 inch)"]

wind = 0
winddir = "Indescernable"

windchills = [ [0,-15,-20,-25,-30,-30,-35,-35], [-5,-15,-20,-25,-30,-30,-35,-35], [-5,-15,-25,-30,-30,-35,-40,-40], [-5,-20,-35,-30,-35,-40,-40,-45], [-5,-20,-25,-30,-35,-40,-45,-45], [-5,-20,-30,-35,-40,-40,-45,-50], [-5,-20,-30,-35,-40,-45,-50,-50], [-5,-20,-35,-35,-40,-45,-50,-50], [-5,-20,-35,-40,-45,-50,-55,-60], [-5,-20,-35,-40,-50,-50,-55,-60], [-5,-25,-35,-45,-55,-60,-65,-65], [-5,-25,-40,-50,-55,-60,-65,-70], [-5,-25,-40,-50,-60,-65,-65,-70], [-5,-30,-40,-50,-60,-65,-70,-70], [-5,-30,-45,-55,-60,-65,-70,-75], [-5,-30,-45,-55,-65,-70,-75,-75], [-5,-30,-45,-55,-65,-70,-75,-75] ]

month_names = ["Thaumont", "Flaurmont", "Yarthmont", "Klairmont", "Felmont", "Fyrmont", "Ambyrmont", "Sviftmont", "Eirmont", "Kaldmont", "Nuwmont", "Vatermont"]
week_day_names = ["Lunadain", "Gromdain", "Tserdain", "Moldain", "Nytdain", "Loshdain", "Soladain"]

month = -1
days = 336*years
temp_today   = temp[temp_id][0][1]
precipitation = 0

days_at_max = 0
days_at_min = 0

special_dummy = 0
spec = "Normal"
special_duration = 0

f = open("{}{}_weather.txt".format(region,biome), "w")
f.write('day, weekday, month, monthday, hi, lo, precip, humiditymod, wind, windir, eff_high, eff_low, spec\n')


#we are going to be doing an entire year's worth of temp
#a year is 28*12=336 days long
for day_raw in range(0,days):
	day = day_raw%336
	if day%336 == 0:
		month = -1
	#we need to see if we are at the start of a new month
	if day % 28 == 0:
		month += 1
		#if we are at a new month, we need to adjust 
		#the max_hi and min_lo
		max_hi = temp[temp_id][month][2]
		min_lo = temp[temp_id][month][0]

	#get the season from the month
	season = month % 4

	#roll the dice to modify the temp
	die_1 = random.randint(1,6)
	die_2 = random.randint(1,6)
	die_3 = random.randint(1,6)
	die_4 = random.randint(1,6)
	die_sum = die_1 + die_2

#first thing we need to check for is special weather
	if special_dummy == 0:
		if (die_1 + die_2) == 2 :
			if die_3 + die_4 < 8:
				special_dummy = 1
				special_id = 1
			if die_3 + die_4 < 5:
				special_dummy = 1
				special_id = 0
		if (die_1 + die_2) == 12:
			if die_3 + die_4 > 9:
				special_dummy = 1
				special_id = 3
			elif die_3 + die_4 > 6:
				special_dummy = 1
				special_id = 2
		spec = "Normal"

#are we already at special weather?
#when we're in a special weather condition,
	if special_dummy == 1:
		# we check for which one
		#coldwave
		if special_weather[temp_id][season][special_id] == 1:
			spec = "Coldwave"
			#see if it's still active or if we need to start
			if special_duration < 1:
				special_duration = random.randint(3,6)
				temp_today -= 4
			if special_duration > 0:
				if min_lo == 0:
					high = -30
					low = -50
				else:
					temp_today = min_lo - 1

		#hurricane
		if special_weather[temp_id][season][special_id] == 2:
			spec = "Hurricane"
			#see if it's still active or if we need to start
			if special_duration < 1:
				special_duration = 4
			if special_duration == 4:
				rain_text = "Lightning Storm (3 inch)"
				wind = 25
				winddir = "From Tropics"
			elif special_duration == 3:
				wind = random.randint(1,6)*20 + 60
				winddir = "From Tropics"
				rain_text = "Hurricane (<12 inch)"
			elif 0 < special_duration < 3:
				wind = 10
				winddir = "Prevailing"
				precipitation = "No Precipitation"
				h_die_1 = random.randint(1,6)
				h_die_2 = random.randint(1,6)
				if h_die_2 + h_die_1 < 7:
					temp_today -= 1
				if h_die_2 + h_die_1 > 7:
					temp_today += 1

		#drought
		if special_weather[temp_id][season][special_id] == 3:
			spec = "Drought"
			#see if it's active or if we need to start
			if special_duration < 1:
				special_duration = random.randint(1,6) + random.randint(1,6) + 2
			if special_duration > 0:
				rain_text = "No Precipitation"

		#gale
		if special_weather[temp_id][season][special_id] == 4:
			spec = "Gale"
			wind = random.randint(1,6)*5 + 40
			winddir = "Prevailing"

		#mist and fog
		if special_weather[temp_id][season][special_id] == 5:
			m_die = random.randint(1,6)
			if m_die < 5:
				spec = "Morning Mist/Fog: {} hours".format(m_die)
			else:
				spec = "Evening Mist/Fog: {} hours".format(m_die)

		#sandstorm/blizzard/duststorm
		if special_weather[temp_id][season][special_id] == 6:
			spec = "Particle Storm"


		#tornado
		if special_weather[temp_id][season][special_id] ==7:
			spec = "Tornado"
			wind = 200

		#extreme precipitation
		if special_weather[temp_id][season][special_id] == 8:
			spec = "Extreme Precipitation"

		#heat wave
		if special_weather[temp_id][season][special_id] == 9:
			spec = "Heatwave"
			#see if it's still active or if we need to start
			if special_duration < 1:
				special_duration = random.randint(3,6)
				temp_today += 4
			if special_duration > 0:
				if max_hi == 25:
					high = 125
					low = 90
				else:
					temp_today = max_hi + 1

	special_duration -= 1
	if special_duration < 1:
		special_dummy = 0




#control for the days spent at an extreme
	if temp_today == max_hi:
		days_at_max += 1
		die_sum -= days_at_max
	if temp_today == min_lo:
		days_at_min += 1
		die_sum += days_at_min
	if temp_today != max_hi or temp_today != min_lo:
		days_at_min = 0
		days_at_max = 0	

#temp only if we're not in a special condition
	if spec != "Coldwave" or spec != "Heatwave" or spec != "Hurricane":
		#use the die rolls to modify the temp
		if die_sum < 3:
			temp_today -= 3
		elif die_sum == 3 or die_sum == 4:
			temp_today -= 2
		elif die_sum == 5 or die_sum == 6:
			temp_today -= 1
		elif die_sum == 7:
			temp_today += 0
		elif die_sum == 8 or die_sum == 9:
			temp_today += 1
		elif die_sum == 10 or die_sum == 11:
			temp_today += 2
		elif die_sum > 11:
			temp_today += 3
		#handle the temp going beyond the bounds
		if temp_today > max_hi:
			temp_today = max_hi
		if temp_today < min_lo:
			temp_today = min_lo

	
#precipitation
	#only do it when we're not at hurricane or extreme precipitation or drought
	if spec != "Hurricane" and spec != "Extreme Precipitation" and spec != "Drought":
		#we only do precipitation when the dice total is even
		if (die_1 + die_2) % 2 == 1:
			precipitation = 0
			rain_text = "No Precipitation"
		if (die_1 + die_2) % 2 == 0:
			if die_1 > die_2:
				precipitation = rain[temp_id][season][0]
			elif die_2 > die_1:
				precipitation = rain[temp_id][season][2]
			elif die_1 == die_2:
				precipitation = rain[temp_id][season][1]
			#cold enough for snow?
			if temp_today < 10:
				rain_text = snow_type[precipitation]
			else:
				rain_text = rain_type[precipitation]
	

#determine hi and lo for the day
	#only if there is no heat or cold wave
	if spec != "Coldwave" and spec != "Heatwave":
		high = int(hi[temp_today])
		low = int(lo[temp_today])

#determine the humidity
	humidity_today = humidity[temp_id][season]
	if humidity_today == 'l':
		h = 1
		humidity_mod = random.randint(21,40)
	elif humidity_today == 'm':
		h = 2
		humidity_mod = random.randint(41,70)
	elif humidity_today == 'h':
		h = 3
		humidity_mod = random.randint(71,90)

#wind
	#only if we're not in a hurricane or tornado or gale
	if spec != "Hurricane" and spec != "Gale" and spec != "Tornado":
		if (die_2 + die_1) == 2:
			wind = 0
			winddir = "Indescernable"
		elif (die_2 + die_1) == 3:
			wind += 15
			winddir = "From Arctic"
		elif (die_2 + die_1) == 4:
			wind += 10
			winddir = "From Arctic"
		elif (die_2 + die_1) == 5:
			wind += 15
			winddir = "Prevailing Direction"
		elif (die_2 + die_1) == 6:
			wind += 10
			winddir = "Prevailing Direction"
		elif (die_2 + die_1) == 7:
			wind += 0
			winddir = "Prevailing Direction"
		elif (die_2 + die_1) == 8:
			wind += -10
			winddir = "Prevailing Direction"
		elif (die_2 + die_1) == 9:
			wind += -15
			winddir = "Prevailing Direction"
		elif (die_2 + die_1) == 10:
			wind += -10
			winddir = "From Tropics"
		elif (die_2 + die_1) == 11:
			wind += -15
			winddir = "From Tropics"
		elif (die_2 + die_1) == 12:
			wind = 0
			winddir = "Indescernable"
	
		if wind < 1:
			wind = 0
			winddir = "Indescernable"
		if wind > 45:
			wind = 45

#effective temperatures
	eff_high = high
	eff_low = low

	#effective temp and humdity and windspeed
	w = int(wind/20)
	high_faux = high
	low_faux = low
	if high_faux > 104:
		high_faux = 104
	if low_faux > 104:
		low_faux = 104
	if w > 4:
		w = 4
	if high > 54:
		eff_high = high + humidity_eff_temp[5*int((high_faux-55)/10) + h][w]
	if low > 54:
		eff_low = low + humidity_eff_temp[5*int((low_faux-55)/10) + h][w]

	#windchill
	if high < 36:
		if wind < 5:
			w_wc = 0
		if wind > 4:
			w_wc = int((wind-5)/5)
		if wind > 39:
			w_wc = 7
		eff_high = windchills[int((high * -1 + 35)/5)][w_wc]
	if low < 36:
		if wind < 5:
			w_wc = 0
		if wind > 4:
			w_wc = int((wind-5)/5)
		if wind > 39:
			w_wc = 7
		low_faux = low
		if low_faux < 49:
			low_faux = 49
		eff_low = windchills[int((low_faux * -1 + 35)/5)][w_wc]

# particle storms require us to have already done a lot of stuff
	if spec == "Particle Storm":
		rain_text = "No Precipitation"
# extreme precipitation requries us to have already done a lot of stuff
	if spec == "Extreme Precipitation":
		x_die = random.randint(1,6)
		if temp < 0:
			rain_text = "No Precipitation"
			if region < 3:
				if x_die < 4:
					rain_text = "Severe Snowstorm"
		elif -1 < temp < 10:
			rain_text = "No Precipitation"
			if region < 3:
				if x_die < 6:
					rain_text = "Severe Snowstorm"
		elif 9 < temp < 30:
			if region < 3:
				if x_die < 6:
					rain_text = "Severe Snowstorm"
				if x_die == 6:
					rain_text = "Ice/Sleet Storm"
		elif 29 < temp < 36:
			if region < 3:
				if x_die < 5:
					rain_text = "Severe Snowstorm"
				if x_die == 5:
					rain_text = "Hailstorm"
				if x_die == 6:
					rain_text = "Ice/Sleet Storm"
			if region > 2:
				rain_text = "Hailstorm"
		elif 35 < temp < 50:
			if region < 3:
				if x_die < 5:
					rain_text = "Lightning Storm"
				if x_die > 4:
					rain_text = "Hailstorm"
			if region > 2:
				rain_text = "Lightning Storm"
				if x_die == 6:
					rain_text = "Hailstorm"
		elif 49 < temp < 75:
			rain_text = "Lightning Storm"
			if region < 3:
				rain_text = "Lightning Storm"
				if x_die == 6:
					rain_text = "Hailstorm"
		elif 74 < temp:
			rain_text = "Lightning Storm"

#output
	#print("{}, {} {}\nHigh: {}  Low: {}\n{}\n".format(week_day_names[(day%28)%7], month_names[month], (day%28)+1, high, low, rain_text))
	f.write("{}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}\n".format(day_raw, week_day_names[(day%28)%7], month_names[month], (day%28)+1, high, low, rain_text, humidity_mod, wind, winddir, eff_high, eff_low, spec))

f.close()