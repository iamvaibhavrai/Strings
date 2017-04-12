def countSubStrings(string):
    characters = [0]*26
    result = 0
    for i in range(len(string)):
        characters[ord(string[i]) - ord('a')] += 1

    for i in range(26):
        result += ((characters[i]*(characters[i]+1))//2)

    return result

def main():
    string = input()
    result = countSubStrings(string)
    print(result)

if __name__ == '__main__':
    main()
