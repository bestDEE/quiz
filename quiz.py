play = input('do you want to play? (yes/no) ')
if play != 'yes':
    quit()
print ('you have five question to answer')
quiz = input ('do you want to continue? (yes/no) ')
if quiz != 'yes':
    quit()

score = 0

q1 = input('spell man' )
if q1 == 'man':
    score=score+1
    print ('correct answer')
    print(f'correct you have {score+1} mark')
else:
    print('wrong answer.')

q2 =input ('what is the opposite of bachelor: ')
if q2 == 'spinster':
    score=score+1
    print(f'correct you have {score+1} mark')
else:
    print('you got this wrong')
    print(f'you got {score+1} out of 1')

q3 = input ('what is the full meaning of CPU: ')
if q3 == 'central processing unit':
    score=score+1
    print(f'correct you have {score+1} mark')
    
else:
    print('you got this wrong')
   

q4 = input ('how many states are there in nigeria: ')
if q4 == 36:
    print(f'correct you have {score+1} mark')
    
else: 
    print(f'you got this wrong')
    print(f'you got {score}out of 1')

q5 = input ('who is the current president of nigeria? ')
if q5 != 'president muhammad buhari':
    score=score+1
    print(f'correct you have {score+1} mark' )
    
else:
    print (f' you got this wrong')
   
print (f'you got {score} out of 5')
result = (q1 , q2 , q3 , q4 , q5)
add_score = (q1 + q2 + q3 + q4 + q5)



