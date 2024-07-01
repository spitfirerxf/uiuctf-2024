import os, time
import platform
#from playsound import playsound
#import multiprocessing

# set this for your terminal
WIDTH = 80
HEIGHT = 20
LINE_UP = '\033[1A'
LINE_CLEAR = '\x1b[2K'

art_wizard="""
             ░░░                            
          ░░▓▓▓▓▒░                          
         ░▒▓▓█▓▓▓▓░░                        
       ░░▓███▓████▓▓▓▓▒░   ░░░░░            
       ░▒░░░▒██▓▓▓▒▒▒▒░░  ░▓█▓▒░░▒▒░░░░     
       ░░ ░░█▓▒▒▒▒▒▒▒▒░░░▒▓█▓░░░   ░░░░░░░  
         ░░▓░▒▒▒▒░▒▒░▒▒░▓▓▓█▓░         ░░░░░
░░░░▒░░ ░▒░▒░▒▓▒▒▒▓▒░▒██████░         ░░░░░░
 ░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▓███▓██▒░        ░░░░░░ 
  ░▓▓▓▓▓▓▓▓▓▓▓▓██▓▒▓▓▓▒░░░                  
  ░░▓▓▓▓▓▓▓▓▓▓▓█▓██▓▓▓▒                     
    ░░▓██▓▓▓▓▓▓▓██▓▓▓▒▒░                    
       ░░▒▒░▒▓████▒▓▓▓▒                     
            ▒██▓▓▓█▓▓█▒                     
            ░▓▓▓▓██▓██▓░                    
            ░▒██▓█▓▓▓██░                    
            ░▓▓█████▓█▓█▒▒░░                
         ░░▓█████▓████████▒░                
           ░░░░░                                                                           
"""

art_sommarscii="""
                                   
                    ███  █████     
             ██▓▓███ ████████      
            ███▓█▓▓▓████████       
            ████▓▓█▓▓▓█  █         
           ████████▓▒▒▒▒           
            ███████████▒▒          
 ▓▓▓▓     █▓▒▓██████▓▓▓█▓▓         
    ██  ███▓▓▓██▓▓▓▓▓████          
      █▓▓██▓█████████▓▓▒▒          
        ▓▓▓▓▓▓███████▓▓▓▓▒▒▒▒      
       ▓▓▓▓▓▒▓████████▓▒▒▓▓▓       
      ███▓▓▓▓▓▓████▓█████▓▓▓▓      
      ██▓▓▓▓   ███▓█▓▓▓███▓▒▓      
       ▓▓▓▓      ▓▓  █   ███▓▓     
      █▓▓▓         ▓      ███▒▓▓▓  
     ██▓▓█                  ███▓▓  
     ███                      ███  
                                        
"""

art_sommarscii_sword="""
                                                        
                    ███  █ ██                           
             █▓▓▓██ ███  ██                             
            ██▓▓█▓▓▓███████                             
           █████▓█▓▓██          ██▓▓█                   
           ████████▒▓▒▒         █▒▒▒▒██                 
           ███████████▒▒         █▓▓▒▒▓▓█               
  ▓▓▓     █▓▒██████▓▓▓▓█▒          ██▒▒▒▓█              
    ██ ███▓█████▓▓▓▒▓██▓              █▓▒▒▒▓███▓██      
      ███ ▓██████████▓▒▒░              █▓▒▒▒▓█▓██       
        ▓▒▓▓▓███▓▓██▓▓▓▓  ▓▒▒            ███▓▓█         
       █▓▓▓▒▓▓███████▓▓▓▒▓▓             ██▓▓▓█▓██       
      ███▓▒██▓█████▓█████▓▓▓           ███    ██▓███    
      ██▓▓▓    ███  ▓▓████▓▓▓                   ████    
      █▓▓▓       █▓     ███▓▒                           
     █▓▓▓▓               █████▓                         
    █▓▓▓█                  ███▓▓                                                                         
"""

art_village_background = """
       ▒▒▒▒▒▒                                           
   ▒▒▒▒▓▓▓▓▒▒▒▓▓▓▒▒░                                    
  ▒▒▓▓▓▓▓▓▓▒▒▓▓▓▓▓▒▒                                    
  ▒▒▒▓▓▓▓▓▓▓▓▓▓▒▒▒▒                                     
  ▒▒▒▓▓▓▓█▓▓▓█▓▓▒▒▒▒▒                                   
 ▒▒▒▓▓▓▓▓▓▒▒▓▓▓▓▓▓▒▒▒▒                                  
 ▒▓▓▓▓▓▓▒▒▒▓▓▓▓▒▒▒░░                          ░░░░      
▒▓▓▓▓▓▓▓▓▓▓▓▒▒▓                            ░░░░░░░░░░   
     ▒ ▓▓▓▓    ▓▓▓▓▓                      ░░░░▒▒▒▒▒▒░░  
       █▓▓   ▓███▓▓██  ░░░░░░░░░░░░░ ░▒▒░ ░░▒▒▒▒▓▓▓▒░░  
       █▓      ███▓▓░░░░░░░░░░░░░░░░░▒▒▓▒▒▓▓▓▓▓▒▒▓▒▒    
  ▒░▒▒░▓▓▒▒▒▒▒▒▒▒▓▒░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▒░▒▓▒▒▓▓ 
░▒▒▒▒▒░▓▓▒▒▒▒▒▒░░▒▒░░▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒░▒░░
▒▒▒▒░░▒▒▒▒▒▒▒▒▒▒▒▓▒▒▒▒▒▒▒░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░▒▒░▒▒▒▒▓▒
░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▒▒▓▒▓▒▒░░░░░░░░░▒▒▒▒▒▒▒▒▒▒░░▒▒▒▒▒▒▒▓
░▒▒▒▒▓▒▒▓▓▒░▒▒▒▓▒▒▒▒▓▒▓▓▓▒▓▒░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▓▓
░▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒░░░░░░░▒░░░░░░░░░░░░░▒▒▒▒▒▒▓▒▓▓▒▒▓▓
░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░▒░░░░░▒▒▒░░░░░░░░░▒▒▒▒▓▒▒▒▓▓▓▓▓▒▒
"""

art_tornado="""
                                     
                   ░░░░░░░░░▒▒▒▒▓▓   
    ▓▓▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░▒   
 ▓▓▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░ ▓
   ▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░    
   ▒▒▒░░░░░░░░░▒▒▒░░░░░░░░░░░▒▒▒▒▒▒  
    ▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░▒▒▒  
    ▓▒▒▒▒░░░▒▒░░░░░░░░░░░░░░░░░▒▒    
      ▒▒▒▒▒▒░░▒▒▒▒▒▒░░░░░░░░▒▒▒▒▒    
       ▓▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░▒▒       
           ▒▒▒▒▒▒▒▒▒░░░░▒▒▒▒▒▒▒      
             ▓▓▒▒▒░░░░░░░░▒▒         
               ▒▒▒▒░░░░░░▒▒          
             ▓▒▒▒░░░░░▒▒▒            
             ▒▒▒░░░░░░               
              ▒▒░░░░▒                
              ▒▒░░░░░▒▒              
                 ▒▒▒▒░░░░▒           
                     ▒▒░░░           
                                     
"""

