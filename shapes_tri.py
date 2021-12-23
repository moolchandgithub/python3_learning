import sys
import json
import yaml
import pathlib
from shapes.triangle import Triangle

def main(args):
    
    """ Area of Triangle from JSON file"""
    tri = get_triangle("inputs/triangle.json")
#    tri = get_triangle("inputs/triangle.yaml")
    
    for triang in tri:
        print(f"Area of Triangle is : {triang.area()}")
        print(f"Perimeter of Triangle is : {triang.perimeter()}")
        print(f"Triangle is Equilateral : {triang.isEquilateral()}")
        print(f"Triangle is Isoscele : {triang.isIsosceles()}")
        print("")
    
    # Create a list of shapes as dictionaries and write as JSON
    with open("outputs/triangle.json", "w") as handle:
        json.dump([gs.to_dict() for gs in tri], handle, indent=4)

def get_triangle(filename):
    
    file_extension = pathlib.Path(filename).suffix
    
    if file_extension == ".json":
        """ Read JSON input file for sides """
        print("************ Reading JSON ****************")
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
        except json.decoder.JSONDecodeError as error:
                print(error)
                raise
        finally:
            file.close()
            
        side = []
        for sides in data["tri_list"]:
            if sides["side1"] + sides["side2"] <= sides["side3"] or sides["side2"] + sides["side3"] <= sides["side1"] or sides["side1"] + sides["side3"] <= sides["side2"]:
                print(f'**** Given Values {sides["side1"]}, {sides["side2"]}, {sides["side3"]} are not a valid Triangle values. ****')
                break
            newsides = Triangle(sides["side1"], sides["side2"], sides["side3"])
            side.append(newsides)
        return side
    
    if file_extension == ".yaml":
        """ Read YAML input file for sides """
        print("************ Reading YAML ****************")
        try:
            with open(filename, 'r') as file:
                data = yaml.safe_load(file)
        except yaml.YAMLError as error:
                print(error)
                raise
        finally:
            file.close()

        side = []
        for sides in data["tri_list"]:
            side_list = data["tri_list"][sides]
            side1 = side_list[0]
            side2 = side_list[1]
            side3 = side_list[2]
            if side1 + side2 <= side3 or side2 + side3 <= side1 or side1 + side3 <= side2:
                print(f"**** Given Values {side1}, {side2}, {side3} are not a valid Triangle values. ****")
                break
            newsides = Triangle(side1, side2, side3)
            side.append(newsides)
        return side
        
if __name__ == "__main__":
    main(sys.argv)        