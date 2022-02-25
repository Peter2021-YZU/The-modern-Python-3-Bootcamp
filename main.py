# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def solve(s):
    a = s.split()
    a = [b[0].upper()+b[1:] for b in a]
    return (" ".join(a))

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(solve('PyCharm is the best'))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
