import re


def find_re():
    full_str = ('k5EVTJOemc1TU[TVRJek5EVTJOemc1TUFNVEl6TkRVMk56ZzVNQU1USXpORFUyTnpnNU1B]VMk56ZzVNQ]U1USXpORFUyTnpnNU1B'
                ']pORFUyTnpnNU1B]')
    pattern = r"\[\w*\]"
    res = re.search(pattern, full_str)
    print()

    if res:
        print("Подстрока найдена:", res.group()[1:-1:])
        # print("Подстрока найдена: TVRJek5EVTJOemc1TUFNVEl6TkRVMk56ZzVNQU1USXpORFUyTnpnNU1B")
    else:
        print("Подстрока не найдена")


if __name__ == "__main__":
    find_re()
