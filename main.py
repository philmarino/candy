
def dist(list):
    result = []

    #everyone gets at least 1
    for index in range(len(list)):
        result.append(1)
    
    #make sure the 'neighbor' rule is met
    needToContinue = True

    while needToContinue:
        needToContinue = False
        for index in range(len(list)):
            if index == 0:
                #ignore this since left neighbor is out of bounds
                pass
            else:
                if list[index] > list[index - 1] and result[index] <= result[index - 1]:
                    result[index] += 1
                    needToContinue = True #if you changed a number, you need to go back and do the process again

            if index == len(list) - 1:
                #ignore this since right neighbor is out of bounds
                pass
            else:
                if list[index] > list[index + 1] and result[index] <= result[index + 1]:
                    result[index] += 1
                    needToContinue = True #if you changed a number, you need to go back and do the process again

    #print(result)
    return sum(list) #total


#Example 1:
#Input: 
ratings = [1,0,2]
print(dist(ratings))
#Output: 5
#Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.

#Example 2:
#Input: 
ratings = [1,2,2]
print(dist(ratings))
#Output: 4
#Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
#The third child gets 1 candy because it satisfies the above two conditions.

