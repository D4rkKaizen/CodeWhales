package main

import (
    "fmt"
    "os"
    "path/filepath"
)

func main() {
    files, err := filepath.Glob("*.py")
    if err != nil {
        fmt.Println("Error:", err)
        return
    }

    for _, file := range files {
        err := os.Remove(file)
        if err != nil {
            fmt.Println("Error deleting file:", file, ":", err)
        } else {
            fmt.Println("Deleted file:", file)
        }
    }
}
