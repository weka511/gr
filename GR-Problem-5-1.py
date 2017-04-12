# Copyright (C) 2017 Greenweaves Software Pty Ltd
#
# This program generates the Penrose--Carter diagram
# for an eternally accelerating observer/particle

import math as m,matplotlib.pyplot as plt

# Create a generator that represents a range of
# floating point numbers
def drange(start, stop, step=0.1,inclusive=True):
     r = start
     while r < stop:
          yield r
          r += step
     if inclusive:
          yield stop

# Create a list of points representing a steadily
# accelerating particle, (t,x) whose cooordinates 
# are given by equation (7) in Lecture Notes
def create_steady_acceleration(a=1.5,s0=-2,s1=2,step=0.1):
     return [(m.sinh(a*s)/a,(m.cosh(a*s)-1)/a)
             for s in drange(s0,s1,step)]

# Convert (t,x) style coordinates for Minkowski space to 
# Coordinates suitable for a Penrose Carter diagram
def convert_to_penrose_carter(z):
     def pp(x):
          print (x)
          return x
     return [(a+b,a-b) for (a,b) in [(m.atan(t+x),m.atan(t-x)) for (t,x) in z]]

# Plot a list of points, assuming Minkowski coordinates
def minkowski_plot(z,figure=1,a=1.5,
                   title='Minkowski Diagram'):
     (t,x)=zip(*z)
     fig=plt.figure(figure)
     ax = fig.add_subplot(111)
     ax.set_aspect('equal')
     plt.rc('text', usetex=True)
     # We want a pair of diagonal lines to separate
     # spacelike and timelike - generate x coordinates
     # for this plot
     x_diagonal=[x-a for x in t]
     plt.plot(x,t,'r',
              x_diagonal,t,'b--',
              x_diagonal,t[::-1],'b--')
     plt.xlabel(r'$x$')
     plt.ylabel(r'$t$')
     plt.title(title)
     plt.savefig('images/GR-Problem-5-1-{0}.png'\
                 .format(figure))

# Plot a list of points, assuming
# Penrose-Carter coordinates     
def penrose_carter_plot(penrose_carter,gap=0.25,figure=1,
                        title='Penrose Carter Diagram'):
     # Function used to represent a light ray from one
     # boundary to another
     def light_ray():
          # Function used to restrict a list to 
          # being within boundafry
          def filter(zs):
               return [(t,x) for (t,x) in zs if abs(x+t)<m.pi] 
          t_last,x_last=penrose_carter[-1]
          return filter([(x+t_last-x_last,x) for x in drange(-2.5,2.5,0.1)])
     (t,x)=zip(*penrose_carter)
     # Generate data for boundary and axes
     boundary_minus=list(drange(-m.pi,0))
     boundary_plus=list(drange(0,m.pi))
     i0=list(drange(-m.pi,m.pi))
     zeroes=len(i0)*[0]
     (t_light,x_light)=zip(*light_ray())
     fig=plt.figure(figure)
     ax = fig.add_subplot(111)
     ax.set_aspect('equal')
     plt.rc('text', usetex=True)
     plt.plot(x,t,'r',
              boundary_minus,boundary_plus,'m--',
              boundary_plus,boundary_plus[::-1],'g--',
              boundary_minus,boundary_minus[::-1],'c--',
              boundary_plus,boundary_minus,'y--',
              i0,zeroes,'b',
              zeroes,i0,'b',
              x_light,t_light,'k:')
     # Label everything
     plt.text(m.pi/2+gap,m.pi/2+gap,r'$\cal{J}^+$')
     plt.text(-m.pi/2-gap,m.pi/2+gap,r'$\cal{J}^+$')
     plt.text(m.pi/2+gap,-m.pi/2-gap,r'$\cal{J}^-$')
     plt.text(-m.pi/2-gap,-m.pi/2-gap,r'$\cal{J}^-$')
     plt.text(m.pi+gap,0,r'$I^0$')
     plt.text(-m.pi-gap,0,r'$I^0$')
     plt.text(0,m.pi+gap,r'$I^+$')
     plt.text(0,-m.pi-gap,r'$I^-$')   
     plt.text(x_light[len(x_light)//2],
              t_light[len(t_light)//2],
              'Light Line',ha='right')
     plt.xlabel(r'$\xi$')
     plt.ylabel(r'$\psi$')
     plt.title(title)
     plt.savefig('images/GR-Problem-5-1-{0}.png'.format(figure))

if __name__=='__main__': 
     # We will do a Minkowski plot over a shorter range 
     # then the Penrose Carter, as otherwise scaling will
     # lose much of the detail from the plot
     
     a=1
     minkowski_plot(
          create_steady_acceleration(a),
          figure=1,
          title='Minkowski Diagram for acceleration={0}'
          .format(a) )
     pc = convert_to_penrose_carter(
               create_steady_acceleration(
                    a,s0=-20, s1=40))
     for p in pc:
          print (p)
     penrose_carter_plot(
          pc,
          figure=2,
          title='Penrose Carter Diagram for a={0}'
          .format(a) )
     
     plt.show()    