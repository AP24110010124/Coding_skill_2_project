"""
data.py
=======
Sample dataset of tourist places with costs and value scores.
Can be extended or replaced with real-world / user-provided data.
"""

from algorithms import Place

SAMPLE_PLACES = [
    # Heritage & History
    Place("Taj Mahal, Agra",             cost=1100, value=98, category="Heritage"),
    Place("Qutub Minar, Delhi",           cost=600,  value=80, category="Heritage"),
    Place("Hampi Ruins, Karnataka",       cost=500,  value=85, category="Heritage"),
    Place("Ajanta Caves, Maharashtra",    cost=700,  value=87, category="Heritage"),
    Place("Konark Sun Temple, Odisha",    cost=400,  value=78, category="Heritage"),

    # Nature & Adventure
    Place("Munnar Tea Gardens, Kerala",   cost=800,  value=90, category="Nature"),
    Place("Coorg, Karnataka",             cost=950,  value=88, category="Nature"),
    Place("Valley of Flowers, UK",        cost=1200, value=95, category="Nature"),
    Place("Spiti Valley, HP",             cost=1500, value=93, category="Nature"),
    Place("Sundarbans, WB",               cost=850,  value=82, category="Nature"),

    # Beaches
    Place("Radhanagar Beach, Andaman",    cost=2000, value=97, category="Beach"),
    Place("Varkala Beach, Kerala",        cost=700,  value=84, category="Beach"),
    Place("Palolem Beach, Goa",           cost=900,  value=86, category="Beach"),
    Place("Om Beach, Gokarna",            cost=500,  value=80, category="Beach"),

    # Spiritual
    Place("Varanasi Ghats, UP",           cost=300,  value=91, category="Spiritual"),
    Place("Golden Temple, Amritsar",      cost=200,  value=96, category="Spiritual"),
    Place("Tirupati Temple, AP",          cost=500,  value=89, category="Spiritual"),
    Place("Kedarnath, Uttarakhand",       cost=1800, value=94, category="Spiritual"),

    # City / Culture
    Place("Jaipur City Palace, Raj",      cost=600,  value=83, category="Culture"),
    Place("Mysore Palace, Karnataka",     cost=400,  value=85, category="Culture"),
    Place("Pondicherry French Quarter",   cost=300,  value=79, category="Culture"),
    Place("Jodhpur Blue City, Raj",       cost=550,  value=86, category="Culture"),
]
