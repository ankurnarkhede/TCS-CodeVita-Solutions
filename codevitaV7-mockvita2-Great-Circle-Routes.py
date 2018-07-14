# 3
#
# 0N,1W
#
# 0N,179E
#
# 90N,0E

import sys
import math

latitude = []
longitude = []


def find_float_ratio(angle):
    return (angle / 360)


def find_angle_subtended_at_centre(lati, longi, i):
    latitude_2 = math.radians (lati[i])
    latitude_1 = math.radians (lati[i - 1])

    longitude_2 = math.radians (longi[i])
    longitude_1 = math.radians (longi[i - 1])

    first_term = math.pow (math.sin ((latitude_2 - latitude_1) / 2), 2)
    second_term = math.cos (latitude_1) * math.cos (latitude_2) * math.pow (math.sin ((longitude_2 - longitude_1) / 2),
                                                                            2)

    central_angle = 2 * math.asin (math.sqrt (first_term + second_term))

    return math.degrees (central_angle)


def main():
    distance = 0
    radius = 6400
    n = int (sys.stdin.readline ().strip ())
    for i in range (0, n, +1):
        lati, longi = (map (str, sys.stdin.readline ().strip ().split (',')))

        # stripping and adjusting signs
        if (lati[-1] == 'S'):
            lati = -int (lati[:-1])
        else:
            lati = int (lati[:-1])

        if (longi[-1] == 'W'):
            longi = -int (longi[:-1])
        else:
            longi = int (longi[:-1])

        latitude.append (lati)
        longitude.append (longi)

        # print('latitude= {} ; longitude= {} '.format(latitude,longitude))

        if (i == 0):
            continue

        angle = find_angle_subtended_at_centre (latitude, longitude, i)

        ratio = find_float_ratio (angle)

        # print("angle= {}; Ratio= {}".format(angle,ratio))

        distance_this_travel = ratio * 2 * math.pi * radius
        distance += distance_this_travel

        # print('Distances=',distance_this_travel,distance)
    print (round (distance))


if __name__ == "__main__":
    main ()
