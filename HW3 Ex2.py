def user_info(**kwargs):
     return ' '.join(kwargs.values())
print(user_info(name = input("Please, enter you name: "), surname = input("Please, enter you surname: "),
                year_of_birth = input("Please, enter your year of birth: "), city = input("Please, enter you city: "),
                e_mail = input("Please, enter you e-mail: "),
                phone_number = input("Please, enter you mobile phone number: ")))
