"""

Paste this in the console of the whatsapp group

document.querySelector(".x78zum5.x1cy8zhl.xisnujt.x1nxh6w3.xcgms0a.x16cd2qt > span").innerHTML.match(/\+\d{2}\s*\d\s*\d\s*\d\s*\d\s*\d\s*\d\s*\d\s*\d\s*\d\s*\d\s*/g).map(number => number.replace(/\s/g, '')).reduce((prev="", curr)=>`${prev}, ${curr}`);

then run this file and add phone numbers to the database and retrieve it.

"""


import sqlite3

con = sqlite3.connect("phoneNumbers.db")

cur = con.cursor()

def checkIfPhoneNumbersTableExists():
    cur.execute("SELECT name FROM sqlite_master")
    for i in cur.fetchall():
        if i[0] == 'PhoneNumbers':
            return True
    else:
        return False


def createPhoneNumbersTable():
    if not checkIfPhoneNumbersTableExists():
        cur.execute("CREATE TABLE PhoneNumbers(PhoneNumber)")


def savePhoneNumbers(phoneNumbersStr:str):
    phoneNumbersValues = [(i.strip(),) for i in phoneNumbersStr.replace("'", "", -1).split(',')]
    cur.executemany("INSERT INTO PhoneNumbers VALUES(?)", phoneNumbersValues)

    cur.execute("select * from PhoneNumbers")
    print(f"\n\x1b[92m{len(phoneNumbersValues)} \x1b[96mPhone numbers added.\nTotal phone numbers:", len(cur.fetchall()), f"\x1b[92m(+{len(phoneNumbersValues)})", "\x1b[0m")

    con.commit()


def display_PhoneNumbers():
    cur.execute("select * from PhoneNumbers")
    for i in cur.fetchall():
        print(i[0])

createPhoneNumbersTable()

while True:
    print("\n\n\x1b[93mEnter choice:\x1b[0m")
    print("\x1b[94m1. Add Phone Number")
    print("2. Show Phone Numbers\x1b[0m")
    choice = input()
    if choice == "1":
        savePhoneNumbers(input("\x1b[94mEnter the phone numbers string: \x1b[0m"))
    elif choice == "2":
        display_PhoneNumbers()