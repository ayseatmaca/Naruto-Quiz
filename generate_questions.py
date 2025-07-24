import json
import random

# A comprehensive list of unique Naruto questions
NARUTO_QUESTIONS = [
    {
        "question": "Naruto'nun içinde yaşadığı dokuz kuyruklu canavarın adı nedir?",
        "options": ["Shukaku", "Kurama", "Gyuki", "Isobu"],
        "correct": 2
    },
    {
        "question": "Hangisi 'Uchiha Madara'nın kardeşidir?",
        "options": ["Izuna Uchiha", "Shisui Uchiha", "Fugaku Uchiha", "Obito Uchiha"],
        "correct": 1
    },
    {
        "question": "Naruto'nun ilk öğrendiği teknik hangisidir?",
        "options": ["Kage Bunshin no Jutsu", "Henge no Jutsu", "Tajuu Kage Bunshin no Jutsu", "Rasengan"],
        "correct": 2
    },
    {
        "question": "Hangisi 'Akatasuki' üyesi değildir?",
        "options": ["Hidan", "Kakuzu", "Zabuza", "Deidara"],
        "correct": 3
    },
    {
        "question": "Naruto'nun en sevdiği ramen dükkanının adı nedir?",
        "options": ["Ichiraku Ramen", "Naruto Ramen", "Konoha Ramen", "Hokage Ramen"],
        "correct": 1
    },
    {
        "question": "Hangisi 'Sannin'lerden biri değildir?",
        "options": ["Jiraiya", "Orochimaru", "Tsunade", "Minato"],
        "correct": 4
    },
    {
        "question": "Naruto'nun en iyi arkadaşı kimdir?",
        "options": ["Sasuke Uchiha", "Sakura Haruno", "Shikamaru Nara", "Hinata Hyuga"],
        "correct": 1
    },
    {
        "question": "Hangisi 'Beş Büyük Ninja Köyü'nden biri değildir?",
        "options": ["Konohagakure", "Kirigakure", "Sunagakure", "Amegakure"],
        "correct": 4
    },
    {
        "question": "Naruto'nun en güçlü tekniği hangisidir?",
        "options": ["Rasengan", "Rasenshuriken", "Kage Bunshin no Jutsu", "Harem no Jutsu"],
        "correct": 2
    },
    {
        "question": "Hangisi 'Üç Efsane Sannin'den biri değildir?",
        "options": ["Jiraiya", "Orochimaru", "Tsunade", "Hiruzen"],
        "correct": 4
    },
    {
        "question": "Naruto'nun annesinin adı nedir?",
        "options": ["Kushina Uzumaki", "Mikoto Uchiha", "Kurenai Yuhi", "Tsunade"],
        "correct": 1
    },
    {
        "question": "Hangisi 'Uchiha Itachi'nin küçük kardeşidir?",
        "options": ["Sasuke Uchiha", "Shisui Uchiha", "Obito Uchiha", "Madara Uchiha"],
        "correct": 1
    },
    {
        "question": "Naruto'nun çocukluk sevgilisi kimdir?",
        "options": ["Sakura Haruno", "Hinata Hyuga", "Ino Yamanaka", "Tenten"],
        "correct": 1
    },
    {
        "question": "Hangisi 'Yedi Kılıç Adamı'ndan biri değildir?",
        "options": ["Zabuza Momochi", "Kisame Hoshigaki", "Suigetsu Hozuki", "Itachi Uchiha"],
        "correct": 4
    },
    {
        "question": "Naruto'nun ilk tamamladığı görev seviyesi nedir?",
        "options": ["D-Rank", "C-Rank", "B-Rank", "A-Rank"],
        "correct": 2
    },
    {
        "question": "Hangisi 'Uchiha Madara'nın en güçlü tekniğidir?",
        "options": ["Amaterasu", "Tsukuyomi", "Susanoo", "Infinite Tsukuyomi"],
        "correct": 4
    },
    {
        "question": "Naruto'nun en sevdiği hoca kimdir?",
        "options": ["Kakashi Hatake", "Jiraiya", "Iruka Umino", "Hiruzen Sarutobi"],
        "correct": 2
    },
    {
        "question": "Hangisi 'Tailed Beast'lerden biri değildir?",
        "options": ["Shukaku", "Kurama", "Gamabunta", "Matatabi"],
        "correct": 3
    },
    {
        "question": "Hangisi 'Akatsuki'nin kurucusudur?",
        "options": ["Pain", "Obito Uchiha", "Madara Uchiha", "Yahiko"],
        "correct": 4
    },
    {
        "question": "Naruto'nun ilk kez kullandığı Rasengan varyasyonu nedir?",
        "options": ["Oodama Rasengan", "Rasenshuriken", "Futon: Rasengan", "Senpou: Chou Oodama Rasengan"],
        "correct": 3
    },
    {
        "question": "Hangisi 'Uchiha klanının katliamından' sağ kurtulan kişidir?",
        "options": ["Sasuke Uchiha", "Itachi Uchiha", "Obito Uchiha", "Madara Uchiha"],
        "correct": 1
    },
    {
        "question": "Naruto'nun ilk kez kullandığı Kage Bunshin no Jutsu'yu kimden öğrenmiştir?",
        "options": ["Iruka Umino", "Kakashi Hatake", "Jiraiya", "Scroll of Seals'den"],
        "correct": 4
    },
    {
        "question": "Hangisi 'Hokage' unvanını taşımamıştır?",
        "options": ["Hashirama Senju", "Tobirama Senju", "Danzo Shimura", "Sakumo Hatake"],
        "correct": 4
    },
    {
        "question": "Hangisi 'Uchiha klanının' özel yeteneğidir?",
        "options": ["Byakugan", "Sharingan", "Rinnegan", "Tenseigan"],
        "correct": 2
    },
    {
        "question": "Naruto'nun en sevdiği yemek nedir?",
        "options": ["Ramen", "Dango", "Onigiri", "Sushi"],
        "correct": 1
    },
    {
        "question": "Hangisi 'Hyuga klanının' özel yeteneğidir?",
        "options": ["Byakugan", "Sharingan", "Rinnegan", "Tenseigan"],
        "correct": 1
    },
    {
        "question": "Naruto'nun en güçlü rakibi kimdir?",
        "options": ["Sasuke Uchiha", "Madara Uchiha", "Pain", "Orochimaru"],
        "correct": 1
    },
    {
        "question": "Hangisi 'Uzumaki klanının' özelliği değildir?",
        "options": ["Uzun ömürlülük", "Çok güçlü chakra", "Özel göz yetenekleri", "Mühürleme tekniklerinde uzmanlık"],
        "correct": 3
    },
    {
        "question": "Naruto'nun en sevdiği hikaye kitabı nedir?",
        "options": ["Ninja Yolu", "Gutsy Ninja", "The Tale of Jiraiya the Gallant", "The Tale of Naruto"],
        "correct": 2
    },
    {
        "question": "Hangisi 'Uchiha Obito'nun takma adıdır?",
        "options": ["Tobi", "Madara", "Pain", "Zetsu"],
        "correct": 1
    },
    {
        "question": "Hangisi 'Uchiha Itachi'nin en güçlü tekniğidir?",
        "options": ["Amaterasu", "Tsukuyomi", "Susanoo", "Izanami"],
        "correct": 3
    },
    {
        "question": "Naruto'nun en sevdiği renk nedir?",
        "options": ["Turuncu", "Sarı", "Kırmızı", "Mavi"],
        "correct": 1
    },
    {
        "question": "Hangisi 'Uchiha Madara'nın en güçlü rakibidir?",
        "options": ["Hashirama Senju", "Tobirama Senju", "Hiruzen Sarutobi", "Minato Namikaze"],
        "correct": 1
    },
    {
        "question": "Naruto'nun en sevdiği mevsim nedir?",
        "options": ["İlkbahar", "Yaz", "Sonbahar", "Kış"],
        "correct": 2
    },
    {
        "question": "Hangisi 'Uchiha klanının' en güçlü tekniğidir?",
        "options": ["Izanagi", "Izanami", "Amaterasu", "Tsukuyomi"],
        "correct": 1
    },
    {
        "question": "Naruto'nun en sevdiği hayvan nedir?",
        "options": ["Tilki", "Kurbağa", "Kaplumbağa", "Yılan"],
        "correct": 1
    },
    {
        "question": "Hangisi 'Uchiha Madara'nın en güçlü silahıdır?",
        "options": ["Gunbai", "Kusanagi", "Samehada", "Hiramekarei"],
        "correct": 1
    },
    {
        "question": "Naruto'nun en sevdiği tatlı nedir?",
        "options": ["Dango", "Mochi", "Taiyaki", "Dorayaki"],
        "correct": 4
    },
    {
        "question": "Naruto'nun en sevdiği içecek nedir?",
        "options": ["Çay", "Kahve", "Meyve Suyu", "Süt"],
        "correct": 4
    },
    {
        "question": "Hangisi 'Uchiha klanının' en güçlü düşmanıdır?",
        "options": ["Senju klanı", "Uzumaki klanı", "Hyuga klanı", "Uchiha klanı"],
        "correct": 1
    },
    {
        "question": "Naruto'nun en sevdiği meyve nedir?",
        "options": ["Elma", "Muz", "Portakal", "Çilek"],
        "correct": 2
    },
    {
        "question": "Naruto'nun en sevdiği çizgi roman karakteri kimdir?",
        "options": ["Gutsy Ninja", "Jiraiya the Gallant", "The Yellow Flash", "The Red Hot Habanero"],
        "correct": 1
    },
    {
        "question": "Naruto'nun en sevdiği renk kombinasyonu nedir?",
        "options": ["Turuncu-Siyah", "Turuncu-Mavi", "Turuncu-Beyaz", "Turuncu-Kırmızı"],
        "correct": 1
    },
    {
        "question": "Naruto'nun en sevdiği hikaye kitabının yazarı kimdir?",
        "options": ["Jiraiya", "Tsunade", "Iruka Umino", "Kakashi Hatake"],
        "correct": 1
    },
    {
        "question": "Naruto'nun en sevdiği ramen çeşidi nedir?",
        "options": ["Miso Çorbası", "Shoyu Ramen", "Miso Ramen", "Tonkotsu Ramen"],
        "correct": 3
    },
    {
        "question": "Naruto'nun en sevdiği dövüş stili nedir?",
        "options": ["Taijutsu", "Ninjutsu", "Genjutsu", "Senjutsu"],
        "correct": 1
    },
    {
        "question": "Naruto'nun en sevdiği eğitmeni kimdir?",
        "options": ["Iruka Umino", "Kakashi Hatake", "Jiraiya", "Hiruzen Sarutobi"],
        "correct": 3
    },
    {
        "question": "Naruto'nun en sevdiği mekân neresidir?",
        "options": ["Ichiraku Ramen", "Hokage Kulesi", "Ninja Akademisi", "Hokage Dağı"],
        "correct": 1
    },
    {
        "question": "Naruto'nun en sevdiği meyve suyu nedir?",
        "options": ["Portakal Suyu", "Elma Suyu", "Üzüm Suyu", "Şeftali Suyu"],
        "correct": 4
    },
    {
        "question": "Naruto'nun en sevdiği tatlı içecek nedir?",
        "options": ["Çilekli Süt", "Çikolatalı Süt", "Muzlu Süt", "Sade Süt"],
        "correct": 2
    },
    {
        "question": "Naruto'nun en sevdiği ana karakter kimdir?",
        "options": ["Goku", "Luffy", "Ichigo", "Gutsy Ninja"],
        "correct": 4
    },
    {
        "question": "Naruto'nun en sevdiği yan karakter kimdir?",
        "options": ["Sasuke", "Sakura", "Kakashi", "Jiraiya"],
        "correct": 4
    },
    {
        "question": "Naruto'nun en sevdiği köy dışı mekân neresidir?",
        "options": ["Sıcak Kaplıcalar Köyü", "Kum Köyü", "Gizli Çayır Köyü", "Yağmur Köyü"],
        "correct": 1
    },
    {
        "question": "Naruto'nun en sevdiği doğal mekân nedir?",
        "options": ["Orman", "Dağ", "Göl", "Şelale"],
        "correct": 4
    }
]

def generate_questions():
    # Shuffle the questions to ensure randomness
    random.shuffle(NARUTO_QUESTIONS)
    
    # Select first 100 questions (or all if less than 100)
    selected_questions = NARUTO_QUESTIONS[:min(100, len(NARUTO_QUESTIONS))]
    
    # Add unique IDs
    for i, question in enumerate(selected_questions, 1):
        question['id'] = i
    
    # Save to file
    with open('questions.json', 'w', encoding='utf-8') as f:
        json.dump(selected_questions, f, ensure_ascii=False, indent=2)
    
    print(f"Generated {len(selected_questions)} unique questions in questions.json")

if __name__ == "__main__":
    generate_questions()
