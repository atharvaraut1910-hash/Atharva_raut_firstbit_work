#Q.2 write a program to calculate simple interest based on principal,rate and time (SI=P*R*T/100)

P = float(input("Enter the principal amount(P):"))
T = float(input("Enter the time of year(T):"))
R = float(input("Enter the rate of interest(R):"))

CI = P *(1 + R/100) **T - P
print(F'the compound interst is:{CI}')
