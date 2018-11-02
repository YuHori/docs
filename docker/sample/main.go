package main

import (
  "log"
  "net/http"
)

func main() {
  //http.Handle("/web", http.StripPrefix("/web", http.FileServer(http.Dir("static"))))
  http.Handle("/", http.FileServer(http.Dir("static")))
  if err := http.ListenAndServe(":8080", nil); err != nil {
      log.Fatal("ListenAndServe: ", err)
  }
}