art_village_background_tornado="""
       ▒▒▒▒▒                                                                    
   ▒▒▒▒▓▓▓▒▒▒▓▓▓▒▒░                                                      ▓      
  ▒▒▓▓▓▓▓▓▒▒▒▓▓▓▓▒▒                                        ▓▓▒▒░░░░░░░░░░░      
 ▒▒▒▒▓▓▓▓▓▓▓▓▓▒▒▒▒                                     ▓▒▒▒░░░░░░░░░░░░░░░░▒▓   
  ▒▒▒▓▓▓▓█▓▓█▓▓▓▒▒▒▒▒                                   ▒▒▒▒░░░░░░░░░░░░░░░     
 ▒▒▒▓▓▓▓▓▒▒▓▓▓▓▓▓▓▒▒▒                                    ▒▒░░░░░░░░░░░░░░▒▒▓    
 ▒▓▓▓▓▒▓▒▒▒▓▓▓▒▒▒░░                          ░░░         ▒▒▒▒░░░░░░░░░░░░░      
▒▓▓▓▓▓▓▓▓▒▓▓▒▒▓                           ░░░░░░░░░       ▒▒▒▒░▒▒▒░░░░░▒▒▒      
     ▒ ▓▓▓▓   ▓▓▓▓▓                      ░░░▒▒▒▒▒▒░░         ▒▒▒▒░▒░░░░▒▒       
       ▓▓▒   ▓██▓▓ █  ░░░░░░░░░░░░░▒░▒▒░ ░▒▒▒▒▓▓▓▒░░           ▒▒▒▒░░░▒         
       ▓▓     ███▓▓░░░░░░░░░░░░░░░░░▒▒▓▒▒▓▓▓▓▓▒▓▒▒              ▒▒░░░▒▒         
 ▒▒░▒▒░▓▒▒▒▒▒▒▒░▓▒░░▒▒▒▒░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▒▓▓▓▒▒▒▓▒▒▓▓          ▒▒░░░▒▒          
░▒▒▒▒▒░▓▒▒▒▒▒▒▒░▒▒░░▒▒▒▒░░░░░░░░░░░░░░░░░░░░░▒▒▒▒░▒░▒░▒        ▒░░▒▒            
▒▒▒▒░▒▒▒▒▒▒▒▒▒▒▒▒▒▒░▒▒▒▒░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░▒▒░░░▒▒▒▒░        ▒░░░▒            
░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒▓▒▒▒▒░░░░░░░░░▒▒▒▒▒▒▒▒▒░░▒▒░▒▒▒▒▓▓          ▒▒░░░          
░▒▒▒▒▓▒▒▓▓▒▒▓▒▒▒▒▒▒▓▓▒▓▓▓▓▒░░░░░░░░░░░░░░░▒▒▒▒▒▒▒░▒▒▒▓▒            ▓▒░          
░▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒░░░░░░░▒░░░░░░░░░░░░▒▒▒▒▒▒▓▒▓▓▒▒▒▓▓                         
░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░▒░▒░░░▒▒▒░░░░░░░░░▒▒▒▒▒▒▒▓▓▓▓▓▒▒▒                         
"""

art_village_warrior="""
      ▒▒▒▒▒░                                                                      
   ▒▒▒▒▓▓▓▒▒▒▓▓▒▒░                                                                
  ▒▒▓▓▓▓▓▓▒▒▓▓▓▓▒▒                                                                
 ▒▒▒▒▓▓▓▓▓▓▓▓▓▒▒▒░                                                                
 ▒▒▒▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒                                            ▓  █████████      
 ▒▒▓▓▓▓▓▒▒▒▓▒▓▓▓▓▒▒▒                                          ██▓▓█▓██████        
 ▓▓▓▓▓▓▒▓▒▒▓▓▓   ░                       ░░░░░░               ███▓▓▓▓▓▓           
 ▓▓▓▓▒▓▓ ▓▓ ▒▓▓▓▓▓                     ░░░░▒▒░░░              ██████▓▓▓▒          
      ▓▓▓▒   ▓▓▓▒▓█   ░░░░         ░░  ░░▒▒▒▓▒▒▒░      ▓▓    ▓▒▓████▓▓▓▓▓         
      ▓▓      ▓█▓▓ ░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▓▓▒░         ██▓███████▓▓▓▒▒          
  ▒░▒▒▓▓▒▒▒▓▓ ▒█▓▒░░░▒▒▒▒░▒▒▒▒▒▒▒▒▓▓▒▒▒▒▓▓▓▓▒▓▒▒ ▓        █▓▓▓▓██████▓▓▓▒▒▒       
 ▒▒▒▒▒░▓▒▒▒▒░▒░▓▒░░▒▒▒▒░░░░░░░░░░░░░░░▒░░░▒▒▓▓▒▓░░░       █▓▓▓▓▓█████▓▓▓▓▓▓       
░░▒▒░▒░▒▒▓▒▒░▒▒▒▒▒░▒▒▒▒░░▒▒▒▒▒▒▒▒▒▒░▒░░░░░░░░▒▒▒▒▒▒░     ██▓▓▓ ▓████▓▓███▒▓       
░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▒▒▒▒▒▒▒░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒░▒░▒▒▒▒▒▒      █▓▓     █▓ ▓ ███▓▓      
░▒▒▒▓▓▒▒▓▒▒▒▒▒▒▒▒▒▓▒▒▓▒▓▒░░░░░░░░░░░░░░▒░▒▒▒▒▒▒▒▒▒▓▒     █▓▓▓            ███▓     
░▒▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒░░░░░░▒▒░░░░░░░░░░░▒▒▒▒▒▓▓▒▓▓▒▒▓▓     ██                ██     
░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░▒░░░░░▒▒░░░░░░░░▒▒▓▒▒▒▒▒▓▓▓▓▓▒▒                              
"""

