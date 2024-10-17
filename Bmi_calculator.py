def calc_bmi(weight,height):
    bmi=weight/(height**2)
    return bmi

def bmi_result(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"


def main():
    print("Welcome to BMI Calculator\n")
    weight=float(input("Enter the Weight in Kilogram: "))
    height=float(input("Enter the Height in Meter: "))
    
    bmi=calc_bmi(weight,height)
    result=bmi_result(bmi)

    print(f"print your Bmi score is :{bmi:.2f} ,The Result is :",result)
    
if __name__=="__main__":
    main()

