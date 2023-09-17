def isPalindrome(s):
    #start 
    i = 0
    # end
    j = len(s) - 1
    # CIVIC
    while i < j:
        if s[i]==s[j]:
            i += 1
            j -=1

        else:
            return False
    return True

print(isPalindrome("civic"))


def twoSum(arr, sum):
    arr.sort()
    i = 0
    j = len(arr)-1
    outputs = []
    while i<j:
        if arr[i] + arr[j]==sum:
            outputs.append([arr[i],arr[j]])
            
        if arr[i] + arr[j]<sum:
            i+=1
        else:
            j-=1
        
    return outputs
        
        
print(twoSum([1,2,3,5,8,9,12,13,16], 10))        
            