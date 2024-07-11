import random
import string

def generate_voucher_code(length=10):
    voucher = ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))
    print(voucher)
    return voucher