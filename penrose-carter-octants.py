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
            
def quad(name,xi_step,upsilon_step):
    print (name)
    for xi in frange(0,5,xi_step):
        for upsilon in frange(0,5,upsilon_step):
            t,x=pc(xi,upsilon)
            print ('({0:6.3f},{1:6.3f})->({2:6.3f},{3:6.3f})'.format(xi,upsilon,t,x))
        
if __name__=='__main__':
    quad("1st Quadrant",math.pi/20,math.pi/20)
    quad("2nd Quadrant",-math.pi/20,math.pi/20)
    quad("3rd Quadrant",-math.pi/20,-math.pi/20)
    quad("4th Quadrant",math.pi/20,-math.pi/20)