# Finds the product of the trees encountered along each slope
def main():
    print("%d is the product" % (trees_encountered(1, 1) * trees_encountered(3, 1) * trees_encountered(5, 1) *
          trees_encountered(7, 1) * trees_encountered(1, 2)))


# Finds the trees encountered along a defined slope with integers right and down
def trees_encountered(right, down):
    # Opens the text file for processing
    with open('input.txt', 'r') as f:
        # Number of trees encountered set to 0
        trees = 0
        position = 0
        length = len(f.readline()) - 1
        # Goes through each line of the text file and checks if there is a tree along the slope
        for line in f:
            # Goes down the correct number of lines
            for x in range(down - 1):
                # Makes sure there is a line before going down
                if f:
                    line = f.readline()
                # End of text file if there is no line, so set the line variable to None and end the loop
                else:
                    line = None
                    break
            # Also end the outer loop if no more lines
            if not line:
                break
            # Increments the horizontal position, accounting for when the pattern repeats
            position = (position + right) % length
            # Checks if there is a tree at the current location
            trees += 1 if line[position] == "#" else 0
        # Returns the number of trees encountered
        return trees


# Executes the main method
if __name__ == '__main__':
    main()
