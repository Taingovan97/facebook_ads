from .model.account import Account


def dataToAccount(data):
    """
    Transfer data (in form of a tuple) to object Account, form data ()
    :param data: data from tuple (uid, name, password, code2fa, cookie, token, bank, status)
    :return: an Account object of data
    """
    account = Account(uid=data[0], name=data[1], password=data[2], code2fa=data[3], )
    return account
