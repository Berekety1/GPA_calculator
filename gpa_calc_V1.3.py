# banner
import os
import sys
import time


black = "\033[0;30m"
red = "\033[0;31m"
green = "\033[0;32m"
yellow = "\033[0;33m"
blue = "\033[0;34m"
purple = "\033[0;35m"
cyan = "\033[0;36m"
white = "\033[0;37m"
# Bold
bblack = "\033[1;30m"
bred = "\033[1;31m"
bgreen = "\033[1;32m"
byellow = "\033[1;33m"
bblue = "\033[1;34m"
bpurple = "\033[1;35m"
bcyan = "\033[1;36m"
bwhite = "\033[1;37m"

bold = '\033[1m'

logo = '''
''' + green + '''  ____ ____   _        ____   ___ _____ 
''' + red + ''' / ___|  _ \ / \      | __ ) / _ \_   _|
''' + cyan + '''| |  _| |_) / _ \     |  _ \| | | || |  
''' + yellow + '''| |_| |  __/ ___ \    | |_) | |_| || |  
''' + blue + ''' \____|_| /_/   \_\___|____/ \___/ |_| version [1.2] 
''' + purple + '''                 |_____|  Developed by [Bereket]                
''' + green + '''
'''



def slowprintt(n):
    for word in n + '\n':
        sys.stdout.write(word)
        sys.stdout.flush()
        time.sleep(0.01)

slowprintt(logo)

def slowprint(n):
    for word in n + '\n':
        sys.stdout.write(word)
        sys.stdout.flush()
        time.sleep(0.04)




intro = '''
==============================================
HELLO I AM 🤖GPA Calculator BOT🤖, THIS IS A DEMO
TYPE SO IF YOU FIND ANY KIND OF BUGS OR HAVE AN IDEA 
PLEASE CONTACT US AT Bereketyimolal8991@gmail.com. 
==============================================
'''
slowprint(intro)
time.sleep(0.4)

