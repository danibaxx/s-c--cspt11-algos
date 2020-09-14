'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    # TBC
    word = 'asdfthlaskdneTHdnaltlehstt'
    # base case -> reach end of string len(word) - 1
    if len(word) == 'th':
        # print(word)
        return 0
    # how many times does "th" occur within word
    else:
        return count_th(word()).title().capitalize().lower()
        
    # needs to call itself -> recursion
    # return the count of the occurences ** case matters **

print(count_th('th'))