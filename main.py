def joining_string_lists():
    string_list = []
    string_list.append("Calvin")
    string_list.append("Hobbes")
    string_list.append("Spaceman")
    string_list.append("Spiff")

    # Now just print the new string. Since we don't
    # have a handle to it, it is printed and discarded
    print(" ".join(string_list))

    # Alternatively, we assign it to a variable (handle),
    # so we can manipulate it further, add to it, print it, etc.
    new_string = " ".join(string_list)
    new_string = new_string.lower()
    new_string = new_string + " Reality continues to ruin my life"
    print(new_string)


def cap_join(l):
    new_l = []
    for s in l:
        new_l.append(s[0].upper() + s[1:])
    return ' '.join(new_l)


if __name__ == '__main__':
    print("Hello, world!")
    joining_string_lists()

    L = ["home", "sweet", "home"]
    print(cap_join(L))


