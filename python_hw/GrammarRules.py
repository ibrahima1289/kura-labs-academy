#Grammar rules script
#Ibrahima Diallo

alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
vowels = ['a','e','i','o','u']
consnants = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','z']
A = ['s','ch','sh','x','z']
B = ['man','child','foot','tooth','mouse','person']
C = ['sheep','deer','fish','series','specie']
yes = True
no = False
counter = 0
#noun = input("Word in singular: ")
while yes:
    noun = input("Word in singular: ")
    for word in alpha:
        
        #Conditions for grammar rules
        word = noun
        if ((noun=='fish') or (noun=='series') or (noun=='species') or (noun in C)):
            word = noun
        elif ((noun[-1] in A) or noun[-2:]=='ch' or noun[-2:]=='sh'):
            word = noun+'es'
            if ((noun[-2] in vowels) and (noun[-1:]=='z')):
                word = noun+'zes'
            
        elif noun[-1]=='f':
            if noun=='roof' or noun=='cliff':
                word = noun+'s'
            else:
                word = noun[:-1]+'ves'
            
        elif noun[-2:]=='fe':
            word = noun[:-2]+'ves'
    
        elif ((noun[-2] in vowels) and (noun[-1]=='y')):
            word = noun+'s'
        
        elif ((noun[-2] in vowels) and (noun[-1]=='o')):
            word = noun+'s'
        
        elif ((noun[-2] in consnants) and (noun[-1]=='y')):
            word = noun[:-1]+'ies'
        
        elif ((noun[-2] in consnants) and (noun[-1]=='o')):
            if ((noun=='piano') or (noun=='photo')):
                word = noun+'s'
            else:
                word = noun+'es'
            
        elif noun in B:
            if noun=='man':
                word = 'men'
            elif noun=='child':
                word = 'children'
            elif noun=='foot':
                word = 'feet'
            elif noun=='tooth':
                word = 'teeth'
            elif noun=='mouse':
                word = 'mice'
            elif noun=='person':
                word = 'people'
        elif (noun[-2:]=='ss'):
            word = noun+'es'
        
        else:
            word = noun+'s'
            
    print(noun,"in plural is",word)
    response = input("Another word (yes / no)? ")
    #Conditions for false input
    counter = counter+1
    c = 0
    while (response != 'yes' and response != 'no'):
        print("Wrong answer, try again.")
        response = input("Another word (yes / no)? ")
        c=c+1
    if response == 'no':
        print("The program created plural for",counter,"nouns.")
        break
    else:
        if response =='yes':
            continue

        
            
            
                            
            
        
