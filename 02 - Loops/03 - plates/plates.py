def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")
        
def is_valid(plate):
    hasNumber = False

    # Minimum 2 characters and maximum 6 characters        
    if  len(plate) < 2 or len(plate) > 6:
        return False
    
    for character in plate:

        # Start with at least 2 letters
        if not plate[1:2].isalpha():
            return False
            
        # No special characters such as symbols, spaces and ponctuations
        if not character.isalnum():
            return False
        
        # Numbers cannot be in the middle of the plate and first number used cannot be a 0 
        if character.isdigit():
            if not hasNumber:
                if character == '0':
                    return False
                hasNumber = True
        else:
            if hasNumber:
                return False
            
    return True
    
main()