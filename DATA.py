

while True:
    try:
        ans = int(input("Enter Registration Number or Type in 0 to exit: "))
        
        if ans == 0:
            print("Exiting program. Goodbye.")
            break

        if ans == 8072226475:
            print("Hello Varsha")
        elif ans == 8897333111:
            print("Hello Vishal")
        elif ans == 8919716517:
            print("Hello Rama Prabha")
        elif ans == 9398634526:
            print("Hello Suresh Kumar")
        else:
            print("Data Unavailable")
            
    except ValueError:
        print("Please enter a valid number.")


        


