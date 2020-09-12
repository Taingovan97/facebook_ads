from BE.core import api, constants

if __name__ == "__main__":
    driver_clone = api.login(constants.username_clone, constants.pass_clone, constants.key2fa_clone)

    # driver_via = api.login(constants.username_via, constants.pass_via, constants.key2fa_via)

    #driver_clone = api.login(constants.username_clone, constants.pass_clone, constants.key2fa_clone, idUser='12345678')

    #driver_via = api.login(constants.username_via, constants.pass_via, constants.key2fa_via, idVia, idClone)
