def computepay(h, r):
    if h <= 40:
        pay = h * r
    else:
        regular_pay = 40 * r
        overtime_pay = (h - 40) * (r * 1.5)
        pay = regular_pay + overtime_pay
    return pay

hrs = input("Enter Hours: ")
rate = input("Enter Rate: ")

h_f = float(hrs)
r_f = float(rate)

p = computepay(h_f, r_f)
print("Pay", p)
