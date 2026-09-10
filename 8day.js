/* 
db.createCollection("students", {
  validator: {
    $jsonSchema: {
      bsonType: "object",

      required: ["name", "password", "email", "height", "phonenumber", "roll", "isMarried", "gender", "dob", "location", "favTeacher", "favSubject"],

      additionalProperties: false,

      properties: {
        name: {
          bsonType: "string",
          description: " name must be a string",
            minLength: 3,
            maxLength: 20,
        },

        password: {
          bsonType: "string",
          description: "password must be a string minimum 8 characters, at least one uppercase letter, one lowercase letter, one number and one special character",
          pattern: "^(?=.*[a-z])(?=.*[A-Z])(?=.*\\d)(?=.*[@$!%*?&])[A-Za-z\\d@$!%*?&]{8,}$"
        },

        email: {
          bsonType: "string",
          description: "email must be a string and must be a valid email address",
          pattern: "^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$"
        },

        height: {
          bsonType: "number",
          description: "height must be a number"
        },

        phonenumber: {
          bsonType: "string",
          description: "phone number must be a string and must be a valid phone number",
            pattern: "^[0-9]{10}$"
        },

        roll: {
          bsonType: "number",
          description: "roll number must be a number"
        },

        isMarried: {
          bsonType: "bool",
          description: "isMarried must be a boolean"
        },

        gender: {
          bsonType: "string",
          description: "gender must be a string"
        },

        dob: {
          bsonType: "date",
          description: "dob must be a date"
        },

        location: {
          bsonType: "object",

          required: ["country", "exactLocation"],

          additionalProperties: false,

          properties: {
            country: {
              bsonType: "string",
              description: "country must be a string"
            },

            exactLocation: {
              bsonType: "string",
              description: "exactLocation must be a string"
            }
          }
        },

        favTeacher: {
          bsonType: "array",
          description: "favTeacher must be an array",

          items: {
            bsonType: "string",
            description: "each teacher must be a string"
          }
        },

        favSubject: {
          bsonType: "array",
          description: "Array of favorite subjects",

          items: {
            bsonType: "object",

            required: ["bookName", "bookAuthor"],

            additionalProperties: false,

            properties: {
              bookName: {
                bsonType: "string",
                description: "must be a string"
              },

              bookAuthor: {
                bsonType: "string",
                description: "must be a string"
              }
            }
          }
        }
      }
    }
  }
});


db.students.insertMany([
  {_id: 1, name: "Ram"},
  {_id:2, name: "sita"},
  {_id:1, name: "hari"},
  {_id:3, name: "gita"},
  {_id:4, name: "shyam"},
  {_id:3, name: "laxmi"},
],
{ordered: true} // this will allow the insertion of other documents even if one document fails due to duplicate _id
);
  




*/