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
