import json
import random
import os
from flask import Flask, render_template, redirect, url_for, session, request, jsonify
from flask_session import Session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'naruto_quiz_secret_key_123'
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

class NarutoQuiz:
    def __init__(self):
        self.questions = self.load_questions()
        self.total_stages = 4
        
    def init_session(self):
        session['current_stage'] = 1
        session['current_question'] = 1
        session['score'] = 0
        session['stage_scores'] = [0] * self.total_stages
        session['stage_passed'] = [False] * self.total_stages
        session['correct_answers'] = 0
        session['used_questions'] = []
        
    def load_questions(self):
        try:
            # Get the absolute path to the questions.json file
            import os
            file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'questions.json')
            print(f"Dosya yolu: {file_path}")
            
            # Check if file exists
            if not os.path.exists(file_path):
                print("Hata: questions.json dosyası bulunamadı!")
                print("Mevcut dizin:", os.getcwd())
                print("Dosya var mı?", os.path.isfile(file_path))
                return []
                
            with open(file_path, 'r', encoding='utf-8') as f:
                questions = json.load(f)
                print(f"Toplam {len(questions)} soru yüklendi.")
                # Shuffle questions
                random.shuffle(questions)
                return questions
        except Exception as e:
            print(f"Hata: Sorular yüklenirken bir hata oluştu: {str(e)}")
            return []
    
    def get_question(self, stage):
        # Get a random question that hasn't been used in this session
        available_questions = [q for q in self.questions if q.get('id') not in session['used_questions']]
        if not available_questions:
            print("Uyarı: Kullanılmayan soru kalmadı!")
            return None
            
        question = random.choice(available_questions)
        session['used_questions'].append(question.get('id'))
        session.modified = True
        return question  # Bu satırı ekledik
        return question
    
    def check_answer(self, question_id, selected_option):
        # Find the question by ID
        question = next((q for q in self.questions if q['id'] == question_id), None)
        if not question:
            return False
            
        is_correct = (selected_option == question['correct'])
        
        if is_correct:
            session['correct_answers'] += 1
            session['score'] += session['current_stage'] * 10  # More points in later stages
        
        # Move to next question or stage
        if session['current_question'] < 5:
            # Move to next question in current stage
            session['current_question'] += 1
        else:
            # End of stage
            stage_idx = session['current_stage'] - 1  # 0-based index
            session['stage_scores'][stage_idx] = session['score']
            session['stage_passed'][stage_idx] = (session['correct_answers'] >= 2)
            
            # Check if we should move to next stage or end the game
            if session['current_stage'] < self.total_stages and session['correct_answers'] >= 2:
                # Move to next stage
                session['current_stage'] += 1
                session['current_question'] = 1
                session['correct_answers'] = 0
            else:
                # End the game if not enough correct answers or it's the last stage
                session['current_question'] = 6  # Set to trigger game over
            
        session.modified = True
        return is_correct
    
# Flask Routes

quiz = NarutoQuiz()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/start')
def start_quiz():
    print("Debug: Quiz başlatılıyor...")
    quiz.init_session()
    
    # Debug için oturum bilgilerini yazdır
    print(f"Debug: Oturum başlatıldı - current_stage: {session['current_stage']}, current_question: {session['current_question']}")
    
    # İlk soruyu al
    question = quiz.get_question(session['current_stage'])
    if not question:
        print("Hata: İlk soru yüklenemedi!")
        return redirect(url_for('show_results'))
    
    # Oturumu güncelle
    session['current_question'] = 1
    session.modified = True
    
    print(f"Debug: İlk soru yüklendi - ID: {question.get('id')}")
    
    return render_template(
        'question.html',
        question=question,
        question_number=1,
        stage=1,
        score=0
    )

@app.route('/question')
def show_question():
    if 'current_stage' not in session:
        return redirect(url_for('start_quiz'))
        
    print(f"Debug: show_question - current_stage: {session['current_stage']}, current_question: {session['current_question']}")
    
    # Check if game is over
    if session['current_question'] > 5 and session['current_stage'] == quiz.total_stages:
        print("Debug: Son etapta son soruya ulaşıldı, sonuçlara yönlendiriliyor...")
        return redirect(url_for('show_results'))
    elif session['current_question'] > 5 and not session['stage_passed'][session['current_stage']-1]:
        print("Debug: Yeterli puan alınamadı, sonuçlara yönlendiriliyor...")
        return redirect(url_for('show_results'))
    
    # Get current question
    question = quiz.get_question(session['current_stage'])
    if not question:
        print("Debug: Soru bulunamadı, sonuçlara yönlendiriliyor...")
        return redirect(url_for('show_results'))
    
    print(f"Debug: Soru başarıyla yüklendi - ID: {question.get('id')}")
    
    return render_template(
        'question.html',
        question=question,
        question_number=session['current_question'],
        stage=session['current_stage'],
        score=session['score']
    )

@app.route('/check', methods=['POST'])
def check_answer():
    if 'current_stage' not in session:
        return jsonify({'redirect': url_for('index')})
        
    try:
        selected_option = int(request.form.get('answer', 0))
        question_id = int(request.form.get('question_id', 0))
        
        is_correct = quiz.check_answer(question_id, selected_option)
        
        # Determine next URL and get next question if needed
        if session['current_question'] > 5 and session['current_stage'] == quiz.total_stages:
            next_url = url_for('show_results')
        elif session['current_question'] > 5 and not session['stage_passed'][session['current_stage']-1]:
            next_url = url_for('show_results')
        else:
            # Get the next question here to ensure it's available
            next_question = quiz.get_question(session['current_stage'])
            if not next_question:
                return jsonify({'redirect': url_for('show_results')})
            next_url = url_for('show_question')
        
        return jsonify({
            'correct': is_correct,
            'redirect': next_url,
            'score': session.get('score', 0)
        })
    except Exception as e:
        print(f"Hata: {str(e)}")
        return jsonify({'error': str(e)}), 400

@app.route('/results')
def show_results():
    if 'current_stage' not in session:
        return redirect(url_for('index'))
        
    total_score = sum(session['stage_scores'])
    max_score = sum([5 * (i+1) * 10 for i in range(quiz.total_stages)])
    score_percentage = (total_score / max_score) * 100 if max_score > 0 else 0
    
    return render_template(
        'result.html',
        score=total_score,
        stage_scores=session['stage_scores'],
        stage_passed=session['stage_passed'],
        score_percentage=score_percentage
    )


if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
