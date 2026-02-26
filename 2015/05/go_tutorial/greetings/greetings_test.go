package greetings

// Ending a filename with _test.go means `go test` will know it contains test functions
// Run tests with `go test`

import (
	"regexp"
	"testing"
)

// Test for successful case
func TestHelloName(t *testing.T) { // `t` is used for logging from the test
	name := "Gladys"
	want := regexp.MustCompile(`\b` + name + `\b`) // BACKTICKS!
	msg, err := Hello("Gladys")

	// Define conditions for test failure
	if !want.MatchString(msg) || err != nil {
		t.Errorf(
			// Formatted as `Function(arg) = [actual result], [desired result]`
			`Hello("Gladys") = %q, %v, want match for %#q, nil`,
			msg,
			err,
			want,
		)
	}
}

// Test for unsuccessful case (i.e. empty name argument)
func TestHelloEmpty(t *testing.T) {
	msg, err := Hello("")

	if msg != "" || err == nil {
		t.Errorf(`Hello("") = %q, %v, want "", error`, msg, err)
	}
}
