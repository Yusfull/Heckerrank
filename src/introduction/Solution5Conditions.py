# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

N = int(raw_input().strip())
if not N % 2 and (N < 6 or N > 20):
    print 'Not',
print 'Weird'