# Finds the number of valid passwords with a certain criteria
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
            least_most, target, password = contents[0].split('-'), contents[1], contents[2]
            # Stores the integers corresponding to the least and most amount of the target letter allowed
            least, most = int(least_most[0]), int(least_most[1])
            # Checks if the criteria is satisfied and adds to the count of valid passwords if satisfied
            count += 1 if (least <= password.count(target) <= most) else 0
        # Prints out the number of valid passwords
        print('%d valid passwords' % count)


# Executes the main method
if __name__ == '__main__':
    main()
