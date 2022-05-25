
def find_anagrams():
    word1 = input('Enter First Word >>>:')
    word2 = input('Enter Second Word >>>:')
    
    # This eliminates the chance of Case confliction.
    a = word1.lower()
    b = word2.lower()

    print(a,b)

    x = sorted(a)
    y = sorted(b)
    
    if x == y:
        print('True')
        return True
    else:
        print('False')
        return False
 
find_anagrams()

