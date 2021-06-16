class Data:

    def __init__(self, first_name, middle_name, last_name, nickname, title, company, address):
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.nickname = nickname
        self.title = title
        self.company = company
        self.address = address

class Contact:

    def __init__(self, home, mobile, work, fax, email, email2, email3, homepage, address2, phone2, notes):#, birthday, anniversary):
        self.home = home
        self.mobile = mobile
        self.work = work
        self.fax = fax
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.homepage = homepage
        #self.birthday = birthday
        #self.anniversary = anniversary
        self.address2 = address2
        self.phone2 = phone2
        self.notes = notes