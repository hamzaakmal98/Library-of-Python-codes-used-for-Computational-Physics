def decimal_to_binary(decimal):
    binary = ""
    while decimal > 0:
        binary = str(decimal % 2) + binary
        decimal //= 2
    return binary

# Test case 1: converting decimal 13 to binary
assert decimal_to_binary(13) == '1101'

# Test case 2: converting decimal 42 to binary
assert decimal_to_binary(42) == '101010'

# Test case 3: converting decimal 255 to binary
assert decimal_to_binary(255) == '11111111'
