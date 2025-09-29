#!/usr/bin/env python3
# -*- coding: utf-8 -*-
selection = 0
while selection != 3:
    
    try:
        selection=int(input("Would you like to convert F to C (1) or C to F (2) ? Press 3 to quit: "))
    
    except ValueError:
        print("Please enter only a number")
        
    if selection == 1:
    
        try:
        
            farenheit_temp=float(input("Enter the Farenheit value : "))
        
        
            celcius_temp=(farenheit_temp - 32)*5/91
        
            print(celcius_temp)
        
        except ValueError:
            print("Please enter only a number")
        
    elif selection == 2:
        
        try:
            celcius_temp=float(input("Enter the Celcius value : "))
        
            farenheit_temp=(celcius_temp*9/5)+32
        
            print(farenheit_temp)
        
        except ValueError:
            print("Please enter only a number")
        
    elif selection == 3:
                print("Goodbye")
                
    else:
        print("Incorrect selection")

    

