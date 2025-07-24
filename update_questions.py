import json
import random

def update_questions():
    # Read the existing questions
    try:
        with open('questions.json', 'r', encoding='utf-8') as f:
            questions = json.load(f)
        print(f"Loaded {len(questions)} existing questions")
    except FileNotFoundError:
        questions = []
        print("No existing questions file found, starting fresh")
    
    # Add unique IDs to existing questions
    for i, question in enumerate(questions, 1):
        question['id'] = i
    
    # Sample questions - in a real scenario, you would add more questions here
    sample_questions = [
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
        }
    ]
    
    # Add sample questions if we don't have enough
    if len(questions) < 100:
        start_id = len(questions) + 1
        for i, question in enumerate(sample_questions, start_id):
            question['id'] = i
            questions.append(question)
    
    # Ensure we have exactly 100 questions (duplicating if necessary)
    while len(questions) < 100:
        question = random.choice(sample_questions).copy()
        question['id'] = len(questions) + 1
        questions.append(question)
    
    # Save the updated questions
    with open('questions.json', 'w', encoding='utf-8') as f:
        json.dump(questions, f, ensure_ascii=False, indent=2)
    
    print(f"Updated questions.json with {len(questions)} questions")

if __name__ == "__main__":
    update_questions()
