import string
import logging from email.utils import parseaddr
import re
import secrets
from . models import Coupon 
from . models import Order
def generate_coupon_code(length=10):
    characters=string.ascii_uppercase+string.digits
    while True:
        code=''.join(secrets.choice(characters)) for _ in range(length))

        if not Coupon.objects.filter(code=code).exists():
            return code
logger=logging.getLogger(__name__)
def is_valid_email(email:str)->bool:
    try:
        if not email or not isinstance(email,str):
            return False

        name,addr=parseaddr(email)
        if not addr:
            return False
        pattern=r'^[a-zA-Z0-9._%+-]+@[a-zA-Z)-9.-]+\.[a-zA-Z]{2,}$"
        if not re.match(pattern,addr):
            return False
        return True
        except Exception as e:
            logger.error(f'Email validation error:{e}')
            return False
def get_daily_sales_total(target_date:date):
    sales_data=(order.objects.filter(created_at__date=target_date).aggregate(total_sum=Sum('total_price')))
    return sales_data['total_sum'] or 0

def is_restaurant_open():
    now=datetime.now()
    current_day=now.weekday()
    current_time=now.time()
    opening_hours={
        0: time(9,0),time(22,0)),
    }
    open_time, close_time=opening_hours[current_day]
    return open_time<=current_time<=close_time


def generate_unique_order_id(length=8):
    characters=string.ascii_uppercase+string.digits
    while True:
        order_id=''.join(secrets.choice(charcters) for _ in range(length))
        if not Order.objects.filter(order_id=order_id).exists():
            return order_id

