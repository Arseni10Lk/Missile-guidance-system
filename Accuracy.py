from math import pi, cos, radians, sqrt, acos, sin


def accuracy(blast_radius, LAT_TARGET, LON_TARGET, LAT_ACTUAL, LON_ACTUAL):
    d_LON = abs(LON_ACTUAL - LON_TARGET) * pi / 180 * 6367449 * cos(radians((LAT_TARGET+LAT_ACTUAL)/2))  # m
    d_LAT = abs(LAT_ACTUAL - LAT_TARGET) * pi / 180 * 6367449  # m
    distance = sqrt(d_LON**2 + d_LAT**2)
    common_area_width = 2*blast_radius-distance;
    if common_area_width <= 0:
        return 0

    centr_angle = 2 * acos((blast_radius-common_area_width/2)/blast_radius)  # rad
    sector_area = centr_angle * blast_radius**2 / 2
    fragment_area = sector_area - 1/2*blast_radius**2*sin(centr_angle)
    intersection_area = fragment_area*2
    return intersection_area/(pi*blast_radius**2)*100  # %


print("%.2f" % accuracy(1000, 34.6588, -118.769745, 34.66386, -118.7713735))
