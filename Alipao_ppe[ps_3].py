print('This program calculate average speed of a moving body')
distance=float(input('Distance: '))
time=float(input('Time: ',))
speed=int(distance)/int(time)
print('Speed=' ,speed, 'm/s')

print('This program calculates Acceleration')
fvelocity=float(input('fvelocity:'))
ivelocity=float(input('ivelocity:'))
time=float(input('time:'))
a=int(fvelocity-ivelocity)/int(time)
print('a=',a,'m/s')

print('This program Calculates Density of a Material')
mass=float(input('Mass: '))
volume=float(input('Volume: ',))
density=int(mass)/int(volume)
print('Density=' ,density, 'g/cm')

print('This program calculates Force')
m=float(input('Mass: '))
a=float(input('Accelrration: '))
f=int(m)*int(a)
print('Force=',f ,'N')

print("This program calculates the kinetic energy of a moving object")
m_string = input("Enter the object's mass in kilograms: ")
m = float(m_string)
v_string = input("Enter the object's speed in meters per second: ")
v = float(v_string)
 
e = 0.5 * m * v * v
print("The object has "+str(e)+" joules of energy.")