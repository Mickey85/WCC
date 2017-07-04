def vowelsCounter(word):
    vowels=['a','e','i','o','u']

    count=0;
    for char in word:
        if(char in vowels):
            count = count+1
            #print char

    return count

print vowelsCounter('apples') # Expected: 2
print vowelsCounter('aeiou') # Expected: 5
print vowelsCounter('why') # Expected: 0
print vowelsCounter('mississippi') # Expected: 4
