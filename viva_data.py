viva_content = {
    "1structure.js": {
        "title": "Basic Structure & CRUD",
        "concepts": [
            {
                "name": "Database & Collection Creation",
                "breakdown": "MongoDB is a NoSQL database organized into Clusters -> Databases -> Collections -> Documents. You create databases with 'use' and collections implicitly by inserting or explicitly with createCollection.",
                "use_case": "Setting up the initial schema-less structure for a new application.",
                "gotcha": "Databases and collections aren't actually created on disk until the first document is inserted.",
                "hook": "Cluster > Database > Collection > Document (C-D-C-D)"
            },
            {
                "name": "Basic CRUD Operations",
                "breakdown": "insertOne/insertMany add documents. find() retrieves them. updateOne/updateMany modify existing documents, and deleteOne/deleteMany remove them.",
                "use_case": "Standard data manipulation for any user-facing app.",
                "gotcha": "updateOne only updates the FIRST document matching the filter, even if multiple match.",
                "hook": "CRUD: Create (insert), Read (find), Update (update), Delete (delete)."
            }
        ],
        "qna": [
            {"q": "Examiner: What is the difference between updateOne and updateMany?", "a": "updateOne modifies only the first document that matches the filter, whereas updateMany modifies all documents matching the filter."},
            {"q": "Examiner: What happens if you try to use a database that doesn't exist?", "a": "MongoDB will switch to it in memory, but it won't be saved to disk until you insert a document into one of its collections."}
        ]
    },
    "2query.js": {
        "title": "Comparison Operators",
        "concepts": [
            {
                "name": "Comparison Operators ($gt, $lt, $in, $ne)",
                "breakdown": "These operators allow filtering documents based on specific value comparisons rather than exact matches. $in matches any value in an array.",
                "use_case": "Finding users over a certain age ($gte: 18) or products within a price range.",
                "gotcha": "$in takes an array of values. Forgetting the brackets (e.g., $in: 'nitan') will result in an error or unexpected behavior.",
                "hook": "Prefix with $ for operators: $gt (greater than), $lt (less than), $ne (not equal)."
            }
        ],
        "qna": [
            {"q": "Examiner: How would you find students whose age is exactly 25 or 30?", "a": "Use the $in operator: { age: { $in: [25, 30] } }"},
            {"q": "Examiner: Can you use multiple comparison operators on the same field?", "a": "Yes, for example { age: { $gte: 18, $lte: 30 } } finds ages between 18 and 30 inclusive."}
        ]
    },
    "3logicalquery.js": {
        "title": "Logical Operators",
        "concepts": [
            {
                "name": "Logical $or and $exists",
                "breakdown": "$or evaluates an array of conditions and returns documents that match at least one. $exists checks if a field is present, regardless of its value.",
                "use_case": "Finding users who either live in 'kathmandu' OR are married. Finding documents where an optional field was actually saved.",
                "gotcha": "$or must be an array of objects. Also, $exists: false will return documents where the field doesn't exist, which is different from a field existing with a null value.",
                "hook": "$or is an array of conditions. $exists is a boolean."
            }
        ],
        "qna": [
            {"q": "Examiner: What is the difference between $exists: true and checking for null?", "a": "A field can exist and have a value of null. $exists: true matches it, but checking {field: null} matches both null values and non-existent fields (in some driver contexts)."},
            {"q": "Examiner: How do you structure an $or query?", "a": "It takes an array of query objects: { $or: [ {condition1}, {condition2} ] }"}
        ]
    },
    "4query.js": {
        "title": "Array & Embedded Document Queries",
        "concepts": [
            {
                "name": "Array Operators ($all, exact match)",
                "breakdown": "Exact array matching requires the exact elements in the exact order. $all matches if all specified elements exist in the array, regardless of order or other elements.",
                "use_case": "Finding a candidate who has both 'html' and 'css' skills, regardless of what else they know ($all).",
                "gotcha": "find({skills: ['html', 'css']}) strictly matches ONLY those two skills in that exact order. Always use $all for subsets.",
                "hook": "$all is unordered inclusion. Exact array is strict sequence."
            },
            {
                "name": "Dot Notation and $elemMatch",
                "breakdown": "Dot notation accesses nested fields. $elemMatch ensures that multiple conditions match the SAME element within an array of objects.",
                "use_case": "Finding a student who scored >70 specifically in the 'mongodb' course.",
                "gotcha": "Dot notation strings MUST be in quotes (e.g., 'address.city'). If you use multiple dot notations for an array, they might match different objects in the array. $elemMatch fixes this.",
                "hook": "Quotes for dots ('a.b'). $elemMatch for SAME array object."
            }
        ],
        "qna": [
            {"q": "Examiner: Why must you use quotes when querying embedded documents with dot notation?", "a": "Because JavaScript object syntax doesn't allow dots in unquoted keys. 'address.city' must be a string key."},
            {"q": "Examiner: When is $elemMatch strictly necessary over dot notation?", "a": "When you have an array of objects and you need multiple conditions to be satisfied by the *same* object in that array."},
            {"q": "Examiner: What happens if you use findOne() but 10 documents match?", "a": "MongoDB stops scanning and returns only the first document it encounters that matches the criteria, based on the natural order or index."}
        ]
    },
    "5day.js": {
        "title": "Projection, Sort, Skip, Limit",
        "concepts": [
            {
                "name": "Query Modifiers (Projection, Sort, Skip, Limit)",
                "breakdown": "Projection includes/excludes fields. Sort orders results. Skip bypasses documents. Limit restricts the count returned.",
                "use_case": "Implementing pagination on a frontend (skip and limit) and hiding passwords (projection).",
                "gotcha": "Execution order is ALWAYS: match -> sort -> skip -> limit -> project, regardless of the order you chain the methods in Node.js.",
                "hook": "Order doesn't matter in code: Sort-Skip-Limit happens naturally."
            }
        ],
        "qna": [
            {"q": "Examiner: If I chain .limit(2).skip(5), what order does MongoDB execute them?", "a": "MongoDB always executes sort, then skip, then limit. So it will skip 5, then limit to 2."},
            {"q": "Examiner: How do you exclude the _id field in projection?", "a": "You must explicitly set it to 0: { _id: 0 }. It is the only field included by default."}
        ]
    },
    "6day.js": {
        "title": "Update Operators",
        "concepts": [
            {
                "name": "Field Update Operators ($set, $inc, $unset)",
                "breakdown": "$set changes a value, $inc increments/decrements a number, and $unset removes a field entirely.",
                "use_case": "Incrementing a view counter ($inc) or updating a user's address ($set).",
                "gotcha": "If you don't use $set and just pass an object to update, older drivers would replace the whole document. Now, update methods require update operators.",
                "hook": "Operators are actions: $set (overwrite), $inc (math), $unset (delete key)."
            },
            {
                "name": "Array Update Operators ($push, $addToSet, $pull)",
                "breakdown": "$push appends to an array. $addToSet appends only if the value doesn't exist. $pull removes matching values.",
                "use_case": "Adding a unique tag to a blog post ($addToSet) or removing a specific item from a cart ($pull).",
                "gotcha": "$push will create duplicates if called multiple times. Use $addToSet to maintain uniqueness in an array.",
                "hook": "$push = duplicates allowed. $addToSet = strictly unique."
            }
        ],
        "qna": [
            {"q": "Examiner: What is an upsert?", "a": "An upsert operation updates a document if it matches the filter, or inserts a new document based on the filter and update data if no match is found."},
            {"q": "Examiner: How do you remove an element from an array?", "a": "Use the $pull operator specifying the condition of the element to remove."}
        ]
    },
    "7day.js": {
        "title": "Schema Validation (Part 1)",
        "concepts": [
            {
                "name": "JSON Schema Validation",
                "breakdown": "MongoDB allows enforcing document structure at the database level using standard JSON Schema formatting inside a validator object.",
                "use_case": "Ensuring a 'users' collection always has a string 'name' and integer 'age', preventing bad data from a buggy backend.",
                "gotcha": "If additionalProperties is false, you MUST explicitly define _id in the properties, otherwise inserts will fail because MongoDB automatically adds an _id.",
                "hook": "Schema validation: Strict typing for a NoSQL database."
            }
        ],
        "qna": [
            {"q": "Examiner: Why do inserts fail when additionalProperties is false even if the data looks perfect?", "a": "Because MongoDB auto-generates the _id field. If you don't list _id in your schema properties, it treats _id as an unauthorized additional property."}
        ]
    },
    "8day.js": {
        "title": "Schema Validation (Part 2) & Ordered Inserts",
        "concepts": [
            {
                "name": "Ordered vs Unordered Inserts",
                "breakdown": "When inserting many documents, ordered: true (default) stops on the first error. ordered: false attempts to insert all documents, ignoring individual failures like duplicate keys.",
                "use_case": "Bulk importing logs where you want to skip duplicates but keep inserting the rest (ordered: false).",
                "gotcha": "Even with ordered: false, if there's a syntax error, the whole operation fails. It only bypasses constraint errors (like duplicate _id).",
                "hook": "Ordered = Stop on red light. Unordered = Run red lights."
            }
        ],
        "qna": [
            {"q": "Examiner: What is the default behavior of insertMany if one document fails a unique index constraint?", "a": "By default (ordered: true), it aborts the operation and subsequent documents in the array are not inserted."}
        ]
    },
    "9day.js": {
        "title": "Aggregation Framework (Basic)",
        "concepts": [
            {
                "name": "Aggregation Pipeline ($match, $project)",
                "breakdown": "The aggregation pipeline processes documents through stages. $match filters early, $project reshapes the output.",
                "use_case": "Complex reporting, calculating average scores, or transforming data shapes before sending to the client.",
                "gotcha": "Always put $match as early as possible. If you project or group first, you lose the ability to use indexes, causing a full collection scan.",
                "hook": "Pipeline is a factory assembly line. Filter ($match) before you assemble ($project)."
            },
             {
                "name": "Arithmetic Expressions ($add, $avg)",
                "breakdown": "Operators used within $project or $group to perform math on fields.",
                "use_case": "Calculating a total score from individual subject scores.",
                "gotcha": "In projection arithmetic, field names MUST be prefixed with a $ (e.g., '$scores.math') to indicate you want the field's value, not the literal string.",
                "hook": "Prefix with $ to get the value in aggregations."
            }
        ],
        "qna": [
            {"q": "Examiner: Why is the order of stages important in an aggregation pipeline?", "a": "Because each stage transforms the data for the next. Filtering with $match first drastically reduces the dataset size and utilizes indexes, improving performance."}
        ]
    },
    "10day.js": {
        "title": "Aggregation: Unwind & Group",
        "concepts": [
            {
                "name": "$unwind",
                "breakdown": "Deconstructs an array field, outputting a new document for each element of the array. The other fields are duplicated.",
                "use_case": "Analyzing tags on blog posts. To count tags, you must first unwind the tags array.",
                "gotcha": "If a document has an empty array or null for that field, $unwind removes the document entirely unless you use preserveNullAndEmptyArrays: true.",
                "hook": "$unwind explodes an array into multiple documents."
            },
             {
                "name": "$group",
                "breakdown": "Groups documents by a specified _id expression and applies accumulator expressions ($sum, $max).",
                "use_case": "Finding the total sales per region, or the maximum age per gender.",
                "gotcha": "The _id field in $group is mandatory. It determines what you are grouping BY. If you want to group everything into one result, use _id: null.",
                "hook": "_id is the 'GROUP BY' key."
            }
        ],
        "qna": [
            {"q": "Examiner: How do you group all documents in a collection together to find the global average?", "a": "You set the _id field in the $group stage to null: { $group: { _id: null, avg: { $avg: '$price' } } }."}
        ]
    },
    "11day.js": {
        "title": "Aggregation: Buckets & Sets",
        "concepts": [
            {
                "name": "$bucket and Accumulators",
                "breakdown": "$bucket categorizes incoming documents into groups, called buckets, based on specified boundaries.",
                "use_case": "Creating histograms, like grouping students by score ranges (60-80, 80-100).",
                "gotcha": "Boundaries must be sorted. The bucket includes the lower bound and excludes the upper bound. You must provide a 'default' bucket for outliers.",
                "hook": "$bucket = Histogram grouping."
            }
        ],
        "qna": [
            {"q": "Examiner: What happens if a document's value falls outside your $bucket boundaries?", "a": "It goes into the bucket specified by the 'default' parameter. If no default is provided, it throws an error."}
        ]
    },
    "12day.js": {
        "title": "Aggregation: $lookup (Joins)",
        "concepts": [
            {
                "name": "$lookup (Left Outer Join)",
                "breakdown": "Performs a join with another collection in the same database to filter in documents from the 'joined' collection.",
                "use_case": "Fetching user details alongside their recent orders (joining 'orders' with 'users').",
                "gotcha": "The result is ALWAYS an array (even if there's only one match). You usually need an $unwind stage right after a $lookup.",
                "hook": "$lookup = SQL JOIN."
            }
        ],
        "qna": [
            {"q": "Examiner: What data type does the 'as' field in a $lookup produce?", "a": "It produces an array containing all matching documents from the foreign collection."}
        ]
    },
    "13day.js": {
        "title": "Indexes and Performance",
        "concepts": [
            {
                "name": "Indexes & Execution Stats",
                "breakdown": "Indexes make queries faster by ordering fields (B-Tree). .explain('executionStats') shows how the query was processed (COLLSCAN vs IXSCAN).",
                "use_case": "Optimizing a slow query that searches by email or username.",
                "gotcha": "Indexes speed up reads but slow down writes (inserts/updates/deletes) because the index must be updated too. Don't index every field.",
                "hook": "COLLSCAN = Bad (reads everything). IXSCAN = Good (reads index)."
            }
        ],
        "qna": [
            {"q": "Examiner: What is a COLLSCAN and why is it problematic?", "a": "Collection Scan. It means the database had to look at every single document to find the result, which is extremely slow on large datasets."},
            {"q": "Examiner: How do you enforce uniqueness on a field?", "a": "Create a unique index: db.collection.createIndex({email: 1}, {unique: true})"}
        ]
    }
}

