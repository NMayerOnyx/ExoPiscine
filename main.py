import os

commande = ''

#default values
param = {'bdd': [(1,3,10,(11,2,2024)),(2,1,13,(19,10,2022)),(3,2,6,(3,11,2004)), (3,1,8,(9,1,2011)) ],
         'nages': [(1, "Brasse"), (2, "Dos"), (3, "Crawl")],
         'nageurs': [(1, "Pierre"), (2, "Paul"), (3, "Léa")]
        }


def reset(param):
    '''réinitialise la bdd'''
    param.clear()
    param['bdd'] = []
    param['nages'] = []
    param['nageurs'] = []


def get_str_from_num_in_list(num, liste):
    """Return str from num into liste"""
    for elt in liste:
        if elt[0]==num:
            return elt[1]
    #la ligne suivante ne devrait jamais être exécutée
    return "unknown"


def cmd_individu(param):
    """Ajoute un nouveau najeur"""
    prénom = input("Prénom du nouveau nageur ? ")
    id = len(param['nageurs'])+1
    param['nageurs'].append( (id,prénom ))
    print(param['nageurs'])


def cmd_nouvelle_nage(param):
    """Ajoute une nouvelle nage au logiciel"""
    nage = input("Quelle nage enregistrer ? ")
    id = len(param['nages'])+1
    param['nages'].append( (id,nage ))
    print(param['nages'])


def cmd_ajout(param):
    """Ajoute un évènement à la liste"""
    for elt in param['nageurs']:
        print(f"{elt[0]:5} : {elt[1]}")
    a = int(get_int_value("Nageur n° ? "))
    for elt in param['nages']:
        print(f"{elt[0]:5} : {elt[1]}")
    b = int(get_int_value("Nage n° ? "))
    c = int(get_int_value("combien de longueur ? "))
    dt_a = int(get_int_value("quel année ? "))
    dt_m = int(get_int_value("quel mois ? "))
    dt_j = int(get_int_value("quel jour ? "))
    d = (dt_j,dt_m,dt_a)
    param['bdd'].append((a,b,c,d))


def cmd_liste(param):
    """Affiche toutes les performances des nageurs"""
    print("Prénom      |  nage   |  longueur  | Date")
    print("------------------------------------------")
    for elt in param['bdd']:
        nageur = get_str_from_num_in_list(elt[0], param['nageurs'])
        nage = get_str_from_num_in_list(elt[1], param['nages'])
        date = elt[3]
        dt_a = date[2]
        dt_m = date[1]
        dt_j = date[0]
        print(f" {nageur:11}| {nage:8}|  {elt[2]}  | {dt_j}-{dt_m}-{dt_a}")


def cmd_nageur(param):
    """Affiche toutes les performances d'un nageur"""
    for elt in param['nageurs']:
        print(f"{elt[0]:5} : {elt[1]}")
    tmp = int(get_int_value("Quel numéro de nageur ? "))
    print("Performances de ", tmp)
    print("  nage   |  longueur  | Date")
    print("--------------------")
    for elt in param['bdd']:
        if elt[0]== tmp:
            nage = get_str_from_num_in_list(elt[1], param['nages'])
            date = elt[3]
            dt_a = date[2]
            dt_m = date[1]
            dt_j = date[0]
            print(f" {nage:8}|  {elt[2]}  | {dt_j}-{dt_m}-{dt_a}")


def cmd_nage(param):
    """Affiche toutes les performances suivant une nage donnée"""
    for elt in param['nages']:
        print(f"{elt[0]:5} : {elt[1]}")
    tmp = int(get_int_value("Quel numéro de nage ? "))
    print("Nage ", tmp)
    print(" Nageur     |  longueur  | Date")
    print("------------------------")
    for elt in param['bdd']:
        if elt[1]== tmp:
            nageur = get_str_from_num_in_list(elt[0], param['nageurs'])
            date = elt[3]
            dt_a = date[2]
            dt_m = date[1]
            dt_j = date[0]
            print(f" {nageur:11}|  {elt[2]}  | {dt_j}-{dt_m}-{dt_a}")

