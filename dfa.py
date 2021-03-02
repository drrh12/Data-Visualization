print("Check the alphabetic of {0,1} of five consecutive strings that contains at least two zeros: \n")
print("Insert the string to be checked below: \n")

alphabet_to_be_checked = str(input())


def check_automata(string):
    pos = string[:5]
    i = 5
    count0, count1 = 0, 0
    while i < len(string):
        if len(pos) == 5:
            first_pos = pos[0]
            if first_pos == "0":
                count0 -= 1
            else:
                count1 -= 1
            pos = pos[1:]
        pos += string[i]
        if pos[-1] == "0":
            count0 += 1
        else:
            count1 += 1
        if count0 < 2:
            print("Accepted -> checking next 5...")
        i += 1
    if pos.count('0') >= 2:
        print("Automata accepted")
    else:
        print("Automata rejected")


check_automata(alphabet_to_be_checked)