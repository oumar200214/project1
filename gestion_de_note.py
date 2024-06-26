from cryptography.fernet import Fernet


'''def cle():
    cle = Fernet.generate_key()
    with open('cle.key', 'wb') as bfile:
         bfile.write(cle)'''
def rechcle():
     with open('cle.key', 'rb') as rbfile:
          cle = rbfile.read()
          return cle
     
recharge = Fernet(rechcle())

def voir():
    with open('note.txt', 'r') as rfile:
         for i in rfile.readlines():
            data = i.rstrip()
            if '|' in data:
                user, note = data.split('|')
                decryptage = recharge.decrypt(note.encode()).decode() 
                print(f'you name is {user} et ton nom est {decryptage}')
            


def ajout():
    while True:
        eleve_nom = input('quel est ton nom: ')
        note_math = input('quel est ta note en math sur 20: ')
        if note_math.isdigit():
            note_math == int(note_math)
        if  '0' <= note_math <= '20':
            break
        else:
            print('Impossible ressayer')
            continue
    with open('note.txt', 'a') as file :
         file.write(eleve_nom + '|' + recharge.encrypt(note_math.encode()).decode() + '\n')
            


#programme principale
while True:
    requete = input('veux tu ajouter ou voir les notes ou "q" pour quite le programme(ajout/voir/q): ').lower()
    if requete == "q":
        break
    elif requete == "ajout":
            ajout()
    elif requete == "voir":
            voir()
    else:
         print('demande invalide')
         continue
    
