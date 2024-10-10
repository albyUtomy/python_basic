wordlists = (
    "unable", "unacceptable", "unaware", "unfortunate", "unusual", 
    "uncertain", "unconventional", "understand", "unseen", "unfold", 
    "unite", "unify", "unknown", "unplug", "unlocked", 
    "unnecessary", "unbreakable", "unrelated", "unintended", "unresolved", 
    "unwanted", "unusual", "unwavering", "unharmed", "unemployed", 
    "unfriendly", "uninterrupted", "unlimited", "unambiguous", "unforgettable", 
    "uncomplicated", "unbounded", "uncontrollable", "uncommon", "unclear", 
    "uncovered", "undeniable", "underestimate", "undergo", "underlying", 
    "understandable", "unexplained", "unjust", "unqualified", "unrepentant", 
    "unresponsive", "unraveled", "unsatisfactory", "unsung", "unspoiled", 
    "unstable", "unthreatening", "unveiled", "unwanted", "unusual", 
    "unvisited", "unwilling", "unwritten", "unmanned", "unruly", 
    "unaccountable", "unbroken", "uncaring", "unfeeling", "uninhabited", 
    "unorthodox", "unparalleled", "unrelenting", "unrestrained", "unscathed", 
    "unscripted", "unsupervised", "untraceable", "untrustworthy", "unusual", 
    "unyielding", "unfit", "unfrequented", "unmet", "unmistakable", 
    "unobserved", "unpromising", "unremitting", "unreplicable", "unsecured", 
    "unshakeable", "unsurpassed", "untempered", "untouched", "unworkable", 
    "unworthy", "uncooperative", "undisputed", "uninhabitable", "unhinged", 
    "unimaginable", "unwavering", "ungrateful", "unjustified", "uncluttered"
)

def horizontal_search(wordlists):
    counter = 1



    if (len(wordlists) == 0):
        print("Empty")


    longest_prefix = wordlists[0]

    for i in range(1,len(wordlists)):
        while counter <= len(longest_prefix) and counter <= len(wordlists[i]):
            if longest_prefix[0:counter] == wordlists[i][0:counter]:
                counter +=1
            else:
                break

        longest_prefix = longest_prefix[0:counter-1]
        counter = 1

    if longest_prefix:
        print("Longest common prefix:", longest_prefix)
    else:
        print("No common prefix found")


# method 2
# divide and conquer
def divide_and_conquer(words):
    if not words:
        return ""
    if len(words)==1:
        return words[0]
    
    mid = len(words)//2
    left_prefix = divide_and_conquer(words[0:mid])
    right_prefix = divide_and_conquer(words[mid:])

    return common_prefix(right_prefix,left_prefix)


def common_prefix(left, right):
    min_length = min(len(left), len(right))
    for i in range(min_length):
        if left[i] != right[i]:

            return left[:i]
    return left[:min_length]
    


# method 3
def sort_and_find(words):
    sorted_tuple = sorted(words)
    # print(sorted_tuple)
    c_prefix = ""

    for i in range(0,len(words[-1])):
        if words[0][0:i] == words[-1][0:i]:
            c_prefix = words[0][0:i]
    print("Sort : ",c_prefix)


horizontal_search(wordlists)
print("Using Divide and Conquer : ",divide_and_conquer(wordlists))
sort_and_find(wordlists)