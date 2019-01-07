# -*- coding: utf-8 -*-

def raomaznie(n):

    #turning the number into an array of digits
    num_array = []
    for i in (str(n)):
        num_array.append(int(i))

    #constructing the conversion dictionary
    roman_dict = {
        1: {  
            1: "I",
            2: "II",
            3: "III",
            4: "IV",
            5: "V",
            6: "VI",
            7: "VII",
            8: "VIII",
            9: "IX"                           
        },
        2: {
            0: "",
            1: "X",
            2: "XX",
            3: "XXX",
            4: "XL",
            5: "L",
            6: "LX",
            7: "LXX",
            8: "LXXX",
            9: "XC"                           
        },     
        3:  {
            0: "",            
            1: "C",
            2: "CC",
            3: "CCC",
            4: "CD",
            5: "D",
            6: "DC",
            7: "DCC",
            8: "DCCC",
            9: "CM"                           
        },  
        4:  {
            0: "",            
            1: "M",
            2: "MM",
            3: "MMM",
            4: "MMMM",
            5: "V̄",
            6: "V̄M",
            7: "V̄MM",
            8: "V̄MMM",
            9: "MX̄"                        
        }  
    }
    romanized = ""
    i = len(num_array)
    for n in num_array:
        romanized = romanized + roman_dict[i][n]
        i -= 1
    
    return romanized

print(raomaznie(2123))

