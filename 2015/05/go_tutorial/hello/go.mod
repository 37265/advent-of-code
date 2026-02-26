module example.com/hello

go 1.25.0

// This was added with `go mod edit -replace [dependency url]=[relative path to local package]`
replace example.com/greetings => ../greetings

// After the `-replace` operation, I ran `go mod tidy` to synchronize the example.com/hello module's dependencies
// That added this line, based on the import for the `greetings` package in `hello.go`.
require example.com/greetings v0.0.0-00010101000000-000000000000 // Pseudo-version number
