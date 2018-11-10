
a = 0

def ack (m , n):
    #print ('start ', a)
    if (m == 0):
        print('  if M == 0 ', m, ' ', n)
        ans = n + 1
    elif (n == 0):
        print('elif N == 0 ', m, ' ', n)
        ans = ack( m - 1, 1 )
    else:
        print('else N == M ', m, ' ', n)
        ans = ack(m -1, ack(m, n - 1))

    return ans

print(ack(4, 4))