import sys


def main():
    coordinate_tuple = (42.376, -71.115) # immutable
    coordinate_list = [42.376, -71.115]
    lonitude, latitude = coordinate_tuple 
    print(f"Coordinate Tuple: {coordinate_tuple[0], coordinate_tuple[1]}") 
    print(f"Coordinate List: {coordinate_list[0]}, {coordinate_list[1]}")

    print(f"{sys.getsizeof(coordinate_tuple)} bytes")
    print(f"{sys.getsizeof(coordinate_list)} bytes")


main()
