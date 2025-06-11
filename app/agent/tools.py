from langchain.tools import tool
from typing import List, Dict, Any, Optional
from app.database import (
    order_collection, user_collection, payment_collection,
    shipping_collection, productinventory_collection,
    productcategory_collection, review_collection,
    giftvoucher_collection, discount_collection,
    admin_collection, book_collection
)
@tool
async def get_admins(
    admin_id: Optional[str] = None,
    name: Optional[str] = None,
    email: Optional[str] = None,
) -> List[Dict[str, Any]]:
    """Fetch all admins."""
    query = {}
    if admin_id:
        query["admin_id"] = admin_id
    if name:
        query["name"] = name
    if email:
        query["email"] = email
    results = await admin_collection.find(query).to_list(length=None)
    return results
@tool
async def get_books(
    book_id: Optional[str] = None,
    title: Optional[str] = None,
    author: Optional[str] = None,
    price: Optional[str] = None,
) -> List[Dict[str, Any]]:
    """Fetch all books from the database."""
    query = {}
    if book_id:
        query["book_id"] = book_id
    if author:
        query["author"] = author
    if title:
        query["title"] = title
    if price:
        query["price"] = float(price)
    results = await book_collection.find(query).to_list(length=None)
    return results
@tool
async def get_discounts(
    discount_id: Optional[str] = None,
    code: Optional[str] = None,
    percentage: Optional[str] = None,
) -> List[Dict[str, Any]]:
    """Fetch all available discounts."""
    query = {}
    if discount_id:
        query["discount_id"] = discount_id
    if code:
        query["code"] = code
    if percentage:
        query["percentage"] = float(percentage)
    results = await discount_collection.find(query).to_list(length=None)
    return results
@tool
async def get_giftvouchers(
    voucher_id: Optional[str] = None,
    amount: Optional[str] = None,
    recipient: Optional[str] = None,
) -> List[Dict[str, Any]]:
    """Fetch all gift vouchers."""
    query = {}
    if voucher_id:
        query["voucher_id"] = voucher_id
    if amount:
        query["amount"] = float(amount)
    if recipient:
        query["recipient"] = recipient
    results = await giftvoucher_collection.find(query).to_list(length=None)
    return results
@tool
async def get_orders(
    order_id: Optional[str] = None,
    user_id: Optional[str] = None,
    total: Optional[str] = None,
    status: Optional[str] = None,
) -> List[Dict[str, Any]]:
    """Fetch orders from the database."""
    query = {}
    if order_id:
        query["order_id"] = order_id
    if user_id:
        query["user_id"] = user_id
    if total:
        query["total"] = float(total)
    if status:
        query["status"] = status
    results = await order_collection.find(query).to_list(length=None)
    return results
@tool
async def get_payments(
    payment_id: Optional[str] = None,
    order_id: Optional[str] = None,
    amount: Optional[str] = None,
    method: Optional[str] = None,
) -> List[Dict[str, Any]]:
    """Fetch all payments info."""
    query = {}
    if payment_id:
        query["payment_id"] = payment_id
    if order_id:
        query["order_id"] = order_id
    if amount:
        query["amount"] = float(amount)
    if method:
        query["method"] = method
    results = await payment_collection.find(query).to_list(length=None)
    return results
@tool
async def get_categories(
    category_id: Optional[str] = None,
    name: Optional[str] = None,
) -> List[Dict[str, Any]]:
    """Fetch all product categories."""
    query = {}
    if category_id:
        query["category_id"] = category_id
    if name:
        query["name"] = name
    results = await productcategory_collection.find(query).to_list(length=None)
    return results
@tool
async def get_inventory(
    product_id: Optional[str] = None,
    stock: Optional[str] = None,
    location: Optional[str] = None,
) -> List[Dict[str, Any]]:
    """Fetch all product inventory."""
    query = {}
    if product_id:
        query["product_id"] = product_id
    if stock:
        query["stock"] = float(stock)
    if location:
        query["location"] = location
    results = await productinventory_collection.find(query).to_list(length=None)
    return results
@tool
async def get_reviews(
    review_id: Optional[str] = None,
    product_id: Optional[str] = None,
    rating: Optional[str] = None,
    comment: Optional[str] = None,
) -> List[Dict[str, Any]]:
    """Fetch all reviews."""
    query = {}
    if review_id:
        query["review_id"] = review_id
    if product_id:
        query["product_id"] = product_id
    if rating:
        query["rating"] = float(rating)
    if comment:
        query["comment"] = comment
    results = await review_collection.find(query).to_list(length=None)
    return results
@tool
async def get_shipping(
    shipping_id: Optional[str] = None,
    order_id: Optional[str] = None,
    status: Optional[str] = None,
    carrier: Optional[str] = None,
) -> List[Dict[str, Any]]:
    """Fetch all shipping info."""
    query = {}
    if shipping_id:
        query["shipping_id"] = shipping_id
    if order_id:
        query["order_id"] = order_id
    if status:
        query["status"] = status
    if carrier:
        query["carrier"] = carrier
    results = await shipping_collection.find(query).to_list(length=None)
    return results
@tool
async def get_users(
    user_id: Optional[str] = None,
    name: Optional[str] = None,
    email: Optional[str] = None,
    phone: Optional[str] = None,
) -> List[Dict[str, Any]]:
    """Fetch all users from the database."""
    query = {}
    if user_id:
        query["user_id"] = user_id
    if name:
        query["name"] = name
    if email:
        query["email"] = email
    if phone:
        query["phone"] = phone
    results = await user_collection.find(query).to_list(length=None)
    return results