#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 19:38:18 2024

@author: user
"""
from datetime import datetime
from dateutil.relativedelta import relativedelta

class pacflix():
    list_of_referral_code = []
    
    def __init__(self, user_name):
        self.user_name = user_name
        self.start_date = None
        self.end_date = None
        self.current_plan = None
        self.duration = 0
        
        pacflix.list_of_referral_code.append(self.user_name)
        print("Your Account has been successfully created, share this code '{}' to your friends to get some benefits.".format ('self.user_name'))
        
        
    def list_plan(self):
        print("List of Pacflix plan:")
        print("1. Basic Plan")
        print("SD Resolution, 1 device, Movies, Rp.120.000,-.")
        print()
        print("2. Standard Plan")
        print("HD Resolution, 2 device, Movies + Sport, Rp.160.000,-.")
        print()
        print("3. Premium Plan")
        print("UHD Resolution, 4 device, Movies + Sport + Original Series, Rp.200.000,-.")
        
    def check_plan(self):
        if (self.current_plan == None):
            print("You do not have any subs yet.")
        else:
            print(f"Your current plan is {self.current_plan}.")
            print(f"Start subs at {self.start_date}.")
            print(f"End subs at {self.end_date}.")
    
    def purchase(self, new_plan, ref_code, duration):
        total_price = 0

        if((ref_code != None) and (ref_code in pacflix.list_of_referral_code)):
            self.duration = duration
            self.start_date = datetime.now()
            self.end_date = self.start_date + relativedelta(months=duration)

            if(new_plan == "Basic Plan"):
                self.current_plan = "Basic Plan"
                total_price = (120_000 - (0.04 * 120_000))
                print(f"You're selected Basic Plan with referral code from {ref_code}, and the price is {total_price}.")

            elif(new_plan == "Standard Plan"):
                self.current_plan = "Standard Plan"
                total_price = (160_000 - (0.04 * 160_000))
                print(f"You're selected Standard Plan with referral code from {ref_code}, and the price is {total_price}.")

            elif(new_plan == "Premium Plan"):
                self.current_plan = "Premium Plan"
                total_price = (200_000 - (0.04 * 200_000))
                print(f"You're selected Premium Plan with referral code from {ref_code}, and the price is {total_price}.")

            else:
                self.duration = 0
                self.start_date = None
                self.end_date = None
                print("Your selected plan is invalid!.")

        elif((ref_code != None) and (ref_code not in pacflix.list_of_referral_code)):
            print("Your referral code is invalid!.")

        elif(ref_code == None):
            self.duration = duration
            self.start_date = datetime.now()
            self.end_date = self.start_date + relativedelta(months=duration)

            if(new_plan == "Basic Plan"):
                self.current_plan = "Basic Plan"
                total_price = 120_000
                print(f"You're selected Basic Plan with price {total_price}.")

            elif(new_plan == "Standard Plan"):
                self.current_plan = "Standard Plan"
                total_price = 160_000
                print(f"You're selected Standard Plan with price {total_price}.")

            elif(new_plan == "Premium Plan"):
                self.current_plan = "Premium Plan"
                total_price = 200_000
                print(f"You're selected Premium Plan with price {total_price}.")

            else:
                self.duration = 0
                self.start_date = None
                self.end_date = None
                print("Your selected plan is invalid!.")

        else:
            print("Something bad happen.")
    
    def upgrade_plan(self, new_plan):
        subs_time = self.end_date - datetime.now()
        total_price = 0
        
        if(subs_time.days > 360):
            if(self.current_plan == "Basic Plan"):
                if(new_plan == "Standard Plan"):
                    self.current_plan = "Standard Plan"
                    total_price = (160000 - (160000 * 0.05))
                    print(f"Upgrade to {self.current_plan}, price {total_price}")
                    
                elif(new_plan == "Premium Plan"):
                    self.current_plan = "Premium Plan"
                    total_price = (200000 - (200000 * 0.05))
                    print(f"Upgrade to {self.current_plan}, price {total_price}")
                    
                else:
                    print("Your selected new plan is invalid!.")
                    
            elif(self.current_plan == "Standard Plan"):
                if(new_plan == "Premium Plan"):
                    self.current_plan = "Premium Plan"
                    total_price = (200000 - (200000 * 0.05))
                    print(f"Upgrade to {self.current_plan}, price {total_price}")
                    
                else:
                    print("Your selected new plan is invalid!.")
            else:
                print("You're unable to downgrade the subs plan.")
                
        else:
            if(self.current_plan == "Basic Plan"):
                if(new_plan == "Standard Plan"):
                    self.current_plan = "Standard Plan"
                    total_price = 160_000
                    print(f"Upgrade to {self.current_plan}, price {total_price}.")

                elif(new_plan == "Premium Plan"):
                    self.current_plan = "Premium Plan"
                    total_price = 200_000
                    print(f"Upgrade to {self.current_plan}, price {total_price}.")

                else:
                    print("Your selected new plan is invalid!.")

            elif(self.current_plan == "Standard Plan"):
                if(new_plan == "Premium Plan"):
                    self.current_plan = "Premium Plan"
                    total_price = 200_000
                    print(f"Upgrade to {self.current_plan}, price {total_price}.")

                else:
                    print("Your selected new plan is invalid!.")

            else:
                print("You're unable to downgrade the subs plan.")
            
                