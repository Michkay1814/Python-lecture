# declariing the appropriate variables 

hourly_rate_member =2
hourly_rate_non_member =5

tax_rate_for_member = 0.1
tax_rate_for_non_member = 0.2

hourly_user_spent =int(input("Enter the hoursspent:"))

is_a_member =str(input("are you a member?:"))
if is_a_member.lower() =="yes":
    hourly_rate = hourly_rate_member
    tax_rate = tax_rate_for_member
    membership_status =" The user is a member"
    
else:
    hourly_rate =hourly_rate_non_member
    tax_rate =tax_rate_for_non_member
    membership_status ="The user is NOT a member"
    
    Total_amount = hourly_user_spent* hourly_rate
    tax_fee = Total_amount*tax_rate
    Total_amount += tax_fee
    
    print(membership_status, "stayed" ,hourly_user_spent ,  "hours for", hourly_rate, 
          "$/hour", "plus the", tax_rate, "the total amount is: the amount)