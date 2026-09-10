/*  
$lookup means join
join products table with orders table
db.products.aggregate([
  {
    $lookup: {
      from: "orders",
      localField: "_id",
      foreignField: "product_id",
      as: "order_details"
    }
  }
])

// join orders table with products table
db.orders.aggregate([
  {
    $lookup: {
      from: "products",
      localField: "product_id",
      foreignField: "_id",
      as: "product_details"
    }
  }
])

// Find products with rating > 4.5
db.products.aggregate([
  {
    $match: {
      rating: { $gt: 4.5 }
})] 

// Display products and claculate where tax: 5% of price
db.products.aggregate([
  {
    $addFields  : { tax: { $multiply: [ "$price", 0.05 ] } }
  }
])


\\ Find the average price of all products
db.products.aggregate([
{
$group: {
_id: null,
averageprice: {$avg:"$price"}
}
}])

// find the maximum price of all products
db.products.aggregate([
  {
    $group: {
      _id: null,
      maxPrice: { $max: "$price" }
    }
  }
])

\\ find the total category
db.products.aggregate([
{
$group:{
_id: null,
category: {$push:"$category"}
}
}
])

db.products.aggregate([
{
$group:{
_id: null,
category: {$addToSet:"$category"}
}
}
])

\\ Find the avergae price of each category
db.products.aggregate([
{
$group: {
_id: "$category",
averageprice: {$avg:"$price"}
}
}
])

\\ Find all brand
db.products.aggregate([
{
$group: {
_id: null,
brand: {$addToSet:"$brand"}
}
}
])







*/