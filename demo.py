idVA = '100005188112837'
idTai = '100050911668510'
idTien = '100007481102571'
idKh = '100006167431862'
idDu = '100005577933869'
p = 'tai@28293839'
from BE.core import constants
# from FacebookWebBot import *
from selenium import webdriver
from BE.core import api_addFr, api_login_dFace, api_accept_friend

#driv, cookie = api_login_dFace.login(fbUsername='100020276508848', fbPassword='nguyenhonganh_safe_pw_2020081912', code_2fa='KQFW ZBBJ 4KK4 WCB4 TCJT MM7L TW72 HLFA' )
#
# api_addFr.addFriend(driv, '100054827978833')
#driv2, cookie2 = api_login_dFace.login(fbUsername='100054827978833', fbPassword='0708952952VN2020', code_2fa='2DYUIJJDCBUU43QZKGZIZFU5L2GTRP2X' )
# api_accept_friend.acceptFr(driv2)

from BE import Account
from BE import facebook
acc1 = Account(uid='100054951511660', password= '0708952952VN2020', code2fa= 'UTULAO3GBZARRR2LSMGD3TRS2Y7RGEYH')
fa1 = facebook(acc=acc1)
fa1.login()

acc2 = Account(uid='100054827978833', password='0708952952VN2020', code2fa='2DYUIJJDCBUU43QZKGZIZFU5L2GTRP2X')
fa2 = facebook(acc2)
#fa1.addFriend(fa2.acc.uid)
# print(fa2.login())