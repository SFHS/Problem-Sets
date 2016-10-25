import time

prime_index = int(input('Which prime do you need? '))
first_prime = 2 # seed the search with the first prime - the rest will be computed

primes_list = [];
primes_list.append(first_prime); # start the list with the first prime
i=first_prime+1

t_start = time.clock()

while(len(primes_list)<prime_index): # test all integers until desired prime found
    is_prime = 1  # consider i to be prime unless proven otherwise
    for p in primes_list: # try and divide i by all the primes found so far
        if p*p>i:
            break # no point testing with primes that are too large
        if (i % p) == 0: # if a divider is found, then i is not prime
            is_prime=0
            break # we know it's not a prime, so stop trying and move on to the next n.
    if is_prime:
        primes_list.append(i) # append i to the list of primes
    i=i+1

## the while statement is over - print the last item on the list:
## that number is the desired prime
t_end= time.clock()
total_time = round(t_end-t_start,6)
print('The ', prime_index, 'th prime is ', primes_list[prime_index-1] ,' (time=', total_time, ' s)' )

        
        
