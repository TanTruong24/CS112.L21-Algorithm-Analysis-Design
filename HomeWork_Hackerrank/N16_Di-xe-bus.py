
def save_crush(s, l):
    sum = 0
    m = 0
    w = 0
    if (l < 4):
        return l * 2
    for i in range(l):
        if (s[i + 3] < s[i] + 7):
            


if __name__ == '__main__':
    s = list(map(int, input().split()))
    l = len(s)
    save_crush(s, l)