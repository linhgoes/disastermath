import csv
codereader = csv.reader(open('country-codes.txt', 'r'), delimiter="\t")
devreader = csv.reader(open('development_code.txt', 'r'), delimiter="\t")

alpha3to2 = {}
i = 0
next(codereader)
for row in codereader:
	alpha3to2[row[1]]=row[0]

i = 0
next(devreader)
for row in devreader:

	if row[1] in alpha3to2 and row[6]:
		alpha2 = alpha3to2[row[1]].lower()
		pct = int(row[6])
		if pct == 5:
			fill = "#006D2C"
		elif pct == 4:
			fill = "#2CA25F"
		elif pct == 3:
			fill = "#66C2A4"
		elif pct == 2:
			fill = "#B2E2E2"
		elif pct == 1:
			fill = "#EDF8FB"
		
		else:
			fill = "#CCCCCC"
		print '.' + alpha2 + ' { fill: ' + fill + '}'
	
	i += 1