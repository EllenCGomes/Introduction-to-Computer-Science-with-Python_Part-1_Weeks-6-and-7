def n_prime(n):   
    x = 2
    div = 2
    count = 0
    total = 0

    while n >= 2 and x <= n:
        while div <= n:
            x % div
            if x % div == 0:
                count = count + 1
            div = div + 1    
        if count == 1:
            total = total + 1
        x = x + 1
        div = 2
        count = 0
    return (total)

