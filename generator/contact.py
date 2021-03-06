from model.contact import Contact
import random
import string
import os.path
import jsonpickle
import getopt
import sys


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_string(prefix, maxlen):
    symbols = string.ascii_letters
    return prefix + ":" + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_phone(prefix, maxlen):
    symbols = string.digits
    return prefix + ":" + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_email(prefix, maxlen):
    symbols = string.ascii_letters
    return prefix + ":" + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))]) + "@" \
           + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Contact(first_name=random_string("first_name", 10), middle_name=random_string("middle_name", 10),
                    last_name=random_string("last_name", 10), nickname=random_string("nickname", 10),
                    title=random_string("title", 10), company=random_string("company", 10),
                    address=random_string("address", 10), home=random_phone("home", 10), mobile=random_phone("mobile", 10),
                    work=random_phone("work", 10), fax=random_phone("fax", 10), email=random_email("email", 5),
                    email2=random_email("email2", 5), email3=random_email("email3", 5), homepage=random_string("homepage", 10),
                    address2=random_string("address2", 10), phone2=random_phone("phone2", 10), notes=random_string("notes", 10),
                    bday="9", bmonth="March",  byear="1990", aday="9", amonth="March", ayear="2090")
            for i in range(n)]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))