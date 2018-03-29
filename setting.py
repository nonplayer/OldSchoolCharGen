"""
This contains all the game setting-specific generators and data.
"""

ages_base = [
    'Early Teens', 'Late Teens', 'Young Adult', 'Adult', 'Middle-Aged', 'Elder', 'Ancient',
]

looks_base = [
    'Drab', 'Threadbare', 'Fancy', 'Filthy', 'Disguised', 'Common',
    'Skivvies', 'Antiquated', 'Anachronistic', 'Slovenly',
]

personality_base = [
    'Accusative', 'Active', 'Adventurous', 'Affable', 'Affectionate', 'Aggressive', 'Agreeable',
    'Aimless', 'Aloof', 'Altruistic', 'Amazed', 'Analytical', 'Angry', 'Animated', 'Annoying',
    'Anxious', 'Apathetic', 'Apologetic', 'Apprehensive', 'Argumentative', 'Arrogant', 'Articulate',
    'Artist', 'Athletic', 'Attentive', 'Beautiful', 'Bigoted', 'Bitter', 'Blustering', 'Boastful',
    'Bookish', 'Bossy', 'Braggart', 'Brash', 'Brave', 'Bullying', 'Callous', 'Calm', 'Candid',
    'Cantankerous', 'Capricious', 'Careful', 'Careless', 'Caring', 'Casual', 'Catty', 'Cautious',
    'Cavalier', 'Charming', 'Chaste', 'Chauvinistic', 'Cheeky', 'Cheerful', 'Childish', 'Chivalrous',
    'Clueless', 'Clumsy', 'Clumsy', 'Cocky', 'Comforting', 'Communicative', 'Complacent', 'Condescending',
    'Confident', 'Conformist', 'Confused', 'Conscientious', 'Conservative', 'Contentious', 'Contrarian',
    'Controlling', 'Contumely', 'Conventional', 'Cooperative', 'Courageous', 'Courteous', 'Cowardly',
    'Coy', 'Crabby', 'Cranky', 'Critical', 'Cruel', 'Cultured', 'Curious', 'Cynical', 'Daring', 'Daring',
    'Deceitful', 'Deceptive', 'Defensive', 'Defiant', 'Deliberate', 'Deluded', 'Depraved', 'Discreet',
    'Dishonest', 'Disingenuous', 'Disloyal', 'Disrespectful', 'Distant', 'Distracted', 'Distraught',
    'Docile', 'Doleful', 'Dominating', 'Dramatic', 'Drug-addled', 'Drunkard', 'Dull', 'Earthy',
    'Eccentric', 'Educated', 'Elitist', 'Emotional', 'Enigmatic', 'Enthusiastic', 'Epicurean', 'Ethical',
    'Excited', 'Expressive', 'Extroverted', 'Faithful', 'Fanatical', 'Fastidious', 'Fatalistic',
    'Fearful', 'Fearless', 'Feisty', 'Feral', 'Feuding', 'Fierce', 'Flamboyant', 'Flippant', 'Flirtatious',
    'Foolhardy', 'Foppish', 'Foreign', 'Forgiving', 'Friendly', 'Frightened', 'Frivolous', 'Frustrated',
    'Funny', 'Furtive', 'Generous', 'Genial', 'Gentle', 'Gloomy', 'Goofy', 'Gossip', 'Graceful', 'Gracious',
    'Grave', 'Greasy', 'Greedy', 'Gregarious', 'Grouchy', 'Groveling', 'Gruff', 'Guilty', 'Gullible',
    'Happy', 'Hard working', 'Harsh', 'Hateful', 'Heartbroken', 'Helpful', 'Hoarder', 'Honest', 'Hopeful',
    'Hostile', 'Humble', 'Humorless', 'Humorous', 'Hungry', 'Idealistic', 'Idiosyncratic', 'Ill',
    'Imaginative', 'Imitative', 'Impatient', 'Impetuous', 'Implacable', 'Impractical', 'Impulsive',
    'Inattentive', 'Incoherent', 'Indifferent', 'Indiscreet', 'Individualist', 'Indolent', 'Indomitable',
    'Indulgent', 'Industrious', 'Inexorable', 'Inexpressive', 'Insecure', 'Insensitive', 'Insomniac',
    'Instructive', 'Intolerant', 'Intransigent', 'Introverted', 'Irreligious', 'Irresponsible',
    'Irreverent', 'Irritable', 'Jealous', 'Jocular', 'Joking', 'Jolly', 'Joyous', 'Judgmental', 'Jumpy',
    'Kind', 'Know-it-all', 'Languid', 'Lawful', 'Layabout', 'Lazy', 'Lethargic', 'Lewd', 'Liar', 'Likable',
    'Lippy', 'Listless', 'Loquacious', 'Loud', 'Loving', 'Loyal', 'Lucky', 'Lust', 'Madcap', 'Magical',
    'Magnanimous', 'Malicious', 'Maudlin', 'Mean', 'Meddlesome', 'Melancholy', 'Melodramatic', 'Merciless',
    'Merry', 'Meticulous', 'Mischievous', 'Miscreant', 'Miserly', 'Modest', 'Moody', 'Moralistic', 'Morbid',
    'Morose', 'Mournful', 'Mousy', 'Mouthy', 'Musical', 'Mysterious', 'Mystical', 'Naive', 'Narrow-minded',
    'Needy', 'Nefarious', 'Nervous', 'Nettlesome', 'Neurotic', 'Nihilist', 'Noble', 'Nonchalant',
    'Nurturing', 'Obdurate', 'Obedient', 'Oblivious', 'Obnoxious', 'Obsequious', 'Obsessive', 'Obstinate',
    'Obtuse', 'Odd', 'Off-putting', 'Optimistic', 'Organized', 'Ornery', 'Orphan', 'Ostentatious',
    'Outgoing', 'Overbearing', 'Overconfident', 'Paranoid', 'Passionate', 'Pathological', 'Patient',
    'Peaceful', 'Peacemaker', 'Pensive', 'Pertinacious', 'Pessimistic', 'Philanderer', 'Philosophical',
    'Phony', 'Pious', 'Playful', 'Pleasant', 'Poised', 'Polite', 'Pompous', 'Pondering', 'Pontificating',
    'Practical', 'Prejudiced', 'Preoccupied', 'Pretentious', 'Promiscuous', 'Proper', 'Proselytizing',
    'Proud', 'Prudent', 'Prudish', 'Prying', 'Puerile', 'Pugnacious', 'Punctual', 'Quiet', 'Quirky',
    'Rascal', 'Rash', 'Realistic', 'Rebellious', 'Reckless', 'Refined', 'Repellent', 'Reserved',
    'Respectful', 'Responsible', 'Restless', 'Reticent', 'Reverent', 'Rigid', 'Risk-taking', 'Romantic',
    'Rude', 'Sadistic', 'Sarcastic', 'Sardonic', 'Sassy', 'Savage', 'Scared', 'Scolding', 'Secretive',
    'Seeker', 'Self-destructive', 'Self-effacing', 'Selfish', 'Selfless', 'Senile', 'Sensible', 'Sensitive',
    'Sensual', 'Sentimental', 'Serene', 'Serious', 'Servile', 'Sexual', 'Shallow', 'Shameful',
    'Shameless', 'Shifty', 'Shrewd', 'Shy', 'Sincere', 'Slanderous', 'Sly', 'Smug', 'Snobbish', 'Sober',
    'Sociable', 'Solemn', 'Solicitous', 'Solitary', 'Sophisticated', 'Spendthrift', 'Spiteful', 'Stern',
    'Stingy', 'Stoic', 'Stubborn', 'Stylish', 'Submissive', 'Sultry', 'Superstitious', 'Surly', 'Suspicious',
    'Sybarite', 'Sycophantic', 'Sympathetic', 'Taciturn', 'Tactful', 'Tattooed', 'Tawdry', 'Teetotaler',
    'Temperamental', 'Tempestuous', 'Thief', 'Thorough', 'Thrifty', 'Thrifty', 'Timid', 'Tolerant',
    'Transparent', 'Treacherous', 'Troublemaker', 'Trusting', 'Truthful', 'Uncommitted', 'Understanding',
    'Unfriendly', 'Unhinged', 'Uninhibited', 'Unpredictable', 'Unruly', 'Unsupportive', 'Vague', 'Vain',
    'Vapid', 'Vengeful', 'Vigilant', 'Violent', 'Vivacious', 'Vulgar', 'Wanderlust', 'Wanton', 'Wasteful',
    'Weary', 'Well-travelled', 'Whimsical', 'Whiny', 'Wicked', 'Wisecracking', 'Wistful', 'Witty',
    'Youthful', 'Zealous',
]

