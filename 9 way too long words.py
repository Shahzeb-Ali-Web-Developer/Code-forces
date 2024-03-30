for i in range(int(input())):
    word = str(input())
    if len(word) <= 10:
        print(word)
    elif len(word) > 10:
        length = len(word)
        count = length - 2

        print(word[0] + str(count) + word[length - 1])