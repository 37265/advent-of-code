package greetings

import (
	"errors"
	"fmt"
	"math/rand"
)

// Function names starting with an uppercase letter are exported by default
// func [name](parameters) (return value(s)) !!! Go functions can return multiple values; FREAKY
func Hello(name string) (string, error) {
	if name == "" {
		return "", errors.New("empty name")
	}

	/*:= declares and initializes a variable in one line, using the value after = to determine type.
	Another way to do it, would be with `var [name] [type]` and then assigning with = on a new line.
	Spintf is the same as printf() in Java. */
	message := fmt.Sprintf(randomFormat(), name)

	return message, nil // nil is null? Go is so different 💁
}

func Hellos(names []string) (map[string]string, error) {
	// Create a map that will associate names with messages
	messages := make(map[string]string) // make(map[[key type]][value type])

	// Uses the Go blank identifier to ignore the index, but normally first arg would be index
	for _, name := range names {
		message, err := Hello(name)

		if err != nil {
			return nil, err
		}

		messages[name] = message
	}

	return messages, nil
}

// This function's name starting with a lowercase letter means it's package-private
func randomFormat() string {
	// A slice of message formats. (Slice is basically ArrayList; grows as needed)
	formats := []string{ // Not passing a size to the brackets -> slice (ArrayList)
		"Hi, %v. Welcome!",
		"Great to see you, %v!",
		"Hail, %v! Well met!", // Closing comma for WHAT???
	}

	return formats[rand.Intn(len(formats))]
}
