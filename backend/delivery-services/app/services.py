from . import db
from .models import Delivery

class DeliveryService:
    def create_delivery(self, delivery_data):
        new_delivery = Delivery(**delivery_data)
        db.session.add(new_delivery)
        db.session.commit()
        return {'id': new_delivery.id, 'order_id': new_delivery.order_id, 'status': new_delivery.status}

    def get_all_deliveries(self):
        deliveries = Delivery.query.all()
        return [{'id': d.id, 'order_id': d.order_id, 'status': d.status} for d in deliveries]

    def get_delivery_by_id(self, delivery_id):
        delivery = Delivery.query.get(delivery_id)
        if delivery:
            return {'id': delivery.id, 'order_id': delivery.order_id, 'status': delivery.status}
        return None

    def update_delivery(self, delivery_id, delivery_data):
        delivery = Delivery.query.get(delivery_id)
        if delivery:
            for key, value in delivery_data.items():
                setattr(delivery, key, value)
            db.session.commit()
            return {'id': delivery.id, 'order_id': delivery.order_id, 'status': delivery.status}
        return None

    def delete_delivery(self, delivery_id):
        delivery = Delivery.query.get(delivery_id)
        if delivery:
            db.session.delete(delivery)
            db.session.commit()
            return True
        return False