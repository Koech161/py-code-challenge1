from lib.add_num import add_numbers
from lib.apply_decorator import apply_decorator
from lib.calculate_factorial import calculate_factorial
from lib.count_vowels import count_vowels
from lib.is_even import is_even
from lib.merge_dicts import merge_dicts
from lib.oop import Car
from lib.reverse_string import reverse_string
from lib.sort_by_age import sort_by_age

def main():
    print("add_numbers(4, 2):", add_numbers(4, 2))

 
    print("is_even(4):", is_even(4))
    print("is_even(7):", is_even(7))

    print("reverse_string('Abel'):", reverse_string("Abel"))

    print("count_vowels('hello world'):", count_vowels("hello world"))

  
    print("calculate_factorial(5):", calculate_factorial(5))

  
    students = [('Abel', 21), ('Eve', 22), ('Bob', 25), ('Diana', 27), ('Charlie', 28)]
    print("sort_by_age(data):", sort_by_age())

 
    dict1 = {"a": 1, "b": 2}
    dict2 = {"b": 3, "c": 4}
    print("merge_dicts(dict1, dict2):", merge_dicts(dict1, dict2))

  
    my_car = Car(make="Toyota", model="Camry", year=2022)
    my_car.display_info()

if __name__ == "__main__":
    main()