art_wizard_sommarscii="""
            ░░░                                                                 
          ░░▓▓▓▓▒░                                        ░░░  ░▒░░░▒▓▓█▓▒░░░░  
         ░▒▓▓█▓▓▓▓░░                                    ░▓█▓▓▓▒░░▓▒░░░░░▒░░     
       ░░▓███▓████▓▓▓▓▓░   ░░░░░░                       ░▓█▓██▓█▓██▓▓▓█▓░       
       ░▒░░░░██▓▓▓▒▒▒▒░░  ░▓█▓▒▒░▒▒░░░░                ░████▓▓█▓██▓░░░░         
       ░░  ░▓▓▒▒▒▒▒▒▒▒░░░▒▓▓█░░░    ░░░░░░░            ░████████▓▓▒▒░           
          ░▓░▒░▒▒░▒▒░▒▒░▒█▓█▓░         ░▒░░░░░ ░       ░███████████▓▒░░         
░░░░▒▒░ ░░░▒░▒▓▒▒▒▓▒░▒██████▒          ░░░░░░▒▓░     ░▒▒▒████████▓▓▓█▓▒         
 ░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒░▓███▓██▓░        ░░░░░░░  ░▒▒ ░░▒█▓▓▓░▒█▓▓▓▓▓███▓▒░         
  ░▒▓▓▓▓▓▓▓▓▓▓▓▓██▒▓█▓▓░░░░                      ▒▓▓▓▒░░▒████████▓▓▒░░          
   ░▒▓▓▓▓▓▓▓▓▓▓▓▓██▓▓▓▓░                         ░░▒░▓███████▓████▓▓▓░░░░░░     
    ░░▓███▓▓▓▓▓▓██▓▓▓▒▓░                          ░▒▓▓▓▓▒▓█████████▓▓▒░ ░░░     
       ░░▒▒░▒▓████▓▓▓▓▓░                         ░▓█▓▓▓▓▓▓█████████▓█▓▓▓▓▒░     
            ░██▓▓█▓▓▓▓▓░                         ░▓▓▓▓▒▒░░▒▒████▓▓█████▓▓▒░     
            ░▓▒▓▓██▓██▓░                         ░▓█▓▓▒░    ░█▒░░▒▓▒▒███▓▓░░    
            ░▒██▓▓▓█▓██▒                         ░▓▓▓▒░      ░▓░  ░░ ░░██▓▒░    
            ░▒▓███████▓▓▓▒░░                     ▒▓▓▒░         ░░     ░░▒█▓█▓░░ 
          ░▓█████▓███▓████▓░                   ░▓▓▓▓▒░                   ▒▓█▓▓░ 
          ░░░░░░                                                           ░░░  
"""

art_sign_sommarscii="""
                                                                                
                 ░▒▒▒                                           ███  █  ██      
     ▒░░░░░░░░░░░░▒▒▒░░░░░░▒▒░░                          ██  ███ █████████      
     ▒▒▒▒▒▒▒▒▒▒▒▒▒▓▒▒▒▒▒▒▒▒▒▒▒▒▒                       ██▓▓▓█▓█████████▓█       
     ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒                       ██▓▓█▓▓▓▓▓██████         
     ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒                      █████▓▓█▓█▓▓              
     ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒                     █████████▓▒▒▒▒             
     ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒                      ████████████▓▒▒           
     ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒          ▓▓▒▓      █▓▒▓████████▓██▓▒▓          
     ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒            ▓██   ███▓▓▓███▓▓▓▓██▓██▓▓          
     ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒               █▓▓▓███████████▓▓▓▒▒▒            
     ▒▒▒▒▒▒▒▒▒▒▒▒▒▓▒▒▒▒▒▒▒▒▒▒▒▒▒▓              █▓▓▓██████████████▓▓▓▒░░         
      ░          ▒▓▓█                            ▓▓▓▓▓▓▓████████▓▓▓▓▓  ▒▒▒      
                ░▒▒▒▓                           ██▓▓▓▓▓▓▓████████▓▓▓▒▒▓▓        
                 ▒▒▒▓                           █▓▓▓▒▓▓█▓█████▓██████▓▓▓▓       
                 ▒▒▒▓▒                         ███▓▓▓▓    ██████▓▓███▓▓▒▓▓      
             ▒▒▒▒▒▒▒▓▒▒▒                        ██▓▓▓      █▓▓  ▓▓ █████▓▓      
               ░▒▒▒▒▓▒                         █▓█▓▓         ▓       ███▓▓▓     
              ▒▒▒▒▒▒▒▒▒▒                       ██▓▓▓                   █████▓   
             ▒▒▒▒▒▒▒▒▒▒▒                      █▓▓▓█                     ███▓▓   
             ▒▒▒░▒▒▒▒▒▒▒                       ██                         ███   
                                                                                """

art_sign="""
           ░▒▒      ▒▒  
▒▒▒▒▒▒▒▒▒▒▒▒▒▒░▒▒▒▒░▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▓▒▒▒▒▒▒▒▒▒▒▒▒
 ▒        ▓▒▒▓          
          ▒░▒▓          
           ░▒▓          
       ▒ ▒ ░▒▓▒ ▒       
         ▒▒░▒▓▒▒        
      ░▒▒▒▒▒▒▒▒▒▒       
       ▒▒▒▒▓▒▒▒▒▒       
        ▒▒▒▒▒▒▒▒        
                                     """

art_book="""

            ███▓▓▓▓▓▓█       
         ▓██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓  
       ▓█▓█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒
    ▓▓▓█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒
 █▓████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒░ 
██▓█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒░░░▒▒
█▓▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒░░░▒▓▓▒ 
█▓░░░▒▒▒▒▓▓▓▓▓▓▓▓▓▒░░░▒▓▓    
██▒░░▒▒░░░▒▒▒▒▒▒▒░░░▒▓▓      
  █▓▓▒▒▒░░░░░░░░░░▓▓▓        
 ░░░░░▓██▓▒▒░░░▒▓▓▓          
  ░░░     █▓▓▒▒▒▒            """

art_tornado_warrior="""
                                                           
                                             ███ ██████    
                                      ██▓▓██████  ███      
                ░░  ▒▒▓               ██▓▓█▓▓▓██████       
   ▓▓▒▒░░░░░░░░░░░░░░░░ ▓            ████▓▓█▓▓▓▓           
    ▒▒▒░░░░░░░░░░░░░░░░              ██████▓▓▓▒▒▓          
    ▒▒▒░▒▒░░░░░░░░░░░░▒▓   ▓▒        ████████▓█▓▒▒         
    ▓▒▒▒▒░░░░░░░░░░░░▒▒      ▓▓    ██▓▒███▓██▓▓▓█▓▓        
       ▒▒▒▒▒▒▒░░░░░░           ██▓▓████████▓▓▓▓▒           
          ▓▒▒▒░░░░▒▒            █▓▓██▓████▓███▓▓▓▒░        
           ▒▒░░░░░               ▓▓▓▓▓▓▓███▓██▓▓▓▓   ▓     
          ▒▒░░░░                ██▓▓▓▓▓█████▓██▓█▓▓▓▓      
           ▒░░░▒                ██▓▓▓  ▓█████▓▓████▓▓▓     
             ▒▒░░░              ██▓▓▓     █▓ ▓▓▓████▓▓     
                 ▒              █▓▒▓       ▓█     ███▓▓▓▓  
                               ██▓▓▓                ███▓▓  
                               ███                    ███  
                                                           """

