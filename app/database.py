from motor.motor_asyncio import AsyncIOMotorClient
mongo_url="mongodb://localhost:27017/"
client=AsyncIOMotorClient(mongo_url)
db=client.ecommdb

admin_collection=db.admins
book_collection=db.books
discount_collection=db.discounts
giftvoucher_collection=db.giftvouchers
order_collection=db.orders
payment_collection=db.payments
productcategory_collection=db.productcategories
productinventory_collection=db.productinventories
review_collection=db.reviews
shipping_collection=db.shippings
user_collection=db.users