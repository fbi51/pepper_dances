# -*- coding: utf-8 -*-
from naoqi import ALProxy

IP, PORT = "127.0.0.1", 9559
bm = ALProxy("ALBehaviorManager", IP, PORT)
motion = ALProxy("ALMotion", IP, PORT)

menu = ["genie","hungarian","jgangnamstyle","kuroneko","la_bamba","locomotion","macarena",
        "nagisanosindbad","nightoffire","ozone","run_the_world","sakura","spring","tomorrow",
        "walk_this_way","asereje","danceoftheknights","danceofthereedflutes"]

try: motion.wakeUp()
except: pass

def stop_dances():
    for b in bm.getRunningBehaviors():
        if any(k in b.lower() for k in menu):
            try: bm.stopBehavior(b)
            except: pass

while True:
    print("\n===== MENU DES DANSES =====")
    for i, d in enumerate(menu, 1): print("{}. {}".format(i, d))
    print("0. Quitter")

    try: choix = int(raw_input("Choisissez une danse : "))
    except:
        print("Entrée invalide");
        continue

    if choix == 0:
        stop_dances()
        try: motion.rest()
        except: pass
        break

    if choix < 1 or choix > len(menu):
        print("Choix hors menu");
        continue

    key = menu[choix-1].lower()
    installed = bm.getInstalledBehaviors()
    targets = [b for b in installed if key in b.lower()]
    if not targets:
        print("Aucun behavior pour '{}'".format(key));
        continue

    stop_dances()
    bm.startBehavior(targets[0])

