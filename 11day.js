/*

db.persons.insertMany([
  {
    name: "A",
    hobbies: ["dancing", "cooking"],
  },
  {
    name: "B",
    hobbies: ["dancing", "singing", "music"],
  },
]);

use group and unwind
db.persons.aggregate([
  { $unwind: "$hobbies" },{
    $group: {
      _id: null,
      uniqueHobbies: { $addToSet: "$hobbies" }
    }
  }
])

db.carts.aggregate([
    {
        $group: {
            _id: null,
            totalAmount: {
                $sum: {
                    $multiply: ["$price", "$quantity"]
                }
            }
        }
    }
])

db.students.aggregate([
    {
        $bucket: {
            groupBy: "$score",
            boundaries: [60, 80, 100],
            default: "Other",
            output: {
                students: { $push: "$$ROOT" }
            }
        }
    }
])





*/
