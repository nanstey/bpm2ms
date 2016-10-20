import sys, argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("bpm", help="input value as beats per minute")
    parser.add_argument("-a", "--all", help="print all values DEFAULT", action="store_true")
    parser.add_argument("-s", "--straight", help="print straight values", action="store_true")
    parser.add_argument("-d", "--dotted", help="print dotted values", action="store_true")
    parser.add_argument("-t", "--triplet", help="print triplet values", action="store_true")
    args = parser.parse_args()

    if ( args.all | args.straight | args.dotted | args.triplet) == False:
        args.all = True

    durations = ["Half", "Quarter", "Eighth", "16th", "32th", "64th", "128th", "256th", "512th", "1024th"]

    sdurs = [] #Straight Durations
    ddurs = [] #Dotted Durations
    tdurs = [] #Triplet Durations

    ms = 240000/ float(args.bpm)

    sdurs.append("%s = %03.2fms" % ("Whole", ms))

    for x in range(10):
        tms = ms / 3
        ms = ms / 2
        dms = ms * 1.5
        dur = durations[x]

        ddurs.append("Dotted %s = %03.2fms" % (dur, dms))
        sdurs.append("%s = %03.2fms" % (dur, ms))
        tdurs.append("Triplet %s = %03.2fms" % (dur, tms))

    if (args.all | args.straight):
        print
        for dur in sdurs:
            print dur
    if (args.all | args.dotted):
        print
        for dur in ddurs:
            print dur
    if (args.all | args.triplet):
        print
        for dur in tdurs:
            print dur

if __name__ == "__main__":
    main()
