#completed 1/28/19

def title_case(title, minor_words=''):
    newtitle = ''    
    title = title.lower().split(' ')
    if minor_words:
        minor_words = minor_words.lower().split(' ') 
    for i, word in enumerate(title):
        for index, letter in enumerate(word):
            if minor_words:
                if (word not in set(minor_words) or i==0) and index == 0:
                    newtitle+=letter.upper()
                else:
                    newtitle+=letter
            else:
                if index == 0:
                    newtitle+=letter.upper()
                else:
                    newtitle+=letter
        if word == title[len(title)-1]:
            newtitle+=''
        else:
            newtitle+=' '   
    return newtitle


#best solution
def title_case(title, minor_words=''):
    title = title.capitalize().split()
    minor_words = minor_words.lower().split()
    return ' '.join([word if word in minor_words else word.capitalize() for word in title])
