from collections import Counter

c1=Counter(debit_of_tally)
c2=Counter(credit_of_bank)
c3=Counter(debit_of_bank)
c4=Counter(credit_of_tally)
cob_dot=c2-c1
dob_cot=c3-c4
cot_dob=c4-c3
dot_cob=c1-c2

print('****** YOGESH SHAH ******')
print('credit of bank not found in debit of tally')
print (list(cob_dot.elements()))
print('debit of bank not found in credit of tally')
print (list(dob_cot.elements()))
print('credit of tally not found in debit of bank')
print (list(cot_dob.elements()))
print('debit of tally not found in credit of bank')
print (list(dot_cob.elements()))