def one_calc():
    slowprint('\n'f'{red}One semester GPA')
    print('==============================================')
    name = input(f'{green}What is your name: ')
    time.sleep(0.2)
    print('==============================================')
    grade = input("\n"f'{green}What is your grade: ')
    time.sleep(0.2)
    print('==============================================')

    total_mark = 0
    total_credit = 0
    main_subject = int(input("\n"f'{yellow}Enter the number of main subjects for this semester: '))
    time.sleep(0.2)
    print('==============================================')
    total_value = 0
    main_grade = ""
    for X in range(0, main_subject):
        mark = float(input("\n"f'{red}Enter the marks  of the main subject: '))
        time.sleep(0.2)
        print('==============================================')
        if mark >= 94.5:
            gpa_value = 4.3
            main_grade = 2.15
        elif 89.5 <= mark < 94.5:
            gpa_value = 4
            main_grade = 2
        elif 84.5 <= mark < 89.5:
            gpa_value = 3.7
            main_grade = 1.85
        elif 74.5 <= mark < 84.5:
            gpa_value = 3.3
            main_grade = 1.65
        elif 70.5 <= mark < 74.5:
            gpa_value = 3
            main_grade = 1.5
        elif 65.5 <= mark < 70.5:
            gpa_value = 2.7
            main_grade = 1.35
        elif 59.5 <= mark < 65.5:
            gpa_value = 2.3
            main_grade = 1.15
        elif 49.5 <= mark < 59.5:
            gpa_value = 2
            main_grade = 1
        else:
            gpa_value = 1
            main_grade = 0.5
        total_value += main_grade

    elective_subject = int(input("\n"f'{yellow}Enter the number of elective subjects for this semester: '))
    time.sleep(0.2)
    print('==============================================')
    total2 = 0
    for Y in range(0, elective_subject):
        elem1 = int(input("\n"f'{red}Enter the marks of the elective subject: '))
        time.sleep(0.2)
        print('==============================================')
        if elem1 >= 94.5:
            real_grade1 = 4.3
            main_grade1 = 1.075
        elif 89.5 <= elem1 < 94.5:
            real_grade1 = 4
            main_grade1 = 1
        elif 84.5 <= elem1 < 89.5:
            real_grade1 = 3.7
            main_grade1 = 0.925
        elif 74.5 <= elem1 < 84.5:
            real_grade1 = 3.3
            main_grade1 = 0.825
        elif 70.5 <= elem1 < 74.5:
            real_grade1 = 3
            main_grade1 = 0.75
        elif 65.5 <= elem1 < 70.5:
            real_grade1 = 2.7
            main_grade1 = 0.675
        elif 59.5 <= elem1 < 65.5:
            real_grade1 = 2.3
            main_grade1 = 0.575
        elif 49.5 <= elem1 < 59.5:
            real_grade1 = 2
            main_grade1 = 0.5
        else:
            real_grade1 = 1
            main_grade1 = 0.25
        total2 += main_grade1
        # calculating one semester gpa
    total = total2 + total_value
    hour1 = 0.5 * main_subject
    hour2 = 0.25 * elective_subject
    credit_hour = hour1 + hour2
    final_total = total / credit_hour
    total_mark += total
    total_credit += credit_hour
    D = f'{green}your total point is {total_mark}'
    E = f'{green}your total credit hour is {total_credit}'


    print("\n""\n""\n""\n"f'{blue}==============================================')
    k = f'{blue}{bold}Name: {name}'
    slowprint(k)
    time.sleep(0.2)
    print('==============================================')
    j = f'{blue}{bold}Grade: {grade}'
    slowprint(j)
    time.sleep(0.2)
    print('==============================================')
    h = f'{blue}{bold}Your GPA is: {final_total}'
    slowprint(h)
    time.sleep(0.2)
    print('==============================================')
    g = input("\n"f'{yellow}Want to see your details(yes/no): ')
    time.sleep(0.2)
    print('==============================================')
    if g.lower() == "yes":
       slowprint(D)
       time.sleep(0.2)
       print('==============================================')
       slowprint(E)
       time.sleep(0.2)
       print('==============================================')
       hour = int(total_credit * 6)
       total_hour = int(hour * 20)
       total_day = int(total_hour/24)
       total_day_rem = total_hour % 24
       slowprint(f'Your total learning hour for one week is {hour} hours''\n')
       slowprint(f'which means you learned around {total_hour} hours or {total_day} consecutive days and {total_day_rem} hours  in one semester')
    elif g.lower() == "no":
       slowprint("\n"'Fine')
       print('==============================================')
    else:
       slowprint("\n""Invalid Input")
       print('==============================================')

    f = input("\n"f'{green}Want to see your rank(yes/no): ')
    time.sleep(0.5)
    if f.lower() == "yes":
       if final_total >= 4.2:
          slowprint("\n"f'{cyan}"Wonderful you are on the top tier, \n \n{bold}TAKE THIS 👑')
       elif 4 <= final_total < 4.2:
          slowprint("\n"f'{cyan}Great job you are on the second tier, \n \nyou deserve an applause 👏')
       elif 3.6 <= final_total < 4:
          slowprint("\n"f'{cyan}Good job you are on the third tier, \n \nyou deserve it take this ✋')
       elif 3.2 <= final_total < 3.6:
          slowprint("\n"f'{cyan}Good grade but it can be better, \n \ni know you can do better 😕')
       elif 2.9 <= final_total < 3.2:
          slowprint("\n"f'{cyan}Good job but you can get better, \n \nyou have got to try hard 😒')
       elif 2.5 <= final_total < 2.9:
          slowprint("\n"f'{cyan}Probation level you got to work hard, \n \nyo you better study  you are in the dead zone 😟')
       else:
          slowprint("\n"f'{cyan}Probation level you got to study hard, \n \n😥😥😥😥😥😥😥😥😥😥😥😥😥')
    elif f.lower() == "no":
       slowprint("\n"'OK')
    else:
       slowprint("\n"'Invalid Input')
    ask = input('do you want to calculate again? Yes/no: ')
    if ask.lower == 'yes' or 'y':
      main()
    elif ask.lower == 'no' or 'n':
      print('Good Bye')
    else:
      print ('invalid input' )
      







