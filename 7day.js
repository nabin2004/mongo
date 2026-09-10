/*
DELETE
db.students.deleteOne({name:"ram"}) // delete one document where name is "ram"
db.students.deleteMany({}) // delete all documents

db.createCollection("users", {
  validator: {
    $jsonSchema: {
      bsonType: "object",
      required: ["name", "age"], //it contain list of required fields
      additionalProperties: false, //it means no additional properties are allowed in the document

      properties: {
        _id: { bsonType: "objectId" }, //you must add _id because you have passed additionalProperties:false
        name: {
          bsonType: "string",
          description: "must be a string and is required",
        },
        age: {
          bsonType: "int",
          description: "must be an integer and is required",
        },
        isMarried: {
          bsonType: "bool",
          description: "must be a boolean and is required",
        }
      },
      },
    },
  },
});

db.users.insertOne({ name: "ram", age: 20, isMarried: false }) // this will work because it has all the required fields and no additional properties
db.users.insertMany({name: "ram", age: 20, isMarried: false,country:"nepal" }) // this will not work because it has additional properties

# rename collection
db.runCommand({
  collMod: "users", //collMode = collection modifier
  validator: {
    $jsonSchema: {
      bsonType: "object",
      additionalProperties: false,
      properties: {
        _id: { bsonType: "objectId" },
        name: {
          bsonType: "string",
          description: "name should be string", //description field is  used so for comment purpose only, it  will not shown in error message
          minLength: 3,
          maxLength: 20,
       
        },
        age: {
          bsonType: "int",
          description: "age should be integer",
        },
        isMarried: {
          bsonType: "bool",
          description: "isMarried should be boolean",
        },
      },
    },
  },
});

db.users.insertMany([
  {
    name: "Pramod",
    age: 24,
    isMarried: false
  },
  {
    name: "Ram",
    age: 28,
    isMarried: true
  },
  {
    name: "Sita",
    age: 25,
    isMarried: false
  }
]);
*/