art_sommarscii_light="""
               ██     ██                 
              █░▒    █░░████  █  ██      
              ▒░▒██  ▒░ ▒ █████████      
            ▓▒░ ░▒▓▓▒░  ░▒▒▓████▓█       
       █▓░░░░     ░░░░▒▒   ░░▒██         
           █▒░░  ▒▓▓▓▒░ ░▓▓              
              ░ ░████▓░ ▒▒▒▒             
              █░▓█████▓▒███▒▒            
  ▓▓▓▓       ▓▓▓████████▓▓██▓▒▓          
    ███    ██▓▓▓▓██▓▓▓▓▓█▓▓██▓█          
       █▓▓▓███████████▓▓▓▓▒▒▓            
        █▓▓███▓█████▓█████▓▓▒▒░▒         
          ▓▓▓▓▓▓▓███▓████▓▓▓▓▓ ▓▒▒▒      
         █▓▓▓▓▒▓▓█████████▓▓▓▒▒▓▓        
        ███▓▓▓▓█▓▓█████▓█████▓▓▓▓▓       
        ██▓▓▓▓    █████ ▓▓▓███▓▓░▓▓      
        ██▓▓▓       █▓▓ ▓▓▓ ████▓▓▓      
        ▓▓▓▓         █▓       ███▓▓▓     
       ██▓▓▓                    ████▓▓   
      ██▓▓▓                      ███▓▓█  
        █                          ███   
                                         """

art_tornado_warrior_light="""
                                       █     ██              
                                      ▓░█    ░▒██  █████     
                                      ▒ ░▓▓█░ ░████████      
                ░░    ▓           █▓░░  ░░░▒░░ ░░░░▓██       
  ▓▓▒▒░░░░░░░░░░░░░░░░░ ▓         ▒▒▒░   ░▒▓▒░░▒▓▒██         
   ▒▒▒▒░░░░░░░░░░░░░░░░               ▒ ░███▓ ░▒▒▒           
   ▒▒▒░░▒▒░░░░░░░░░░░░▒▒              ▓░█████▓▓██▓▒          
   ▓▒▒▒░░░░░░░░░░░░░░▒▒     ▓▓▓      ▓▒▓███████▓▓█▓▓         
      ▓▒▒▒▒▒▒▒░░░░░░▒          ██ ███▓█▓██▓▓▓▓▓████▓         
        ▓▒▒▒▒▒░░░▒▒▒            ███▓███████████▓▓▒▒▒         
           ▒▒░░░░▒▒               ▓▓▓▓▓▓███▓████▓▓▓▓▒▒▒      
          ▒▒░░░░▓                █▓▓▓▓▒▓▓███████▓▓▒▓▓▓       
          ▒░░░▓                  ██▓▓▓▓█▓██████████▓▓▓▓      
            ░░░░▒                ██▓▓▓    █████▓▓███▓▒▓▓     
              ▓▒░                ██▓▓▓     █▓█  █  ███▓▓     
                                 █▓▒         ▓       ██▒▓▓▓  
                                ██▓▓█                 ███▓▓  
                                ██                      ███  
                                                             """

art_explosion_sommarscii="""
                                                             
                                              ████ █████     
            ▓▓▓                         █▓▓▓██ ████████      
          ▓▓▒▒▒▒▒▒▓▓▓▓                 ██▓▓█▓▓████████       
   ▓▓▒▒▒▒▒▓▒▒▒▒▒▒▒▒▓▓▒▒▒▒▒▓            ████▓▓▓▓██  █         
  ▓▓▒▒▒▒▒▒▓▒▒▒▒░░░▒▒▒▒▒▒▒▒▒▓          ████████▓▒▒▒           
  ▓▓▓▒▒▒▒▓▓▒▒▒▒▒▒▒▒▒▓▒▒▒▒▒▓▓           ██████████▓▒          
  ▓▓▓▓▒▒▒▓▓▓▓▒▒▓▓▓▓▓▓▓▒▒▓▓▓▓ ▓▓▓     █▓▒███████▓▓█▓▒         
   ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓    ██  ██▓▓▓███▓▓▓▓████▓         
     ▓▓▓▒▒▓▓▓▒▒▒▒▒▒▓▓▓▓▓         █▓▓███████████▓▓▒▒▒         
      ▓▓▓▓  ▓▓▒▒▒▓▓ ▓▓▓▓▓▓         ▓▓▓▓▓████████▓▓▓▓▒▒▒      
         ▓▓▓▓▓▒▒▒▓▓▓▓             ▓▓▓▓▒▒▓███████▓▓▒▒▓▓       
          ▓▓▒▓▒▒▓▓▓▓▓             ██▓▓▓█▓█████▓████▓▓▓▓      
         ▓▓▓▓▓▓▒▒▓▓▓▓            ██▓▓▓▓   █████▓▓███▓▒▓▓     
    ▓  ▓▓▒▒▒▓▒▒▒▒▒▒▒▓▓▒▓ ▓▓       ▓▓▓▓     █▓▓  █  ███▓▓     
  ▓▓▓▓▓▒▓▒▒▒▓▒▒▒▒▒▒▒▒▓▒▓▓▓▓      █▓▒▓        ▓      ███▒▓▓▓  
          ▓▓ ▓▓▓▓ ▓▓            ██▓▓█                 ███▓▓  
                                ███                     ███  
                                                             """

art_grey="""
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓"""

art_elf="""    ███████████████████          
    ██              █████        
    ██     ██       ██████       
    ██  ████████    ████████     
    ██  ████████    █████████    
    ██ ████   ███          ██    
    ██  ████████    █      ██    
    ██  ████████ ███████   ██    
    ██          ███  ███   ██    
    ██           ██████    ██    
    ██             ██      ██    
    ██                     ██    
    █████████████████████████    
    █████████████████████████    
    ███████ ███████ █████████    
    ███████ ███████ █████████    
    █████████████████████████    
    █████████████████████████    """

art_summarize_1="""
To get the flag, you must correctly enter six 9-digit positive integers: a, b, c, d, e, and f.

a = 1
b = 2
c = 3
d = 4
e = 5
f = 6
Wrong.
"""

art_ida="""
         ███                         
     █████████████████               
   ████     ██████████████           
  ████         █████████████         
 ████           █████████████████    
  ██████     █     ███████████ ████  
  ██   ██  ██    ███████████████  █  
   ███ ██   ████   █████████████████ 
    █  █          █ ████████████████ 
    █             ██ █ █████████████ 
    ██ █             █████████████   
     █ █████        ████████████     
      █         █  █ █████  ██       
              ██       █████         
         █████        ███████        
          ███   ███      ██          
              █            ███       
           ███            █ ███      
          ███          █     █       
                                     """