def cum_calc():
    slowprint('\n'f'{red}Cumulative GPA')
    print('==============================================')
    name = input(f'{green}What is your name: ')
    time.sleep(0.2)
    print('==============================================')
    grade = input("\n"f'{green}What is your grade: ')
    time.sleep(0.2)
    print('==============================================')

    total_mark = 0
    total_credit = 0
    
    x = int(input("\n"f'{blue}How many semester do you want to calculate: '))
    time.sleep(0.2)
    while x == 1:
        print("\n""\n"f'{red}''''if you want to calculate only for one semester, 
choose the calculate for one semester option from the home page.
        ''')
        x = int(input("\n"f'{blue}How many semester do you want to calculate: '))
    print('==============================================')
    
    for i in range(0, x):
       main_subject = int(input("\n"f'{yellow}Enter the number of main subjects for this semester: '))
    
    
       
       time.sleep(0.2)
       print('==============================================')
       total_value = 0
       main_grade = ""
       cum_A = 0
       for X in range(0, main_subject):
          mark = float(input("\n"f'{red}Enter the marks  of the main subject: '))
          time.sleep(0.2)
          print('==============================================')
          if mark >= 94.5:
            gpa_value = 4.3
            main_grade = 2.15
          elif 89.5 <= mark < 94.5:
            gpa_value = 4
            main_grade = 2
          elif 84.5 <= mark < 89.5:
            gpa_value = 3.7
            main_grade = 1.85
          elif 74.5 <= mark < 84.5:
            gpa_value = 3.3
            main_grade = 1.65
          elif 70.5 <= mark < 74.5:
            gpa_value = 3
            main_grade = 1.5
          elif 65.5 <= mark < 70.5:
            gpa_value = 2.7
            main_grade = 1.35
          elif 59.5 <= mark < 65.5:
            gpa_value = 2.3
            main_grade = 1.15
          elif 49.5 <= mark < 59.5:
            gpa_value = 2
            main_grade = 1
          else:
            gpa_value = 1
            main_grade = 0.5
          total_value += main_grade

       elective_subject = int(input("\n"f'{yellow}Enter the number of elective subjects for this semester: '))
       time.sleep(0.2)
       print('==============================================')
       total2 = 0
       for Y in range(0, elective_subject):
          elem1 = int(input("\n"f'{red}Enter the marks of the elective subject: '))
          time.sleep(0.2)
          print('==============================================')
          if elem1 >= 94.5:
            real_grade1 = 4.3
            main_grade1 = 1.075
          elif 89.5 <= elem1 < 94.5:
            real_grade1 = 4
            main_grade1 = 1
          elif 84.5 <= elem1 < 89.5:
            real_grade1 = 3.7
            main_grade1 = 0.925
          elif 74.5 <= elem1 < 84.5:
            real_grade1 = 3.3
            main_grade1 = 0.825
          elif 70.5 <= elem1 < 74.5:
            real_grade1 = 3
            main_grade1 = 0.75
          elif 65.5 <= elem1 < 70.5:
            real_grade1 = 2.7
            main_grade1 = 0.675
          elif 59.5 <= elem1 < 65.5:
            real_grade1 = 2.3
            main_grade1 = 0.575
          elif 49.5 <= elem1 < 59.5:
            real_grade1 = 2
            main_grade1 = 0.5
          else:
            real_grade1 = 1
            main_grade1 = 0.25
          total2 += main_grade1
       total = total2 + total_value
       hour1 = 0.5 * main_subject
       hour2 = 0.25 * elective_subject
       hour = hour1 + hour2
       total_mark += total
       total_credit += hour 
       final_total = total / hour
       C = "\n"f'{purple}{bold}Your GPA for this semester is : {final_total}'
       slowprint(C)
       print('==============================================')  
    final_cum_gpa = total_mark / total_credit
    D = "\n"f'{cyan}{bold}Your total point is : {total_mark}'
    E = "\n"f'{cyan}{bold}Your total credit hour is : {total_credit}'
    Z = "\n"f'{blue}{bold}your cumulative GPA is : {final_cum_gpa} '

    print("\n""\n""\n""\n""\n"f'{red}==============================================')
    l = f'{red}{bold}Name: {name.capitalize()}'
    slowprint(l)
    time.sleep(0.2)
    print('==============================================')
    o = "\n"f'{red}{bold}Grade: {grade}'
    slowprint(o)
    time.sleep(0.2)
    print('==============================================')
    slowprint(Z)
    time.sleep(0.2)
    print('==============================================')
    
    g = input("\n"f'{yellow}Want to see your details(yes/no): ') 
    time.sleep(0.2)
    print('==============================================')
    if g.lower() == "yes":
       slowprint(D)
       time.sleep(0.2)
       print('==============================================')
       slowprint(E)
       time.sleep(0.2)
       print('==============================================')
       hour = int(total_credit * 6)
       total_hour = int(hour * 20)
       total_day = int(total_hour/24)
       total_day_rem = total_hour % 24
       slowprint(f'Your total learning hour for one week is {hour} hours''\n')
       slowprint(f'which means you learned around {total_hour} hours or {total_day} consecutive days and {total_day_rem} hours  in {x} semester')
    elif g.lower() == "no":
       slowprint("\n"'Fine')
       print('==============================================')
    else:
       slowprint("\n""Invalid Input")
       print('==============================================')

    f = input("\n"f'{green}Want to see your rank(yes/no): ')
    time.sleep(0.5)
    if f.lower() == "yes":
       if final_cum_gpa >= 4.2:
          slowprint("\n"f'{cyan}"Wonderful you are on the top tier, \n \n{bold}TAKE THIS 👑')
       elif 4 <= final_cum_gpa < 4.2:
          slowprint("\n"f'{cyan}Great job you are on the second tier, \n \nyou deserve an applause 👏')
       elif 3.6 <= final_cum_gpa < 4:
          slowprint("\n"f'{cyan}Good job you are on the third tier, \n \nyou deserve it take this ✋')
       elif 3.2 <= final_cum_gpa < 3.6:
          slowprint("\n"f'{cyan}Good job you are on the third tier, \n \nyou deserve it take this ✋')
       elif  2.9 <= final_cum_gpa < 3.2:
          slowprint("\n"f'{cyan}Good job but you can get better, \n \nyou have got to try hard 😒')
       elif 2.5 <= final_cum_gpa < 2.9:
          slowprint("\n"f'{cyan}Probation level you got to work hard, \n \nyo you better study  you are in the dead zone 😟')
       else:
          slowprint("\n"f'{cyan}Probation level you got to study hard, \n \n😥😥😥😥😥😥😥😥😥😥😥😥😥')
    elif f.lower() == "no":
       slowprint("\n"'OK')
    else:
       slowprint("\n"'Invalid Input')

    ask = input('do you want to calculate again? Yes/no: ')
    if ask.lower == 'yes' or 'y':
      main()
    elif ask.lower == 'no' or 'n':
      print('Good Bye')
    else:
      print ('invalid input' )







        

