package main

import (
	"fmt"
	"os"
	"strings"
)

const inputFileName string = "input.txt"

func main() {
	input := readLines()

	doPartOne(input)
	doPartTwo(input)
}

// Reads lines from the input file
func readLines() []string {
	data, err := os.ReadFile(inputFileName)

	if err != nil {
		panic(err)
	}

	stringData := string(data)
	lines := strings.Split(stringData, "\n")

	return lines
}

// ---------------------------------- Part 1 stuff ------------------------------------------------
func doPartOne(input []string) {
	nNiceStrings := 0
	for _, line := range input {
		if hasGteThreeVowels(line) && hasPair(line) && hasNoBadstrings(line) {
			nNiceStrings++
		}
	}

	fmt.Printf("Part 1 | Number of nice strings: %d\n", nNiceStrings)
}

// Checks whether a line contains at least three vowels (non-distinct)
func hasGteThreeVowels(line string) bool {
	vowels := [5]string{"a", "e", "i", "o", "u"}
	nVowels := 0

	for _, vowel := range vowels {
		nVowels += strings.Count(line, vowel)
		if nVowels >= 3 {
			return true
		}
	}

	return false
}

// Checks whether a line contains a pair
func hasPair(line string) bool {
	for i := range line {
		if i < len(line)-1 {
			if line[i] == line[i+1] {
				return true
			}
		}
	}

	return false
}

// Checks whether a line contains none of the bad substrings
func hasNoBadstrings(line string) bool {
	badStrings := [4]string{"ab", "cd", "pq", "xy"}

	for _, badString := range badStrings {
		if strings.Contains(line, badString) {
			return false
		}
	}

	return true
}

// ---------------------------------- Part 2 stuff ------------------------------------------------
func doPartTwo(input []string) {
	nNiceStrings := 0
	for _, line := range input {
		if hasRepeatingPair(line) && hasSandwich(line) {
			nNiceStrings++
		}
	}

	fmt.Printf("Part 2 | Number of nice strings: %d", nNiceStrings)
}

// Checks whether any pair of letters appears twice in the string
func hasRepeatingPair(line string) bool {
	for i := range line {
		if i < len(line)-2 {
			pair := string(line[i]) + string(line[i+1])
			restOfString := line[i+2:]

			if strings.Contains(restOfString, pair) {
				return true
			}
		}
	}

	return false
}

// Checks if there is a letter that repeats with exactly one letter between it and its repeated occurence
// E.g. 'xyx'
func hasSandwich(line string) bool {
	for i := range line {
		if i < len(line)-2 {
			if line[i] == line[i+2] {
				return true
			}
		}
	}

	return false
}
