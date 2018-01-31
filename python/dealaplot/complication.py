#-------------------------------------------------------------------------------
#
# --> Plot Complications from Deal-a-Plot Cards
#
# I pulled the complications off of the 1930s "Deal-a-Plot" cards.
# Useful when you need a random event or plot twist.
#
# Note, the source is really dated. These are unedited except for spelling.
#
#-------------------------------------------------------------------------------


import random

count = raw_input("\nHow many complications?  ")

complications = ["Loss", "Malady", "Invitation", "Admission", "Failure", "Battle", "Avalanche", "Fright", "Burglary", "Deprivation", "Betrothal", "Retirement", "Race", "Explosion", "Wound", "Incitement", "Insinuation", "Mystery", "Exchange", "Feud", "Vandalism", "Apparition", "Exposure", "Capture", "Intrigue", "Prophecy", "Alienation", "Impersonation", "Brawl", "Favor", "Option", "Risk", "Trial", "Warning", "Scandal", "Inquest", "Advance", "Deal", "Compromise", "Enchantment", "Release", "Pursuit", "Call", "Abortion", "Trade", "Visit", "Revelation", "Theft", "Migration", "Renunciation", "Shooting", "Festival", "Expulsion", "Abdication", "Transgression", "Union", "Mirage", "Alienation", "Camouflage", "Ban", "Adjustment", "Sanction", "Resignation", "Barrage", "Danger", "Edict", "Appropriation", "Honor", "Incentive", "Round-up", "Rumor", "Penalty", "Escape", "Agreement", "Dissipation", "Truce", "Suffocation", "Regret", "Plagiarism", "Repair", "Subterfuge", "Accusation", "Catastrophe", "Punishment", "Achievement", "Disgrace", "Blizzard", "Exhortation", "Disinheritance", "Invasion", "Obligation", "Slander", "Strike", "Repudiation", "Snowstorm", "Deliverance", "Reprieve", "Recuperation", "Protest", "Bribe", "Debauch", "Estrangement", "Provocation", "Rescue", "Stoppage", "Conspiracy", "Brawl", "Conquest", "Restraint", "Struggle", "Retraction", "Signal", "Perjury", "Obstinacy", "Dream", "Separation", "Extortion", "Discord", "Cave-in", "Misdeed", "Divorce", "Impropriety", "Escapade", "Envy", "Incarnation", "Appointment", "Denunciation", "Mistake", "Need", "Initiation", "Merger", "]", "Forgiveness", "Substitution", "Default", "Assault", "Dread", "Casualty", "SOS", "Break", "Hardship", "Evasion", "Promise", "Turmoil", "Arrest", "Proposal", "Indictment", "Purchase", "Humiliation", "Arrival", "Stratagem", "Relinquishment", "Concealment", "Debut", "Holdup", "Foreclosure", "Refusal", "Disobedience", "Abduction", "Forfeit", "Ascent", "Separation", "Reproof", "Offense", "Storm", "Request", "Treachery", "Revolution", "Annulment", "Experience", "Fight", "Outrage", "Holiday", "Misgiving", "Funeral", "Disaster", "Attempt", "Repulse", "Forecast", "Flogging", "Murder", "Quest", "Hoodoo", "Torture", "Dispute", "Proof", "Descent", "Illness", "Travail", "Lesson", "Furlough", "Absconding", "Acquittal", "Confession", "Revenge", "Surrender", "Criticism", "Blockade", "Disillusionment", "Reprisal", "Arrest", "Joke", "Offer", "Loan", "Misfortune", "Promotion", "Benefit", "Demand", "Engagement", "Death", "Journey", "Mission", "Riot", "Surprise", "Recovery", "Contest", "Drowning", "Bequest", "Execution", "Rebuff", "Discovery", "Premonition", "Frustration", "Emergency", "Abuse", "Quarrel", "Mishap", "Pledge", "Antagonism", "Defeat", "Disqualification", "Respite", "Trap", "Sleep", "Accident", "Bereavement", "Foreboding", "Tyranny", "Prank", "Sorcery", "Fraud", "Exile", "Adoption", "Contest", "Crime", "Judgement", "Peril", "Caress", "Calamity", "Debt", "Delusion", "Collision", "Embezzlement", "Convalescence", "Inflation", "Knavery", "Damage", "Famine", "Search", "Operation", "Seance", "Transfer", "Villainy", "Epidemic", "Curse", "Amour", "Duel", "Wager", "Remonstrance", "Acceptance", "Deluge", "Raid", "Celebration", "Incantation", "Message", "Award", "Excursion", "Repentance", "Payment", "Overdose", "Burden", "Fire", "Prosecution", "Appeal", "Lie", "Flood", "Electrocution", "Shipwreck", "Secret", "Habit", "Legacy", "Affront", "Dividend", "Return", "Hallucination", "Misunderstanding", "Blow", "Miracle", "Sacrifice", "Reformation", "Trance", "Rage", "Seduction", "Duty", "Debate", "Frolic", "Neglect", "Stigma", "Crash", "Birth", "Dare", "Task", "Onslaught", "Bankruptcy", "Eviction", "Settlement", "Frenzy", "Proclamation", "Discourtesy", "Embarrassment", "Mania", "Imposture", "Adjournment", "Blackmail", "Forgery", "Decision", "Flirtation", "Bluff", "Injury", "Artifice", "Enticement", "Delay", "Refuge", "Tragedy", "Investment", "Claim", "Intimacy", "Loyalty", "Command", "Citation", "Baptism", "Misquotation", "Pardon", "Suspicion", "Temptation", "Suicide", "Insult", "Conflict", "Deception", "Rape", "Outbreak", "Invention", "Triumph", "Detour", "Jubilee", "Challenge", "Imitation", "Ransom", "Panic", "Ruse", "Imposition", "Meeting", "Omen", "Denial", "Orgy", "Flight", "Marriage", "Ostracism", "Wreck", "Rejection", "Siege", "Embargo", "Banquet", "Decree", "Treason", "Threat", "Scheme", "Abandonment", "Blunder", "Elopement", "Foul play", "Romance", "Plot", "Fatality", "Kidnapping", "Oath", "Gamble", "Misalliance", "Eulogy", "Resolve", "Trip", "Sentence", "Banishment", "Encounter", "Division", "Error", "Alarm", "Filibuster", "Drouth", "Confiscation", "Veto", "Ambuscade", "Desertion", "Restoration", "Trick", "Vindication", "Assassination", "Hunt", "Oversight", "Election", "Attack", "Apology", "Gift", "Rebuttal", "Obstruction", "Resolution", "Hurricane", "Service", "Illumination", "Retreat", "Contribution", "Coercion", "Lynching", "Sedative", "Help", "Repeal", "Objection", "Departure", "Ceremony", "Betrayal", "Donation"]

try:
    count = int(count)
    dc = str(count)
except:
    count = random.randint(1,3)
    dc = "random " + str(count)

print("\n..." + dc + " complications:")

print("\nComplications: " + ', '.join(random.sample(complications, count)))
