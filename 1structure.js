
/*
cluster
    database    
        collection
            document => individual data


to access database from terminal
mongosh

1. to see all database
    show dbs

2. to create database
    use <databaseName> => use daraz

3. to create collection
    db.createCollection("<collectionName>")

4. to see all collection
    show collections

5. naming convention
    databaseName => singular
    collectionName => plural

daraz
    products
    users


create document
db.products.insertOne({name:"laptop", price:100000})
db.products.insertMany([{name:"Tv", price:50000}, {name:"Mobile", price:20000}])

read document
db.products.find()


update document
db.products.updateOne(filter, updatedata) => updateOne({name:"laptop"}, {$set:{price:120000}})
db.products.updateOne({name:"Tv"}, {$set:{name:"tv", price:120000, quantity:10}})

delete document
db.products.deleteOne(filter)

db.products.deleteOne({name:"Mobile"})
*/

/*

Product.create(data)
Product.find()
Product.findById(id)
Product.findByIdAndUpdate(id, data)=>(filter, data)
Product.findByIdAndDelete(id)


//difference between sql and nosql

*/


