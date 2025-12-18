print('''
     %           %
         %           %
            %           %
               %          %
                 %          %
                   %          %                   :::
                    %          %                ::::::
                 %%%%%%  %%%%%%%%%            ::::::::
              %%%%%ZZZZ%%%%%%   %%%ZZZZ     ::::::::::         ::::::
             %%%ZZZZZ%%%%%%%%%%%%%%ZZZZZZ  :::::::::::    :::::::::::::::::
             ZZZ%ZZZ%%%%%%%%%%%%%%%ZZZZZZZ::::::::::***:::::::::::::::::::::
          ZZZ%ZZZZZZ%%%%%%%%%%%%%%ZZZZZZZZZ::::::***:::::::::::::::::::::::
        ZZZ%ZZZZZZZZZZ%%%%%%%%%%ZZZZZZ%ZZZZ:::***:::::::::::::::::::::::
       ZZ%ZZZZZZZZZZZZZZZZZZZZZZZ%%%%% %ZZZ:**::::::::::::::::::::::
      ZZ%ZZZZZZZZZZZZZZZZZZZ%%%%% | | %ZZZ *:::::::::::::::::::
      Z%ZZZZZZZZZZZZZZZ%%%%%%%%%%%%%%%ZZZ::::::::::::::::::::::::::
       ZZZZZZZZZZZ%%%%%ZZZZZZZZZZZZZZZZZ%%%%:::ZZZZ:::::::::::::::::
         ZZZZ%%%%%ZZZZZZZZZZZZZZZZZZ%%%%%ZZZ%%ZZZ%ZZ%%*:::::::::::
            ZZZZZZZZZZZZZZZZZZ%%%%%%%%%ZZZZZZZZZZ%ZZ%:::*:::::::
            *:::%%%%%%%%%%%%%%%%%%%%%%%ZZZZZZZZZZ%%%*::::*::::
          *:::::::%%%%%%%%%%%%%%%%%%%%%%%ZZZZZ%%      *:::Z
         **:ZZZZ:::%%%%%%%%%%%%%%%%%%%%%%%%%%%ZZ      ZZZZZ
        *:ZZZZZZZ       %%%%%%%%%%%%%%%%%%%%%ZZZZ    ZZZZZZZ
       *::::ZZZZZZ         %%%%%%%%%%%%%%%ZZZZZZZ      ZZZ
        *::ZZZZZZ           Z%%%%%%%%%%%ZZZZZZZ%%
          ZZZZ              ZZZZZZZZZZZZZZZZ%%%%%
                           %%%ZZZZZZZZZZZ%%%%%%%%
                          Z%%%%%%%%%%%%%%%%%%%%%
                          ZZ%%%%%%%%%%%%%%%%%%%
                          %ZZZZZZZZZZZZZZZZZZZ
                          %%ZZZZZZZZZZZZZZZZZ
                           %%%%%%%%%%%%%%%%
                            %%%%%%%%%%%%%
                             %%%%%%%%%
                              ZZZZ
                              ZZZ
                             ZZ
                            Z''')
print("Welcome to the Treasure Island")
print("Your mission is to find the treasure.")
choice = input("You're at the cross road, where do you want to go? type left or right")
if choice == "left":
    choice = input("you have encountered a lake, type swim to swim across the lake or type 'wait' to decide to wait")
    if choice == "wait":
        choice = input("You have encountered a house with 3 doors, one red, one blud, one yellow. which color would you like to choose?")
        if choice == "red":
            print(" You have been burned by fire. Game Over")
        elif choice == "blue":
            print("You have been eaten by beast. Game over")
        elif choice == "yellow":
            print("Congratulations! You found the treasure! You Win!")
        else: 
            print("Invalid choice. Game Over")
    else:
        print("You have been attacked by trout. Game over") 
elif choice == "right":
    print("You have fell into a hole. Game Over")
else:
    print("Invalid choice. Game Over")
