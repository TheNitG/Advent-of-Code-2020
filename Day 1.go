package main

/*
Imports all necessary libraries to execute the file
*/
import (
	"fmt"
	"io"
	"os"
)

/*
Executes the code to find the two numbers adding up to 2020 and also what their product is
*/
func main() {
	// Opens the input text file
	data, err := os.Open("input.txt")
	// If the file has issues, the rest of the code will not execute and it will say "Invalid file"
	if err != nil {
		fmt.Println("Invalid file")
		os.Exit(1)
		return
	}
	// Integer array that stores the numbers from the input text file
	var numbers []int
	// Fills the integer array
	for {
		// Current number to be found
		var number int
		// Looks for the next integer in the text file
		_, err = fmt.Fscanf(data, "%d\n", &number)
		// If there is an error, the code will stop and stops the code from continuing if the end of file was not reached
		if err != nil {
			if err == io.EOF {
				break
			}
			os.Exit(1)
		}
		// Appends the current number to the integer array
		numbers = append(numbers, number)
	}
	// Calls the method that finds which two numbers add up to 2020
	num1, num2 := find2020(numbers)
	// Prints the two numbers, their sum, and their product all in a friendly way
	fmt.Printf("%[1]d + %[2]d = 2020, %[1]d * %[2]d = %[3]d", num1, num2, num1*num2)
}

/*
Method that finds the two numbers that add up to 2020 and returns them, else returns 0, 0 if no match is found
*/
func find2020(data []int) (int, int) {
	// Length of the integer array
	length := len(data)
	// Nested for loop that tries each combination of numbers to find the pair that adds up to 2020
	for indexX := 0; indexX < length; indexX++ {
		for indexY := 0; indexY < length; indexY++ {
			num1, num2 := data[indexX], data[indexY]
			if num1+num2 == 2020 {
				// Returns when a match is found
				return num1, num2
			}
		}
	}
	// Returns 0, 0 if no match is found
	return 0, 0
}
