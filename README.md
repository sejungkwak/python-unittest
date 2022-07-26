# Python unittest

## Function Pseudo Code

```
our_function(list_of_numbers):

    raise TypeError if list not passed into function

    if list contains an even number of even numbers:

        return True
```

## Suggested Tests

1. Should raise a __TypeError__ if a list is not passed into the function
2. If numbers is __empty__, return False
3. If the number of even numbers is __odd__, return False
4. If the number of even numbers is __0__, return False
5. If the number of even number is __even__, return True