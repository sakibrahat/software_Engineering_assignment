from app.models import Item

class ItemViewModel:
    def __init__(self, item=None):
        self.item = item

    def to_dict(self):
        if self.item:
            return {
                'id': self.item.id,
                'name': self.item.name,
                'description': self.item.description,
                'created_at': self.item.created_at,
                'updated_at': self.item.updated_at,
            }
        return None

    @staticmethod
    def get_all_items():
        items = Item.objects.all()
        return [ItemViewModel(item).to_dict() for item in items]

    @staticmethod
    def get_item_by_id(item_id):
        item = Item.objects.filter(id=item_id).first()
        return ItemViewModel(item) if item else None
