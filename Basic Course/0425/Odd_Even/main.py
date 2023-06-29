x=int(input('Enter an integer: '))
y=x%2
# "1.5" --> int로 casting 못 해요
# "1" --> int로 casting 가능

if y==0:
    print('The integer is an even number.')
else:
    print('The integer is an odd number.')

#failsafe 안전하게
