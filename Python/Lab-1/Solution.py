tuition = float(input("Enter Tuition Fee: "))
lab = float(input("Enter Lab Fee: "))
library = float(input("Enter Library Fee: "))
exam = float(input("Enter Exam Fee: "))
discount = float(input("Enter Discount Amount: "))

total = tuition + lab + library + exam

after_discount = total - discount

annual = after_discount * 2

monthly = annual / 12

print("\nTuition Fee:", tuition)
print("Lab Fee:", lab)
print("Library Fee:", library)
print("Exam Fee:", exam)
print("Total Fee:", total)
print("Discount:", discount)
print("Fee after Discount:", after_discount)
print("Annual Fee:", annual)
print("Monthly Installment:", round(monthly, 2))