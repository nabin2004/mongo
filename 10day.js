/*
$addfields

db.students.aggregate([
  {
    $addFields: {
      full_name: {
        $concat: ["$name", " ", "$surname"]
      }
    }
  }
])  

$unwind
db.orders.aggregate([
  {
    $unwind: {
      path: "$products",
      preserveNullAndEmptyArrays: true
    }
  }
])

$group
db.teachers.aggregate([
  {
    $group: {
      _id: "$gender",
      names: {
        $push: "$name"
      },
      data: { $push: "$$ROOT" },
      totalNoOfData: { $sum: 1 },
      maxAge: { $max: "$age" },
      minAge: { $min: "$age" },
      avgAge: { $avg: "$age" }
    }
  }
])











*/