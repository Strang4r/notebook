def info(name, lname, birth, city, mail, phone):
    print(f'hi, {name} {lname} you are {birth}, from {city}, your email {mail}, and ur phone number {phone}')

info(
    name=input("ur name?"),
    lname=input("ur last name?"),
    birth=input("ur birth date?"),
    city=input("where are you from?"),
    mail=input("ur email?"),
    phone=input("ur phone number?"),
)