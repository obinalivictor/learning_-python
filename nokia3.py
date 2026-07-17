while True:
 
    main_menu = """
Welcome to Nokia 3310
 
Press 1 for Phonebook
Press 2 for Messages
Press 3 for Chat
Press 4 for Call Register
Press 5 for Tones
Press 6 for Settings
Press 7 for Call Divert
Press 8 for Games
Press 9 for Calculator
Press 10 for Reminders
Press 11 for Clock
Press 12 for Profiles
Press 13 for SIM Services
Press 0 to Exit
"""
 
    print(main_menu)
 
    main_menu_choice = int(input("Enter your choice: "))
 
    match main_menu_choice:
 
        case 1:
 
            while True:
 
                phonebook_menu = """
Press 1 for Search
Press 2 for Service Nos
Press 3 for Add Name
Press 4 for Erase
Press 5 for Edit
Press 6 for Assign Tone
Press 7 for Send B'Card
Press 8 for Options
Press 9 for Speed Dials
Press 10 for Voice Tags
Press 0 to Go Back
"""
 
                print(phonebook_menu)
 
                phonebook_choice = int(input("Enter your choice: "))
 
                match phonebook_choice:
 
                    case 1:
                        print("What do you want to search for?")
 
                    case 2:
                        print("What number?")
 
                    case 3:
                        print("Enter name")
 
                    case 4:
                        print("Do you want to delete?")
 
                    case 5:
                        print("Edit")
 
                    case 6:
                        print("Choose ring tone")
 
                    case 7:
                        print("Who do you want to send a card to?")
 
                    case 8:
 
                        while True:
 
                            options_menu = """
Press 1 for Type of View
Press 2 for Memory Status
Press 0 to Go Back
"""
 
                            print(options_menu)
 
                            option_choice = int(input("Enter your choice: "))
 
                            match option_choice:
 
                                case 1:
                                    print("Type of View")
 
                                case 2:
                                    print("Memory Status")
 
                                case 0:
                                    break
 
                                case _:
                                    print("Invalid input")
 
                    case 9:
                        print("Speed Dial")
 
                    case 10:
                        print("Voice Tags")
 
                    case 0:
                        break
 
                    case _:
                        print("Invalid input")
 
        case 2:
 
            while True:
 
                message_menu = """
Press 1 for Write Messages
Press 2 for Inbox
Press 3 for Outbox
Press 4 for Picture Messages
Press 5 for Templates
Press 6 for Smileys
Press 7 for Message Settings
Press 8 for Info Service
Press 9 for Voice Mailbox Number
Press 10 for Service Command Editor
Press 0 to Go Back
"""
 
                print(message_menu)
 
                message_choice = int(input("Enter your choice: "))
 
                match message_choice:
 
                    case 1:
                        print("Start typing")
 
                    case 2:
                        print("Inbox")
 
                    case 3:
                        print("Received Messages")
 
                    case 4:
                        print("Picture Messages")
 
                    case 5:
                        print("Templates")
 
                    case 6:
                        print("Smileys")
 
                    case 7:
 
                        while True:
 
                            message_settings = """
Press 1 for Set 1
Press 2 for Common
Press 0 to Go Back
"""
 
                            print(message_settings)
 
                            settings_choice = int(input("Enter your choice: "))
 
                            match settings_choice:
 
                                case 1:
 
                                    while True:
 
                                        set1_menu = """
Press 1 for Message Centre Number
Press 2 for Messages Sent As
Press 3 for Message Validity
Press 0 to Go Back
"""
 
                                        print(set1_menu)
 
                                        set1_choice = int(input("Enter your choice: "))
 
                                        match set1_choice:
 
                                            case 1:
                                                print("Message Centre Number")
 
                                            case 2:
                                                print("Messages Sent As")
 
                                            case 3:
                                                print("Message Validity")
 
                                            case 0:
                                                break
 
                                            case _:
                                                print("Invalid input")
 
                                case 2:
 
                                    while True:
 
                                        common_menu = """
Press 1 for Delivery Reports
Press 2 for Reply Via Same Centre
Press 3 for Character Support
Press 0 to Go Back
"""
 
                                        print(common_menu)
 
                                        common_choice = int(input("Enter your choice: "))
 
                                        match common_choice:
 
                                            case 1:
                                                print("Delivery Reports")
 
                                            case 2:
                                                print("Reply Via Same Centre")
 
                                            case 3:
                                                print("Character Support")
 
                                            case 0:
                                                break
 
                                            case _:
                                                print("Invalid input")
 
                                case 0:
                                    break
 
                                case _:
                                    print("Invalid input")
 
                    case 8:
                        print("Info Service")
 
                    case 9:
                        print("Voice Mailbox Number")
 
                    case 10:
                        print("Service Command Editor")
 
                    case 0:
                        break
 
                    case _:
                        print("Invalid input")
 
        case 3:
            print("Chat")
 
        case 4:
 
            while True:
 
                call_register_menu = """
Press 1 for Missed Calls
Press 2 for Received Calls
Press 3 for Dialled Calls
Press 4 for Erase Recent Call Lists
Press 5 for Show Call Duration
Press 6 for Show Call Costs
Press 7 for Call Cost Settings
Press 8 for Prepaid Credit
Press 0 to Go Back
"""
 
                print(call_register_menu)
 
                call_register_choice = int(input("Enter your choice: "))
 
                match call_register_choice:
 
                    case 1:
                        print("Missed Calls")
 
                    case 2:
                        print("Received Calls")
 
                    case 3:
                        print("Dialled Calls")
 
                    case 4:
                        print("Erase Recent Call Lists")
 
                    case 5:
 
                        while True:
 
                            show_call_duration_menu = """
Press 1 for Last Call Duration
Press 2 for All Calls Duration
Press 3 for Received Calls Duration
Press 4 for Dialled Calls Duration
Press 5 for Clear Timers
Press 0 to Go Back
"""
 
                            print(show_call_duration_menu)
 
                            duration_choice = int(input("Enter your choice: "))
 
                            match duration_choice:
 
                                case 1:
                                    print("Last Call Duration")
 
                                case 2:
                                    print("All Calls Duration")
 
                                case 3:
                                    print("Received Calls Duration")
 
                                case 4:
                                    print("Dialled Calls Duration")
 
                                case 5:
                                    print("Clear Timers")
 
                                case 0:
                                    break
 
                                case _:
                                    print("Invalid input")
 
                    case 6:
 
                        while True:
 
                            show_call_cost_menu = """
Press 1 for Last Call Cost
Press 2 for All Calls Cost
Press 3 for Clear Counters
Press 0 to Go Back
"""
 
                            print(show_call_cost_menu)
 
                            cost_choice = int(input("Enter your choice: "))
 
                            match cost_choice:
 
                                case 1:
                                    print("Last Call Cost")
 
                                case 2:
                                    print("All Calls Cost")
 
                                case 3:
                                    print("Clear Counters")
 
                                case 0:
                                    break
 
                                case _:
                                    print("Invalid input")
 
                    case 7:
 
                        while True:
 
                            call_cost_settings_menu = """
Press 1 for Call Cost Limit
Press 2 for Show Costs In
Press 0 to Go Back
"""
 
                            print(call_cost_settings_menu)
 
                            settings_choice = int(input("Enter your choice: "))
 
                            match settings_choice:
 
                                case 1:
                                    print("Call Cost Limit")
 
                                case 2:
                                    print("Show Costs In")
 
                                case 0:
                                    break
 
                                case _:
                                    print("Invalid input")
 
                    case 8:
                        print("Prepaid Credit")
 
                    case 0:
                        break
 
                    case _:
                        print("Invalid input")
 
        case 5:
 
            while True:
 
                tones_menu = """
Press 1 for Ringing Tone
Press 2 for Ringing Volume
Press 3 for Incoming Call Alert
Press 4 for Composer
Press 5 for Message Alert Tone
Press 6 for Keypad Tones
Press 7 for Warning and Game Tones
Press 8 for Vibrating Alert
Press 9 for Screen Saver
Press 0 to Go Back
"""
 
                print(tones_menu)
 
                tones_choice = int(input("Enter your choice: "))
 
                match tones_choice:
 
                    case 1:
                        print("Ringing Tone")
 
                    case 2:
                        print("Ringing Volume")
 
                    case 3:
                        print("Incoming Call Alert")
 
                    case 4:
                        print("Composer")
 
                    case 5:
                        print("Message Alert Tone")
 
                    case 6:
                        print("Keypad Tones")
 
                    case 7:
                        print("Warning and Game Tones")
 
                    case 8:
                        print("Vibrating Alert")
 
                    case 9:
                        print("Screen Saver")
 
                    case 0:
                        break
 
                    case _:
                        print("Invalid input")
 
        case 6:
 
            while True:
 
                settings_menu = """
Press 1 for Call Settings
Press 2 for Phone Settings
Press 3 for Security Settings
Press 4 for Restore Factory Settings
Press 0 to Go Back
"""
 
                print(settings_menu)
 
                settings_choice = int(input("Enter your choice: "))
 
                match settings_choice:
 
                    case 1:
 
                        while True:
 
                            call_settings_menu = """
Press 1 for Automatic Redial
Press 2 for Speed Dialling
Press 3 for Call Waiting Options
Press 4 for Own Number Sending
Press 5 for Phone Line in Use
Press 6 for Automatic Answer
Press 0 to Go Back
"""
 
                            print(call_settings_menu)
 
                            call_settings_choice = int(input("Enter your choice: "))
 
                            match call_settings_choice:
 
                                case 1:
                                    print("Automatic Redial")
 
                                case 2:
                                    print("Speed Dialling")
 
                                case 3:
                                    print("Call Waiting Options")
 
                                case 4:
                                    print("Own Number Sending")
 
                                case 5:
                                    print("Phone Line in Use")
 
                                case 6:
                                    print("Automatic Answer")
 
                                case 0:
                                    break
 
                                case _:
                                    print("Invalid input")
 
                    case 2:
 
                        while True:
 
                            phone_settings_menu = """
Press 1 for Language
Press 2 for Cell Info Display
Press 3 for Welcome Note
Press 4 for Network Selection
Press 5 for Lights
Press 6 for Confirm SIM Service Actions
Press 0 to Go Back
"""
 
                            print(phone_settings_menu)
 
                            phone_settings_choice = int(input("Enter your choice: "))
 
                            match phone_settings_choice:
 
                                case 1:
                                    print("Language")
 
                                case 2:
                                    print("Cell Info Display")
 
                                case 3:
                                    print("Welcome Note")
 
                                case 4:
                                    print("Network Selection")
 
                                case 5:
                                    print("Lights")
 
                                case 6:
                                    print("Confirm SIM Service Actions")
 
                                case 0:
                                    break
 
                                case _:
                                    print("Invalid input")
 
                    case 3:
 
                        while True:
 
                            security_settings_menu = """
Press 1 for PIN Code Request
Press 2 for Call Barring Service
Press 3 for Fixed Dialling
Press 4 for Closed User Group
Press 5 for Phone Security
Press 6 for Change Access Codes
Press 0 to Go Back
"""
 
                            print(security_settings_menu)
 
                            security_settings_choice = int(input("Enter your choice: "))
 
                            match security_settings_choice:
 
                                case 1:
                                    print("PIN Code Request")
 
                                case 2:
                                    print("Call Barring Service")
 
                                case 3:
                                    print("Fixed Dialling")
 
                                case 4:
                                    print("Closed User Group")
 
                                case 5:
                                    print("Phone Security")
 
                                case 6:
                                    print("Change Access Codes")
 
                                case 0:
                                    break
 
                                case _:
                                    print("Invalid input")
 
                    case 4:
                        print("Restore Factory Settings")
 
                    case 0:
                        break
 
                    case _:
                        print("Invalid input")
 
        case 7:
            print("Call Divert")
 
        case 8:
            print("Games")
 
        case 9:
            print("Calculator")
 
        case 10:
            print("Reminders")
 
        case 11:
 
            while True:
 
                clock_menu = """
Press 1 for Alarm Clock
Press 2 for Clock Settings
Press 3 for Date Setting
Press 4 for Stopwatch
Press 5 for Countdown Timer
Press 6 for Auto Update of Date and Time
Press 0 to Go Back
"""
 
                print(clock_menu)
 
                clock_choice = int(input("Enter your choice: "))
 
                match clock_choice:
 
                    case 1:
                        print("Alarm Clock")
 
                    case 2:
                        print("Clock Settings")
 
                    case 3:
                        print("Date Setting")
 
                    case 4:
                        print("Stopwatch")
 
                    case 5:
                        print("Countdown Timer")
 
                    case 6:
                        print("Auto Update of Date and Time")
 
                    case 0:
                        break
 
                    case _:
                        print("Invalid input")
 
        case 12:
            print("Profiles")
 
        case 13:
            print("SIM Services")
 
        case 0:
            print("bye.")
            break
 
        case _:
            print("Invalid input")

