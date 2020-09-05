import pyotp

def get_code_2fa(code):
    code = code.replace(" ", "")
    totp = pyotp.TOTP(code)
    return totp.now()