/*

find({skills: "html"})
find({skills: ["html", "css"]})//exact match sequence also matter
{skills:{$in:["html","css"]}}//any one match
{skills:{$nin:["html","css"]}}//any one match not included any of them
{skills:{$all:["html", "css"]}}//all match
{"address.city":"kathmandu"}//embedded document ko data read or extract garnu xa vane double quote use garna parxa
{"courses.course":"mongodb", "courses.marks":{$gte:70}} //double quote use garna parxa when embedded document ko data read or extract garnu xa vane 

*/

// main topic today
// searching embedded document
// {courses:{$elemMatch:{course:"mongodb", marks:{gte:70}}}}
//db.students.find({}).count()
//db.students.find({name:"arjun"}).count()


//db.students.findOne({name:"arjun"}) // findOne() method will return only one document even if there are multiple documents with the same name

// data = document vanxa    
// Array of object = embedded document vanxa 


db.students.insertMany([
{
  name: "nitan",
  age: 28,
  skills: ["html","css","javascript"],
  hobbies: ["reading","music"],
  address: { city: "kathmandu", country: "nepal" },
  courses: [
      {course: "mongodb", duration: "three", marks: 80},
      {course: "react", duration: "two", marks: 60}
  ]
},
{
  name: "ram",
  age: 22,
  skills: ["html"],
  hobbies: ["football","music"],
  address: { city: "pokhara", country: "nepal" },
  courses: [
      {course: "nodejs", duration: "four", marks: 75}
  ]
},
{
  name: "john",
  age: 30,
  skills: ["python","mongodb"],
  hobbies: ["reading","travel"],
  address: { city: "delhi", country: "india" },
  courses: [
      {course: "python", duration: "four", marks: 90},
      {course: "mongodb", duration: "two", marks: 65}
  ]
},
{
  name: "hari",
  age: 25,
  skills: ["css","javascript"],
  hobbies: ["travel","music"],
  address: { city: "bhaktapur", country: "nepal" },
  courses: [
      {course: "react", duration: "two", marks: 55}
  ]
},
{
  name: "sita",
  age: 27,
  skills: ["html","css"],
  hobbies: ["reading"],
  address: { city: "kathmandu", country: "nepal" },
  courses: [
      {course: "mongodb", duration: "two", marks: 85}
  ]
}
])


