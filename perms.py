# http://code.activestate.com/recipes/578227-generate-the-parity-or-sign-of-a-permutation/
def perm_parity(lst):
    '''\
    Given a permutation of the digits 0..N in order as a list, 
    returns its parity (or sign): +1 for even parity; -1 for odd.
    '''
    parity = 1
    for i in range(0,len(lst)-1):
        if lst[i] != i:
            parity *= -1
            mn = min(range(i,len(lst)), key=lst.__getitem__)
            lst[i],lst[mn] = lst[mn],lst[i]
    return parity    

def duplicate(indices):
    if len(indices)<2:
        return False
    if indices[0] in indices[1:]:
        return True
    return duplicate(indices[1:])

def epsilon(indices):
    return 0 if duplicate(indices) else perm_parity(indices)

def product(mu,nu,gamma,sigma):
    return sum( epsilon([mu,nu,alpha,beta]) * epsilon([alpha,beta,gamma,sigma]) for alpha in range(4) for beta in range(4) )
   

if __name__ == '__main__':
    count=0
    for mu in range(4):
        for nu in range(4):
            for gamma in range(4):
                for sigma in range(4):
                    p= product(mu,nu,gamma,sigma)
                    if p!=0:
                        print (mu, nu, gamma,sigma,p)
                        count +=1
    print (count)