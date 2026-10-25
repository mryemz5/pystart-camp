
def vowel(metin):
    vowels="aeıuioöüAEIİOÖUÜ"
    x=0
    for letter in metin:
        if letter in vowels:
            x+=1
    return x
result=vowel("python öğreniyorum") 
print(result)       

def lenghtword(cumle):
     word=cumle.split()
     k=""
     for x in word:
      if len(x)> len(k):
          k=x
     return k     
result=lenghtword("kod yazmak pratik ister")
print(result)          








