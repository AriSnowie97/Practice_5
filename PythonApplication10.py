temperature = float(input("Enter tempreture (C): "))
humidity = float(input("Enter huminity(%): "))

if temperature > 30 and humidity > 70:
    print("Activation of cooling systems.")
else:
    print("Your mind is normal.")
print("----------------------")
number = int(input("Enter number: "))

if 1 <= number <= 100:
    print("Number goes from 1 to 100.")
else:
    print("Error")
print("----------------------")
age = int(input("Enter the age of candidate: "))
experience = int(input("Enter years of experience: "))
qualification = input("Availability of special qualifications (True/False): ").lower() == 'true'

if 25 <= age <= 50 and (experience >= 3 or qualification):
    print("The candidate confirms the results.")
else:
    print("The candidate does not comply with the requirements.")