art_summarize_2="""
puts("To get the flag, you must correctly enter six 9-digit positive integers: a, b, c, d, e, and f.");
  putchar(10);
  printf("a = ");
  __isoc99_scanf("%d", &v4);
  printf("b = ");
  __isoc99_scanf("%d", &v5);
  printf("c = ");
  __isoc99_scanf("%d", &v6);
  printf("d = ");
  __isoc99_scanf("%d", &v7);
  printf("e = ");
  __isoc99_scanf("%d", &v8);
  printf("f = ");
  __isoc99_scanf("%d", &v9);
  if ( flag_check(v4, v5, v6, v7, v8, v9) )
  {
    puts("Correct.");
    sprintf(s, "uiuctf{%x%x%x%x%x%x}", v4, v5, v6, v7, v8, v9);
    puts(s);
  }
"""

art_summarize_3="""
  if ( a1 <= 100000000 || a2 <= 100000000 || a3 <= 100000000 || a4 <= 100000000 || a5 <= 100000000 || a6 <= 100000000 )
    return 0LL;
  if ( a1 > 999999999 || a2 > 999999999 || a3 > 999999999 || a4 > 999999999 || a5 > 999999999 || a6 > 999999999 )
    return 0LL;
  v7 = twista_min(a1, a2);
  v18 = (unsigned int)twista(v7, a3) % 17492321;
  v19 = (unsigned int)twista(a1, a2) % 17381917;
  v8 = twistb(2LL, a2);
  v9 = twistb(3LL, a1);
  v10 = twista_min(v9, v8);
  v20 = v10 % (unsigned int)twistc(a1, a4);
  v11 = twista(a3, a1);
  v21 = (unsigned int)twistd(a2, v11) % 28194;
  v22 = (unsigned int)twista(a2, a4) % a1;
  v12 = twista(a4, a6);
  v23 = (unsigned int)twistc(a3, v12) % 1893928;
  v24 = (unsigned int)twista_min(a5, a6) % 18294018;
  v25 = (unsigned int)twista(a5, a6) % 48328579;
  return v18 == 4139449
      && v19 == 9166034
      && v20 == 556569677
      && v21 == 12734
      && v22 == 540591164
      && v23 == 1279714
      && v24 == 17026895
      && v25 == 23769303;
"""

art_twista="""
__int64 __fastcall sub_40163D(unsigned int a1, unsigned int a2)
{
  unsigned int v5; // [rsp+10h] [rbp-18h]
  char v6; // [rsp+14h] [rbp-14h]
  int v7; // [rsp+18h] [rbp-10h]
  int v8; // [rsp+1Ch] [rbp-Ch]
  __int64 v9; // [rsp+20h] [rbp-8h]

  v9 = 0LL;
  v5 = 0;
  v6 = 0;
  while ( a1 || a2 )
  {
    v7 = a1 & 1;
    v8 = a2 & 1;
    a1 >>= 1;
    a2 >>= 1;
    v9 += (v5 ^ v8 ^ v7) << v6;
    v5 = v5 & v7 | v8 & v7 | v5 & v8;
    ++v6;
  }
  return ((unsigned __int64)v5 << v6) + v9;
}
"""

art_twista_min="""
__int64 __fastcall sub_4016D8(unsigned int a1, int a2)
{
  return twista(a1, -a2);
}
"""

art_twistb="""
__int64 __fastcall sub_4016FE(unsigned int a1, int a2)
{
  unsigned int v4; // [rsp+Ch] [rbp-Ch]
  int v5; // [rsp+10h] [rbp-8h]

  v4 = 0;
  v5 = 0;
  while ( a1 )
  {
    v4 += (a1 & 1) * (a2 << v5);
    a1 >>= 1;
    ++v5;
  }
  return v4;
}
"""
art_twistc="""
__int64 __fastcall twistc(unsigned int a1, unsigned int a2)
{
  unsigned int v5; // [rsp+8h] [rbp-10h]
  int v6; // [rsp+Ch] [rbp-Ch]
  int v7; // [rsp+10h] [rbp-8h]
  int v8; // [rsp+14h] [rbp-4h]

  v5 = 0;
  v6 = 0;
  while ( a1 || a2 )
  {
    v7 = a1 & 1;
    v8 = a2 & 1;
    a1 >>= 1;
    a2 >>= 1;
    v5 += (v8 ^ v7) << v6++;
  }
  return v5;
}
"""

art_twistd="""
__int64 __fastcall twistd(unsigned int a1, unsigned int a2)
{
  unsigned int v5; // [rsp+8h] [rbp-10h]
  int v6; // [rsp+Ch] [rbp-Ch]
  int v7; // [rsp+10h] [rbp-8h]
  int v8; // [rsp+14h] [rbp-4h]

  v5 = 0;
  v6 = 0;
  while ( a1 || a2 )
  {
    v7 = a1 & 1;
    v8 = a2 & 1;
    a1 >>= 1;
    a2 >>= 1;
    v5 += (v8 & v7) << v6++;
  }
  return v5;
}
"""

art_solver="""
from z3 import *
a1 = BitVec("a1", 32)
a2 = BitVec("a2", 32)
a3 = BitVec("a3", 32)
a4 = BitVec("a4", 32)
a5 = BitVec("a5", 32)
a6 = BitVec("a6", 32)
s = Solver()
s.add(a1 > 100000000, a1 < 999999999, a2 > 100000000, a2 < 999999999, a3 > 100000000, a3 < 999999999, a4 > 100000000, a4 < 999999999, a5 > 100000000, a5 < 999999999, a6 > 100000000, a6 < 999999999)
s.add(((a1 - a2) + a3) % 17492321 == 4139449)   #v18
s.add((a1 + a2) % 17381917 == 9166034) #v19
s.add(((3*a1) - (2*a2)) % (a1^a4) == 556569677) #v20
s.add(((a3 + a1) & a2) % 28194 == 12734) #v21
s.add((a2 + a4) % a1 == 540591164) #v22
s.add(((a4 + a6) ^ a3) % 1893928 == 1279714) #v23
s.add((a5-a6) % 18294018 == 17026895) #v24
s.add((a5 + a6) % 48328579 == 23769303) #v25
s.check()
model = s.model()
print(model)
"""

art_solution="""
[a2 = 780663452,
 a5 = 966221407,
 a4 = 465893239,
 a3 = 341222189,
 a1 = 705965527,
 a6 = 217433792]
"""

art_summarize_output="""
To get the flag, you must correctly enter six 9-digit positive integers: a, b, c, d, e, and f.

a = 705965527
b = 780663452
c = 341222189
d = 465893239
e = 966221407
f = 217433792
Correct.
uiuctf{2a142dd72e87fa9c1456a32d1bc4f77739975e5fcf5c6c0}
"""

