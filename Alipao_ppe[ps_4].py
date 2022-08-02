txt='Payslip'
x= txt.center(50,'=')
print(x)

txt='Employee Information'
e=txt.center(50,'=')
print(e)

name=input('Employee Name:')
time=float(input('Rendered Hours:'))
Rph=float(input('Rate per Hour:'))
G=int(input('Gross Salary:'))

txt='Deduction'
r=txt.center(50,'=')
print(r)

s=float(input('SSS:'))
p=float(input('PhilHealth:'))
l=float(input('Loans:'))
t=float(input('Tax:'))
total=int(s)-int(p)-int(l)-int(t)
print('Total Deduction:' ,total)

txt='Net Salary'
n=txt.center(50,'=')
print(n)

Php=int(time)+int(Rph)+int(G)-int(total)
print('Php:',Php)