backgrounds_base = [
    'Accountant', 'Acrobat', 'Actor', 'Alchemist', 'Animal seller', 'Animal trainer', 'Apiarist',
    'Apothecary', 'Architect', 'Armourer', 'Artillerist', 'Artist', 'Astrologer', 'Author', 'Baker',
    'Banker', 'Barber', 'Barkeep', 'Beggar', 'Blacksmith', 'Boat builder', 'Bodyguard', 'Bookbinder',
    'Bounty hunter', 'Bow maker', 'Brewer', 'Builder', 'Butcher', 'Calligrapher', 'Candle maker',
    'Captain', 'Caravan driver', 'Carpenter', 'Carpet maker', 'Cart maker', 'Cartographer', 'Carver',
    'Cavalry', 'Cheese maker', 'Chef', 'Clerk', 'Clock maker', 'Cloth dyer', 'Clothier', 'Clown',
    'Coach driver', 'Cobbler', 'Composer', 'Cook', 'Cooper', 'Coppersmith', 'Counterfeiter', 'Courier',
    'Courtesan', 'Courtier', 'Custodian', 'Demagogue', 'Doctor', 'Engineer', 'Engraver', 'Explorer',
    'Falconer', 'Farmer', 'Fence', 'Fisher', 'Fletcher', 'Flower seller', 'Food seller', 'Forester',
    'Forger', 'Fortune teller', 'Fruit seller', 'Furniture maker', 'Furrier', 'Gambler', 'Gamekeeper',
    'Gardener', 'General', 'Glass maker', 'Goldsmith', 'Governess', 'Grave digger', 'Groom', 'Guard',
    'Guide', 'Haberdasher', 'Hatter', 'Healer', 'Herald', 'Horse trader', 'Hosteler', 'Hunter',
    'Illustrator', 'Innkeeper', 'Jailer', 'Jester', 'Jeweller', 'Judge', 'Labourer', 'Laundress',
    'Lawyer', 'Lead smith', 'Leather worker', 'Librarian', 'Linen maker', 'Locksmith', 'Maid', 'Marine',
    'Mercenary', 'Merchant', 'Midwife', 'Miller', 'Miner', 'Minstrel', 'Moneylender', 'Musician',
    'Navigator', 'Net maker', 'Noble', 'Nurse', 'Official', 'Outfitter', 'Page', 'Painter', 'Paper maker',
    'Pawnbroker', 'Peasant', 'Peddler', 'Perfumer', 'Pharmacist', 'Photographer', 'Physician', 'Pilgrim',
    'Pilot', 'Pimp', 'Pirate', 'Playwright', 'Plumber', 'Poacher', 'Police', 'Porter', 'Potter', 'Priest',
    'Printer', 'Professor', 'Prospector', 'Prostitute', 'Purser', 'Ranger', 'Ratcatcher', 'Roofer',
    'Rope maker', 'Runner', 'Saddler', 'Sail maker', 'Sailor', 'Scavenger', 'Scholar', 'Scout', 'Scribe',
    'Sculptor', 'Servant', 'Server', 'Sharpener', 'Shepherd', 'Shipwright', 'Shopkeeper', 'Silk trader',
    'Silversmith', 'Soap maker', 'Soldier', 'Spice trader', 'Squire', 'Stabler', 'Stevedore', 'Steward',
    'Stonemason', 'Student', 'Tailor', 'Tattooist', 'Tax collector', 'Taxidermist', 'Teacher', 'Thief',
    'Thug', 'Tile maker', 'Tinker', 'Trader', 'Trapper', 'Undertaker', 'Veterinarian', 'Vintner',
    'Water seller', 'Weaponsmith', 'Weaver', 'Wheelwright', 'Wine seller', 'Woodcutter'
]

settings = {
    'default': {
        'age': ages_base,
        'looks': looks_base,
        'personality': personality_base,
        'background': backgrounds_base,
    },
    'fantasy': {},
}


def get_setting_data(setting='fantasy'):
    setting_data = dict(settings['default'])
    setting_specific = dict(settings[setting.lower()])
    setting_data.update(setting_specific)
    return setting_data


if __name__ == "__main__":
    my_setting = get_setting_data('fantasy')
    print(my_setting)
