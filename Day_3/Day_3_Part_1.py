# Finds the trees encountered along the slope
def main():
    # Opens the text file for processing
    with open('input.txt', 'r') as f:
        # Number of trees encountered set to 0
        trees = 0
        position = 0
        length = len(f.readline()) - 1
        # Goes through each line of the text file and checks if there is a tree along the slope
        for line in f:
            # Increments the horizontal position, accounting for when the pattern repeats
            position = (position + 3) % length
            # Checks if there is a tree at the current location
            trees += 1 if line[position] == "#" else 0
        # Prints out the number of trees encountered
        print('%d trees encountered' % trees)


# Executes the main method
if __name__ == '__main__':
    main()
