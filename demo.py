idVA = '100005188112837'
idTai = '100050911668510'
idTien = '100007481102571'
idKh = '100006167431862'
idDu = '100005577933869'
p = 'tai@28293839'

from BE.core import api_login, api_addFr

driv, cookie = api_login.login(idTai, p)
run = api_addFr.addFriend(driv, idKh)