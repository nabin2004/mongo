/* 
Aggregation
$match = same as find() query

db.teachers.aggregate([{$match: {}}])
db.teachers.aggregate([{$match: {name: "A"}}])

$sort
db.teachers.aggregate([{$match: {}}, {$sort: {name: 1, age: -1}}]) // 1 for ascending order and -1 for descending order,{}])

$limit
db.teachers.aggregate([{$match: {}}, {$sort: {name: 1}}, {$limit: 4}]) // 1 for ascending order and -1 for descending order,{}])

$skip
db.teachers.aggregate([{$match: {}}, {$skip: 2}]) // 1 for ascending order and -1 for descending order,{}])
db.teachers.aggregate([{$match: {}}, {$limit: 3}, {$skip: 2}]) // 1 for ascending order and -1 for descending order,{}])

$PROJECT
db.students.aggregate([{$match: {}}, {$project: {name: 1}}])
db.students.aggregate([{$match: {}}, {$project: {name: 1, _id: 0}}]) // this will not show _id field
db.students.aggregate([{$match: {}}, {$project: {name: 1, student_age: "$age"}}]) // this will show name and country field but not _id field
db.students.aggregate([
  {
    $match: {}
  },
  {
    $project: {
      name: 1,
      student_age: "$age",
      total_score: {
        $add: [
          "$scores.math",
          "$scores.english",
          "$scores.science"
        ]
      }
    }
  }
])

db.students.aggregate([
  {
    $match: {}
  },
  {
    $project: {
      _id: 0,
      name: 1,
      country: 1,
      student_age: "$age",
      total_score: {
        $add: [
          "$scores.math",
          "$scores.english",
          "$scores.science"
        ]
      },
      average_score: {
        $avg: [
          "$scores.math",
          "$scores.english",
          "$scores.science"
        ]
      }
    }
  }
])

db.students.aggregate([
  {
    $match: {}
  },
  {
    $project: {
      _id: 0,
      name: 1,
      country: 1,
      student_age: "$age",

      total_score: {
        $add: [
          "$scores.math",
          "$scores.english",
          "$scores.science"
        ]
      },

      average_score: {
        $avg: [
          "$scores.math",
          "$scores.english",
          "$scores.science"
        ]
      },

      min_score: {
        $min: [
          "$scores.math",
          "$scores.english",
          "$scores.science"
        ]
      },

      max_score: {
        $max: [
          "$scores.math",
          "$scores.english",
          "$scores.science"
        ]
      }
    }
  }
])


db.students.aggregate([
  {
    $match: {}
  },
  {
    $project: {
      _id: 0,
      name: 1,
      country: 1,
      student_age: "$age",

      total_score: {
        $add: [
          "$scores.math",
          "$scores.english",
          "$scores.science"
        ]
      },

      average_score: {
        $avg: [
          "$scores.math",
          "$scores.english",
          "$scores.science"
        ]
      },

      min_score: {
        $min: [
          "$scores.math",
          "$scores.english",
          "$scores.science"
        ]
      },

      max_score: {
        $max: [
          "$scores.math",
          "$scores.english",
          "$scores.science"
        ]
      }
    }
  }
])

db.students.aggregate([
  {
    $match: {}
  },
  {
    $project: {
      _id: 0,
      name: 1,
      country: 1,
      student_age: "$age",

      total_score: {
        $add: [
          "$scores.math",
          "$scores.english",
          "$scores.science"
        ]
      },

      average_score: {
        $avg: [
          "$scores.math",
          "$scores.english",
          "$scores.science"
        ]
      },

      min_score: {
        $min: [
          "$scores.math",
          "$scores.english",
          "$scores.science"
        ]
      },

      max_score: {
        $max: [
          "$scores.math",
          "$scores.english",
          "$scores.science"
        ]
      },

      full_name: {
        $concat: ["$name", " ", "$surname"]
      },

      percentage: {
        $multiply: [
          {
            $divide: [
              {
                $add: [
                  "$scores.math",
                  "$scores.english",
                  "$scores.science"
                ]
              },
              300
            ]
          },
          100
        ]
      }
    }
  }
])



*/