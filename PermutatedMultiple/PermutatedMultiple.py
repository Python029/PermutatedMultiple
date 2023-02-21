num = 125874
numbers = False
multiples = [0,0,0,0,0,0]
digits = []


while True:
    num+=1
    for i in range(0,len(multiples)):
        multiples[i] = num*(i+1)   
    for i in range(0,len(multiples)):        
        digits.clear()
        digits = [z for z in str(multiples[i])]
        comparison = [z for z in str(num)]
        comparison.sort()
        digits.sort()
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

print(f"The number that contains the same digits from 1x to 6x is: {multiples[0]}")
print(f"Numbers 1x through 6x: {multiples}")
