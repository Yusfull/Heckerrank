# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.


y = input()
def is_leap(y):
    leap = False
    if ( y%4 == 0 and y%100 != 0 ) or ( y%100 == 0 and y%400 == 0 ): leap = True
    
    # Write your logic here
    return leap
print is_leap(y)