/* global use, db */
use("erneyp")
db.auth(" root", " example")


db.products.insertOne({
  "name":"iphon",
  "price":"100",
  "description":"ifhon is smart",
  "category":"smarphone"
})
