#version 2.7.1
import time
import datetime
import webbrowser
import logging
import codecs
import csv
import getpass
import os
from tkinter import *
from tkinter import messagebox
#filemode='w' for overwriting and erase for continued logs
log_format = "%(asctime)s::%(levelname)s::%(name)s::"\
"%(filename)s::%(lineno)d::%(message)s"
logging.basicConfig(filename='/home/home/Desktop/flow_state/logfile.log' , level='DEBUG', format=log_format)
logging.info("***---INIT---***")
logging.info(os.name)
logging.info(os.getcwd())
li=[]
todo=[]
td='y'
er_0_0_1=er_0_0_4=0
pro=avoid=0
pro_check=ch='n'
logging.debug("---START---")
print("are you a new user? y/n")
usrin=input()
if usrin == 'y' or usrin == 'Y':
    with open("/home/home/Desktop/flow_state/cred.csv","a") as f:
        csv_writer =csv.writer(f)
        while (1):
            new_usr=input("enter username = ")
            new_pass=getpass.getpass("enter password = ")
            csv_writer.writerow([new_usr,new_pass])
            time.sleep(0.5)
            print("new user created")
            logging.info("new user created")
            window = Tk()
            window.eval("tk::PlaceWindow %s center" % window.winfo_toplevel())
            window.withdraw()
            messagebox.showinfo("user","user created")
            window.deiconify()
            window.destroy()
            window.quit()
            f.close()
            break
