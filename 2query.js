/*
db.students.insertMany([
{
    name: "nitan",
    age: 32,
    city: "kathmandu",
    isMarried: false,
    salary: 50000,
    hobbies: ["coding", "reading"]
},
{
    name: "ram",
    age: 25,
    city: "pokhara",
    isMarried: true,
    salary: 35000,
    hobbies: ["football", "travel"]
},
{
    name: "hari",
    age: 18,
    city: "lalitpur",
    isMarried: false,
    salary: 20000
},
{
    name: "sita",
    age: 29,
    city: "bhaktapur",
    isMarried: true,
    salary: 45000,
    hobbies: ["music"]
},
{
    name: "gita",
    age: 21,
    city: "kathmandu",
    isMarried: false,
    salary: 25000
},
{
    name: "john",
    age: 35,
    city: "biratnagar",
    isMarried: true,
    salary: 70000,
    hobbies: ["gaming", "travel"]
},
{
    name: "alice",
    age: 27,
    city: "pokhara",
    isMarried: false,
    salary: 40000
},
{
    name: "bob",
    age: 15,
    city: "butwal",
    isMarried: false,
    salary: 10000
},
{
    name: "emma",
    age: "24",
    city: "dharan",
    isMarried: false,
    salary: 30000
},
{
    name: "david",
    city: "janakpur",
    isMarried: true,
    salary: 55000
},
{
    name: "sophia",
    age: 42,
    city: "kathmandu",
    salary: 90000
},
{
    name: "mohan",
    age: 30,
    city: "pokhara",
    isMarried: true,
    salary: 60000
}
])


comparison operator
    general search
        .find({})
        .find({field: value})=> db.students.find({city: "kathmandu"})
        .find({name:"nitan", age:32})

comparison operatios=>operator ko aghadi dollar sign lagauxau

comparision operator 
    general search 
        .find({})
        .find({name:"nitan"})
        .find({name:"nitan", age:32})
    comparions operators
        $eq,$ne,$gt,$gte,$lt,$lte,$in , $nin, $mod
        .find({name:"nitan"})
        .find({name:{$eq:"nitan"}})
        .find({name:{$ne:"nitan"}})
        .find({name:{$in:["nitan","ram"]}})
        .find({name:{$nin:["nitan","ram"]}})
        .find({age:{$gt:30}})
        .find({age:{$gte:30}})
        .find({age:{$lt:30}})
        .find({age:{$lte:30}})
        .find({age:{$gte:12,$lte:25}}) => range
        .find({age: { $mod: [5, 0] }}) => mod with 5 is 0

*/