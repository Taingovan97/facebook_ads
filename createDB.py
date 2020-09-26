from BE.dao.sqliteHelper import SqliteHelper
from constants import DATABASE_PATH

db = SqliteHelper(DATABASE_PATH)
db.create_table("""CREATE TABLE accountFb(
                            uid TEXT PRIMARY KEY,
                            name TEXT,
                            password TEXT,
                            code2fa TEXT,
                            cookie TEXT,
                            token TEXT,
                            bank TEXT,
                            status TEXT
                        )""")
# from constants import SQLITE3_PATH
# test = SqliteHelper(SQLITE3_PATH)
# test.create_table("""CREATE TABLE users(
#                             id INTEGER PRIMARY KEY AUTOINCREMENT,
#                             name TEXT NOT NULL,
#                             year INTEGER,
#                             admin INTEGER
#                         )""")
# test.create_table("""CREATE TABLE accountFb(
#                             uid TEXT PRIMARY KEY,
#                             name TEXT,
#                             password TEXT,
#                             code2fa TEXT,
#                             cookie TEXT,
#                             token TEXT,
#                             bank TEXT,
#                             status TEXT
#                         )""")
# test.edit("INSERT INTO users (name, admin) VALUES ('Baby', 0)")
# name = 'users'
# print(test.select("SELECT * FROM " + name)[0][1])
# test.edit("UPDATE users SET test_column = NULL WHERE name = 'Jack'")
# print(test.select("SELECT * FROM users"))
# test.edit("DELETE FROM users WHERE name = 'Baby'")
# test.edit("INSERT INTO users (name, year, admin) VALUES ('Tom', 1990, 0), ('Hoa', 1989, 0), "
#           "('Peter', 1995, 1), ('Lía', 1997, 0), ('Top', 1988, 0), ('Zack', 1980, 0), "
#           "('Lisa', 1990, 0), ('Rick', 1990, 0)")
# test.edit("ALTER TABLE users ADD test_column TEXT")
# from model.account import Account
#
# def dataToAccount(data):
#     account = Account(uid=data[0], password=data[1], code2fa=data[2], bank=data[3])
#     return account
#
# account_table_name = 'accountFb'
# # test.edit("DROP TABLE " + account_table_name)
# account1 = Account(uid='100054860317371', password='0708952952VN2020', code2fa="7SOEEZUFJBI33VFGOT4NWNO66Q2NAIYH")
# account2 = Account(uid='100054699734965', password='0708952952VN2020', code2fa="YMTWDEYMKY3HPWIZHGDTXRUZVJMPMCNC")
# account3 = Account(uid='100054951511660', password='0708952952VN2020', code2fa="UTULAO3GBZARRR2LSMGD3TRS2Y7RGEYH")
# test.edit("INSERT INTO " + account_table_name + " (uid, password, code2fa, bank) "
#                                         "VALUES ('" + account3.uid + "', '" + account3.password +
#                                         "', '" + account3.code2fa + "', '" + account3.bank + "')")
# print(test.select("SELECT * FROM " + account_table_name + " WHERE uid = " + account.uid)[0][3])
# test.edit("UPDATE " + account_table_name + " SET password = '" + account1.password +
#                                         "', code2fa = '" + account1.code2fa + "', bank = '" + account1.bank +
#                                         "' WHERE uid = '" + account1.uid + "'")
# list = test.select("SELECT * FROM " + account_table_name)
# liseAcc = []
# for data in list:
#     liseAcc.append(dataToAccount(data))
# print(liseAcc[1].password)
# test.edit("DELETE FROM " + account_table_name + " WHERE uid = " + account3.uid)
