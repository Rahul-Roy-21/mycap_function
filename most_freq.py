def most_frequent(s):
    freq = {}
    
    for ch in s.lower():
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1
    
    most_frequent = list(freq.items())
    most_frequent.sort(key=lambda x:x[1], reverse=True)
    return dict(most_frequent)

if __name__ == '__main__':
    s = input("Please Enter a String: ")
    mf = most_frequent(s)

    for key,value in mf.items():
        if value < 10:
            print('{} = 0{}'.format(key, value))
        else:
            print('{} = {}'.format(key, value))