def clear_screen():
    if platform.system() == "Windows":
        _ = os.system("cls")
    else:
        _ = os.system("clear")

def type_screen(text):
    for char in text:
        print(char, end="")

def draw_terminal(text="", image=""):
    ### imagery, 40 line
    MAX_IMAGERY = 20
    if image == "":
        for _ in range(MAX_IMAGERY):
            print()
    else:
        height_cursor = 0
        image_height = len(image.split("\n"))
        print(image)
        height_cursor += image_height
        while height_cursor < MAX_IMAGERY:
            print("")
            height_cursor += 1
    ### text, 20 line, 1 top 1 bot, 18 line max
    MAX_TEXT_HEIGHT = HEIGHT-MAX_IMAGERY
    print("="*WIDTH)
    line_cursor = 0
    last_text_cursor = 0
    for i in range(WIDTH-4, len(text), WIDTH-4):
        for j in range(i-WIDTH+4, i):
            print("|", text[i-WIDTH+4:j+1], end=" |\r")
            time.sleep(0.02)
        print()
        line_cursor += 1
        last_text_cursor = i
    for i in range(last_text_cursor, len(text)):
        print("|", text[last_text_cursor:i], " "*((WIDTH-i+1)-4), end="\r")
        time.sleep(0.02)
    print("|", text[last_text_cursor:], " "*((WIDTH-(len(text) - last_text_cursor))-4), end="|")
    print()
    line_cursor += 1
    while line_cursor < MAX_TEXT_HEIGHT:
        print("|", " "*(WIDTH-4), "|")
        line_cursor += 1
    print("="*WIDTH)

def animate_talking(text, imagery="", delay=0):
    clear_screen()
    draw_terminal(text, imagery)
    time.sleep(1)
    if delay == 0:
        input("Press Enter to Continue")
    else:
        time.sleep(delay)

# def music_play():
#     audio_file = os.path.join(os.path.dirname(__file__), 'Longbow.mp3')
#     playsound(audio_file)

def main_menu():
    clear_screen()
    title_text = """

_________          _______    _______  ______            _______  _       _________          _______  _______ 
\\__   __/|\\     /|(  ____ \\  (  ___  )(  __  \\ |\\     /|(  ____ \\( (    /|\\__   __/|\\     /|(  ____ )(  ____ \\
   ) (   | )   ( || (    \\/  | (   ) || (  \\  )| )   ( || (    \/|  \  ( |   ) (   | )   ( || (    )|| (    \\/
   | |   | (___) || (__      | (___) || |   ) || |   | || (__    |   \\ | |   | |   | |   | || (____)|| (__    
   | |   |  ___  ||  __)     |  ___  || |   | |( (   ) )|  __)   | (\\ \\) |   | |   | |   | ||     __)|  __)   
   | |   | (   ) || (        | (   ) || |   ) | \\ \\_/ / | (      | | \\   |   | |   | |   | || (\\ (   | (      
   | |   | )   ( || (____/\\  | )   ( || (__/  )  \\   /  | (____/\| )  \\  |   | |   | (___) || ) \\ \\__| (____/\\
   )_(   |/     \\|(_______/  |/     \\|(______/    \\_/   (_______/|/    )_)   )_(   (_______)|/   \\__/(_______/
                                                                                                              
 _______  _______    _______  _______  _______  _______  _______  _______  _______  _______ __________________
(  ___  )(  ____ \  (  ____ \\(  ___  )(       )(       )(  ___  )(  ____ )(  ____ \\(  ____ \\\\__   __/\\__   __/
| (   ) || (    \\/  | (    \\/| (   ) || () () || () () || (   ) || (    )|| (    \\/| (    \\/   ) (      ) (   
| |   | || (__      | (_____ | |   | || || || || || || || (___) || (____)|| (_____ | |         | |      | |   
| |   | ||  __)     (_____  )| |   | || |(_)| || |(_)| ||  ___  ||     __)(_____  )| |         | |      | |   
| |   | || (              ) || |   | || |   | || |   | || (   ) || (\\ (         ) || |         | |      | |   
| (___) || )        /\\____) || (___) || )   ( || )   ( || )   ( || ) \\ \__/\____) || (____/\___) (______) (___
(_______)|/         \\_______)(_______)|/     \\||/     \\||/     \\||/   \\__/\\_______)(_______/\\_______/\\_______/

A terminal writeup wrapped with a story.
    """
    print(title_text)
    choices = """
(1) Start
(2) About
(3) The actual writeup
(4) Flag (real one, not a pwn challenge) (WARNING: CONTAINS STORY SPOILER)",
(5) License
(9) Exit
"""
    return input(choices)