slides_data = [
    {
        "id": "crud-playbook",
        "deck_number": 1,
        "icon": "⚡",
        "category": "CRUD & Core",
        "filename": "MongoDB_CRUD_Survival_Guide.pdf",
        "title": "MongoDB CRUD Playbook",
        "description": "Essential foundational playbook for database creation, collections, document insertion, and robust query patterns.",
        "topics": ["insertOne / insertMany", "find() queries", "updateOne / updateMany", "delete filters", "Cursor methods"],
        "highlights": [
            "Implicit database & collection creation gotchas",
            "updateOne vs updateMany behavioral divergence",
            "Projection mechanics & cursor iteration optimization"
        ],
        "size": "10.6 MB",
        "related_lessons": [
            {"num": "1", "title": "Basic Structure & CRUD"},
            {"num": "5", "title": "Projection, Sort, Skip, Limit"}
        ]
    },
    {
        "id": "operator-playbook",
        "deck_number": 2,
        "icon": "🔍",
        "category": "Operators & Arrays",
        "filename": "MongoDB_Operator_Playbook.pdf",
        "title": "MongoDB Operator Playbook",
        "description": "Comprehensive reference guide to comparison, logical, and element query operators for high-precision filtering.",
        "topics": ["$gt / $gte / $lt / $lte", "$in / $nin", "$and / $or / $nor", "$exists / $type", "Regex Filters"],
        "highlights": [
            "$in array syntax traps vs single value mistakes",
            "Short-circuit evaluation in compound $or queries",
            "$exists: false vs null field nuances"
        ],
        "size": "10.9 MB",
        "related_lessons": [
            {"num": "2", "title": "Comparison Operators"},
            {"num": "3", "title": "Logical Operators"}
        ]
    },
    {
        "id": "array-query-playbook",
        "deck_number": 3,
        "icon": "🧩",
        "category": "Operators & Arrays",
        "filename": "MongoDB_Array_Query_Playbook.pdf",
        "title": "MongoDB Array Query Playbook",
        "description": "Mastering nested arrays, multidimensional objects, subdocuments, and targeted document querying in MongoDB.",
        "topics": ["$all", "$elemMatch", "$size", "Positional operator $", "Dot notation"],
        "highlights": [
            "Why simple dot notation fails on multi-criteria array objects",
            "$elemMatch exact mechanics for subdocument arrays",
            "$size exact match limits & indexing workarounds"
        ],
        "size": "14.9 MB",
        "related_lessons": [
            {"num": "4", "title": "Array & Embedded Document Queries"}
        ]
    },
    {
        "id": "update-operator-dossier",
        "deck_number": 4,
        "icon": "🔄",
        "category": "CRUD & Core",
        "filename": "MongoDB_Update_Operator_Dossier.pdf",
        "title": "MongoDB Update Operator Dossier",
        "description": "Field modifications, array mutations, upserts, and atomic state transitions without data corruption.",
        "topics": ["$set / $unset", "$inc / $mul", "$push / $pull / $pop", "$addToSet / $each", "upsert: true"],
        "highlights": [
            "Accidental document replacement without $set",
            "$addToSet deduplication vs $push append behavior",
            "Array filters with $[identifier] for selective sub-updates"
        ],
        "size": "8.9 MB",
        "related_lessons": [
            {"num": "6", "title": "Update Operators"}
        ]
    },
    {
        "id": "schema-dossier",
        "deck_number": 5,
        "icon": "🛡️",
        "category": "Schema & Architecture",
        "filename": "MongoDB_Schema_Dossier.pdf",
        "title": "MongoDB Schema Dossier",
        "description": "JSON schema validation, strict typing rules, data integrity enforcement, and ordered vs unordered execution.",
        "topics": ["$jsonSchema", "bsonType validation", "required properties", "validationLevel", "ordered inserts"],
        "highlights": [
            "ordered: true failure rollback behavior vs ordered: false",
            "Strict bsonType validation with regex patterns",
            "validationAction: error vs warn production tradeoffs"
        ],
        "size": "18.0 MB",
        "related_lessons": [
            {"num": "7", "title": "Schema Validation (Part 1)"},
            {"num": "8", "title": "Schema Validation (Part 2) & Ordered Inserts"}
        ]
    },
    {
        "id": "aggregation-mastery",
        "deck_number": 6,
        "icon": "📊",
        "category": "Aggregation",
        "filename": "MongoDB_Aggregation_Mastery.pdf",
        "title": "MongoDB Aggregation Mastery",
        "description": "Comprehensive pipeline stages from basic transforms and joins to complex multi-stage analytical queries.",
        "topics": ["$match & $project", "$group & accumulators", "$unwind arrays", "$lookup joins", "$bucketAuto", "$facet"],
        "highlights": [
            "Pipeline order optimization ($match first for early filter)",
            "$lookup produce array gotcha requiring $unwind",
            "RAM limit (100MB) per stage & allowDiskUse option"
        ],
        "size": "18.9 MB",
        "related_lessons": [
            {"num": "9", "title": "Aggregation Framework (Basic)"},
            {"num": "10", "title": "Aggregation: Unwind & Group"},
            {"num": "11", "title": "Aggregation: Buckets & Sets"},
            {"num": "12", "title": "Aggregation: $lookup (Joins)"}
        ]
    },
    {
        "id": "interview-dossier",
        "deck_number": 7,
        "icon": "🎯",
        "category": "Viva & Interviews",
        "filename": "MongoDB_Interview_Dossier.pdf",
        "title": "MongoDB Interview Dossier",
        "description": "Curated high-yield architectural, indexing, replication, and performance questions for technical rounds.",
        "topics": ["Indexing (B-Tree, compound, multikey)", "Execution stats (IXSCAN vs COLLSCAN)", "WiredTiger storage", "Replica sets & Sharding"],
        "highlights": [
            "Index ESR rule (Equality, Sort, Range) design principles",
            "Covered queries (0 document scan from disk)",
            "Write concerns, read concerns, and replica election failovers"
        ],
        "size": "9.4 MB",
        "related_lessons": [
            {"num": "13", "title": "Indexes and Performance"}
        ]
    },
    {
        "id": "viva-blueprint",
        "deck_number": 8,
        "icon": "🎓",
        "category": "Viva & Interviews",
        "filename": "MongoDB_Viva_Blueprint.pdf",
        "title": "MongoDB Viva Blueprint",
        "description": "High-impact active recall blueprint designed for viva exams, oral board questions, and rapid oral review.",
        "topics": ["Examiner gotchas & traps", "Key definitions & syntax", "BSON vs JSON", "ACID & Transactions", "C-D-C-D hierarchy"],
        "highlights": [
            "BSON binary serialization vs JSON text differences",
            "Multi-document ACID transactions via sessions",
            "Examiner trick questions on null vs missing keys"
        ],
        "size": "11.1 MB",
        "related_lessons": []
    }
]

