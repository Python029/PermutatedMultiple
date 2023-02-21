num = 125874
numbers = False
multiples = [0,0,0,0,0,0]
digits = []

#Find the next number after 125874 where 1x - 6x all contain the same digits
while True:  
    #Add the multiples of num to a list
    for i in range(0,len(multiples)):
        multiples[i] = num*(i+1)   
    for i in range(0,len(multiples)):        
        digits.clear()
        #Seperate individual digits of num and its multiples
        digits = [z for z in str(multiples[i])]
        comparison = [z for z in str(num)]
        #Sort digits for easier comparison
        comparison.sort()
        digits.sort()
        #Compare digits and break loop if conditions are met
        for x in range(0,len(comparison)):           
            if(comparison[x]==digits[x]):
                numbers=True
            else:
                numbers=False
                break
        if(numbers==False):
            break
    if(numbers):
        break      
    num+=1

print(f"The number that contains the same digits from 1x to 6x is: {multiples[0]}")
print(f"Numbers 1x through 6x: {multiples}")
