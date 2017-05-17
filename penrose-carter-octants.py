import math

def pc(xi,upsilon):
    t_plus_x = math.tan((upsilon+xi)/2)
    t_minus_x = math.tan((upsilon-xi)/2)
    return ((t_plus_x+t_minus_x)/2,(t_plus_x-t_minus_x)/2)

def frange(start,nsteps,stepsize, limit=math.pi/4):
    for i in range(nsteps):
        x=start+i*stepsize
        if abs(x)<limit:
            yield(x)
            
def octant(index,xi_step,upsilon_step,xi_may_dominate):
    dominance='Xi Dominates' if xi_may_dominate else 'Upsilon dominates'
    print ('Octant {0}: {1}'.format(index, dominance))
    for xi in frange(0,5,xi_step):
        for upsilon in frange(0,5,upsilon_step):
            xi_dominates = abs(xi)>abs(upsilon)
            if (xi_may_dominate and xi_dominates) or ((not xi_may_dominate) and (not xi_dominates)):           
                t,x=pc(xi,upsilon)
                print ('({0:6.3f},{1:6.3f})->({2:6.3f},{3:6.3f})'.format(xi,upsilon,t,x))
        
if __name__=='__main__':
    octant('I',math.pi/20,math.pi/20,True)
    octant('II',math.pi/20,math.pi/20,False)
    octant('III',-math.pi/20,math.pi/20,False)
    octant('IV',-math.pi/20,math.pi/20,True)
    octant('V',-math.pi/20,-math.pi/20,True)
    octant('VI',-math.pi/20,-math.pi/20,False)
    octant('VII',math.pi/20,-math.pi/20,False)
    octant('VIII',math.pi/20,-math.pi/20,True)