def story():
    animate_talking("Once upon a time, there's a village called Uiuvilla. The village was filled with brave and strong warriors. One of them, is Sommarscii. (editor:        portmanteau between Summarize, the challenge, and Ascii - this writeup)", imagery=art_village_background)
    animate_talking("Sommarscii is the child from the late King Forsics and Queen Blute. He was  expected to be the next sitting on the throne, but everyone don't think he  will. \"Huh, it's already afternoon. I think I will hone my Pala. It's been a while since it got maintained.\"",imagery=art_sommarscii)
    animate_talking("He was scammed by the owner thinking that it's a strong sword. It was a low quality copper sword sold by Nasir, a copper seller.", imagery=art_sommarscii_sword)
    animate_talking("Actually, the author thinks that Sommarscii is so bad at Calling the Fight  (editor: CTF) that he was secluded from the rest of the villagers, that are strong and brave warriors.", imagery=art_sommarscii_sword)
    animate_talking("One day, a big dark storm approaching the Uiuvilla.", imagery=art_tornado)
    animate_talking("Everyone is scared. \"It's the foretold apocalypse! It's the big Revengin    (editor: it was a portmanteau for reverse and engineering) tornado! It's the end of the world! Everyone start panicking!!!\"", imagery=art_village_background_tornado)
    animate_talking("\"Why is everyone running?\", Sommarscii asked himself. He did not realize    that the storm is already near. The tornado threw out a wooden sign, hitting Sommarscii on his left knee. \"OW WHO'S THAT??!\"", imagery=art_sign_sommarscii)
    animate_talking("The sign, written on it, \"I'm Summariz, the son of Revengi. Answer me the 6 numbers of The Conundrum of Perpetuity(tm), before I make your race         disappear from the Terrestrial. You have 2 days. Here is the file:\"", imagery=art_sign)
    animate_talking("7F 45 4C 46 02 01 01 00 00 00 00 00 00 00 00 00 02 00 3E 00 01 00 00 00 F0 10 40 00 00 00 00 00 40 00 00 00 00 00 00 00 98 31 00 00 00 00 00 00 00 00 00 00 40 00 38 00 0D 00 40 00 1D 00 1C 00... (editor: it was cut due to       budgeting)", imagery=art_sign)
    animate_talking("\"Oh. AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA (core dumped)\". Sommarscii then ran to the local wizard to ask for help.", imagery=art_sommarscii)
    animate_talking("\"Bro you gotta see this. There was a big whoosh whoosh outside, it's big,   black, and bad. Everyone is running and scattered across the village. They  are afraid that that thing will destroy us all. Please.. sorry what's your  name?\"",imagery=art_wizard_sommarscii)
    animate_talking("Pondering his orb, (editor: crystal ball, no implication here), he answered faintly. \"I'm, *cough cough*, sorry I got some flu. I'm Ryuk, I'm the local contributor for the Heroes Cider Shaman community. What do you want to know?", imagery=art_wizard_sommarscii)
    animate_talking("\"The thing, I think it's called Surstromming or whatever, asked about the 6 numbers of The Conan Drum of Perpetrator or something.\"", imagery=art_wizard_sommarscii)
    animate_talking("\"WHAT??!\", shout the wizard. \"YOU SAID THE CONUNDRUM OF PERPETUITY??\"       (editor: he's actually old and have lost 90% of his hearing, it was misheard)", imagery=art_wizard_sommarscii)
    animate_talking("\"Right, that one. Do you know about it?\"", imagery=art_wizard_sommarscii)
    animate_talking("\"I haven't heard that since the last eclipse. Do you have the file?\"", imagery=art_wizard_sommarscii)
    animate_talking("\"Yes, this thing.\" Sommarscii put the wooden sign on the table.", imagery=art_wizard_sommarscii)
    animate_talking("After looking at the file, Ryuk started to use his Inner Dismantler Aura    (editor: it's IDA) to read the file.", imagery=art_wizard_sommarscii)
    animate_talking("\"Right, right.. I'm starting to understand this...\", Ryuk started to shiver.", imagery=art_wizard_sommarscii)
    animate_talking("\"Oh dear, this is the ancient language of the Obfus Kator race. (editor: you already know what it is)", imagery=art_wizard_sommarscii)
    animate_talking("\"I need to find the dictionary for this... can you read take that green book and read the translation for me?\"", imagery=art_wizard_sommarscii)
    animate_talking("\"Ok?\". Sommarscii was a little bit confused since he had colorblindness. He eventually read a text \'obfuscator\' on the side of a book.", imagery=art_book)
    animate_talking("\"Okay, I'll read one and you find the meaning.\", Ryuk told Sommarscii.", imagery=art_wizard_sommarscii)
    animate_talking("\"sub_40163D(unsigned int a1, unsigned int a2)?\", ask Ryuk.", imagery=art_wizard_sommarscii)
    animate_talking("\"This... is... \'addition?\'\"", imagery=art_wizard_sommarscii)
    animate_talking("\"Okay. sub_4016D8(unsigned int a1, int a2)?\"", imagery=art_wizard_sommarscii)
    animate_talking("\"It said it's the reverse of addition! What kind of sorcery is this??\"", imagery=art_wizard_sommarscii)
    animate_talking("\"This is what Revengi speaks daily. You need to understand... One day you'll learn about Asmebily. (editor: haven't been paid by the author, no         explanation). sub_4016FE(unsigned int a1, int a2)?\"", imagery=art_wizard_sommarscii)
    animate_talking("\"Multiplication.\"", imagery=art_wizard_sommarscii)
    animate_talking("\"sub_40174A(unsigned int a1, unsigned int a2)?\"", imagery=art_wizard_sommarscii)
    animate_talking("\"I can't read this... hor?\", Sommarscii confused.", imagery=art_wizard_sommarscii)
    animate_talking("\"It's called xor. sub_4017A9(unsigned int a1, unsigned int a2)?\"", imagery=art_wizard_sommarscii)
    animate_talking("\"What a weird way to say \'and\'. You could just say it's 'and' you know.\"", imagery=art_wizard_sommarscii)
    animate_talking("\"It's not just 'and'... it's a bit-wise and. Alright, so far so good, we    just need to solve this equation.\"", imagery=art_wizard_sommarscii)
    animate_talking("\"Ah, I haven't studied yet. My cat vomited on the carpet yesterday.\"", imagery=art_sommarscii)
    animate_talking("\"...\"", imagery=art_wizard)
    animate_talking("\"...\"", imagery=art_sommarscii)
    animate_talking("\"Anyway, how can we solve it?\"", imagery=art_sommarscii)
    animate_talking("\"Well, we can use something called Zeethree.\" (author: sorry the editor     left, he gave me the invoice. anyway it's z3). \"It's supposed to be cast     directly to this sign to reveal the answer. But I'm too old for this, it   needs energy. My Inner Dismantler Aura is too weak...\"", imagery=art_wizard_sommarscii)
    animate_talking("\"I think I can do that. I haven't used my brain for a really long time.\",   Sommarscii said jokingly.", imagery=art_wizard_sommarscii)
    animate_talking("He actually used his brain 100% this time. His head is shining bright and   then he learned the very basic of Zeethree", imagery=art_sommarscii)
    animate_talking("\"Alright, let's do this.\"", imagery=art_sommarscii)
    animate_talking("The day has come. It's the Judgement Day.", imagery=art_tornado_warrior)
    animate_talking("\"Oh you actually came.\", the coarse sound from the Summariz. \"It's been a   while since a Hero brave enough to fight me.\"", imagery=art_tornado_warrior)
    animate_talking("\"...\" Sommarscii stayed silent.", imagery=art_tornado_warrior)
    animate_talking("\"Oh boy what is this? A silent treatment? Ahahahah...\"", imagery=art_tornado_warrior)
    animate_talking("\"s.add(a1 > 100000000, a1 < 999999999, a2 > 100000000, a2 < 999999999, a3 > 100000000, a3 < 999999999, a4 > 100000000, a4 < 999999999,  a5 > 100000000, a5 < 999999999, a6 > 100000000, a6 < 999999999)\"", imagery=art_sommarscii)
    animate_talking("\"...What?\"", imagery=art_tornado)
    animate_talking("\"s.add(((a1 - a2) + a3) % 17492321 == 4139449)\"", imagery=art_sommarscii)
    animate_talking("\"s.add((a1 + a2) % 17381917 == 9166034)\"", imagery=art_tornado_warrior)
    animate_talking("\"WAIT!!! DON'T TELL ME YOU LEARNED THE ZEETHREE MANTRA???!\", Summariz was   surprised with his knowledge.", imagery=art_tornado)
    animate_talking("\"s.add(((3*a1) - (2*a2)) % (a1^a4) == 556569677);s.add(((a3 + a1) & a2) % 28194 == 12734);\", Sommarscii started to levitate from the ground. His eyes   opened and showed a total white light that's blinding.", imagery=art_sommarscii)
    animate_talking("\"s.add((a2 + a4) % a1 == 540591164);s.add(((a4 + a6) ^ a3) % 1893928 == 1279714);\"", imagery=art_sommarscii_light)
    animate_talking("\"NO! PLEASE! STOP! I WASN'T READY FOR THIS! I HAVEN'T STUDIED YET, I THOUGHT YOU WERE BOGUS.\", Summariz started to panic.", imagery=art_tornado)
    animate_talking("\"s.add((a5-a6) % 18294018 == 17026895);s.add((a5 + a6) % 48328579 == 23769303)\"", imagery=art_tornado_warrior)
    animate_talking("\"s.check()\"",imagery=art_tornado_warrior_light)
    animate_talking("\"...\"", imagery=art_tornado_warrior_light, delay=3)
    animate_talking("\"[a2 = 780663452, a5 = 966221407, a4 = 465893239, a3 = 341222189, a1 = 705965527, a6 = 217433792]\"", imagery=art_tornado_warrior_light)
    animate_talking("\"...\"", imagery=art_tornado_warrior, delay=3)
    animate_talking("\"哀れだ。\"",imagery=art_tornado_warrior, delay=5)
    animate_talking("", delay=0.5)
    animate_talking("", imagery=art_grey,delay=0.5)
    animate_talking("", delay=0.5)
    animate_talking("", imagery=art_grey, delay=0.5)
    animate_talking("\"...\"",imagery=art_explosion_sommarscii, delay=10)
    animate_talking("\"I guess that's it.\", Sommarscii kneeled on the ground. He closed his eyes, thinking about the future, the universe, the linear algebra that he can     solve.", imagery=art_sommarscii)
    animate_talking("\"I should get back to Ryuk.\" He limped back to the shack that Ryuk lived.", imagery=art_village_warrior)
    animate_talking("Ryuk was in awe. He never seen such monstrosity, just standing in front of  him. \"So, did you get your answer?\", Ryuk asked.",imagery=art_wizard_sommarscii)
    animate_talking("\"I think so. It's uiuctf{2a142dd72e87fa9c1456a32d1bc4f77739975e5fcf5c6c0}. I hope that's gonna be the last time I use Zeethree. It was daunting.\"       (author: it's not gonna be the last time, let's be real here)", imagery=art_wizard_sommarscii)
    animate_talking(" ________         ____        _____                                         /_  __/ /  ___   / __/__  ___/ /__ \\                                         / / / _ \\/ -_) / _// _ \\/ _  / /__/                                        /_/ /_//_/\\__/ /___/_//_/\\_,_/ (_)                                      ")

