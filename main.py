# Add python code in this file
# -*- coding: utf-8 -*-

import csv


def get_cities():
    with open('cities.csv') as f:
        cities = [city for city in csv.DictReader(f)]
        return cities


def process_points():
    with open('points.csv') as f:
        points = []
        cities = get_cities()
        for point in csv.DictReader(f):
            for city in cities:
                TopLeft_X = int(city['TopLeft_X'])
                TopLeft_Y = int(city['TopLeft_Y'])
                BottomRight_X = int(city['BottomRight_X'])
                BottomRight_Y = int(city['BottomRight_Y'])
                point_X = int(point['X'])
                point_Y = int(point['Y'])

                in_x_range = (BottomRight_X >= point_X >= TopLeft_X)
                in_y_range = (BottomRight_Y >= point_Y >= TopLeft_Y)

                if in_x_range and in_y_range:
                    point['City'] = city['Name']
                    break

            if not point.get('City'):
                point['City'] = 'None'
            points.append(point)
        return points


if __name__ == '__main__':
    with open('output_points.csv', 'w') as f:
        fieldnames = ['ID', 'X', 'Y', 'City']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        points = process_points()
        writer.writeheader()
        writer.writerows(points)
