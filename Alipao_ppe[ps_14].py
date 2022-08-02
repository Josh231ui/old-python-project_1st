from operator import *

print('This program calculate average speed of a moving body')
distance=float(input('Distance: '))
time=float(input('Time: ',))
speed= truediv(distance,time)
print('Speed=' ,speed, 'm/s')

print('This program calculates Acceleration')
fvelocity=float(input('fvelocity:'))
ivelocity=float(input('ivelocity:'))
time=float(input('time:'))
a= sub(fvelocity, ivelocity)/int(time)
print('a=',a,'m/s')

print('This program Calculates Density of a Material')
mass=float(input('Mass: '))
volume=float(input('Volume: ',))
density= truediv(distance, time)
print('Density=' ,density, 'g/cm')

print('This program calculates Force')
m=float(input('Mass: '))
a=float(input('Accelrration: '))
f= mul(m, a)
print('Force=',f ,'N')

print("This program calculates the kinetic energy of a moving object")
m_string = input("Enter the object's mass in kilograms: ")
m = float(m_string)
v_string = input("Enter the object's speed in meters per second: ")
v = float(v_string)
 
e = mul(0.5,mul(m, mul(v, v)))
print("The object has "+str(e)+" joules of energy.")
print("\n")
tuple_result = (speed,a,density,f,e)
tuple_result_equivalent = ["speed","acceleration","density","force","kinetic_energy"]
for i in range(len(tuple_result)):
	print(f"{tuple_result_equivalent[i]} value is {tuple_result[i]}")
print("\n")
print(f"Here is the tuple: \n{tuple_result}")