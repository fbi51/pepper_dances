# pepper_dances
Programme pour lancer les danses de Pepper

## Sélecteur de danses NAO (Choregraphe Behaviors)

Petit script Python qui affiche un menu en console pour lancer des danses (behaviors) installées sur un robot **NAO / Pepper** via **NAOqi**.  
Le script s’assure aussi qu’une seule danse tourne à la fois en arrêtant les behaviors de danse déjà en cours avant d’en démarrer un nouveau.

---

## Fonctionnalités

- Réveille le robot (`wakeUp`)
- Affiche un menu de danses en console
- Lance le behavior correspondant au choix de l’utilisateur
- Stoppe automatiquement les autres danses en cours
- Permet de quitter proprement en arrêtant les danses

---

## Prérequis

- Robot **Pepper** allumé et accessible sur le réseau
- NAOqi disponible 2.5.x ou 2.7.x (connexion via IP/PORT)
- Python **2.7** (le script utilise `raw_input`, typique Python 2)
- Les dances/behaviors doivent être **installés** sur le robot (souvent via la sélection des danses sur le cloud d'Aldebaran et la mise à jour sur l'application "Robot Settings")

Modules NAOqi utilisés :
- `ALBehaviorManager`
- `ALMotion`

---

## Installation / Configuration

1. Connecte-toi en SSH sur ton Pepper via ton device (PC/Téléphone/Tablette). Il faut être sur le même réseau wifi que ton Pepper.
2. Copie le script de ton device vers ton Pepper 
3. Lance le script : python dances.py
