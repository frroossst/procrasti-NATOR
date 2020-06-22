#version 1.3.0
import time
import datetime
print("procrasti-NATOR 2020")
print("created by -frroossst 02:14 31 May 2020")
time.sleep(1)
print("Commands:")
time.sleep(0.25)
print("/begin - to initiate program")
time.sleep(0.1)
print("/end - to terminate program")
time.sleep(0.1)
print("/cont - to continue the program")
time.sleep(0.1)
print("/avoid - to count avoidable distractions")
time.sleep(0.1)
print("/pomodoro - to initiate 25x4 pomodoro timer")
time.sleep(0.1)
print("/man - to view the manual")
time.sleep(0.1)
print("/log - to view the distraction log")
time.sleep(0.1)
print("/break - to take a break")
time.sleep(0.5)
now=datetime.datetime.now()
dist_timings=[]
break_timings=[]
avoid=pro=br=br_total=br_timez=pomo_count=0
ch = '/begin'
print("start time =",now)
while ch == '/begin' or ch == '/cont' or ch=='/avoid' or ch=='/break' or ch =='/log' or ch=='/pomodoro':
    print("Did you find your mind wander off?")
    pro_check = input()
    if pro_check == 'y' or pro_check == 'Y':
        pro += 1
        dist_timings.append(datetime.datetime.now())
        print("Total number of times you've been distracted this session :", pro)
        ch = input("command :")
        if ch == '/avoid':
            avoid+=1
            print("Total number of avoidable distraction =",avoid,"of",pro)
        elif ch == '/man':
            pro-=1
            print('procrasti-NATOR 2020 MANUAL')
            errid=input("Enter error code :")
            if errid =='0.0.1':
                print()
                print("id = 0.0.1")
                print("type = null error")
                print("source = pro=0 && avoid=0")
                print("soln = rerun the program with pro!=0 and/or avoid!=0")
            elif errid =='0.0.2':
                print()
                print("id = 0.0.2")
                print("type = underflow error")
                print("source = break time value entered is negative")
                print("soln = enter a value of break timing >0")
        elif ch == '/log':
            pro-=1
            n=1
            print()
            print("---distracrions---")
            for i in dist_timings:
                print()
                print('number',n,'distraction at',i)
                n+=1
            '''add 1st 2nd 3rd rather than number'''
            m=1
            print()
            print("---breaks---")
            for j in break_timings:
                print()
                print('number',m,'break at',j)
                m+=1
        elif ch == '/break':
            break_timings.append(datetime.datetime.now())
            pro-=1
            br_time=int(input("Enter break duration (in minutes) :"))
            if br_time<0:
                print("UNDERFLOWED TIMINGS")
                print("ERROR CODE : 0.0.2 | Refer the manual for debug")
                break    
            else:            
                br_timez=br_time*60          
                time.sleep(br_timez)
                br+=1
                print("total number of breaks =",br)
                br_total+=br_time 
        elif ch == '/pomodoro':
            pro-=1
            print("pomodoro set for 25 minutes")
            pomo_count+=1
            pomo_timer=25*60            
            time.sleep(pomo_timer)
            print("pomodoro session completed")
            if pomo_count%4 == 0:
                print()
                print("pomodoro sessions completed =",pomo_count)
                print("you deserve a break")            
    elif pro==0 and avoid==0:
        print("NULL ERROR")
        print("ERROR CODE : 0.0.1 | Refer the manual for debug")
        break
    else:
        print('total distractions =', pro)
        print('avoidable distractions =',avoid)
        print('unavoidable distractions =',pro-avoid)
        print('distraction quotient =',(avoid/pro)*100,'%')
        print('total breaks =',br)
        print('total time spent in breaks =',br_total,'minute(s)')  
        print('total pomodoro sessions =',pomo_count)      
        later=datetime.datetime.now()
        print('end time =',later)        
        ch = 'n'
'''x.y.z 
x= major changes
y= new features/additions
z= minor bug fixes'''
"""YES I DO REALIZE IT IS A DISTRACTION TRACKER RATHER THAN PROCRASTINATION TRACKER UGH!""" 
