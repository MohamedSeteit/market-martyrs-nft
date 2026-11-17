import json
import os

# إنشاء الفولدر
os.makedirs("trader_metadata_92_final", exist_ok=True)

# بيانات الشخصيات والوصف
traits_map = {
    "Owl": {"style": "The Technical Owl", "quote": "In charts we trust. Emotions are just noise on the blockchain."},
    "Fox": {"style": "The Aggressive Fox", "quote": "High risk, maximum leverage, pure adrenaline."},
    "Turtle": {"style": "The HODLer Turtle", "quote": "Slow, steady, and unbreakable. Long-term compounding is the way."},
    "Monkey": {"style": "The FOMO Monkey", "quote": "Bought the top, sold the bottom. Coping with green candles."},
    "Cat": {"style": "The Swing Cat", "quote": "Patience is a virtue. Waiting for the perfect setup to strike."},
    "Raccoon": {"style": "The Scalper Raccoon", "quote": "In and out in seconds. Chasing pennies until they make millions."},
    "Bear": {"style": "The Bear Market Master", "quote": "Thriving in the red. Blood in the streets is my comfort zone."}
}

# دالة ذكية لتحديد الحيوان بناءً على خريطتك بالمللي
def get_animal(i):
    if i in [1, 2, 8, 9, 52, 53] or 18 <= i <= 28: return "Owl"
    if i in [3, 4, 5] or 29 <= i <= 40: return "Fox"
    if i in [6, 7] or 41 <= i <= 51: return "Turtle"
    if i in [10, 11] or 54 <= i <= 62: return "Monkey"
    if i in [12, 13] or 63 <= i <= 74: return "Cat"
    if i in [14, 15, 16] or 75 <= i <= 82: return "Raccoon"
    if i == 17 or 83 <= i <= 92: return "Bear"
    return "Unknown"

# توليد الـ 92 ملف
for i in range(1, 93):
    animal = get_animal(i)
    style_info = traits_map[animal]
    
    metadata = {
        "name": f"Market Martyr #{i}",
        "description": "A premium PFP collection dedicated to the raw psychology, existential dread, and emotional rollercoaster of crypto trading. Representing the elite archetypes of the digital markets.",
        "image": f"ipfs://bafybeialsg5depxajkgjpv7mnzxq3raps7wwazwvjxyngckes4lxxjcfre/{i}.png", # لا تنسَ وضع الـ CID هنا
        "attributes": [
            {"trait_type": "Background", "value": "Solid Dark Midnight Blue"},
            {"trait_type": "Expression", "value": "Deadpan Drool"},
            {"trait_type": "Trading Style", "value": style_info["style"]},
            {"trait_type": "Character Type", "value": f"Anthropomorphic {animal}"},
            {"trait_type": "Market Philosophy", "value": style_info["quote"]}
        ]
    }
    
    with open(f"trader_metadata_92_final/{i}", "w") as f:
        json.dump(metadata, f, indent=4)

print("تم توليد 92 ملف ميتاداتا بنجاح ومطابقتهم مع خريطة الصور!")