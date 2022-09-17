def spin_words(sentence):
    
    sentence_splited = sentence.split()
    
    for i in sentence_splited:
        
        if len(i) >= 5:
            
            sentence_splited[sentence_splited.index(i)] = i[::-1]
    
    return ' '.join(sentence_splited)