'''
this will be the generator class, called by the base program

NOTES TO SELF:
If Demi (or Optional?), use profShort instead of status, plus subref 3d6 to reference random gear
Else If Human (or Core?), generate social status 3d6 and subref 3d6 again for use with equipment randomization.

Don't forget half-stats for TNU
'''

import random

import dice
import equipment
import professions
import spells
import systems

def gen_stats(PAs, system='TNU'):
    getSys = system
    validSystems = ['TNU']
    if getSys not in validSystems:
        getSys = 'TNU'
    spread = dice.get_spread(getSys, PAs)
    return spread


def gen_spells(pr, al, nu):
    my_spellsList = spells.get_spells(pr, al, nu)
    return my_spellsList

def print_spells(prof, align, num):
    printList = list(gen_spells(prof, align, num))
    print("\nMy Character's List of Spells:")
    print("------------------------------")
    for each in printList:
        print(each)
    return

def gen_social(status):
    social = {'title': '', 'mod': 0, 'label': ''}
    if status == 18:
        social.update({'title': 'Royalty', 'mod': 3, 'label': 'royal'})
    elif status >= 16:
        social.update({'title': 'Greater Nobility', 'mod': 2, 'label': 'greater'})
    elif status >= 13:
        social.update({'title': 'Lesser Nobility', 'mod': 1, 'label': 'lesser'})
    elif status >= 9:
        social.update({'title': 'Middle Class', 'mod': 0, 'label': 'middle'})
    elif status >= 6:
        social.update({'title': 'Poor', 'mod': -1, 'label': 'poor'})
    elif status >= 4:
        social.update({'title': 'Peasantry', 'mod': -2, 'label': 'peasant'})
    else:
        social.update({'title': 'Scum', 'mod': -3, 'label': 'wretched'})
    return social

def generate(gameSystem, flagPrint=False):
    # first let's load those system prefs - for later expansion
    sysPrefs = dict(systems.get_system_prefs(gameSystem))
    # let's get that juicy character data!
    genData = []
    myData = dict(professions.get_profession())
    mD = myData
    myFlags = list(mD['flags'])
    # now let's break it out:
    myProfS = mD['profShort']
    myProfL = mD['profLong']
    myLvl = int(mD['level'])
    myAlign = random.choice(mD['alignAllowed'])
    myPAs = list(mD['primAttr'])
    myStats = gen_stats(myPAs, gameSystem)
    mySocial = int(dice.roll(3, 6))
    myClass = dict(gen_social(mySocial))
    myHD = mD['hd']
    if sysPrefs['hasHPs']:
        print("This System DOES have Hit Points!")
    if 'haspa' in mD['flags']:
        myPA = 'Yes'
    else:
        myPA = 'None'
    # let's get that gear list:
    myGear = list(equipment.get_gear(myProfS, myClass['label']))
    myWeapons = list(filter(lambda x: x.startswith('WEAPON: '), myGear))
    myArmour = list(filter(lambda x: x.startswith('ARMOUR: '), myGear))
    myWeaponList = []
    myArmourList = []
    for x in myWeapons:
        myGear.remove(x)
        myWeaponList.append(str.title(x[8:]))
    for x in myArmour:
        myGear.remove(x)
        myArmourList.append(str.title(x[8:]))
    # let's get those spells now:
    if 'caster' in mD['flags']:
        is_caster = True
        myCastStat = mD['casterStat']
        myCastMod = myStats[mD['casterStat']]['mod']
        myMastr = myLvl + myCastMod
        if myMastr > 0:
            mySpells = list(gen_spells(myProfS, myAlign, myMastr))
        else:
            mySpells = []
    else:
        is_caster = False
    # let's build the final dump of data:
    # genData = [my_ProfS, my_ProfL, my_Lvl, my_Align, my_Stats]
    # for local testing, print to debug:
    if flagPrint:
        print("\nNOTICE: You are running in test mode, on-screen print is enabled")
        print("\nA new random character for " + str(sysPrefs['fullName']))
        print("-----------------------------------------------------")
        #print("Raw Data Print: ", genData)
        print("Profession: " + myProfL + "; Level: " + str(myLvl) + "; Alignment:", myAlign.title())
        print("Hit Die: d" + str(myHD) + "; Psychic Armour: " + str(myPA) + "; Social Status: " + myClass['title'] + "("+ str(myClass['mod']) + ")" )
        print("---------------")
        print("\nAttribute Scores:")
        print("-----------------")
        for key, value in dict.items(myStats):
            print(key + ": " + str(value['val']) + ' (' + str(value['mod']) + ')')
        print("\nMy Weapons:")
        print("-----------")
        for x in myWeaponList:
            print(x)
        print("\nMy Armour:")
        print("----------")
        for x in myArmourList:
            print(x)
        print("\nMy Gear:")
        print("--------")
        for x in myGear:
            print(x)
        if is_caster:
            print("\nSpells Known:")
            print("-------------")
            if myMastr <= 0:
               print("I have no spells because I am the worst", myProfL, "ever!")
            else:
                for i in mySpells:
                    print(i)
    return genData

if __name__ == "__main__":
    # if run as-is, flagPrint "True" will enable screen print of character
    generate('TNU', True)
