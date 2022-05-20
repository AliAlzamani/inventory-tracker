from flask_sqlalchemy import SQLAlchemy
 
db = SQLAlchemy()
 
class ItemModel(db.Model):
    __tablename__ = "table"
 
    id = db.Column(db.Integer, primary_key=True)
    item_id = db.Column(db.Integer(),unique = True)
    discription = db.Column(db.String())
    quantity = db.Column(db.Integer())
    manufacturer = db.Column(db.String(80))
 
    def __init__(self, item_id,discription,quantity,manufacturer):
        self.item_id = item_id
        self.discription = discription
        self.quantity = quantity
        self.manufacturer = manufacturer
 
    def __repr__(self):
        return f"{self.discription}:{self.item_id}"
