import string
import logging from email.utils import parseaddr
import re
import secrets
from . models import Coupon
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