def cmd_date(param):
    """Affiche toutes les performances correspondantes a une date donnée"""
    dtr_a = int(get_int_value("quel année ? "))
    dtr_m = int(get_int_value("quel mois ? "))
    dtr_j = int(get_int_value("quel jour ? "))
    for elt in [bdd] :
        date = elt[3]
        dt_a = date[2]
        dt_m = date[1]
        dt_j = date[0]
        if dtr_a == dt_a and dtr_m == dt_m and dtr_j == dt_j :
            nageur = get_str_from_num_in_list(elt[0], param['nageurs'])
            nage = get_str_from_num_in_list(elt[1], param['nages'])
            date = elt[3]
            dt_a = date[2]
            dt_m = date[1]
            dt_j = date[0]
            print(f" {nageur:11}| {nage:8}|  {elt[2]}  | {dt_j}-{dt_m}-{dt_a}")

    
def cmd_nageur_stats(param):
    """Affiche toutes les performances d'un nageur ainsi que ses statistiques"""
    for elt in param['nageurs']:
        print(f"{elt[0]:5} : {elt[1]}")
    tmp = int(get_int_value("Quel numéro de nageur ? "))
    print("Performances de ", tmp)
    print("  nage   |  longueur ")
    print("--------------------")
    min=99999
    max=0
    tot=0
    ct=0
    moy=0
    for elt in param['bdd']:
        if elt[0]== tmp:
            nage = get_str_from_num_in_list(elt[1], param['nages'])
            if elt[2] < min :
                min = elt[2]
            if elt [2] > max :
                max = elt[2]
            tot += elt[2]
            ct += 1
            print(f" {nage:8}|  {elt[2]}")
    moy = tot / ct
    print("Minimum : ", min)
    print("Maximum : ", max)
    print("Moyenne : ", moy)
    


def cmd_exit(param):
    tmp = input("En êtes-vous sûr ? (o)ui/(n)on ")
    if tmp == 'o':
        cmd_save(param, 'save.backup')
        return False
    else:
        return True


def cmd_save(param, filename = 'save.csv'):
    '''sauvegarde complète de la BDD'''
    fichier = open(filename, 'w')
    # sauvegarde des nageurs
    fichier.write('@ nageurs\n')
    for elt in param['nageurs']:
        fichier.write(str(elt[0])+','+str(elt[1])+"\n")
    # sauvegarde des nages
    fichier.write('@ nages\n')
    for elt in param['nages']:
        fichier.write(str(elt[0])+','+str(elt[1])+"\n")
    # sauvegarde des données
    fichier.write('@ bdd\n')
    for elt in param['bdd']:
        fichier.write(str(elt[0])+','+str(elt[1])+','+str(elt[2])+"\n")
    fichier.close()


def cmd_load(param, filename = 'save.csv'):
    '''chargement complet la BDD avec réinitialisation'''
    reset(param)
    key = ''
    fichier = open(filename, 'r')
    for line in fichier:
        line.strip()
        if line[-1] == '\n':
            line = line[:-1]
        if line[0]=='#':
            continue
        if line[0]=='@':
            key = line[2:]
            continue
        if key =='':
            continue
        tmp = line.split(',')
        # convertion en int de ce qui doit l'être
        if key == 'bdd':
            for i in range(len(tmp)):
                tmp[i] = int(tmp[i])
        if key == 'nages' or key == 'nageurs':
            tmp[0] = int(tmp[0])
        param[key].append(tuple(tmp))
    fichier.close()


def get_cmd():
    '''Traitement de la commande d'entrée'''
    msg = input("Que faut-il faire ? ")
    msg = msg.lower()
    return msg

def get_int_value(message):
    while True:
        try:
            msg = int(input(message))
            return msg
        except:
            print("Indiquez bien une valeur numérique")




#
#   Programme principal
#
isAlive = True
if os.path.exists('save.backup'):
    cmd_load(param, 'save.backup')
while isAlive:
    commande = get_cmd()

    if commande == 'ajout' or commande == '1':
        cmd_ajout(param)
        continue
    
    if commande == 'individu' or  commande == '2':
        cmd_individu(param)
        continue

    if commande == 'nouvelle nage' or  commande ==  '3':
        cmd_nouvelle_nage(param)
        continue

    if commande == 'liste' or commande == '4':
        cmd_liste(param)
        continue

    if commande == 'nageur' or commande == '5':
        cmd_nageur(param)
        continue

    if commande == 'nage' or commande == '6':
        cmd_nage(param)
        continue

    if commande == 'save' or commande == '7':
        cmd_save(param)
        continue

    if commande == 'load' or commande == '8':
        cmd_load(param)
        continue

    if commande == 'exit' or commande == '9':
        isAlive = cmd_exit(param)
        continue

    if commande == 'stat' or commande == '10':
        isAlive = cmd_nageur_stats(param)
        continue

    print(f"Commande {commande} inconnue")