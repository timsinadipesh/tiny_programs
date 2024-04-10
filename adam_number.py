def check_adam_number(num):
    """
    An Adam number is a number that verifies this property: 
    its square is the reverse of the square of its reverse

    takes an integer num
    returns True if this number is an Adam number, otherwise False
    """
    rev = str(num)
    rev = int(rev[-1::-1])

    num2, rev2 = num**2, rev**2
    
    num2, rev2 = str(num2), str(rev2)

    if num2 == rev2[-1::-1]:
        return True

    return False

print(check_adam_number(31))