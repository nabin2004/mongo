// db.students.find({}, {age: 1, _id:0}) // _id:0 means we don't want to show the _id field in the result and limit doesnot work on _id field because it is unique for each document so it will always be shown in the result but we can hide it by using _id:0 in projection
//db.students.find({}, {age:0}) // for password or any other field we can use 0 to hide that field
//db.students.find({}, {age:1}) // for password or any other field we can use 1 to show that field
//db.students.find({}, {name:1, age:1}) // for password or any other field we can use 1 to show that field
//db.students.find({}, {name:1, age:0}) // for password or any other field we can use 1 to show that field and 0 to hide that field



// Sorting in mongodb
//db.students.find().sort({age:1}) // 1 for ascending order
//db.students.find().sort({age:-1}) // -1 for descending order
//db.students.find().sort({name:1}) // 1 for ascending order
//db.students.find().sort({name:-1}) // -1 for descending order
//db.students.find({}).sort({name:1, age:-1}) // 1 for ascending order and -1 for descending order
//db.students.find({}).sort({name:1, age:1}) // 1 for ascending order and -1 for descending order


// Limit and skip in mongodb
//db.students.find().limit(2) // limit the number of documents returned
//db.students.find().skip(2) // skip the first 2 documents
//db.students.find().skip(2).limit(2) // skip the first 2 documents and limit the number of documents returned to 2
//db.students.find({}).limit(2).skip(2) // its the same as above but the order of limit and skip is different but the result will be same
// limit order is at last and skip order is at first in mongodb but the result will be same so order is not important in mongodb for limit and skip but the result will be same
// orders of mongodb sequence = find() -> sort() -> skip() -> limit() -> projection() -> count() -> explain() -> hint() -> maxTimeMS() -> allowDiskUse() -> collation() -> comment() -> readConcern() -> writeConcern() -> session() -> readPreference()

// NOTE:

// EXECUTION ORDER
// => find, sort, skip, limit, projection


//db.students.find().skip(10).limit(5) // skip the first 10 documents and limit the number of documents returned to 5

//{}=> it is default value so it doesnot matter if we write it or not in find() method but writing is good here so writing always

//db.students.deleteMany({}) // delete all documents in the collection



// db.students.updateMany





