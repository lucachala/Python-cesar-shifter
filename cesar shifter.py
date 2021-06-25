#Github: https://github.com/tucas17gamer
#project make at "mundo maker" (https://www.mundomaker.cc/)

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

coded_text = ' '
decoded_text = ' '

func = (input('You wanna to encode or decode?\n'))
key = int(input('Key (number) add - for negative numbers (1234 for + and -12345 for negative):\n'))



if func=='encode':
    text = (input('Text to code:\n'))
    for num_text_encoder in range(len(text)):
        if text[num_text_encoder] in alphabet: 
            coded_text=coded_text+alphabet[(alphabet.index(text[num_text_encoder])+key)%52]
        else:
            coded_text=coded_text+text[num_text_encoder]
    print('Text encoded:', coded_text)

elif func=='decode':
    text = (input('Text to decode:\n'))
    for num_text_decoder in range(len(text)):
        if text[num_text_decoder] in alphabet:
            decoded_text=decoded_text+alphabet[(alphabet.index(text[num_text_decoder])-key)%52]
        else:
            decoded_text=decoded_text+text[num_text_decoder]
    print('Text decoded:', decoded_text)
input('Press any key to left')
