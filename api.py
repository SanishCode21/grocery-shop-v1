from flask_restful import Api, Resource, reqparse
from flask import jsonify
from models import db, Category, Product, Order
from datetime import datetime

api = Api()

# ----------- CATEGORY ENDPOINT -----------
class CategoryResource(Resource):
    def get(self):
        categories = Category.query.all()
        return jsonify([{"id": c.id, "name": c.name} for c in categories])

# ----------- PRODUCT ENDPOINTS (CRUD) -----------

product_parser = reqparse.RequestParser()
product_parser.add_argument('name', type=str, required=True)
product_parser.add_argument('price', type=float, required=True)
product_parser.add_argument('category_id', type=int, required=True)
product_parser.add_argument('quantity', type=int, required=True)
product_parser.add_argument('man_date', type=str, required=True)


class ProductListResource(Resource):
    def get(self):
        products = Product.query.all()
        return [
            {
                "id": p.id,
                "name": p.name,
                "price": p.price,
                "category_id": p.category_id,
                "quantity": p.quantity,
                "man_date": p.man_date.strftime("%Y-%m-%d")
            }
            for p in products
        ], 200

    def post(self):
        args = product_parser.parse_args()
        try:
            man_date = datetime.strptime(args['man_date'], "%Y-%m-%d").date()

            product = Product(
                name=args['name'],  # type: ignore
                price=args['price'], # type: ignore
                category_id=args['category_id'], # type: ignore
                quantity=args['quantity'],  # type: ignore
                man_date=man_date   # type: ignore
            )

            db.session.add(product)
            db.session.commit()

            return {
                "message": "Product added successfully.",
                "product": {
                    "id": product.id,
                    "name": product.name,
                    "price": product.price,
                    "category_id": product.category_id,
                    "quantity": product.quantity,
                    "man_date": product.man_date.strftime("%Y-%m-%d")
                }
            }, 201

        except Exception as e:
            return {"error": str(e)}, 400
        
class ProductResource(Resource):
    def get(self, id):
        product = Product.query.get_or_404(id)
        return jsonify({
            "id": product.id,
            "name": product.name,
            "price": product.price,
            "category_id": product.category_id,
            "quantity": product.quantity,
            "man_date": product.man_date.strftime("%Y-%m-%d")
        })

    def put(self, id):
        product = Product.query.get_or_404(id)
        args = product_parser.parse_args()
        try:
            product.name = args['name']
            product.price = args['price']
            product.category_id = args['category_id']
            product.quantity = args['quantity']
            product.man_date = datetime.strptime(args['man_date'], "%Y-%m-%d")
            db.session.commit()
            return jsonify({"message": "Product updated successfully."})
        except Exception as e:
            return jsonify({"error": str(e)}), 400

    def delete(self, id):
        product = Product.query.get_or_404(id)
        db.session.delete(product)
        db.session.commit()
        return jsonify({"message": "Product deleted successfully."})

# ----------- ORDER ENDPOINT -----------

class OrderResource(Resource):
    def get(self):
        orders = Order.query.all()
        return jsonify([
            {
                "id": o.id,
                "transaction_id": o.transaction_id,
                "product_id": o.product_id,
                "quantity": o.quantity,
                "price": o.price
            } for o in orders
        ])

# ----------- API ROUTES -----------
api.add_resource(CategoryResource, '/api/categories')
api.add_resource(ProductListResource, '/api/products')
api.add_resource(ProductResource, '/api/products/<int:id>')
api.add_resource(OrderResource, '/api/orders')
