# Finds the number of valid passwords with a certain criteria Pt 2.
def main():
    # Opens the text file for processing
    with open('input.txt', 'r') as f:
        # Number of valid passwords set to 0
        count = 0
        # Goes through each line of the text file and checks if the password is valid
        for line in f:
            # Makes the line easier to process and splits it into an array
            contents = line.replace(':', '').split(' ')
            # Stores each component of the array as needed
            indices, target, password = contents[0].split('-'), contents[1], contents[2]
            # Stores the integers corresponding to the least and most amount of the target letter allowed
            index1, index2 = int(indices[0]) - 1, int(indices[1]) - 1
            # Stores the length of the password for quick access
            length = len(password)
            # Number of occurrences of the target character in the two specified indices
            occurrences = 0
            # If the password has a character at the first index
            if length > index1:
                # If the character at the first specified index is the target character, increment occurrences
                if password[index1] == target:
                    occurrences += 1
                # If the password has a character at the second index
                if length > index2:
                    # If the character at the second specified index is the target character, increment occurrences
                    if password[index2] == target:
                        occurrences += 1
            # Only add to the valid password count if it only occurs once out of the two indices
            if occurrences == 1:
                count += 1
        # Prints out the number of valid passwords
        print('%d valid passwords' % count)


# Executes the main method
if __name__ == '__main__':
    main()