def about():
    print('''
+------------------------------------------------+
|                                                |
|       1.About the program                      |
|       2.About the developer                    |
|       3.Contact the developer                  |
|       4.Back to home                           |
+------------------------------------------------+
''')
    select = int(input(f'{yellow}Enter selection: '))
    if select == 1:
        print(f'{red}''''
=================================================
HELLO I AM 🤖GPA Calculator BOT🤖, I CAN CALCULATE
YOUR ONE SEMESTER GPA ALSO YOUR CUMULATIVE GPA, YOU
JUST TELL ME YOUR MARKS.
=================================================''')
        time.sleep(4)
        return about()
    elif select == 2:
        print(f'{blue}''''
=================================================
GLAD TO KNOW THAT YOU ARE CURIOUS ABOUT ME.
MY NAME IS BEREKET. WELL THAT'S EVERYTHING YOU NEED
TO KNOW ABOUT ME 
=================================================''')
        time.sleep(4)
        return about()
    elif select == 3:
        print(f'{cyan}''''
=================================================
HI IF YOU FIND ANY BUGS, ISSUES OR HAVE AN IDEA
OR WANT TO COLLABORATE CONTACT ME AT
TELEGRAM - @No_thing_is_here_bro
GMAIL - Bereketyimolal8991@gmail.com 
=================================================''')
        time.sleep(4)
        return about()
    elif select == 4:
      return main()    
    else:
        print(f'{green}+------------------------------------+')
        print(f'{yellow}|        Incorrect selection         |')
        print(f'{red}+------------------------------------+')
        time.sleep(1)
        return about()





def how_to():
   print(f'{cyan}''''
=================================================
            HOW TO CALCULATE
IF YOU WANT TO CALCULATE ONLY ONE SEMESTER USE 
1(CALCULATE ONE SEMESTER GPA)\n
IF YOU WANT TO CALCULATE YOUR CUMULATIVE GPA USE
2(CALCULATE CUMULATIVE GPA)\n\n'''f'{blue}''''

                   FAQ
WHAT ARE MAIN SUBJECTS- MAIN SUBJECTS ARE SUBJECTS
WITH A FULL CREDIT HOUR, LIKE MATHS OR PHYSICS\n
WHAT ARE ELECTIVE SUBJECTS - ELECTIVE SUBJECTS ARE
SUBJECTS WITH A HALF CREDIT HOUR, LIKE HPE\n
WHAT IS CREDIT HOUR - A credit hour is the unit of
measurement used to indicate the amount of instructional
and learning time required to achievethe student learning 
outcomes of a college(highschool)-level course.\n\n
'''f'{green}''''
            CREDIT HOUR CONVERSION
1 CREDIT = 6 HOURS PER WEEK
2 CREDIT = 12 HOURS PER WEEK
3 CREDIT = 18 HOURS PER WEEK
4 CREDIT = 24 HOURS PER WEEK
5 CREDIT = 30 HOURS PER WEEK
6 CREDIT = 36 HOURS PER WEEK

=================================================''')
   time.sleep(10) 
   main()







def main():
   print('''
+------------------------------------------------+
|                                                |
|       1.Calculate one semester GPA             |
|       2.Calculate cumulative GPA               |
|       3.About                                  |
|       4.How to calculate                       |
|       99.Exit                                  |      
|                                                |
+------------------------------------------------+
''')
   selection = (input(f'{blue}Enter your selection: '))
   if selection == '1':
        return one_calc()
   elif selection == '2':
        return cum_calc()

   elif selection == '3':
        return about()
   elif selection == '4':
      return how_to()
   elif selection == '99':
        print("\n"'Fine, Good byee')
   else:
        print('+------------------------------------+')
        print("|        Incorrect selection         |")
        print('+------------------------------------+')
        time.sleep(1)
        return main()
  

main()
 
