/* 
db.students.updateMany({name:"ram"}, {$set:{country:"nepal"}}) // update all documents where name is "ram" and set country to "nepal"
db.students.updateMany({},{$inc:{age:10}}) // increment age by 10 for all documents
db.students.updateMany({},{$inc:{age:-10}}) // decrement age by 10 for all documents
db.students.updateMany({},{$mul:{age:10}}) // multiply age by 10 for all documents
db.students.updateMany({},{$mul:{age:1/10}}) // divide age by 10 for all documents
db.students.updateMany({},{$rename:{course:"subject"}}) // rename course field to subject for all documents
db.students.updateMany({},{$unset:{city:"", age:""}}) // remove city field from all documents

upsert
db.students.updateMany(filter, data, upsert)

db.students.updateMany({name:"ram"}, {$set:{country:"nepal"}}, {upsert:true})
db.students.updateMany({name:"roshan"}, {$set:{country:"nepal"}}, {upsert:true}) // if upsert is false then it will not create a new document if no document is found with the filter condition

delete
db.students.deleteMany({}) // delete all documents 

update array
db.students.updateMany({name:"ram"}, {$push:{skills:"react"}})
db.students.updateMany({name:"ram"}, {$addToSet:{skills:"css"}})
db.students.updateMany({name:"ram"}, {$addToSet:{skills:"python"}})
 
remove data using pop
db.students.updateMany({name:"gita"}, {$pop:{skills:1}})
db.students.updateMany({name:"sita"}, {$pull:{skills:"html"}})
db.students.updateMany({name:"ram"}, {$pullAll:{skills:["html","react"]}})
db.students.updateMany({}, {$pull:{experience:{company:"A"}}})
*/
