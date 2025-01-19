
import math
div = 2;
largest_prime = 1;
#num = 13195;
num = 600851475143;
for div in range(3, int(math.sqrt(num)) + 1, 2):
    if(num % div == 0):
        
        #print(q)
        for i in range(2,div):
            if(div%i) == 0:
                #print(div,"is not a prime number")
                break
        else:
            #print(div,"is a prime number")
 
            if(div>largest_prime):
                largest_prime = div
print(largest_prime,"is largest prime factor")
                

#print (q)


    