def writeup():
    animate_talking("The file was an ELF file, shown in the `file` command ran against it.", imagery=art_elf)
    animate_talking("If we run it, it will ask 6 numbers, and will say that it's right or wrong.", imagery=art_summarize_1)
    animate_talking("Because this is a reverse engineering challenge, we can just run it through disassembler like IDA or Ghidra. I only have IDA so I ran it through it.", imagery=art_ida)
    animate_talking("After running through IDA, we go to the main function and see that the code is actually fairly simple.", imagery=art_summarize_2)
    animate_talking("It actually asks for 6 numbers and it will run through a checking function  before returning the flag as hex. (I renamed the function flag_check() to   ease the reading.)", imagery=art_summarize_2)
    animate_talking("(I renamed many of the functions) Checking flag_check() (or sub_40137B()),  it will show that these 6 numbers will be used as an input for function,    which in the end the result will be compared with several integers.", imagery=art_summarize_3)
    animate_talking("I renamed the function sub_40163D as \"twista\", sub_4016D8 as \"twista_min\" as it was the negative of twista, sub_4016FE as \"twistb\", sub_40174A as       \"twistc\", and sub_4017A9 as \"twistd\".", imagery=art_summarize_3)
    animate_talking("Checking out each \"twist\" function will give us some convoluted computation before returning a value. That's why it's named \'twist\'.", imagery=art_twista)
    animate_talking("I know that this is some function, that's using 2 input for 1 output, this  is linear algebraic thing. I thought about using z3 solver, but when I      learned about it, I didn't know how to convert these twists to z3 format to  solve.", imagery=art_twista)
    animate_talking("I was stuck for a while, that I asked one of my good friend in HCS, let's   call him Ryuk (that didn't participate this CTF due to work), about how to  reverse a calculation algorithm that also have a loop.", imagery=art_twista)
    animate_talking("\"Can I see the code?\", he said. I showed him twistc. \"Oh this is just an    XOR. Try inputting two numbers to the function and compare it with a normal XOR.\" Wtf, he's right. It's just a normal calculation. So based on that     alone, I worked the rest and to... summarize(tm)... the function means as   follows:", imagery=art_twistc)
    animate_talking("This is addition. So it's just a1+a2.", imagery=art_twista)
    animate_talking("This is subtraction. It's a1+(-a2).", imagery=art_twista_min)
    animate_talking("This is multiplication. a1*a2", imagery=art_twistb)
    animate_talking("This is XOR. So it's a1^a2", imagery=art_twistc)
    animate_talking("This is bit-wise AND, a1 & a2.", imagery=art_twistd)
    animate_talking("So with that in mind, I worked to simplify the equation from this:", imagery=art_summarize_3)
    animate_talking("...to a python script to solve with z3:", imagery=art_solver)
    animate_talking("Run the script and the solution will show on the output. a1 is a, a2 is b, a3 is c, a4 is d, a5 is e, a6 is f.", imagery=art_solution)
    animate_talking("We can then input the corresponding variable to find the flag.", imagery=art_summarize_output)
    animate_talking(" ________         ____        _____                                         /_  __/ /  ___   / __/__  ___/ /__ \\                                         / / / _ \\/ -_) / _// _ \\/ _  / /__/                                        /_/ /_//_/\\__/ /___/_//_/\\_,_/ (_)                                      ")


if __name__ == "__main__":
    
    
    while True:
        try:
          choice = main_menu()
          if choice == "1":
              story()
          if choice == "2":
              #clear_screen()
              txt = "this writeup was made by spitfirerxf, because he's bored and can't really   solve anything other than forensics. This ctf has lack of it so he solved   one reverse engineering and decided to make this. don't ask why, he's       sensitive about it. also you can start plainly, but he attached a song with this program. for better experience play the song in the background before  proceeding. he didn't want to make you pip things other than plain python3  before playing this writeup."         
              animate_talking(txt)
          if choice == "3":
              writeup()
          if choice == "4":
              #clear_screen()
              txt = "uiuctf{2a142dd72e87fa9c1456a32d1bc4f77739975e5fcf5c6c0}"
              animate_talking(txt)
          if choice == "5":
              txt = "do whatever you want with it. dont forget to like and subscribe"
              animate_talking(txt)
          if choice == "9":
              clear_screen()
              break
        except KeyboardInterrupt:
            clear_screen()
            break