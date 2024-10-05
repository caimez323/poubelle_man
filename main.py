from PIL import ImageGrab
import pytesseract
import tkinter as tk
import pyautogui

pytesseract.pytesseract.tesseract_cmd = "C:\\Users\\Clément\\AppData\\Local\\Programs\\Tesseract-OCR\\tesseract.exe"

XX = 827

Poubelle_Coo_Dic = {"Poubelles orange" : 682,\
                    "Poubelles marrons" : 700,\
                    "Poubelles blanches" : -683,\
                    "Poubelles grises" : 724,\
                    "Poubelles jaunes" : -700,\
                    "Poubelles vertes foncees" : -682,\
                    "Poubelles vertes claires" : -720,\
                    "Poubelles noires": 655,\
                    "Plus" : 744
                    }


Poubelle_Dechet_Dic = { Poubelle_Coo_Dic["Poubelles orange"] : ["gobelet en plastique"],\
           Poubelle_Coo_Dic["Poubelles marrons"] : ["gobelet en carton"],\
           Poubelle_Coo_Dic["Poubelles blanches"] : ["bouchon en plastique"],\
           Poubelle_Coo_Dic["Poubelles grises"] : ["Idée notée sur un pense-bête","Sac en papier propre"],\
           Poubelle_Coo_Dic["Poubelles jaunes"] : ["bouteille en plastique"],\
           Poubelle_Coo_Dic["Poubelles vertes foncees"] : ["bouteille en verre"],\
           Poubelle_Coo_Dic["Poubelles vertes claires"] : ["canette de soda"],\
           Poubelle_Coo_Dic["Poubelles noires"] : ["Bouchon en métal", "Trognon de pomme","Croûte de pizza","Touillette en plastique", "couvert en plastique" ,"Boule de papier en Aluminium", "Mouchoir en papier","Sac en papier souillé"]\
            }


def f_click(x,y,dmy = False):
    pyautogui.moveTo(x, y)
    if not dmy:
        pyautogui.click()

# Fonction pour capturer la zone de l'écran et extraire le texte
def capture_screen():
    try:
        # Coordonnées de la zone à capturer
        x1,y1,x2,y2 = 750,610,1350,820
        img = ImageGrab.grab(bbox=(x1, y1, x2, y2))
        
        # Extraire le texte de l'image capturée
        text = pytesseract.image_to_string(img)
        return text
    except Exception as e:
        print(f"Une erreur s'est produite : {e}")
        return None

# Configuration de l'interface utilisateur avec Tkinter
root = tk.Tk()
root.withdraw()  # Cacher la fenêtre principale

# Capturer l'écran et stocker le texte extrait dans une variable
captured_text = capture_screen()
if captured_text is not None:
    #print("Texte capturé")
    #print(captured_text.strip().lower())
    captured_text = captured_text.lower()

    # Déplacer la souris à une position spécifique (par exemple, (500, 500)) et cliquer

    if "sortir" in captured_text:
        traite = captured_text.split("\n")
        #On doit d'abord cliquer sur le premier dechet, puis on récupère le premier item
        f_click(XX,679)
        thisLine = traite[2]
        for poubelle_type, poubelle_mange in Poubelle_Dechet_Dic.items():
            if any(mot.lower() in thisLine.lower() for mot in poubelle_mange) :#dechet va dans cette poubelle:
                #print("Le dechet {} va dans la poubelle {}".format(thisLine,poubelle_type))
                #Si on est négatif on doit changer de page
                if poubelle_type < 0:
                    poubelle_type = -poubelle_type
                    f_click(XX,Poubelle_Coo_Dic["Plus"]+30)
                #Dans tout les cas:
                f_click(XX,poubelle_type+30)
    f_click(-900,900)

else:
    print("La capture d'écran a échoué.")
