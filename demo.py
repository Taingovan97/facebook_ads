idVA = '100005188112837'
idTai = '100050911668510'
idTien = '100007481102571'
idKh = '100006167431862'
idDu = '100005577933869'
p = 'tai@28293839'
from BE.core import constants
from FacebookWebBot import *
from selenium import webdriver
from BE.core import api_addFr, api_login_dFace

driv, cookie = api_login_dFace.login(fbUsername=100020276508848, fbPassword='nguyenhonganh_safe_pw_2020081912', code_2fa='KQFW ZBBJ 4KK4 WCB4 TCJT MM7L TW72 HLFA' )
api_addFr.addFriend(driv, '100054979471718')
api_addFr.addFriend(driv, '100054728444028')
api_addFr.addFriend(driv, '100054697154892')
