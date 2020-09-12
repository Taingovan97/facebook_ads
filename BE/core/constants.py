# acc 3
username_clone = '100054940742066'
pass_clone = '0708952952VN2020'
key2fa_clone = '7I4O64Z2C2A24WQM2Q3ZYLAHU6OR6FFY'
# acc 2
username_via = "100054727874205"
pass_via = "0708952952VN2020"
key2fa_via = "674DQOOCZPD2FVTGT6QNJBCL7TZDJIMO"

# Chrome path
CHROME_PATH = r'C:\Users\Administrator\Downloads\Compressed\chromedriver_win32\chromedriver.exe'

def getUrl(idFriend):
    url = "https://www.facebook.com/ajax/add_friend/action/?to_friend=" + idFriend + "&action=add_friend&how_found=profile_button&ref_param=unknown&link_data[gt][type]=xtracking&link_data[gt][xt]=48.%7B%22event%22%3A%22add_friend%22%2C%22intent_status%22%3Anull%2C%22intent_type%22%3Anull%2C%22profile_id%22%3A100007481102571%2C%22ref%22%3A1%7D&link_data[gt][profile_owner]=100007481102571&link_data[gt][ref]=timeline%3Atimeline&logging_location=&http_referer=https%3A%2F%2Fwww.facebook.com%2F%3Fref%3Dtn_tnmn&floc=profile_button&frefs[0]=unknown"
    return url

def getHeader(idFriend, str):
    headers = {
        'authority': 'www.facebook.com',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36',
        'viewport-width': '710',
        'content-type': 'application/x-www-form-urlencoded',
        'accept': '*/*',
        'origin': 'https://www.facebook.com',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://www.facebook.com/?id=' + idFriend,
        'accept-language': 'en-US,en;q=0.9,vi;q=0.8,fr;q=0.7',
        'cookie': str
    }
    return headers

def getPayLoad(idUser):
    payload = '__user=' + idUser + '&__a=1&__dyn=7AgNeS4amaWxd2u6aJGi9FxqeCwKAKGgmAGt94WpEbE9ES2N6xCaxubwTwyCwVBDyubnyorxuF98ScDKaxeUPwExaawCx138S2SQh6UXU9468Oajz8gCxm3i5VokKeyEqx66Ecolm26q499oeGzUWeCxy1hzFVk3K6UowJxCWxS68nBy8pK44WwTgCmfx-byEkyob-1dx3xiGzXAxeQm3a4ogzd29pUiAUG2HQ7FbBojUC6po-fz8Cm4U9898GfxnCxi7Wz8GEcE-h2EgVFXAy8aElxeaKE-3m4rybCzogy898e8Wqexp2UtGi9zEO2-by8ix22mbwgUuG15xmE9EjwgEiK8xi8BwBzUuwFABwkUjxy224Umwso88co9oy5olxa2m4UcUSUjwhE&__csr=&__req=bh&__beoa=0&__pc=PHASED%3ADEFAULT&dpr=1&__ccg=EXCELLENT&__rev=1002636893&__s=0gddvj%3Atoxfuv%3A74i0ia&__hsi=6870840823560647435-0&__comet_req=0&fb_dtsg=AQGMpYl37ZuY%3AAQFBnJ7M4FMs&jazoest=21975&__spin_r=1002636893&__spin_b=trunk&__spin_t=1599677290'
    return payload
