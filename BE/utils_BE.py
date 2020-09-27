"""Utils write for Controller"""


def check_unavailable_list(listAccount: list, listAvailableAccount: list):
    """
    Check if account in list account is in list available account and return an tuple of unavailable account
    :param listAccount: list form [[uid, pass, code2fa], ...]
    :param listAvailableAccount: list form [Account object, ...]
    :return: tuple of list unavailable account
    """
    listUnavailableAcc = []
    for acc in listAccount:
        # listUnavailableAcc.append(tuple(acc))
        flag = True
        if len(listAvailableAccount) != 0:
            for acc_available in listAvailableAccount:
                if acc_available.uid == acc[0]:
                    # listUnavailableAcc.remove(tuple(acc))
                    flag = False
                    break
        if flag:
            listUnavailableAcc.append(tuple(acc))
    listUnavailableAcc = tuple(listUnavailableAcc)
    return listUnavailableAcc


def get_available_account(listUid: list, listAvailableAccount: list):
    listAccounts = []
    for uid in listUid:
        flag = False
        acc_available = None
        for acc in listAvailableAccount:
            if uid == acc.uid:
                acc_available = acc
                flag = True
                break
        if flag:
            listAccounts.append(acc_available)

    return listAccounts
