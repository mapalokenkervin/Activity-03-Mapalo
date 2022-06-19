import Mapalo_script_2_ev as EV
import Mapalo_script_2_stat as ST
import math 

def ContinueOrExit():
    select = int(input("\nDo you want to try again? \n[1] Yes  [2] No \nOption: "))
    if select == 1: main()
    elif select == 2: exit()
    else: 
        print("Invalid...")
        ContinueOrExit()
        

def main():

    print("***************Welcome To Pokemon STAT & EV Calculator***************\n\n")
    while True:
        base = int ( input ("Base HP: "))
        level = int ( input ("Level: "))
        ev = int ( input ("EV must be [0 - 255] \nEV: "))
        iv = int ( input ("IV must be [0 - 31] \nIV: "))
            
        if iv > 31:
            print("IV exceeds\n")  
            main() 

        if ev > 255:
            print("EV exceeds\n") 
            main()

        else:    
            print("Proceeding...")
            break

    while True:
        print("\nChoose Pokemon Calculator Type \n[1] EV Calculator \n[2] Stat Calculator ")
        choice = int(input("\nInput your choice: "))
    
        if choice == 1:
            stats = int(input("Stats: "))
            pick = int(input("[1] Beneficial [2] Hindering \nModidier: "))
            if pick == 1:
                mod = 1.1

            elif pick == 2:
                mod = 0.9

            else:
                print("Invalid Input...")
            
            totalEV = EV.evCompute.computeEV(base, iv, ev, level, mod, stats)
            if totalEV <=500:
                print("Total EV:", totalEV)
            
            else:
                print("Pokemon's Total EV Exceeds...")
            ContinueOrExit()
        

        elif choice == 2:
            sel = int(input("\nCompute other stats? [1] Yes [2] No \nSelect: "))
            if sel == 1: 
                sele = str(input("\n[att] [def] [spatt] [spdef] [spd]\nWhat Stat would you like to compute?: "))    
                if sele == 'att': 
                    sta = 'Attack'   
                    selec = int(input("\n[1] Beneficial [2] Hindering \nNature: "))   
                    if selec == 1:
                        nat = 1.1

                    elif selec == 2:
                        nat = 0.9
                
                if sele == 'def':
                    sta = 'Defense'    
                    selec = int(input("\n[1] Beneficial [2] Hindering \nNature: "))   
                    if selec == 1:
                        nat = 1.1

                    elif selec == 2:
                        nat = 0.9
                
                if sele == 'spatt':  
                    sta = 'Special Attack'  
                    selec = int(input("\n[1] Beneficial [2] Hindering \nNature: "))   
                    if selec == 1:
                        nat = 1.1

                    elif selec == 2:
                        nat = 0.9

                if sele == 'spdef':  
                    sta = 'Special Defense'  
                    selec = int(input("\n[1] Beneficial [2] Hindering \nNature: "))   
                    if selec == 1:
                        nat = 1.1

                    elif selec == 2:
                        nat = 0.9

                if sele == 'spd':    
                    sta = 'Speed'
                    selec = int(input("\n[1] Beneficial [2] Hindering \nNature: "))   
                    if selec == 1:
                        nat = 1.1

                    elif selec == 2:
                        nat = 0.9
                
                other = ST.statCompute.otherStat(base, ev, level, iv, nat)
                if other <= 510:
                    print("\nComputing", sta,"Value =", other)
                
                else:
                    print("Pokemon's Total EV Exceeds...")
                ContinueOrExit()

            elif sel == 2:
                chp = ST.statCompute.health(base, ev, level, iv)
                if chp <= 510:
                    print ("HP Value:", chp)
                else:
                    print("Pokemon's Total EV Exceeds...")
                ContinueOrExit()

            else:
                print("Invalid Input...")
                       
        else:
            print("Invalid Input...")

main()