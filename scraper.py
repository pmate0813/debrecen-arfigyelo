import json
from datetime import datetime

updated_data = {
    "last_updated": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    "products": [
        # Alapvető élelmiszerek
        {"id": "milk", "name": "Tej 2.8% (1L)"},
        {"id": "cheese", "name": "Trappista sajt (1kg)"},
        {"id": "chicken", "name": "Csirkemellfilé (1kg)"},
        {"id": "eggs", "name": "Tojás (10 db, M-es)"},
        {"id": "rice", "name": "Rizs (1kg)"},
        {"id": "pasta", "name": "Spagetti tészta (500g)"},
        {"id": "bread", "name": "Fehér kenyér (1kg)"},
        {"id": "oil", "name": "Napraforgó étolaj (1L)"},
        {"id": "sourcream", "name": "Tejföl 20% (330g)"},
        {"id": "butter", "name": "Vaj (100g)"},
        
        # Zöldség & Gyümölcs
        {"id": "banana", "name": "Banán (1kg)"},
        {"id": "apple", "name": "Alma (1kg)"},
        {"id": "potato", "name": "Burgonya (1kg)"},
        
        # Diák kedvencek
        {"id": "coffee", "name": "Szemes/Őrölt Kávé (250g)"},
        {"id": "water", "name": "Ásványvíz (1.5L)"},
        {"id": "energydrink", "name": "Energiaital (250ml)"},
        
        # Háztartás & Higiénia
        {"id": "tp", "name": "Toalettpapír (3 rétegű, 10 tek)"},
        {"id": "detergent", "name": "Mosógél (kb. 30 mosás)"},
        {"id": "dishsoap", "name": "Mosogatószer (1L)"},
        {"id": "paper_towel", "name": "Papírtörlő (2 tekercs)"}
    ],
    "stores": {
        "Auchan (Debrecen, Kishatár u.)": {
            "milk": 309, "cheese": 2090, "chicken": 1879, "eggs": 499, "rice": 429, 
            "pasta": 339, "bread": 499, "oil": 549, "sourcream": 419, "butter": 449,
            "banana": 599, "apple": 399, "potato": 299, "coffee": 990, "water": 119,
            "energydrink": 219, "tp": 1029, "detergent": 2190, "dishsoap": 619, "paper_towel": 399
        },
        "Lidl (Debrecen, Derék u. / Hadházi út)": {
            "milk": 315, "cheese": 2190, "chicken": 1899, "eggs": 529, "rice": 449, 
            "pasta": 355, "bread": 529, "oil": 569, "sourcream": 439, "butter": 469,
            "banana": 649, "apple": 429, "potato": 319, "coffee": 1049, "water": 129,
            "energydrink": 229, "tp": 1099, "detergent": 2399, "dishsoap": 649, "paper_towel": 429
        },
        "ALDI (Debrecen, Ötvenhatosok tere)": {
            "milk": 315, "cheese": 1999, "chicken": 1949, "eggs": 519, "rice": 459, 
            "pasta": 349, "bread": 529, "oil": 559, "sourcream": 429, "butter": 459,
            "banana": 629, "apple": 419, "potato": 309, "coffee": 1029, "water": 125,
            "energydrink": 225, "tp": 1149, "detergent": 2299, "dishsoap": 629, "paper_towel": 419
        },
        "Penny (Debrecen, István út / Sámsoni út)": {
            "milk": 295, "cheese": 2150, "chicken": 1890, "eggs": 509, "rice": 439, 
            "pasta": 355, "bread": 489, "oil": 539, "sourcream": 399, "butter": 439,
            "banana": 589, "apple": 389, "potato": 289, "coffee": 979, "water": 109,
            "energydrink": 199, "tp": 1049, "detergent": 2199, "dishsoap": 599, "paper_towel": 389
        },
        "Tesco (Debrecen, Kishegyesi út)": {
            "milk": 329, "cheese": 2250, "chicken": 1919, "eggs": 539, "rice": 469, 
            "pasta": 369, "bread": 549, "oil": 579, "sourcream": 449, "butter": 479,
            "banana": 659, "apple": 449, "potato": 329, "coffee": 1090, "water": 139,
            "energydrink": 239, "tp": 1199, "detergent": 2490, "dishsoap": 679, "paper_towel": 449
        },
        "Spar (Debrecen, Plaza / Malompark)": {
            "milk": 349, "cheese": 2490, "chicken": 1999, "eggs": 559, "rice": 499, 
            "pasta": 399, "bread": 599, "oil": 599, "sourcream": 479, "butter": 499,
            "banana": 699, "apple": 479, "potato": 349, "coffee": 1190, "water": 149,
            "energydrink": 249, "tp": 1299, "detergent": 2699, "dishsoap": 699, "paper_towel": 479
        }
    }
}

with open('prices.json', 'w', encoding='utf-8') as f:
    json.dump(updated_data, f, ensure_ascii=False, indent=4)
