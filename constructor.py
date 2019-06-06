class cash_register :
    ##Constructor a cash register with cleared item count and total
    #
    def __init__(self):
        self._item_count = 0
        self._total_price = 0.0

## Adds an item to this cash register
# #@param price the price of this item
#
    def add_item(self, price) :
        self._item_count = self._item_count  + 1
        self._total_price = self._total_price + price
## Gets the price of all items in the current sale.
#  @return the total price
#
    def get_total(self):
        return self._total_price
## Gets the number of items in the current sale.
# @return the item count
# 
    def get_count(self):
        return self._item_count
## Clear the item count and the total.
# 
    def clear(self):
        self._item_count = 0
        self._total_price = 0.0

register = cash_register()
register.add_item(5)
register.add_item(20)
register.add_item(30)
register.clear()
print(register.get_total())
print(register.get_count())

        
