flag = os.getenv('flag')

def encrypt(s):
     alphabet = 'abcdefghijklmnopqrstuvwxyz'
     s = s.lower()
     
     keyShift = 13
     strings = ''
     for i in s:
         if i.isalpha():
            encryptedCharacter = alphabet.index(i) + keyShift
            if encryptedCharacter > 25:
                 encryptedCharacter = alphabet.index(i) - keyShift

            strings +=alphabet[encryptedCharacter]
         else:
            strings += i
     return strings[::-1]
  
 
print(encrypt(flag))

# output : }31gbe_ugvj_enyvzvf_fv_fvug{tnys