#alphabet just a litle twrik to make it a bit harder to crark
alphabet = ['g', 'x', 'h', 'v', 'j', 'q', 'a', 'k', 'z', 'p', 'm', 'o', 'b', 'y', 'd', 'w', 'n', 's', 'f', 'u', 'l', 'i', 'c', 'e', 'r', 't','g', 'x', 'h', 'v', 'j', 'q', 'a', 'k', 'z', 'p', 'm', 'o', 'b', 'y', 'd', 'w', 'n', 's', 'f', 'u', 'l', 'i', 'c', 'e', 'r', 't']
ciper_on=True
while ciper_on:
    while True:
        type= input("Do you what to encrypt or decrypt: Press 'e' for encrypt or 'd' for decrypt:\n")
         
        if type in ('e','d'):
           break
        else:
            print(f"You did not enter the correct type of cipher. Please enter 'e' or 'd'.Please choose again:{type}")
    
    text=input("Enter your message?\n")
    while True:
        shift=input('Enter shift key:\n')
        try:
            shift=int(shift)
            #Handing error for shiftkey numbers more than alphabet
            shift=shift%26
            break
        except ValueError:
            print(f'Shift key must be a whole number you entered {shift}')
    
    #decrypt and encry function ()
    def ciper (type,text,shift):
        nwrd=""
        shift=int(shift)
        text=text.lower()
        for letter in text:
            if letter in alphabet:
                if type=="e":
                    nw=alphabet.index(letter)+shift
                    nwrd=nwrd+alphabet[nw]
                elif type=="d":
                    nw=alphabet.index(letter)-shift
                    nwrd=nwrd+alphabet[nw]
            else:
                #To hannding special charaters and spaces
                nwrd=nwrd+letter 
        return print(nwrd)
            
    ciper(type,text,shift)
    game_change=input("Do you want to continue? Please 'yes' to continue and any key to exit: ")
    if game_change=="yes":
        ciper_on=True
    else:
        print('Goodbye')
        ciper_on=False