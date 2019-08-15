import random
# متن کاربر را بگیرد
def get_guess():
    return list(input(" enter a simple number \n"))

# یک عدد تصادفی درست کند
def gen_code():
    digits = [ str(num) for num in range(0,10) ]
    # print (digits) # برای دیباگ
    random.shuffle(digits)
    return digits[:3]

# سرنخ درست کند
def gen_clues(code,guess):
    if code ==guess :
        print('well done yo won')
        return "CODE CRACKED!"
    clues = []
    for idx,dig in enumerate(guess):
        if dig == code[idx]:
            print('match') # برای دیباگ
            clues.append('match')
        elif dig in code:
            clues.append('close')
    if clues == []:
        return ['NOPE']
    else:
        return clues


# print header
def header():
    print('-----------------------------------------')
    print('WELCOME ')
    print('crack the code ')
    print('RULES : 1 - no digit is repeted twice in number \n\
        2 - and code is three digits')
    print('-----------------------------------------')

# و یک منطق اجرای بازی داشته باشد
def main():
    header()
    secret_code = gen_code()
    clues_report = [] 
    while clues_report != "CODE CRACKED!" :
        guess = get_guess()
        clues_report = gen_clues(secret_code,guess)
        print('here is ur resault')
        for clue in clues_report:
            print (clue)
# print(get_guess() )  # برای دیباگ
# print( type(get_guess()) ) # برای دیباگ
# print(gen_code()) # برای دیباگ
if __name__ == "__main__":
    main()