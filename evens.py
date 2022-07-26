def even_number_of_evens(numbers):
    """
    Should raise a TypeError if a list is not passed into the function
    error message: "A list was not passed into the function"
    if numbers is empty return False
    if the number of even numbers is odd, return False
    if the number of even numbers is 0, return False
    if the number of even numbers is even, return True
    """

    if not isinstance(numbers, list):
        raise TypeError("A list was not passed into the function")

    evens = sum(1 for num in numbers if num % 2 == 0)
    return bool(evens and evens % 2 == 0)


if __name__ == '__main__':
    print(even_number_of_evens(5))
