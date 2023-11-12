enter_letter = input()
capital_lis = ['A', 'B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
count = 0
lengh = len(enter_letter)
for i in enter_letter:
    for j in capital_lis:
        if(i == j):
            count = count+1
if( count >=((lengh // 2)+1)):
    print(enter_letter.upper())
else:
    print(enter_letter.lower())

