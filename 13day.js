/*
Note:
query time increases:
if the number of document increases.
if the size of document increases.

Two types of scan:
1. collscan scan: scan all documents in a collection.
2. indexscan scan: scan all documents in a collection using index.

1: Ascending order
2: Descending order

db.people.find({country: "Nepal"}).explain("executionStats")

db.people.createIndex({country:1})

db.users.find({Age: {$gt: 50}}).explain("executionStats")

db.users.createIndex({Age:1})

unique
db.customers.createIndex({email:1}, {unique:true})

db.customers.insertMany([{name:"anup", age:22, email:"anup@.com"}])
db.customers.createIndex({name:1,age:1}, {unique:true})

*/