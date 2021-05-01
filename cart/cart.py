from	decimal	import	Decimal
from	django.conf	import	settings
from	preghome.models	import	Product
from coupons.models import Coupon 

class Cart(object):
    def __init__(self, request):
        """
            Initialize the cart
        """
        self.session = request.session 
        cart = self.session.get(settings.CART_SESSION_ID)

        if not cart:
            #save an empty  cart in the session
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart
        #we require the cart to be initialized with arequest onject, we store the current session
        #using self.session to make it accessible to the other mthds of the Cart class.
        #we firstly try to get the cart from the current session using 
        #self.session.get(settings.CART_SESSION_ID),if no cart is present in the session,
        #we create an empty cart by setting an empty dictionary in the session
        #expect our cart dictionary to use product IDs as keys and adictionary with quantity and
        #price as the value for each key



        #==ading the code to initialzie the coupon from the current session
        #store current applied coupon
        self.coupon_id = self.session.get('coupon_id')#get the coupon_id session key from the current session
        #and store its value in the Cart object
    def add(self, product, quantity=1, update_quantity=False):
        """Add aproduct to the cart or update its quantity"""
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity':	0,'price':	str(product.price)}
        else:
            self.cart[product_id]['quantity']	+=	quantity
        self.save()#  ===save the cart in the session, save mthd marks the sessionas modified
        #= True this tells django that the session has changed and needs to be saved
        #use the product id AS AKEY IN the cart's content dictionary,convert the product ID into
        #astring because django uses JSON to serialize session data,remember to convert product
        #price into string inorder to serialize it
        
    def save(self):
        #mark the session as modified to make sure it gets saved
        self.session.modified = True
        #===mthd to reove product from the cart.
    def remove(self,product):
        """Remove	a	product	from	the	cart"""
        product_id	=	str(product.id)
        if	product_id	in	self.cart:
            del	self.cart[product_id]
            self.save()#removes agiven product from the cart dictionary and calls the save() mthd
            #to upadte the cart in the session
        
    def __iter__(self):
        """iterate over the items in the cart and get products from the database"""
        product_ids = self.cart.keys()
        #ge the	product	objects	and	add	them to	the	cart
        products = Product.objects.filter(id__in=product_ids)
        cart = self.cart.copy()
        for product in products:
            cart[str(product.id)]['product'] = product
        for item in cart.values():
            item['price'] =  Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item
            #we retrieve the product instances that are presnet in the cart to include them in the
            #cart items,we copy the current cart in the cart variable and add the Product instances
            #to it.
            #finally iterate over the cart items,converting the item's price backnto decimal and add
            #atotal_price attribute to each item,now we can iterate over the items in the cart.

    def __len__(self):
        """count all items in the cart"""
        return sum(item['quantity'] for item in self.cart.values())

    #mthd to calculate the total cost of items in the cart

    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())

    #now a mthd to clear the cart sessio
    def  clear(self):
        #remove cart from session
        del self.session[settings.CART_SESSION_ID]
        self.save()

    @property#specifies that the attribute is also an attribute of the Cart object.
    def coupon(self):
        if self.coupon_id:
            return Coupon.objects.get(id=self.coupon_id)
        return None 
    def get_discount(self):
        if self.coupon:
            return (self.coupon.discount / Decimal('100')) * self.get_total_price()
        return Decimal('0')
    
    def get_total_price_after_discount(self):
        return self.get_total_price() - self.get_discount()

#coupon mthd is defined as property,if cart contains a coupon_id attribute,the Coupon object with the given ID
#is returned

#