else:
    with open("/home/home/Desktop/flow_state/cred.csv","r") as f:
        csv_reader=csv.reader(f)
        usr_cred=input("enter username : ")  
        li.append(usr_cred)
        usr_pass=getpass.getpass("enter password : ")      
        li.append(usr_pass)
        for row in csv_reader:
            er_0_0_1+=1
            if li == row:
                time.sleep(1)
                logging.info("|USER|")
                logging.info(usr_cred)
                print("logging in ","......")
                time.sleep(1.25)
                logging.info("login successful")
                print()   
                print("welcome","* ",usr_cred," *")
                ch='/begin'
                print()                
                print("procrasti-NATOR 2020")
                print("created by -frroossst 02:14 31 May 2020")
                time.sleep(1)
                print("Commands :")
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
                print("/sound - view OST that *might* help you concentrate")
                time.sleep(0.1)
                print("/todo - create and manage a todo list")
                time.sleep(0.1)
                print("/calc - to open a web calculator")
                time.sleep(0.1)
                print("/man - to view the manual")
                time.sleep(0.1)
                print("/credit - to  view appropriate credits")
                time.sleep(0.1)
                print("/dopamine - check dopamine levels")
                '''print("/log - to view the distraction log")'''
                time.sleep(0.1)
                print("/detox - to clear reward logs")
                time.sleep(0.1)
                print("/break - to take a break")
                time.sleep(0.5)
                pro_check=='n'
                now=datetime.datetime.now()
                dist_timings=break_timings=[]
                avoid=pro=br=br_total=br_timez=pomo_count=calc=deauth=dope=achv=0
                ch = '/begin'
                print("start time =",now)
                while ch == '/begin' or ch == '/cont' or ch=='/avoid' or ch=='/break' or ch =='/log' or ch=='/pomodoro' or ch=='/sound' or ch=='/todo' or ch=='/calc' or ch=='/credit':
                    print("Did you find your mind wander off?")
                    pro_check = input()
                    if pro_check == 'y' or pro_check == 'Y':
                        pro += 1
                        deauth+=1
                        td=='y'
                        logging.debug("/cont")
                        dist_timings.append(datetime.datetime.now())
                        print("Total number of times you've been distracted this session : ", pro)
                        ch = input("command : ")
                        if ch == '/avoid':
                            logging.debug("/avoid")
                            avoid+=1
                            print("Total number of avoidable distraction =",avoid,"of",pro)
                            with open(usr_cred,"a") as pts:
                                    pts.write("-10 \n")
                        elif ch == '/man':
                            pro-=1
                            man=open("/home/home/Desktop/flow_state/manual.html","r")
                            webbrowser.open_new_tab('manual.html')
                        elif ch == '/break':
                            logging.debug("/break")
                            break_timings.append(datetime.datetime.now())
                            pro-=1
                            br_time=int(input("Enter break duration (in minutes) : "))
                            if br_time<0:
                                logging.error("0.0.2")
                                print("UNDERFLOWED TIMINGS")
                                print("ERROR CODE : 0.0.2 | Refer the manual for debug")
                                break    
                            else:
                                logging.debug("break start")            
                                br_timez=br_time*60          
                                time.sleep(br_timez)
                                br+=1
                                window = Tk()
                                window.eval("tk::PlaceWindow %s center" % window.winfo_toplevel())
                                window.withdraw()
                                messagebox.showinfo("procrast-NATOR","Break has ended", icon ='warning')
                                window.deiconify()
                                window.destroy()
                                window.quit()
                                print("total number of breaks = ",br)
                                br_total+=br_time 
                                logging.debug("break end")
                        elif ch == '/pomodoro':
                            with open(usr_cred,"a") as pts:
                                pts.write("10 \n")
                                logging.debug("pomodoro start")
                                pro-=1
                                print("\n 1. standard timer \n 2. custom timer")
                                type_pomo=int(input())
                                if type_pomo == 1:
                                    print("pomodoro set for 25 minutes")
                                    pomo_count+=1
                                    pomo_timer=25*60            
                                    time.sleep(pomo_timer)
                                    logging.debug("pomodoro end")
                                    print("pomodoro session completed")
                                    if pomo_count%4 == 0:
                                        print()
                                        logging.debug("one pomodoro set completed")
                                        print("pomodoro sessions completed = ",pomo_count)
                                        print("you deserve a break") 
                                #custom pomodoro timer block             
                                elif type_pomo == 2:
                                    logging.debug("custom pomodoro started")
                                    custom_timer=int(input("Enter custom time : "))
                                    pomo_count+=1
                                    custom_timer=custom_timer*60
                                    time.sleep(custom_timer)
                                    logging.debug("custom pomodoro end")
                                    if pomo_count%4 == 0:
                                        print()
                                        logging.debug("one pomodoro set completed")
                                        print("pomodoro sessions completed = ",pomo_count)
                                        print("you deserve a break") 
                        elif ch == '/sound':
                            logging.debug("/sound")            
                            pro-=1
                            print("1. assassin's creed iv black flag")
                            print("2. assassin's creed ii")
                            print("3. assassin's creed odyssey")
                            print("4. best of mozart")
                            vid_choice=int(input("select = "))
                            if vid_choice == 1:
                                logging.debug("vid_choice = 1")
                                webbrowser.open_new("https://www.youtube.com/watch?v=JYVMnLUZu9Y&t=1320s")
                                with open(usr_cred,"a") as pts:
                                    pts.write("10 \n")
                            elif vid_choice == 2:
                                logging.debug("vid_choice = 2")
                                webbrowser.open_new("https://www.youtube.com/watch?v=iriiZOeInDg&t=5415s")
                                with open(usr_cred,"a") as pts:
                                    pts.write("10 \n")
                            elif vid_choice == 3:
                                logging.debug("vid_choice = 3")
                                webbrowser.open_new("https://www.youtube.com/watch?v=fwthw9Sy_RU")
                                with open(usr_cred,"a") as pts:
                                    pts.write("10 \n")
                            elif vid_choice == 4:
                                logging.debug("vid_choice =4")
                                webbrowser.open_new("https://www.youtube.com/watch?v=Rb0UmrCXxVA")            
                                with open(usr_cred,"a") as pts:
                                    pts.write("10 \n")              
                            #miserere mei deus            
                            elif vid_choice == 5:
                                print("are you sure you want to continue? y/n")
                                #easter egg                                
                                ee=input()
                                if ee == 'n' or 'N':
                                    logging.info("---miserere mei deus---")
                                    webbrowser.open_new("https://www.youtube.com/watch?v=36Y_ztEW1NE")  
                                    with open(usr_cred,"a") as pts:
                                        pts.write("100 \n")
                            else:
                                logging.debug("invalid video choice")
                                print("ERROR CODE : 0.0.3 | Refer the manual for debug")           
                        elif ch=='/todo':
                            logging.debug("/todo")
                            td='y'
                            pro-=1
                            while td=='y':                                    
                                print()
                                time.sleep(0.75)        
                                print("\n 1. add an item \n 2. strikeoff an item \n 3. view current list")
                                print()
                                ch_td=int(input(": "))
                                if ch_td == 1:
                                    elmnt=input("enter the element : ")
                                    todo.append(elmnt)
                                    print("current list : ")
                                    print(todo)
                                    len_todo=len(todo)
                                    print()
                                    logging.debug("element added to list")
                                    td=input("do you want to continue? ")
                                    with open(usr_cred,"a") as pts:
                                        pts.write("5 \n")
                                elif ch_td ==2:
                                    strk=int(input("which item do you want to remove? "))
                                    len_todo=len(todo)
                                    strk=strk-1
                                    if strk<0:
                                        logging.error("0.0.5")
                                        print("UNDERFLOW ERROR")
                                        print("ERROR CODE : 0.0.5 | Refer the manual for debug")
                                        print()
                                        break
                                    else:
                                        len_todo=len(todo)
                                        if strk >= len_todo:
                                            logging.error("0.0.6")
                                            print("OVERFLOW ERROR")
                                            print("ERROR CODE : 0.0.6 | Refer the manual for debug")
                                            print()
                                            break
                                        else:
                                            todo.pop(strk)
                                            print("current list : ")
                                            print(todo)
                                            print()
                                            logging.debug("element removed from the list")
                                            with open(usr_cred,"a") as pts:
                                                pts.write("10 \n")
                                            td=input("do you want to continue? ")
                                elif ch_td==3:
                                    logging.debug("list printed")
                                    print()
                                    for i in todo:
                                        print(i)
                                    td=input("do you want to continue? ")                                
                        elif ch=='/calc':
                            calc+=1
                            logging.debug("/calc")
                            print("1. scientific calculator 2. graphical calculator") 
                            calc_type=int(input())
                            if calc_type ==1:
                                logging.debug("scientific calc")
                                webbrowser.open_new("https://www.desmos.com/scientific")
                                with open(usr_cred,"a") as pts:
                                    pts.write("10 \n")
                            elif calc_type==2:
                                logging.debug("graphing calc")
                                webbrowser.open_new("https://www.desmos.com/calculator")
                                with open(usr_cred,"a") as pts:
                                    pts.write("10 \n")
                            else:
                                logging.debug("invalid calc type choice")
                                print("ERROR CODE : 0.0.3 | Refer the manual for debug")
                        elif ch=='/credit':
                            logging.debug("/credit")
                            pro-=1                            
                            print()
                            print("the code in its entirety was written by frroossst (me) | frroossst@protonmail.com |")
                            print()
                            print("the '/calc' function utilizes an online web application ie https://www.desmos.com/")
                            print()
                            print("'/sound' funcition utilizes the https://www.youtube.com/ website for playing videos")
                            print()    
                            print("the amount of dopamine accumulated does not represent actual amount of dopomine it is just a reward system")
                            print()
                        elif ch=='/dopamine':
                            logging.debug("/dopamine")
                            pro-=1
                            with open(usr_cred,"r") as pts:
                                content=pts.readlines()
                                for i in content:
                                    achv=int(i)
                                    dope=dope+achv
                                print(dope,"nanograms of dopamine accumulated *")
                        elif ch=='/detox':
                            pro-=1
                            logging.debug("/detox")
                            with open(usr_cred,"w") as rf:
                                rf.write("0")
                    elif pro==0 and avoid==0:
                        logging.error("0.0.1")
                        er_0_0_1=1                        
                        print("NULL ERROR")
                        print("ERROR CODE : 0.0.1 | Refer the manual for debug")
                        break
                    else:
                        #add achievements and points
                        logging.debug("---END---")
                        print('here is a breakdown of your session',usr_cred)
                        print('total distractions = ', pro)
                        print('avoidable distractions = ',avoid)
                        print('unavoidable distractions = ',pro-avoid)
                        print('distraction quotient = ',(avoid/pro)*100,'%')
                        print('total breaks = ',br)
                        print('total time spent in breaks = ',br_total,'minute(s)')  
                        print('total pomodoro sessions = ',pomo_count)
                        print('total number of times you used calculator = ',calc)      
                        later=datetime.datetime.now()
                        print('end time = ',later)
                        f.close()
                        er_0_0_4=1       
                        ch = 'n'
                else:
                    break
            elif pro_check!='n' or pro_check !='N' and er_0_0_1==0 and er_0_0_4!=1:
                logging.critical("authentication failure")
                print("ERROR CODE : 0.0.4 | Refer the manual for debug")
            elif ch=='/end':
                ch='n'
                #version naming scheme
                #x.y.z 
                #x= major changes
                #y= new features/addition
                #z= minor bug fixes
                """YES I DO REALIZE IT IS A DISTRACTION TRACKER RATHER THAN PROCRASTINATION TRACKER UGH!"""
