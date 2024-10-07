from app.models import Delivery, db

def create_delivery(data):
    delivery = Delivery(user_id=data['user_id'], address=data['address'], status='Pending')
    db.session.add(delivery)
    db.session.commit()
    return delivery

def get_delivery_by_id(delivery_id):
    return Delivery.query.filter_by(id=delivery_id).first()
