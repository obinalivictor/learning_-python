
   
   do{
    String mainMenu = """
   
  welcome to nokia 3310 
   press 1 for phonebook        
  press 2 for messages        
  press 3 for chat       
  press 4 for call register       
  press 5 for tones      
  press 6 for settings      
  press 7 for call divert      
  press 8 for games       
  press 9 for calculator       
  press 10 for reminders       
  press 11 for clock       
  press 12 for profiles       
  press 13 for sim services     
  press 0 for Exit  
          
   """;
                     
     System.out.println(mainMenu) ;  
              mainMenuChoice = input.nextInt();
   
                               switch(mainMenuChoice){
                          
                  case 1:      System.out.println("phonebook");
                  
                           int phonebookmenuchoice;
                  
                        do{
                        
                       String phonebookmenu = """
   
  
           
 press 1 for search        
 press 2 for  service nos        
 press 3 for  add name        
 press 4 for  erase
 press 5 for  edit        
 press 6 for  assign tone        
 press 7 for  send b'cord        
 press 8 for   options  
 press 9 for  speed dials   
 press 10 for  voice type   
     
   """; 
  
                       System.out.println(phonebookmenu);
  
               phonebookmenuchoice = input.nextInt();
                      switch(phonebookmenuchoice){
   
                   case 1:System.out.println("what do you want to search for");break;
                   case 2:System.out.println("what number");break;
                   case 3:System.out.println("enter name");break;
                   case 4:System.out.println("doyou want to delete");break;
                   case 5:System.out.println("edir");break;
                   case 6:System.out.println("choose ring tone");break;
                   case 7:System.out.println("who do you want to send a card to");break;
                   case 8:System.out.println("optionmenu");
   
                                 int optionmenuchoice;
                                  do{
                                   
                                  String optionmenu = """
   
   
  press 1 to type of view 
  press 2 to memory status 
   """;
                              System.out.println(optionmenu);                 
                      
                            optionmenuchoice = input.nextInt();
   
                               switch(optionmenuchoice){
                         case 1:System.out.println("type of view");break;
                         case 2:System.out.println("memory status");break;
                         default:System.out.println("invalid input");break;
                     }
                     
                     }while(optionmenuchoice != 0);
                      break;
                              case 9:System.out.println("speed dial");break;
                              case 10:System.out.println("voice type");break;
                         
                         }
                           //break;
                           
                               }while(phonebookmenuchoice != 0);
                               
   				break;
   				
                            case 2:System.out.println("messages");
                            
                                     int messagemenuchoice;
                                    do{
                            
                               String messagemenu = """
   
   
 press 1 for write messages        
 press 2 for  inbox       
 press 3 for  outbox       
 press 4 for  picture messages
 press 5 for  templates       
 press 6 for  smileys       
 press 7 for  message settings        
 press 8 for   info service  
 press 9 for  voice mailbox number   
 press 10 for  service command editor   
     
   """; 
       
     	                                    System.out.println(messagemenu);
                                    messagemenuchoice = input.nextInt();
                                     switch(messagemenuchoice){
  
                                     case 1:System.out.println("start typing");break;   
                                                                             		
                                    case 2:System.out.println("inbox");break;                                            
                                    case 3:System.out.println("received messages");break;
                                    case 4:System.out.println("picture messages");break;
                                    case 5:System.out.println("templates");break;
                                    case 6:System.out.println("smileys");break;
                                    case 7:System.out.println("messages settings");
                                         int messagessettingschoice;
                                           do{
                                           
                                          String messagessettings =  """
                                          
                                          
      press 1 for set1                                    
      press 2 for common3                                    
          """;       
                                      System.out.println(messagessettings);    
                                      messagessettingschoice = input.nextInt();
                                          
                                         switch(messagessettingschoice){
                                       case 1:System.out.println("set1");
                                             
                                             int  set1choice;
                                        
                                        do{
                                         String set1 = """
                                          
   press 1 for message centre number                  
  press 2 for messages sent as                  
  press 3 for message validity                  
                    
   """;                         
                                        
                                      System.out.println(set1);    
                                       set1choice = input.nextInt();      
                                          switch(set1choice){
                                          case 1:System.out.println("message centre number");break;
                                          case 2:System.out.println("message sent as");break;
                                          case 3:System.out.println("message validity");break;
                                          default:System.out.println("invalid input");break;
                                       } 
                                       
                                      } while(set1choice != 0);
                                       break; 
                                       
                                       case 2:System.out.println("common3"); 
                                       
                                        int common3choice;
                                            do{
                                          String common3 = """
                                          
                             
  press 1 for delivery reports
   press 2 for reply via same centre
   press 3 for character support
   
   """;                                    
                                        System.out.println(common3);  
                                          common3choice = input.nextInt(); 
                                          switch(common3choice){
                                          case 1:System.out.println("delivery reports");break;
                                          case 2:System.out.println("reply via same centre");break;
                                          case 3:System.out.println("charactetr support");break;
                                          default:System.out.println("invalid input");break;
                                         }
                                         
                                         }  while(common3choice != 0);
                                         break;
                                         }
                                       }  while(messagessettingschoice != 0);
                                         break;
                                  
                                         case 8:System.out.println("info service");break;
                                         case 9:System.out.println("voice mailbox number");break;
                                         case 10:System.out.println("service command editor");break;
                                       
                                      }   
                                      
                                       
                                     }  while(messagemenuchoice != 0);
                                       
                                       break;
   
   
                                     case 3:System.out.println("chat");
                                       String chat = "chat";
                                       
                                       System.out.println(chat);
                                     
                                     break;
   
   
                                     case 4:System.out.println("call register");
                                     
                                     int callregistermenuchoice;
                                       do{
                                     String callregistermenu = """
                                     
  press 1 for missed calls 
  press 2 for received calls 
  press 3 for dialled calls 
  press 4 for erase recent call lists 
  press 5 for show call duration 
  press 6 for show call costs 
  press 7 for call cost settings                                   
  press 8 for prepaid credit                                   
                                     
     """;                    
     
                             System.out.println(callregistermenu);
                         callregistermenuchoice = input.nextInt();
                          switch(callregistermenuchoice){
                           case 1:System.out.println("missed calls");break;
                           case 2:System.out.println("received calls");break;
                           case 3:System.out.println("dialled calls");break;
                            case 4:System.out.println("erase recent call lists");break;
                            case 5:System.out.println("show call duration");
                               
                                int showcalldurationmenuchoice;
                                  do{
                            
                            String showcalldurationmenu = """
  
   press 1 for last call duration
   press 2 for all calls duration
   press 3 for received call duration                        
   press 4 for   dialled calls duration                      
   press 5 for clear timers
        """;                                    
                                 System.out.println(showcalldurationmenu);
                                showcalldurationmenuchoice =input.nextInt();  
                                 switch(showcalldurationmenuchoice){
                                 case 1:System.out.println("25 min");break;
                                 case 2:System.out.println("34 min");break;
                                 case 3:System.out.println("4min");break;
                                 case 4:System.out.println("5 min");break;
                                 case 5:System.out.println(" cear");break;
                                 default:System.out.println("invalid input");break;
                             }
                             
                             }while(showcalldurationmenuchoice != 0);
                             
                            break;
                            
                            case 6:System.out.println("show call costs");
                            
                            int showcallcostmenuchoice;
                               do
                               {
                            String showcallcostmenu = """
                            
 press 1 for last call cost                           
  press 2 for all calls cost                         
  press 3 for clear counters                          
       """;                     
                                System.out.println(showcallcostmenu);
                                 showcallcostmenuchoice = input.nextInt();
                            switch(showcallcostmenuchoice){
                             case 1:System.out.println("2300");break;
                            case 2:System.out.println("500");break;
                            case 3:System.out.println("clear");break;
                             default:System.out.println("invalid input");break;
                            }
                            
                            }while(showcallcostmenuchoice != 0);
                            
                            break;
                             case 7:System.out.println("call cost settings");
                             
                             int callcostsettingsmenuchoice;
                             
                                 do{
                               String callcostsettingsmenu = """
                               
    press 1 for call cost limit                           
    press 2 for show costs in                         
           """;                  
                             System.out.println(callcostsettingsmenu);
                               callcostsettingsmenuchoice = input.nextInt();
                               switch(callcostsettingsmenuchoice){
                                case 1:System.out.println("34");break;
                                case 2:System.out.println("show cost in");break;
                                 default:System.out.println("invalid input");break;
                        } 
                        }while( callcostsettingsmenuchoice != 0);
                                          
                             break;
                             case 8:System.out.println("prepaid credit");break;
                             
                                   } 
                                   // break;
                                   }while(callregistermenuchoice != 0);
                                   break;
   
                          
                          
                          
                          
                          
                          case 5:System.out.println("tones menu");
                          
                          int tonesmenuchoice;
                          do
                          {
                          String tonesmenu = """
                          
   press 1 for  ringing tone                      
    press 2 for  ringing volume                      
    press 3 for  incoming call alert                      
     press 4 for composer                      
     press 5 for message alert tune                       
    press 6 for   keypad tones                     
     press 7 for  warning and game tones                     
      press 8 for vibrating alerts                     
        press 9 for screen saver                   
                          
       """;                   
                                 System.out.println(tonesmenu);
                          tonesmenuchoice = input.nextInt();
                          switch(tonesmenuchoice){
                          case 1:System.out.println("ringing tone");break;
                          case 2:System.out.println("ringing volume");break;
                          case 3:System.out.println("incoming call alert");break;
                          case 4:System.out.println("composer");break;
                          case 5:System.out.println("message alert tune");break;
                          case 6:System.out.println("keypad tones");break;
                          case 7:System.out.println("warning and game tones");break;
                          case 8:System.out.println("vibrating alerts");break;
                          case 9:System.out.println("screen saver");break;
                          default:System.out.println("invalid input");break;
                         }
                         
                         }while(tonesmenuchoice != 0);
                           break;
                         
                         case 6:System.out.println("settingsmenu");
                         
                         int settingsmenuchoice;
                             do{
                         
                           String settingsmenu ="""
                         
  press 1 for call settings                       
  press 2 for phone settings                       
  press 3 for security settings                       
  press 4 for restore factory settings                       
                         
         """;                
                                         System.out.println(settingsmenu);            
                                    settingsmenuchoice = input.nextInt();
                                     switch(settingsmenuchoice){
                                      case 1:System.out.println("search contacts");
                                      
                                        int callsettingsmenuchoice;
                                      
                                               do{                                    
                                        String callsettingsmenu= """
                                      
 press 1 for  automatic redial                                  
  press 2 for speed dialing                                    
  press 3 for  call waiting options                                   
 press 4 for   own number sending                                  
 press 5 for   phone line in use                                  
 press 6 for   automatic answer                                  
       """;                                          
                                      
                                      System.out.println(callsettingsmenu);
                                     callsettingsmenuchoice = input.nextInt();  
                                        switch(callsettingsmenuchoice){
                                        case 1:System.out.println("redial");break;
                                         case 2:System.out.println("go shead");break;                                   
                                         case 3:System.out.println("call options");break;
                                        case 4:System.out.println("send number");break;
                                        case 5:System.out.println("phone line in use");break;
                                        case 6:System.out.println("proceed");break; 
                                      default:System.out.println("invalid input");break;
                                      
                                      }
                                      }while(callsettingsmenuchoice != 0);
                                      
                                      break;
                                      
                                       case 2:System.out.println("phone settings");
                                           
                                           int phonesettingsmenuchoice;
                                            do{
                                            String phonesettingsmenu = """
    
    press 1 for language
    press 2 for cell info display
    press 3 for welcome note
    press 4 for  network selection                       
     press 5 for lights
     press 6 for confirm sim service actions
                                       
        """;
                                   System.out.println(phonesettingsmenu);
                                 phonesettingsmenuchoice = input.nextInt();
                                    switch(phonesettingsmenuchoice){
                                       case 1:System.out.println("select language");break;
                                       case 2:System.out.println("display");break;
                                       case 3:System.out.println("whello");break;
                                       case 4:System.out.println("choose a network");break;
                                        case 5:System.out.println("nights and eyecare");break;
                                        case 6:System.out.println("network percent");break;
                                        default:System.out.println("invalid input");break;
                             
                                      }
                                        }while(phonesettingsmenuchoice != 0);
                                       break;
                                       
                                       case 3:System.out.println("security settings");
                                       
                                       int securitysettingsmenuchoice;
                                       
                                            do{
                                            
                                          String securitysettingsmenu = """
                                       
   press 1 for pin code request                                   
   press 2 for call barring service
   press 3 for fixed dialling
   press 4 for closed user group
   press 5 for phone security
    press 6 for change access codes
     """;
                                  System.out.println(securitysettingsmenu);
                                       securitysettingsmenuchoice = input.nextInt();    
                                        switch(securitysettingsmenuchoice){
                                        case 1:System.out.println("enter code");break;
                                          case 2:System.out.println("bar the call");break;
                                          case 3:System.out.println("fixed dialling");break;
                                          case 4:System.out.println("closed user group");break;
                                            case 5:System.out.println("enter password");break;
                                             case 6:System.out.println(" codes change");break;
                                             default:System.out.println("invalid input");break;
                                             }
                                             
                                             }while(securitysettingsmenuchoice != 0);
                                             
                                       break;
                                       
                                       case 4:System.out.println("erase data");break;
                                    }
                                    }while(settingsmenuchoice != 0);
                                    
                                     break;
                         
                         
                         case 7: System.out.println("call divert");break;
                         
                         
                         case 8:System.out.println("games");break;
                          
                          case 9:System.out.println("calculator");break;
                          
                          case 10:System.out.println("reminders");break;
                          
                          case 11:System.out.println("clock");
                          
                            int clockmenuchoice;
                          
                                  do{
                              String clockmenu = """
                          
  press 1 for  alarm clock                      
   press 2 for clock settings                      
  press 3 for   date setting                     
   press 4 for  stopwatch                     
  press 5 for   countdown timer    
  press 6 for auto update of date and time
  
                   """;
                                                             System.out.println(clockmenu);
                                                               clockmenuchoice = input.nextInt();
                                                             switch(clockmenuchoice){
                                                             case 1:System.out.println("set till 2:30");break;
                                                             case 2:System.out.println("settings");break;
                                                             case 3:System.out.println("date setting");break;
                                                             case 4:System.out.println("stopwatch");break;
                                                             case 5:System.out.println("countdown timer");break;
                                                             case 6:System.out.println("network updated time");break;
                                                             default:System.out.println("invalid input");break;
                                                        }     
                                                           
                                                           }while(clockmenuchoice != 0);  
                                                         break;
                          
                                             case 12:System.out.println("profiles");break;
                          
                                case 13:System.out.println("sim services");break;
                               //case 0:System.out.println(mainMenu);break;
                               }
                               
   }while(mainMenuChoice != 0);
       }
   }
