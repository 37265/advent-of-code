package main // In Go, code executed as an application must be in a main package.

import (
	"fmt"
	"log"

	"example.com/greetings" // looks like non-standard libraries are imported with space between lines
)

func main() {
	/*
		The log package customizes the console output, it seems.
		SetPrefix just makes the logger print some value every time the console outputs something.
		SetFlags(0) disables printing the time, source file, and line number in case of an error log(?)
		↑ That's right. E.g. SetFlags(8) *does* print the line number where the error was logged.
	*/
	log.SetPrefix("greetings: ")
	log.SetFlags(0)

	// When a function returns multiple values, declare n vars for n values
	// message, err := greetings.Hello("")

	// Slice of names (for input)
	names := []string{"Gladys", "Frank", "Tina"}

	messages, err := greetings.Hellos(names)

	if err != nil {
		// Uses one of log's built-in functions
		log.Fatal(err)
	}

	// range seems to automatically use the length of the given collection
	// The first arg is actually the key in the map, not a numeric index for the loop
	for key, message := range messages {
		fmt.Printf("%v: %v\n", key, message)
	}
}

// Build and install the application with `go build` and `go install`
