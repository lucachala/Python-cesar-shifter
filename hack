#Github: https://github.com/tucas17gamer
#project make at "mundo maker" (https://www.mundomaker.cc/)
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
text = (input('Text to crack: '))
result = ''
resultult = ''
for i in range(len(alphabet)):
    
    for j in range(len(text)):
        if text[j] in alphabet:
            result=result+alphabet[(alphabet.index(text[j])+i)%52]
        
        else:
            result=result+text[j]
            
    resultult=resultult+'Key:'+str(i)+' Text: '+result+'\n'
    print('Key:'+str(i)+' Text: '+result)
    result=''

with open("result_file.txt", "wt", encoding='utf-8') as result_file:
    result_file.write('Key:'+str(i)+' Text: '+resultult)
