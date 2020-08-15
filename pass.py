from random import shuffle, randint, SystemRandom
# basic use

import string



def get_pass(leng=0, symbols=False):



    if (leng > 0 and leng <= 62):

        chars = [chr(i) for i in range(32,127) if (chr(i).isalpha() or chr(i).isdigit())]

        if symbols:

            symbs = [chr(i) for i in range(32,127) if not (chr(i).isalpha() ) and not (chr(i).isdigit() )]

            symbs = symbs[1:] #no space

            chars += symbs

            #print symbs

        shuffle(chars)

        temp = "".join(chars)

    

        #print temp

        # pick from temp

        passw = ""

        for x in range(leng):

            passw += chars[ randint(0,len(chars) - 1 ) ]

        print (passw)

    else:

        print("incorrect length...")

    

get_pass(4, False)



get_pass(32, True)

get_pass(32, False)


#x = 0

#while (x < 100):

#   get_pass(62, True)

#   x+=1

#f=''.join(SystemRandom().choice(string.ascii_lowercase + string.ascii_uppercase + string.digits) for _ in range(100))

##f=''.join(SystemRandom().choice(string.printable) for _ in list(range(100)))
##
##
##
##x=string.printable
##
##i=x.index("~") + 1
##
##
##
##x=x[:i]
##
##print(x)

#for b in x:

#    print(("...", b))

