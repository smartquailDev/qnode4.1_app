from decimal import Decimal
from django.conf import settings
from services.models import Product
from coupons.models import Coupon
from orders.models import Order


class Cart_C(object):

    def __init__(self, request):
        """
        Initialize the cart.
        """
        self.session = request.session
        cart_c = self.session.get(settings.CART_C_SESSION_ID)
        if not cart_c:
            # save an empty cart in the session
            cart_c = self.session[settings.CART_C_SESSION_ID] = {}
        self.cart_c = cart_c
        self.coupon_id = self.session.get('coupon_id')
        self.order_id = self.session.get('order_id')

    def __iter__(self):
        """
        Iterate over the items in the cart and get the products 
        from the database.
        """
        product_ids = self.cart_c.keys()
        order_ids = self.cart_c.keys()
        # get the product objects and add them to the cart
        products = Product.objects.filter(id__in=product_ids)
        orders = Order.objects.filter(id__in=order_ids)

        cart_c = self.cart_c.copy()
        
        for order in orders:
            cart_c[str(order.id)]['order'] = order
        
        for item in cart_c.values():
            item['first_name'] = item['first_name']
            item['last_name'] = item['last_name']
            item['CI'] = Decimal(item['CI'])
            item['email'] = item['email']
            item['address'] = item['address']
            item['city'] = item['city']
            item['created'] = item['created']
            yield item

        for product in products:
            cart_c[str(product.id)]['product'] = product

        for item in cart_c.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item
    
    def __len__(self):
        """
        Count all items in the cart.
        """
        return sum(item['quantity'] for item in self.cart_c.values())

    def add(self, product, quantity=1, update_quantity=False):
        """
        Add a product to the cart or update its quantity.
        """
        product_id = str(product.id)
        if product_id not in self.cart_c:
            self.cart_c[product_id] = {'quantity': 0,
                                      'price': str(product.price)}
        if update_quantity:
            self.cart_c[product_id]['quantity'] = quantity
        else:
            self.cart_c[product_id]['quantity'] += quantity
        self.save()

    def save(self):
        # mark the session as "modified" to make sure it gets saved
        self.session.modified = True

    def remove(self, product):
        """
        Remove a product from the cart.
        """
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())

    def clear(self):
        # remove cart from session
        del self.session[settings.CART_C_SESSION_ID]
        self.save()


    @property
    def coupon(self):
        if self.coupon_id:
            return Coupon.objects.get(id=self.coupon_id)
        return None

    def get_discount(self):
        if self.coupon:
            return (self.coupon.discount / Decimal('100'))*self.get_total_price()
        return Decimal('0')

    def get_total_price_after_discount(self):
        return self.get_total_price() - self.get_discount()
        