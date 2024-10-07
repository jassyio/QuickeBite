from app.models import Delivery, db
import logging

logging.basicConfig(level=logging.INFO)
def create_delivery(data):
    logging.info(f'Creating delivery for user {data["user_id"]}')
    delivery = Delivery(user_id=data['user_id'], address=data['address'], status='Pending')
    db.session.add(delivery)
    db.session.commit()
    return delivery

def get_delivery_by_id(delivery_id):
    logging.info(f'Retrieving delivery with id {delivery_id}')
    return Delivery.query.filter_by(id=delivery_id).first()
