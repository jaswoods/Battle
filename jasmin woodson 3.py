#!/usr/bin/env python
# coding: utf-8

# In[2]:


def main():
    
    texte = input("Entre yon texte : ")
    
    nombre_mots = len(texte.split())

    mots = texte.split()
    texte_modifie = []
    for mot in mots:
        if mot[0].lower() in ['a', 'e', 'i', 'o', 'u', 'y']:
            mot_modifie = mot.capitalize()
        else:
            mot_modifie = mot.lower()
        texte_modifie.append(mot_modifie)
    texte_modifie = ' '.join(texte_modifie)

    if "hack" in texte.lower():
        resultat = "Viris"
    else:
        resultat = "Pa gen viris"
    
    print(f"Nombre mot : {nombre_mots}")
    print(f"Texte modifié : {texte_modifie}")
    print(resultat)

if __name__ == "__main__":
    main()


# In[ ]:




