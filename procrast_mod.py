#version 2.5.5
import time
import datetime
import webbrowser
import logging
import codecs
import csv
import getpass
from tkinter import *
from tkinter import messagebox
#filemode='w' for overwriting and erase for continued logs
log_format = "%(asctime)s::%(levelname)s::%(name)s::"\
"%(filename)s::%(lineno)d::%(message)s"
logging.basicConfig(filename='/home/home/Desktop/flow_state/logfile.log' , level='DEBUG', format=log_format)
li=[]
er_0_0_1=0
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
            break
else:
    with open("/home/home/Desktop/flow_state/cred.csv","r") as f:
        csv_reader=csv.reader(f)
        usr_cred=input("enter username : ")  
        li.append(usr_cred)
        usr_pass=getpass.getpass("enter password : ")      
        li.append(usr_pass)
        for row in csv_reader:
            if li == row:
                time.sleep(1)
                print()
                print("logging in...")
                logging.info("login successful")    
                print()
                time.sleep(1)
                ch='/begin'
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
                print("/man - to view the manual")
                '''time.sleep(0.1)
                print("/log - to view the distraction log")'''
                time.sleep(0.1)
                print("/break - to take a break")
                time.sleep(0.5)
                pro_check=='n'
                now=datetime.datetime.now()
                dist_timings=break_timings=[]
                avoid=pro=br=br_total=br_timez=pomo_count=0
                ch = '/begin'
                print("start time =",now)
                while ch == '/begin' or ch == '/cont' or ch=='/avoid' or ch=='/break' or ch =='/log' or ch=='/pomodoro' or ch=='/sound':
                    print("Did you find your mind wander off?")
                    pro_check = input()
                    if pro_check == 'y' or pro_check == 'Y':
                        pro += 1
                        logging.debug("/cont")
                        dist_timings.append(datetime.datetime.now())
                        print("Total number of times you've been distracted this session : ", pro)
                        ch = input("command : ")
                        if ch == '/avoid':
                            logging.debug("/avoid")
                            avoid+=1
                            print("Total number of avoidable distraction =",avoid,"of",pro)
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
                            vid_choice=int(input("select = "))
                            if vid_choice == 1:
                                logging.debug("vid_choice = 1")
                                webbrowser.open_new("https://www.youtube.com/watch?v=JYVMnLUZu9Y&t=1320s")
                            elif vid_choice == 2:
                                logging.debug("vid_choice = 2")
                                webbrowser.open_new("https://www.youtube.com/watch?v=iriiZOeInDg&t=5415s")
                            elif vid_choice == 3:
                                logging.debug("vid_choice = 3")
                                webbrowser.open_new("https://www.youtube.com/watch?v=fwthw9Sy_RU")
                            #miserere mei deus            
                            elif vid_choice == 4:
                                print("are you sure you want to continue? y/n")
                                #easter egg                                
                                ee=input()
                                if ee == 'n' or 'N':
                                    logging.info("---miserere mei deus---")
                                    webbrowser.open_new("https://www.youtube.com/watch?v=36Y_ztEW1NE")
                            else:
                                logging.debug("invalid video choice")
                                print("ERROR CODE : 0.0.3 | Refer the manual for debug")           
                    elif pro==0 and avoid==0:
                        logging.error("0.0.1")
                        er_0_0_1=1                        
                        print("NULL ERROR")
                        print("ERROR CODE : 0.0.1 | Refer the manual for debug")
                        break
                    else:
                        logging.debug("---END---")
                        print('total distractions = ', pro)
                        print('avoidable distractions = ',avoid)
                        print('unavoidable distractions = ',pro-avoid)
                        print('distraction quotient = ',(avoid/pro)*100,'%')
                        print('total breaks = ',br)
                        print('total time spent in breaks = ',br_total,'minute(s)')  
                        print('total pomodoro sessions = ',pomo_count)      
                        later=datetime.datetime.now()
                        print('end time = ',later)        
                        ch = 'n'
        else:
            if pro_check!='n' or pro_check !='N' and er_0_0_1==0:
                logging.critical("authentication failure")
                print("ERROR CODE : 0.0.4 | Refer the manual for debug")
                #version naming scheme
                #x.y.z 
                #x= major changes
                #y= new features/addition
                #z= minor bug fixes
                """YES I DO REALIZE IT IS A DISTRACTION TRACKER RATHER THAN PROCRASTINATION TRACKER UGH!"""
