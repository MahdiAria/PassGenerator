while(True):
    

    import random


    import pyfiglet

    
    from colorama import Fore,Back,Style

    
    Logo = pyfiglet.figlet_format("Password Generator", font= "slant")
    
    
    print(Fore.MAGENTA,(Logo))
    
    
    
      
    print("\n")
    
    
    reshte = input("𝙏𝙤𝙤𝙤𝙡 𝙥𝙖𝙨𝙨𝙬𝙤𝙧𝙙 => "); reshte = int(reshte)
    
    
    print("\n")
    
    
    print( ''.join([random.choice
                        (
                            'abcdefghijklmnopqrstuvwxyz'
                            +
                            'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
                            +
                            '!@#$%^&*()_+,><;./?`'
                            +
                            '1234567890'
                        )
                        for i in range(reshte)]))
                        
                        
    print("\n")
      
    
                                              
    Edame = input("𝗧𝗿𝘆 𝗔𝗴𝗮𝗶𝗻 :  𝘆/𝗻 : ")
    
                        
    if Edame == "y" or Edame == "yes":
        
        
        print("\n")
        
        
        print(" [ 𝐀𝐆𝐀𝐈𝐍 ] ")
        
        
        continue
    
    
    elif Edame == "n" or Edame == "no":
        
        
        print("\n")
        
        
        print(" [ 𝐂𝐋𝐎𝐒𝐄 ] ")
        
        
        break
                            
                            
    print(Edame)
