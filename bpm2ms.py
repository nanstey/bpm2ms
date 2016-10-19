import sys
# from music21 import duration

durations = ["Half", "Quarter", "Eigth", "16th", "32th", "64th", "128th", "256th", "512th", "1024th"]

sdurs = [] #Straight Durations
ddurs = [] #Dotted Durations
tdurs = [] #Triplet Durations

bpm = float(sys.argv[1])
ms = 240000/bpm

sdurs.append("%s = %03.2fms" % ("Whole", ms))

for x in range(10):
    tms = ms / 3
    ms = ms / 2
    dms = ms * 1.5
    dur = durations[x]

    ddurs.append("Dotted %s = %03.2fms" % (dur, dms))
    sdurs.append("%s = %03.2fms" % (dur, ms))
    tdurs.append("Triplet %s = %03.2fms" % (dur, tms))

print
for dur in sdurs:
    print dur

print
for dur in ddurs:
    print dur

print
for dur in tdurs:
    print dur
